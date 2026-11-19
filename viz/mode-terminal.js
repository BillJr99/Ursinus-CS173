/* Terminal: local asciicast v2 playback. No shell commands execute in the browser.
   Supports line-oriented output, SGR removal, CR and backspace, not cursor-addressed TUIs.
   The selectable transcript is always available when clipboard access is unavailable. */
(function () {
  'use strict';
  const el = id => document.getElementById(id);
  const S = {id:null,time:0,duration:0,playing:false,speed:1,pacing:'line',frame:0,events:[],markers:[],sess:null,epoch:0,selectedMarker:null};
  let saved=[], copyTimer=null, motion=null, motionChanged=null;
  const reduced=()=>window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function resetCopy() {
    clearTimeout(copyTimer);copyTimer=null;
    if(el('terminal-copy')) el('terminal-copy').textContent='Copy transcript';
  }
  // Presentation timing only. Keep captured output chunks unchanged, with gaps capped at 2 s.
  const CHAR_TIME=1/24, LINE_HOLD=0.09;
  function demoEvents(sess,pacing) {
    const events=[], markers=[];let at=0;
    for(const [index,step] of (sess.steps||[]).entries()) {
      for(const marker of sess.markers||[]) if(marker.step===index) {
        markers.push({...marker,at});events.push([at,'m',marker.title]);
      }
      events.push([at,'o','$ ']);
      const line=pacing==='line';
      // ANSI-bearing commands are opaque. Preserve CRLF and all other command bytes.
      const parts=/[\x1b\x80-\x9f]/.test(step.cmd)?[step.cmd]:
        step.cmd.match(line?/[^\n]*\n|[^\n]+/g:/\r\n|[\s\S]/gu)||[];
      for(const part of parts) {
        const typed=[...part].length*CHAR_TIME;
        events.push([at+(line?CHAR_TIME:typed),'o',part]);
        at+=typed+(line?LINE_HOLD:0);
      }
      at+=0.25;events.push([at,'o','\r\n']);
      let previous=0;
      const chunks=step.cast&&step.cast.length?step.cast:[[0,step.output||'']];
      for(const [stamp,text] of chunks) {
        at+=Math.max(0,Math.min(2,stamp-previous));previous=stamp;events.push([at,'o',text]);
      }
      if(chunks.length&&chunks[chunks.length-1][1]&&!chunks[chunks.length-1][1].endsWith('\n'))events.push([at,'o','\r\n']);
      at+=0.65;
    }
    return {events,markers,duration:Math.ceil(at*1000)/1000};
  }
  function plain(raw) {
    // Keep erase-in-line sequences until the cursor-aware pass below. Other CSI
    // sequences (including colour) remain presentation-only in this line renderer.
    raw=raw.replace(/\x1b\][^\x07]*(?:\x07|\x1b\\)/g,'');
    const lines=['']; let row=0,col=0,returned=false;
    const tokens=raw.match(/\x1b\[[0-?]*[ -/]*[@-~]|[\s\S]/gu)||[];
    for(const c of tokens) {
      if(c.startsWith('\x1b[')) {
        const erase=/^\x1b\[([012]?)K$/.exec(c);
        if(erase) {
          const mode=Number(erase[1]||0),line=lines[row];
          if(mode===0)lines[row]=line.slice(0,col);
          else if(mode===1)lines[row]=' '.repeat(Math.min(col+1,line.length))+line.slice(col+1);
          else lines[row]='';
          returned=false;
        }
        continue;
      }
      if(c==='\n') {row++;lines[row]='';col=0;returned=false;}
      else if(c==='\r') {col=0;returned=true;}
      else if(c==='\b') col=Math.max(0,col-1);
      else if(c==='\t'||c>=' ') {
        // Delay the redraw until text arrives, so CRLF preserves the finished line.
        if(returned) {lines[row]='';returned=false;}
        const text=c==='\t'?' '.repeat(8-col%8):c,line=lines[row];
        lines[row]=line.slice(0,col).padEnd(col,' ')+text+line.slice(col+text.length);
        col+=text.length;
      }
    }
    return lines.join('\n');
  }
  function pause() {S.playing=false;cancelAnimationFrame(S.frame);if(el('terminal-play')) el('terminal-play').textContent='Play';if(el('terminal-status'))el('terminal-status').textContent=S.time>=S.duration?'Playback complete':'Paused';}
  function draw() {
    if(!el('terminal-player')) return;
    el('terminal-screen').textContent=plain(S.events.filter(e=>e[1]==='o'&&e[0]<=S.time).map(e=>e[2]).join(''));
    el('terminal-screen').scrollTop=el('terminal-screen').scrollHeight;
    el('terminal-seek').value=S.time;
    const status=S.time>=S.duration?'Playback complete':S.playing?'Playing':'Paused';
    if(el('terminal-status').textContent!==status)el('terminal-status').textContent=status;
    let active=-1;
    S.markers.forEach((m,i)=>{if(m.at<=S.time) active=i;});
    // A clicked marker owns the note until playback or another seek takes over.
    if(S.selectedMarker!==null)active=S.selectedMarker;
    const note=active>=0?S.markers[active].note:S.sess.description||'';
    if(el('terminal-note').textContent!==note)el('terminal-note').textContent=note;
    document.querySelectorAll('.terminal-marker').forEach((b,i)=>{b.setAttribute('aria-current',String(i===active));});
  }
  function seek(t,marker=null) {resetCopy();pause();S.selectedMarker=marker;S.time=Math.max(0,Math.min(Number(t)||0,S.duration));draw();}
  function play() {
    resetCopy();S.selectedMarker=null;
    if(reduced()||S.speed===0) {seek(S.duration);return;}
    if(S.playing) return pause();
    if(S.time>=S.duration) S.time=0;
    S.playing=true;el('terminal-play').textContent='Pause';S.epoch=performance.now();
    const tick=now=>{
      if(!S.playing) return;
      S.time=Math.min(S.duration,S.time+(now-S.epoch)/1000*S.speed);S.epoch=now;draw();
      if(S.time>=S.duration) pause();else S.frame=requestAnimationFrame(tick);
    };
    S.frame=requestAnimationFrame(tick);
  }
  function node(tag,attrs={},text='') {
    const n=document.createElement(tag);for(const [k,v] of Object.entries(attrs))n.setAttribute(k,v);n.textContent=text;return n;
  }
  async function show(ctx) {
    pause(); const epoch=++S.loadEpoch;
    const [sess,response]=await Promise.all([ctx.fetchJson('sessions/'+encodeURIComponent(ctx.id)+'.json.gz'),fetch('terminals/'+encodeURIComponent(ctx.id)+'.cast')]);
    if(!response.ok) throw new Error('Terminal recording missing');
    const rows=(await response.text()).trim().split('\n').map(x=>JSON.parse(x)),header=rows.shift();
    if(header.version!==2||!rows.every(e=>Array.isArray(e)&&e.length===3&&Number.isFinite(e[0])&&e[0]>=0&&typeof e[2]==='string')) throw new Error('Invalid asciicast v2 recording');
    if(epoch!==S.loadEpoch) return;
    S.id=ctx.id;S.sess=sess;S.events=rows;S.selectedMarker=null;
    S.scripted=sess.provenance==='scripted';
    if(header.code_viz_provenance&&header.code_viz_provenance!==(sess.provenance||'recorded'))throw new Error('Terminal provenance mismatch');
    S.duration=Math.max(Number(header.duration)||0,...rows.map(e=>e[0]));
    const castMarkers=rows.filter(e=>e[1]==='m');
    S.markers=(sess.markers||[]).slice().sort((a,b)=>a.step-b.step).map((m,i)=>({...m,at:castMarkers[i]?castMarkers[i][0]:0}));
    // Only opt-in demos use the session's explicit command boundaries; never infer them from a cast.
    const demo=sess.demo&&Array.isArray(sess.steps)&&sess.steps.length&&sess.steps.every(step=>typeof step?.cmd==='string');
    if(demo) Object.assign(S,demoEvents(sess,S.pacing));
    S.time=reduced()?S.duration:Math.min(S.duration,Math.max(0,ctx.pos||0));
    el('list').hidden=true;el('example').hidden=false;el('title').textContent=sess.title||ctx.id;
    saved=[];
    for(const selector of ['#example > .controls','#example > .cols']) {
      const n=document.querySelector(selector);saved.push([n,n.hidden]);n.hidden=true;
    }
    const panel=node('div',{id:'terminal-player','data-provenance':sess.provenance||'recorded'}),bar=node('div',{class:'terminal-controls'});
    const toggle=node('button',{id:'terminal-play',type:'button'},'Play');toggle.disabled=reduced();toggle.onclick=play;bar.append(toggle);
    const label=node('label',{},'Speed '),speed=node('select',{id:'terminal-speed','aria-label':'Playback speed'});
    [0.1,0.25,0.5,0.75,1,2,4,16,0].forEach(n=>speed.append(node('option',{value:n},n?n+'x':'Instant')));speed.value=S.speed;
    speed.onchange=()=>{
      S.speed=Number(speed.value);S.epoch=performance.now();
      if(S.playing&&S.speed===0)seek(S.duration);
    };label.append(speed);bar.append(label);
    if(demo) {
      const pacingLabel=node('label',{},'Command pacing '), pacing=node('select',{id:'terminal-pacing',title:'Changing command pacing restarts the demo'});
      pacing.append(node('option',{value:'line'},'Line by line'),node('option',{value:'character'},'Character by character'));
      pacing.value=S.pacing;
      pacing.onchange=()=>{
        S.pacing=pacing.value;Object.assign(S,demoEvents(sess,S.pacing));
        seekbar.max=S.duration;seek(reduced()?S.duration:0);
      };
      pacingLabel.append(pacing);bar.append(pacingLabel);
    }
    const theme=node('select',{id:'terminal-theme','aria-label':'Terminal theme'});
    ['system','light','dark'].forEach(x=>theme.append(node('option',{value:x},x)));
    theme.onchange=()=>{if(theme.value==='system')delete document.documentElement.dataset.theme;else document.documentElement.dataset.theme=theme.value;};bar.append(theme);
    const copy=node('button',{id:'terminal-copy',type:'button'},'Copy transcript');
    copy.onclick=async()=>{
      try {await navigator.clipboard.writeText(el('terminal-transcript').textContent);if(!copy.isConnected)return;copy.textContent='Copied';}
      catch(e) {if(!copy.isConnected)return;el('terminal-transcript-details').open=true;const range=document.createRange();range.selectNodeContents(el('terminal-transcript'));const selection=getSelection();selection.removeAllRanges();selection.addRange(range);copy.textContent='Select and copy transcript';}
      clearTimeout(copyTimer);copyTimer=setTimeout(resetCopy,1800);
    };bar.append(copy);
    const seekbar=node('input',{id:'terminal-seek',type:'range',min:0,max:S.duration,step:'0.001',value:S.time,'aria-label':'Playback position'});seekbar.oninput=()=>seek(seekbar.value);bar.append(seekbar);
    bar.append(node('span',{id:'terminal-status','aria-live':'polite'}));panel.append(bar);
    panel.append(node('p',{id:'terminal-provenance',role:'note'},S.scripted?'Illustration: typical output; yours may differ':'Recorded output'));
    panel.append(node('pre',{id:'terminal-screen',tabindex:0,'aria-label':S.scripted?'Illustrative terminal output':'Recorded terminal output'}));
    const notes=node('div',{class:'terminal-notes'}),markers=node('div',{class:'terminal-markers','aria-label':'Recording markers'});
    S.markers.forEach((m,i)=>{const b=node('button',{class:'terminal-marker',type:'button'},m.title);b.onclick=()=>seek(m.at,i);markers.append(b);});notes.append(markers,node('p',{id:'terminal-note','aria-live':'polite'}));panel.append(notes);
    const details=node('details',{id:'terminal-transcript-details'});details.append(node('summary',{},'Selectable transcript'),node('pre',{id:'terminal-transcript',tabindex:0},plain(rows.filter(e=>e[1]==='o').map(e=>e[2]).join(''))));panel.append(details);
    el('example').append(panel);draw();
    const onMotion=()=>{pause();toggle.disabled=reduced();if(reduced()) {S.time=S.duration;draw();}};
    motion=window.matchMedia('(prefers-reduced-motion: reduce)');motionChanged=onMotion;motion.addEventListener('change',motionChanged);
  }
  S.loadEpoch=0;
  window.CVIZ_MODES.register('terminal',{
    label:'Terminal',show,
    go(to){if(to==='+1')play();else if(to==='-1')seek(S.time-5);else seek(to);},
    pos(){return S.time;},url(){return {s:Math.round(S.time*1000)/1000};},
    hide(){pause();resetCopy();if(motion){motion.removeEventListener('change',motionChanged);motion=null;}S.loadEpoch++;const n=el('terminal-player');if(n)n.remove();saved.forEach(([n,h])=>{n.hidden=h;});saved=[];}
  });
  if(new URLSearchParams(location.search).has('embed'))document.body.classList.add('terminal-embed');
})();
