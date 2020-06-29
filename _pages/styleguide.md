---
layout: default
permalink: /Style-Guide
title: "CS173: Intro to Computer Science - Style Guide"
excerpt: "CS173: Intro to Computer Science - Style Guide"
    
---

As we've discussed an experienced, it's possible to write code that works, but which is completely unreadable and difficult to debug as a result.  Furthermore, we want to get you into the habit of writing good code that is easy for others to read and which is hence *easier to maintain*.  In practice, if people can't read your code, they'll just do it over from scratch their own way.  It would be a shame for all of your hard work to go to waste!  
                    
Below are some rules to help keep you on the rails as you design (they have been adapted from [Professor Schilling](https://www.ursinus.edu/live/profiles/133-ann-marie-v-schilling)).  On many assignments, 10% of the grade will depend on adhering to these rules

##All rules
                    
*   [Indentation/Brackets](#indentation)
*   [Naming Conventions](#naming)
*   [Documentation: Overview](#documentationoverview)
*   [Documentation: Inline Code](#documentationinline)
*   [Documentation: Methods](#documentationmethods)
*   [Appropriate Loop Choices](#loopchoices)
*   [Exiting Appropriately](#xiting)
*   [The Break Command](#breaking)
*   [The GOTO Command](#goto)
*   [Positive Boolean Variable Names](#boolean)
*   [Boolean Variable Comparisons](#booleancompare)
*   [Breaking Up Long Boolean Statements](#booleanbreakup)
*   [Robustness](#robustness)
*   [No Magic Numbers!](#magicnumbers)
*   [Capitalizing Final Variables](#finalcaps)
*   [Methods Returning At The End](#methodsreturn)
*   [Efficiently Written Code](#efficient)
*   [Avoid Compound Method Calls](#compoundmethods)
*   [Text Input Prompts](#textprompts)
*   [Variable Scoping](#variablescoping)

<a name="indentation"></a>
## Indentation / Brackets
All code must follow proper indentation and bracket conventions.  This includes, but is not limited to, conditionals, loops, and methods.  Brackets should be at the end of each if statement, even if the body contains only one line.  You should get into the habit of setting up your brackets and tabbing when you first complete a method, loop, or conditional statement, but before you type anything in it.  If you go completely off the rails, Netbeans can save you if you click <code>Source-&gt;Format</code>

### Bad Code
First of all, this code is missing brackets around the if statement.  This makes it easy to have a bug if you decide to add the line, because only the first line is considered to be in the body of the if statement.  Second of all, the tabbing is all over the place.  This makes it easy to miss a closing brace somewhere, which can be very difficult to resolve for multiply nested blocks.

<div><div id="highlighter_996110" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">for</code> <code class="cpp plain">(</code><code class="cpp color1 bold">int</code> <code class="cpp plain">i = 0; i &lt; 100; i++) {</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">if</code> <code class="cpp plain">(i%2 == 0 &amp;&amp; i%3 == 0)</code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">System.out.println(i + </code><code class="cpp string">" is divisible by 6"</code><code class="cpp plain">);</code></div><div class="line number4 index3 alt1"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>  

### Good Code
Here's a better version of the above example, in which brackets are applied and aligned properly

<div><div id="highlighter_852586" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp keyword bold">for</code> <code class="cpp plain">(</code><code class="cpp color1 bold">int</code> <code class="cpp plain">i = 0; i &lt; 100; i++) {</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">if</code> <code class="cpp plain">(i%2 == 0 &amp;&amp; i%3 == 0) {</code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">System.out.println(i + </code><code class="cpp string">" is divisible by 6"</code><code class="cpp plain">);</code></div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">} </code></div><div class="line number5 index4 alt2"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div> 



                <hr><h2><a name="naming">2. Naming Conventions</a></h2>
                <p>
                    </p><ul>
                        <li>
                            Variable and method names should be in <a href="https://en.wikipedia.org/wiki/Camel_case">camel case</a>; that is, the first letter should be in lower case, and each new word should be capitalized, with no spaces or underscores in between the words.
                        </li>
                        <li>
                            Variables and methods should be descriptive of what the variable holds.
                        </li>
                        <li>
                            For loop counters should be something short such as <code>i</code>, <code>j</code>, or <code>k</code>.  You may also use a descriptive, but still short, name for a for loop counter such as <code>row</code> or <code>col</code><p></p>
                        </li>
                        <li>
                            Method names should start with a verb (this includes boolean methods that start with the verb "is").
                        </li>
                    </ul>
                      

                <div id="badcode">
                    <h3>Bad Code</h3>
                </div>
                <p>
                    The names of the variables are not descriptive, and the method is not written as a verb or in camel case.
                </p>
                <div><div id="highlighter_491282" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp keyword bold">public</code> <code class="cpp keyword bold">static</code> <code class="cpp keyword bold">void</code> <code class="cpp plain">coolstuff(</code><code class="cpp color1 bold">int</code> <code class="cpp plain">x) {</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp color1 bold">int</code> <code class="cpp plain">myvar = x;</code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">do</code> <code class="cpp plain">{</code></div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">System.out.print(myvar + </code><code class="cpp string">" "</code><code class="cpp plain">);</code></div><div class="line number5 index4 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">myvar = (myvar + 7)%12;</code></div><div class="line number6 index5 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">}</code></div><div class="line number7 index6 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">while</code><code class="cpp plain">(myvar != x);</code></div><div class="line number8 index7 alt1"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>  


                <div id="goodcode">
                    <h3>Good Code</h3>
                </div>
                <p>
                    The method is now a verb that describes what it does, and its name and all variables are written in camel case (assuming "halfstep" is one word) and in descriptive language.
                </p>
                <div><div id="highlighter_264142" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp keyword bold">public</code> <code class="cpp keyword bold">static</code> <code class="cpp keyword bold">void</code> <code class="cpp plain">printCircleOfFifths(</code><code class="cpp color1 bold">int</code> <code class="cpp plain">halfstepInit) {</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp color1 bold">int</code> <code class="cpp plain">halfstepCurr = halfstepInit;</code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">do</code> <code class="cpp plain">{</code></div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">System.out.print(halfstepCurr + </code><code class="cpp string">" "</code><code class="cpp plain">);</code></div><div class="line number5 index4 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">halfstepCurr = (halfstepCurr + 7)%12;</code></div><div class="line number6 index5 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">}</code></div><div class="line number7 index6 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">while</code><code class="cpp plain">(halfstepCurr != halfstepInit);</code></div><div class="line number8 index7 alt1"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>
                
                <hr><h2><a name="documentationoverview">3. Documentation: Overview</a></h2>
                <p>     
                    All files must have comments near the top of the main program’s file containing the following information:  Author’s name, Assignment name, Date, Class, Short description of the project.  For complete information on writing Java documentation, visit <a href="http://www.ctralie.com/Teaching/CS173_S2020/www.oracle.com/technetwork/java/javase/tech/index-137868.html">this link</a> or <a href="http://www.tutorialspoint.com/java/java_documentation.htm">this link</a>.  As an example, here's a comment at the top of a file
                        
                        
                    <div><div id="highlighter_294963" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp comments">/**</code></div><div class="line number2 index1 alt1"><code class="cpp comments">* The Stack class represents a last-in-first-out stack of objects. </code></div><div class="line number3 index2 alt2"><code class="cpp comments">* @author&nbsp; Chris Tralie CS 173</code></div><div class="line number4 index3 alt1"><code class="cpp comments">* @version 0.1, January 2020</code></div><div class="line number5 index4 alt2"><code class="cpp comments">* Note that this version is not thread safe.</code></div><div class="line number6 index5 alt1"><code class="cpp comments">*/</code></div></div></td></tr></tbody></table></div></div>
                </p>


                <hr><h2><a name="documentationinline">4. Documentation: Inline code</a></h2>
                    <p>
                        All variables (except for loop counters) must be documented.  Do not state the obvious. This clutters up your code and does not convey any information to the reader.
                    </p>

                    <div id="badcode">
                        <h3>Bad Code</h3>
                    </div>
                    <div><div id="highlighter_859921" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp color1 bold">int</code> <code class="cpp plain">numCounter;&nbsp;&nbsp;&nbsp;&nbsp; </code><code class="cpp comments">//counts numbers</code></div></div></td></tr></tbody></table></div></div>

                    <div id="goodcode">
                        <h3>Good Code</h3>
                    </div>
                    <div><div id="highlighter_37991" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp color1 bold">int</code> <code class="cpp plain">numCounter;&nbsp;&nbsp;&nbsp;&nbsp; </code><code class="cpp comments">// Keeps track of how many </code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp comments">// integers the user has entered</code></div></div></td></tr></tbody></table></div></div>


                <hr><h2><a name="documentationmethods">5. Documentation: Methods</a></h2>
                    <p>
                        All methods will have documentation including, but not limited to: 
                        </p><ol>
                            <li>Method summary</li>
                            <li>Parameter descriptions</li>
                            <li>Return value descriptions</li>
                        </ol>
                        These comments should appear above the method name in a particular format, which makes it easy to automatically generate web pages describing the code (for instance, see documentation for the <a href="https://algs4.cs.princeton.edu/code/javadoc/edu/princeton/cs/algs4/StdAudio.html">audio code</a> we've been using, which was generated this way).  In NetBeans, if you type out the definition of the method and then type <code>/**</code> followed by <code>ENTER</code>, it will automatically generate a correctly formatted comment, which you can fill in with details.  Below is an example (courtesy of <a href="https://www.ursinus.edu/live/profiles/133-ann-marie-v-schilling">Professor Schilling</a>) of what it should look like:
                    <p></p>

                    <div><div id="highlighter_307828" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div><div class="line number9 index8 alt2">9</div><div class="line number10 index9 alt1">10</div><div class="line number11 index10 alt2">11</div><div class="line number12 index11 alt1">12</div><div class="line number13 index12 alt2">13</div><div class="line number14 index13 alt1">14</div><div class="line number15 index14 alt2">15</div><div class="line number16 index15 alt1">16</div><div class="line number17 index16 alt2">17</div><div class="line number18 index17 alt1">18</div><div class="line number19 index18 alt2">19</div><div class="line number20 index19 alt1">20</div><div class="line number21 index20 alt2">21</div><div class="line number22 index21 alt1">22</div><div class="line number23 index22 alt2">23</div><div class="line number24 index23 alt1">24</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp comments">/**</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">* Returns an Image object that can then be painted on the screen. </code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">* The url argument must specify an absolute {@link URL}. The name</code></div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">* argument is a specifier that is relative to the url argument. </code></div><div class="line number5 index4 alt2"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">* &lt;p&gt;</code></div><div class="line number6 index5 alt1"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">* This method always returns immediately, whether or not the </code></div><div class="line number7 index6 alt2"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">* image exists. When this applet attempts to draw the image on</code></div><div class="line number8 index7 alt1"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">* the screen, the data will be loaded. The graphics primitives </code></div><div class="line number9 index8 alt2"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">* that draw the image will incrementally paint on the screen. </code></div><div class="line number10 index9 alt1"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">*</code></div><div class="line number11 index10 alt2"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">* @param&nbsp; url&nbsp; an absolute URL giving the base location of the image</code></div><div class="line number12 index11 alt1"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">* @param&nbsp; name the location of the image, relative to the url argument</code></div><div class="line number13 index12 alt2"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">* @return&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; the image at the specified URL</code></div><div class="line number14 index13 alt1"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">* @see&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Image</code></div><div class="line number15 index14 alt2"><code class="cpp spaces">&nbsp;</code><code class="cpp comments">*/</code></div><div class="line number16 index15 alt1"><code class="cpp keyword bold">public</code> <code class="cpp plain">Image getImage(URL url, String name) {</code></div><div class="line number17 index16 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">Image image = null;</code></div><div class="line number18 index17 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">try</code> <code class="cpp plain">{</code></div><div class="line number19 index18 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">image = getImage(</code><code class="cpp keyword bold">new</code> <code class="cpp plain">URL(url, name));</code></div><div class="line number20 index19 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">} </code><code class="cpp keyword bold">catch</code> <code class="cpp plain">(MalformedURLException e) {</code></div><div class="line number21 index20 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">e.printStackTrace();</code></div><div class="line number22 index21 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">}</code></div><div class="line number23 index22 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">return</code> <code class="cpp plain">image;</code></div><div class="line number24 index23 alt1"><code class="cpp spaces">&nbsp;</code><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>

                    <hr><h2><a name="loopchoices">6. Appropriate Loop Choices</a></h2>

                        <p>
                            Code will be graded on appropriate loop choice.  Using a while where a for loop is more appropriate will result in a deduction.  You should use a do while loop where appropriate.  Breaking out of a loop for any condition aside from the loop control will result in a deduction.
                        </p>

                        <div id="badcode">
                            <h3>Bad Code</h3>
                        </div>
                        <p>
                            Since the loop below starts at 0 and stops at 9, a for loop is much more appropriate.  Furthermore, the code uses a break statement, which can be confusing.
                        </p>
                        <div><div id="highlighter_94372" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div><div class="line number9 index8 alt2">9</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp color1 bold">int</code> <code class="cpp plain">i = 0;</code></div><div class="line number2 index1 alt1"><code class="cpp color1 bold">int</code> <code class="cpp plain">sum = 0;</code></div><div class="line number3 index2 alt2"><code class="cpp keyword bold">while</code> <code class="cpp plain">(</code><code class="cpp keyword bold">true</code><code class="cpp plain">) {</code></div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">if</code> <code class="cpp plain">(i &gt;= 10) {</code></div><div class="line number5 index4 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">break</code><code class="cpp plain">;</code></div><div class="line number6 index5 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">}</code></div><div class="line number7 index6 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">sum += Math.</code><code class="cpp functions bold">pow</code><code class="cpp plain">(2, (</code><code class="cpp color1 bold">double</code><code class="cpp plain">)i);</code></div><div class="line number8 index7 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">i++;</code></div><div class="line number9 index8 alt2"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>

                        <div id="goodcode">
                            <h3>Good Code</h3>
                        </div>
                        <div><div id="highlighter_301476" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp color1 bold">int</code> <code class="cpp plain">sum = 0;</code></div><div class="line number2 index1 alt1"><code class="cpp keyword bold">for</code> <code class="cpp plain">(</code><code class="cpp color1 bold">int</code> <code class="cpp plain">i = 0; i &lt; 10; i++) {</code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">sum += Math.</code><code class="cpp functions bold">pow</code><code class="cpp plain">(2, (</code><code class="cpp color1 bold">double</code><code class="cpp plain">)i);</code></div><div class="line number4 index3 alt1"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>




                        <div id="badcode">
                            <h3>Bad Code</h3>
                        </div>
                        <p>
                            Since the loop below starts at 0 and stops at 9, a for loop is much more appropriate.  Furthermore, the code uses a break statement, which can be confusing.
                        </p>

                        <hr>
                            <p>
                                As another example, the code below would be better stylistically in a do while loop
                            </p>
                        <div><div id="highlighter_797461" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp color1 bold">int</code> <code class="cpp plain">choice = </code><code class="cpp functions bold">rand</code><code class="cpp plain">.nextInt(4);</code></div><div class="line number2 index1 alt1"><code class="cpp keyword bold">while</code> <code class="cpp plain">(choice==temp){</code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">choice = </code><code class="cpp functions bold">rand</code><code class="cpp plain">.nextInt(4);</code></div><div class="line number4 index3 alt1"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>

                        <div id="goodcode">
                            <h3>Good Code</h3>
                        </div>
                        <div><div id="highlighter_101756" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp color1 bold">int</code> <code class="cpp plain">choice = -1;</code></div><div class="line number2 index1 alt1"><code class="cpp keyword bold">do</code> <code class="cpp plain">{</code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">choice = </code><code class="cpp functions bold">rand</code><code class="cpp plain">.nextInt(4);</code></div><div class="line number4 index3 alt1"><code class="cpp plain">}</code></div><div class="line number5 index4 alt2"><code class="cpp keyword bold">while</code> <code class="cpp plain">(choice==temp);</code></div></div></td></tr></tbody></table></div></div>

                <hr><h2><a name="exiting">7. Exiting Appropriately</a></h2>
                    <p>
                        Ending the program anywhere except for the last line of the main will result in a deduction.  (In other words, no <code>exit(0)</code> in the middle of your code)
                    </p>

                <hr><h2><a name="breaking">8. The Break Command</a></h2>
                    <p>
                        The <code>break</code> command should only appear in a <code>switch</code> statement, and not in a loop.
                    </p>

                <hr><h2><a name="goto">9. The GOTO Command</a></h2>
                    <p>
                        Do not use <code>goto</code> anywhere in your code!  It is an artifact from older programming languages and leads to <a href="https://en.wikipedia.org/wiki/Spaghetti_code">spaghetti code</a>.
                    </p>

                <hr><h2><a name="boolean">10. Positive Boolean Variable Names</a></h2>
                    <p>
                        To avoid confusion, boolean variable names should convey the positive case.  In other words <code>isReady</code>, <code>isValid</code>, <code>isProperTime</code> are good Boolean variable names.  Some not so good names are <code>readyCheck</code>, <code>notValid</code>, <code>checkTime</code>.
                    </p>

                <hr><h2><a name="booleancompare">11. Boolean Variable Comparisons</a></h2>
                <p>
                    Conditional checks must not compare booleans to <code>true</code> or false
                </p>
                
                <p>
                    </p><h2>Example 1:</h2>

                    <div id="badcode">
                        <h3>Bad Code</h3>
                    </div>
                    <div><div id="highlighter_541924" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp keyword bold">if</code> <code class="cpp plain">((isValid == </code><code class="cpp keyword bold">true</code><code class="cpp plain">) || (isReady == </code><code class="cpp keyword bold">false</code><code class="cpp plain">)) {</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">...</code></div><div class="line number3 index2 alt2"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>
                    
                    
                    <div id="goodcode">
                        <h3>Good Code</h3>
                    </div>
                    <div><div id="highlighter_202298" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp keyword bold">if</code> <code class="cpp plain">(isValid || !isReady) {</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">...</code></div><div class="line number3 index2 alt2"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>
                <p></p>

                <p>
                    </p><h2>Example 2:</h2>

                    <div id="badcode">
                        <h3>Bad Code</h3>
                    </div>
                    <div><div id="highlighter_637420" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp comments">// This code "toggles" a boolean variable</code></div><div class="line number2 index1 alt1"><code class="cpp comments">// back and forth</code></div><div class="line number3 index2 alt2"><code class="cpp keyword bold">if</code> <code class="cpp plain">(isToggled == </code><code class="cpp keyword bold">true</code><code class="cpp plain">) {</code></div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">isToggled = </code><code class="cpp keyword bold">false</code><code class="cpp plain">;</code></div><div class="line number5 index4 alt2"><code class="cpp plain">}</code></div><div class="line number6 index5 alt1"><code class="cpp keyword bold">else</code> <code class="cpp keyword bold">if</code> <code class="cpp plain">(isToggled == </code><code class="cpp keyword bold">false</code><code class="cpp plain">) {</code></div><div class="line number7 index6 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">isToggled = </code><code class="cpp keyword bold">true</code><code class="cpp plain">;</code></div><div class="line number8 index7 alt1"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>
                    
                    
                    <div id="goodcode">
                        <h3>Good Code</h3>
                    </div>
                    <div><div id="highlighter_463173" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp plain">isToggled = !isToggled;</code></div></div></td></tr></tbody></table></div></div>
                <p></p>





                <hr><h2><a name="booleanbreakup">12. Breaking Up Long Boolean Statements</a></h2>
                    <p>
                        Long conditionals should not appear as <code>while</code> or <code>if</code> conditions.  Use a <code>boolean</code> variables for readability and self-documentation
                    </p>
                    
                    <p>
    
                        </p><div id="badcode">
                            <h3>Bad Code</h3>
                        </div>
                        <div><div id="highlighter_839063" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp keyword bold">if</code> <code class="cpp plain">((value &lt;10) || (value &gt;45)) || (response ==”t”) &amp;&amp; ((season ==FALL) || (season==SPRING))){</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">...</code></div><div class="line number3 index2 alt2"><code class="cpp plain">};</code></div></div></td></tr></tbody></table></div></div>
                        
                        
                        <div id="goodcode">
                            <h3>Good Code</h3>
                        </div>
                        <div><div id="highlighter_202051" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp comments">//check if price is ok, consumer agrees, and time is right</code></div><div class="line number2 index1 alt1"><code class="cpp plain">boolean isReady =&nbsp;&nbsp; ((value &lt;10) || (value &gt;45)) </code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">&amp;&amp; (response ==”t”) </code></div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">&amp;&amp; ((season ==FALL) </code></div><div class="line number5 index4 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">|| (season==SPRING)));</code></div><div class="line number6 index5 alt1"><code class="cpp keyword bold">if</code> <code class="cpp plain">(isReady){</code></div><div class="line number7 index6 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp comments">//do some stuff</code></div><div class="line number8 index7 alt1"><code class="cpp plain">};</code></div></div></td></tr></tbody></table></div></div>
                    <p></p>




                    <hr><h2><a name="robustness">13. Robustness</a></h2>
                        <p>
                            All input must be checked.  Bad input must be handled gracefully; code must not crash on any inputs.  Bad input must not be handled silently.  If the user gives bad input, they must be notified and given a choice to re-enter or quit the program.
                        </p>
                        
                        <p>
        
                            </p><div id="badcode">
                                <h3>Bad Code</h3>
                            </div>
                            <div><div id="highlighter_572514" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp comments">// Code to convert a fraction to a decimal</code></div><div class="line number2 index1 alt1"><code class="cpp plain">Scanner in = </code><code class="cpp keyword bold">new</code> <code class="cpp plain">Scanner(System.in);</code></div><div class="line number3 index2 alt2"><code class="cpp plain">System.out.print(</code><code class="cpp string">"Enter numerator: "</code><code class="cpp plain">);</code></div><div class="line number4 index3 alt1"><code class="cpp color1 bold">double</code> <code class="cpp plain">num = in.nextDouble();</code></div><div class="line number5 index4 alt2"><code class="cpp plain">System.out.print(</code><code class="cpp string">"Enter denominator: "</code><code class="cpp plain">);</code></div><div class="line number6 index5 alt1"><code class="cpp color1 bold">double</code> <code class="cpp plain">denom = in.nextDouble();</code></div><div class="line number7 index6 alt2"><code class="cpp plain">System.out.println(num/denom);</code></div></div></td></tr></tbody></table></div></div>
                            
                            
                            <div id="goodcode">
                                <h3>Good Code</h3>
                            </div>
                            <div><div id="highlighter_247970" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div><div class="line number9 index8 alt2">9</div><div class="line number10 index9 alt1">10</div><div class="line number11 index10 alt2">11</div><div class="line number12 index11 alt1">12</div><div class="line number13 index12 alt2">13</div><div class="line number14 index13 alt1">14</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp comments">// Code to convert a fraction to a decimal</code></div><div class="line number2 index1 alt1"><code class="cpp plain">Scanner in = </code><code class="cpp keyword bold">new</code> <code class="cpp plain">Scanner(System.in);</code></div><div class="line number3 index2 alt2"><code class="cpp color1 bold">double</code> <code class="cpp plain">num = 0, denom = 0;</code></div><div class="line number4 index3 alt1"><code class="cpp keyword bold">do</code> <code class="cpp plain">{</code></div><div class="line number5 index4 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">System.out.print(</code><code class="cpp string">"Enter numerator: "</code><code class="cpp plain">);</code></div><div class="line number6 index5 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">num = in.nextDouble();</code></div><div class="line number7 index6 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">System.out.print(</code><code class="cpp string">"Enter denominator: "</code><code class="cpp plain">);</code></div><div class="line number8 index7 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">denom = in.nextDouble();</code></div><div class="line number9 index8 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">if</code> <code class="cpp plain">(denom == 0) {</code></div><div class="line number10 index9 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">System.out.println(</code><code class="cpp string">"Cannot have 0 in denominator!"</code><code class="cpp plain">);</code></div><div class="line number11 index10 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">}</code></div><div class="line number12 index11 alt1"><code class="cpp plain">}</code></div><div class="line number13 index12 alt2"><code class="cpp keyword bold">while</code> <code class="cpp plain">(denom == 0);</code></div><div class="line number14 index13 alt1"><code class="cpp plain">System.out.println(num/denom);</code></div></div></td></tr></tbody></table></div></div>
                        <p></p>



                        <hr><h2><a name="magicnumbers">14. No Magic Numbers!</a></h2>
                            <p>
                                A "magic number" is a number in the program that should be defined as a final constant, especially if it's used more than once, since the programmer only has to update it in one place to change all instances.
                            </p>
                            
                            <p>
            
                                </p><div id="badcode">
                                    <h3>Bad Code</h3>
                                </div>
                                <div><div id="highlighter_543652" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp color1 bold">double</code> <code class="cpp plain">Td = 44100/(440*Math.</code><code class="cpp functions bold">pow</code><code class="cpp plain">(2, 1/12.0));</code></div><div class="line number2 index1 alt1"><code class="cpp color1 bold">int</code> <code class="cpp plain">T = (</code><code class="cpp color1 bold">int</code><code class="cpp plain">)Math.round(Td);</code></div><div class="line number3 index2 alt2">&nbsp;</div><div class="line number4 index3 alt1"><code class="cpp color1 bold">int</code> <code class="cpp plain">N = (</code><code class="cpp color1 bold">int</code><code class="cpp plain">)(Math.round(44100*duration));</code></div></div></td></tr></tbody></table></div></div>
                                
                                
                                <div id="goodcode">
                                    <h3>Good Code</h3>
                                </div>
                                <div><div id="highlighter_899505" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div><div class="line number9 index8 alt2">9</div><div class="line number10 index9 alt1">10</div><div class="line number11 index10 alt2">11</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp comments">// The sample rate</code></div><div class="line number2 index1 alt1"><code class="cpp keyword bold">public</code> <code class="cpp keyword bold">static</code> <code class="cpp plain">final </code><code class="cpp color1 bold">int</code> <code class="cpp plain">FS = 44100;</code></div><div class="line number3 index2 alt2">&nbsp;</div><div class="line number4 index3 alt1"><code class="cpp plain">...</code></div><div class="line number5 index4 alt2">&nbsp;</div><div class="line number6 index5 alt1"><code class="cpp comments">// Compute the period one halfstep above a 440hz A</code></div><div class="line number7 index6 alt2"><code class="cpp color1 bold">double</code> <code class="cpp plain">Td = FS/(440*Math.</code><code class="cpp functions bold">pow</code><code class="cpp plain">(2, 1/12.0));</code></div><div class="line number8 index7 alt1"><code class="cpp color1 bold">int</code> <code class="cpp plain">T = (</code><code class="cpp color1 bold">int</code><code class="cpp plain">)Math.round(Td);</code></div><div class="line number9 index8 alt2">&nbsp;</div><div class="line number10 index9 alt1"><code class="cpp comments">// Compute the number of samples over a particular duration of seconds</code></div><div class="line number11 index10 alt2"><code class="cpp color1 bold">int</code> <code class="cpp plain">N = (</code><code class="cpp color1 bold">int</code><code class="cpp plain">)(Math.round(FS*duration));</code></div></div></td></tr></tbody></table></div></div>
                            <p></p>

                            <hr><h2><a name="finalcaps">15. Capitalizing Final Variables</a></h2>
                                <p>
                                    All final variables must be in all caps.
                                </p>


                                <p>
            
                                    </p><div id="badcode">
                                        <h3>Bad Code</h3>
                                    </div>
                                    <code>
                                        public static final int secondsInDay = 24*3600;
                                    </code>
                                    
                                    <br><br>
                                    <div id="goodcode">
                                        <h3>Good Code</h3>
                                    </div>
                                    <code>
                                        public static final int SECONDS_IN_DAY = 24*3600;
                                    </code>
                                <p></p>


                                <hr><h2><a name="methodsreturn">16. Methods Returning At The End</a></h2>
                                    <p>
                                        Methods may only return at the end of the method, not in the middle
                                    </p>
    
    
                                    <p>
                
                                        </p><div id="badcode">
                                            <h3>Bad Code</h3>
                                        </div>
                                        <div><div id="highlighter_618868" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp keyword bold">public</code> <code class="cpp keyword bold">static</code> <code class="cpp plain">boolean isEven(</code><code class="cpp color1 bold">int</code> <code class="cpp plain">x) {</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">if</code> <code class="cpp plain">(x % 2 == 0) {</code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">return</code> <code class="cpp keyword bold">true</code><code class="cpp plain">;</code></div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">}</code></div><div class="line number5 index4 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">return</code> <code class="cpp keyword bold">false</code><code class="cpp plain">;</code></div><div class="line number6 index5 alt1"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>
                                        
                                        
                                        <div id="goodcode">
                                            <h3>Good Code</h3>
                                        </div>
                                        <div><div id="highlighter_724644" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp keyword bold">public</code> <code class="cpp keyword bold">static</code> <code class="cpp plain">boolean isEven(</code><code class="cpp color1 bold">int</code> <code class="cpp plain">x) {</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">boolean result = </code><code class="cpp keyword bold">false</code><code class="cpp plain">;</code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">if</code> <code class="cpp plain">(x % 2 == 0) {</code></div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">result = </code><code class="cpp keyword bold">true</code><code class="cpp plain">;</code></div><div class="line number5 index4 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">}</code></div><div class="line number6 index5 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">return</code> <code class="cpp plain">result;</code></div><div class="line number7 index6 alt2"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>
                                    <p></p>



                                    <hr><h2><a name="efficient">17. Efficiently Written Code</a></h2>
                                        <p>
                                            Code must be efficient as possible without sacrificing readability.  This includes, but is not limited to chaining your if statements, using the least amount of variable declarations as possible, and using the smallest data type necessary.  For instance, if the user is to answer 1,2,3,4 as a response, use an int, not a double.
                                        </p>
        


                                        <hr><h2><a name="compoundmethods">18. Avoid Compound Method calls</a></h2>
                                            <p>
                                                Compounding methods and parameters makes your code difficult to read and debug, so split up method calls using variables when appropriate.
                                            </p>
            
            
                                            <p>
                        
                                                </p><div id="badcode">
                                                    <h3>Bad Code</h3>
                                                </div>
                                                <div><div id="highlighter_475591" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp color1 bold">int</code> <code class="cpp plain">myInt = Integer.parseInt(in.getLine().charAt(2));</code></div></div></td></tr></tbody></table></div></div>
                                                
                                                
                                                <div id="goodcode">
                                                    <h3>Good Code</h3>
                                                </div>
                                                <div><div id="highlighter_479290" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp plain">String inputLine = in.getLine();</code></div><div class="line number2 index1 alt1"><code class="cpp color1 bold">char</code> <code class="cpp plain">id = inputLine.charAt(2);</code></div><div class="line number3 index2 alt2"><code class="cpp color1 bold">int</code> <code class="cpp plain">myInt = Integer.parseInt(id);</code></div></div></td></tr></tbody></table></div></div>
                                            <p></p>



                                            <hr><h2><a name="textprompts">19. Text Input Prompts</a></h2>
                                                <p>
                                                    Prompts must be meaningful and input must appear on the same line as the prompt.  There must be a space between the prompt and the input the user gives.
                                                </p>
                
                
                                                <p>
                            
                                                    </p><div id="badcode">
                                                        <h3>Bad Code</h3>
                                                    </div>
                                                    <div><div id="highlighter_585122" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp plain">System.out.println(</code><code class="cpp string">"Enter something"</code><code class="cpp plain">);</code></div><div class="line number2 index1 alt1"><code class="cpp color1 bold">int</code> <code class="cpp plain">x = in.nextInt();</code></div></div></td></tr></tbody></table></div></div>
                                                    
                                                    
                                                    <div id="goodcode">
                                                        <h3>Good Code</h3>
                                                    </div>
                                                    <div><div id="highlighter_869946" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp plain">System.out.print(</code><code class="cpp string">"Please enter a prime number: "</code><code class="cpp plain">);</code></div><div class="line number2 index1 alt1"><code class="cpp color1 bold">int</code> <code class="cpp plain">x = </code><code class="cpp color1 bold">int</code><code class="cpp plain">.nextInt();</code></div></div></td></tr></tbody></table></div></div>
                                                <p></p>


                                            <hr><h2><a name="variablescoping">20. Variable Scoping</a></h2>

                                            <p>
                                                All variable declarations must be within the scope of a method unless the professor gives permission to put a variable within the class  scope.
                                            </p>


                
                                            <p>
                            
                                                </p><div id="badcode">
                                                    <h3>Bad Code</h3>
                                                </div>
                                                <div><div id="highlighter_688616" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div><div class="line number9 index8 alt2">9</div><div class="line number10 index9 alt1">10</div><div class="line number11 index10 alt2">11</div><div class="line number12 index11 alt1">12</div><div class="line number13 index12 alt2">13</div><div class="line number14 index13 alt1">14</div><div class="line number15 index14 alt2">15</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp color1 bold">int</code><code class="cpp plain">[] refs = {3,28,7,4,9,6,11,8,5,10,7,12};</code></div><div class="line number2 index1 alt1">&nbsp;</div><div class="line number3 index2 alt2"><code class="cpp keyword bold">public</code> <code class="cpp keyword bold">static</code> <code class="cpp color1 bold">int</code> <code class="cpp plain">getWeekday(</code><code class="cpp color1 bold">int</code> <code class="cpp plain">year, </code><code class="cpp color1 bold">int</code> <code class="cpp plain">month, </code><code class="cpp color1 bold">int</code> <code class="cpp plain">day) {</code></div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp color1 bold">int</code> <code class="cpp plain">weekday = 0;</code></div><div class="line number5 index4 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp color1 bold">int</code> <code class="cpp plain">ydoomsday=getDoomsdayYear(year);</code></div><div class="line number6 index5 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp color1 bold">int</code> <code class="cpp plain">reference = 0;</code></div><div class="line number7 index6 alt2">&nbsp;</div><div class="line number8 index7 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">if</code><code class="cpp plain">(isALeapYear(year);){</code></div><div class="line number9 index8 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">refs[0]=4;</code></div><div class="line number10 index9 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">refs[1]=29;</code></div><div class="line number11 index10 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">}</code></div><div class="line number12 index11 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">reference = refs[month-1];</code></div><div class="line number13 index12 alt2">&nbsp;</div><div class="line number14 index13 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">...</code></div><div class="line number15 index14 alt2"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>
                                                
                                                
                                                <div id="goodcode">
                                                    <h3>Good Code</h3>
                                                </div>
                                                <div><div id="highlighter_729630" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div><div class="line number9 index8 alt2">9</div><div class="line number10 index9 alt1">10</div><div class="line number11 index10 alt2">11</div><div class="line number12 index11 alt1">12</div><div class="line number13 index12 alt2">13</div><div class="line number14 index13 alt1">14</div><div class="line number15 index14 alt2">15</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp keyword bold">public</code> <code class="cpp keyword bold">static</code> <code class="cpp color1 bold">int</code> <code class="cpp plain">getWeekday(</code><code class="cpp color1 bold">int</code> <code class="cpp plain">year, </code><code class="cpp color1 bold">int</code> <code class="cpp plain">month, </code><code class="cpp color1 bold">int</code> <code class="cpp plain">day) {</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp color1 bold">int</code><code class="cpp plain">[] refs = {3,28,7,4,9,6,11,8,5,10,7,12};</code></div><div class="line number3 index2 alt2">&nbsp;</div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp color1 bold">int</code> <code class="cpp plain">weekday = 0;</code></div><div class="line number5 index4 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp color1 bold">int</code> <code class="cpp plain">ydoomsday=getDoomsdayYear(year);</code></div><div class="line number6 index5 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp color1 bold">int</code> <code class="cpp plain">reference = 0;</code></div><div class="line number7 index6 alt2">&nbsp;</div><div class="line number8 index7 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">if</code><code class="cpp plain">(isALeapYear(year);){</code></div><div class="line number9 index8 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">refs[0]=4;</code></div><div class="line number10 index9 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">refs[1]=29;</code></div><div class="line number11 index10 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">}</code></div><div class="line number12 index11 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">reference = refs[month-1];</code></div><div class="line number13 index12 alt2">&nbsp;</div><div class="line number14 index13 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">...</code></div><div class="line number15 index14 alt2"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>
                                            <p></p>


<!--Syntax highlighting in Javascript!-->
<script type="text/javascript" src="../assets/js/shCore.js.download"></script>
<script type="text/javascript" src="../assets/js/shBrushJScript.js.download"></script>
<script type="text/javascript" src="../assets/js/shBrushCpp.js.download"></script>
<script type="text/javascript" src="../assets/js/shBrushMatlabSimple.js.download"></script>
<script type="text/javascript" src="../assets/js/shBrushPython.js.download"></script>
<link type="text/css" rel="stylesheet" href="../assets/css/shCoreDefault.css">
<script type="text/javascript">SyntaxHighlighter.all();</script>