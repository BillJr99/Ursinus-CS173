---
layout: exercise
permalink: /Modules/IntroExercise
title: "CS173: Intro to Computer Science"
excerpt: "CS173: Intro to Computer Science"

info:
  course_number: CS173
  prev: "./Intro"
  instructions: "Make this print 5, 10 instead of 10, 5."
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: "http://www.billmongan.com"
  feedbackprocess: | 
    const _0x1513=['length','split'];(function(_0x280d5c,_0x15135f){const _0x53436e=function(_0xd60316){while(--_0xd60316){_0x280d5c['push'](_0x280d5c['shift']());}};_0x53436e(++_0x15135f);}(_0x1513,0x10c));const _0x5343=function(_0x280d5c,_0x15135f){_0x280d5c=_0x280d5c-0x0;let _0x53436e=_0x1513[_0x280d5c];return _0x53436e;};let pos=feedbackString[_0x5343('0x1')](',');for(let i=0x0;i<pos[_0x5343('0x0')];i++){pos[i]=parseFloat(pos[i]);}
  correctcheck: |
    const _0x5f2a=['length','split'];(function(_0x79fdb7,_0x5f2a36){const _0x238483=function(_0x34aa41){while(--_0x34aa41){_0x79fdb7['push'](_0x79fdb7['shift']());}};_0x238483(++_0x5f2a36);}(_0x5f2a,0x84));const _0x2384=function(_0x79fdb7,_0x5f2a36){_0x79fdb7=_0x79fdb7-0x0;let _0x238483=_0x5f2a[_0x79fdb7];return _0x238483;};let pos=feedbackString[_0x2384('0x1')](',');for(let i=0x0;i<pos[_0x2384('0x0')];i++){pos[i]=parseFloat(pos[i]);}
 
files:
  - filename: "File.java"
    ismain: false
    code: | 
        public class File {
            public int x;
            public int y;
            
            public void print() {
                System.out.println(this.x + "," + this.y);
            }
        }
    
  - filename: "Main.java"
    ismain: true
    code: |
        File f = new File();
        f.x = 10;
        f.y = 5;
        f.print();
  
---
Welcome! 