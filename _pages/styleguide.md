---
layout: default
permalink: /Style-Guide
title: "CS173: Intro to Computer Science - Style Guide"
excerpt: "CS173: Intro to Computer Science - Style Guide"

---

Style Guide
===========

As we've discussed an experienced, it's possible to write code that
works, but which is completely unreadable and difficult to debug as a
result. Furthermore, we want to get you into the habit of writing good
code that is easy for others to read and which is hence *easier to
maintain*. In practice, if people can't read your code, they'll just do
it over from scratch their own way. It would be a shame for all of your
hard work to go to waste!

Below are some rules to help keep you on the rails as you design (they
have been adapted from [Professor
Schilling](https://www.ursinus.edu/live/profiles/133-ann-marie-v-schilling) and from [Professor Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-tralie)).
On many assignments, 10% of the grade will depend on adhering to these
rules

All rules:
----------

1.  [Indentation/Brackets](#indentation)
2.  [Naming Conventions](#naming)
3.  [Documentation: Overview](#documentationoverview)
4.  [Documentation: Inline Code](#documentationinline)
5.  [Documentation: Methods](#documentationmethods)
6.  [Appropriate Loop Choices](#loopchoices)
7.  [Exiting Appropriately](#xiting)
8.  [The Break Command](#breaking)
9.  [The GOTO Command](#goto)
10. [Positive Boolean Variable Names](#boolean)
11. [Boolean Variable Comparisons](#booleancompare)
12. [Breaking Up Long Boolean Statements](#booleanbreakup)
13. [Robustness](#robustness)
14. [No Magic Numbers!](#magicnumbers)
15. [Capitalizing Final Variables](#finalcaps)
16. [Methods Returning At The End](#methodsreturn)
17. [Efficiently Written Code](#efficient)
18. [Avoid Compound Method Calls](#compoundmethods)
19. [Text Input Prompts](#textprompts)
20. [Variable Scoping](#variablescoping)

<a name="indentation"></a>

Indentation / Brackets
-------------------------

All code must follow proper indentation and bracket conventions. This
includes, but is not limited to, conditionals, loops, and methods.
Brackets should be at the end of each if statement, even if the body
contains only one line. You should get into the habit of setting up your
brackets and tabbing when you first complete a method, loop, or
conditional statement, but before you type anything in it. If you go
completely off the rails, Netbeans can save you if you click
`Source->Format`

### Bad Code

First of all, this code is missing brackets around the if statement.
This makes it easy to have a bug if you decide to add the line, because
only the first line is considered to be in the body of the if statement.
Second of all, the tabbing is all over the place. This makes it easy to
miss a closing brace somewhere, which can be very difficult to resolve
for multiply nested blocks.

<div><div id="highlighter_996110" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">Top</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">for</code> <code class="cpp plain">(</code><code class="cpp color1 bold">int</code> <code class="cpp plain">i = 0; i &lt; 100; i++) {</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">if</code> <code class="cpp plain">(i%2 == 0 &amp;&amp; i%3 == 0)</code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">System.out.println(i + </code><code class="cpp string">" is divisible by 6"</code><code class="cpp plain">);</code></div><div class="line number4 index3 alt1"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>  

### Good Code

Here's a better version of the above example, in which brackets are
applied and aligned properly

<div><div id="highlighter_852586" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">Top</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp keyword bold">for</code> <code class="cpp plain">(</code><code class="cpp color1 bold">int</code> <code class="cpp plain">i = 0; i &lt; 100; i++) {</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp keyword bold">if</code> <code class="cpp plain">(i%2 == 0 &amp;&amp; i%3 == 0) {</code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">System.out.println(i + </code><code class="cpp string">" is divisible by 6"</code><code class="cpp plain">);</code></div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">} </code></div><div class="line number5 index4 alt2"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div> 

* * * * *

Naming Conventions
---------------------

-   Variable and method names should be in [camel
    case](https://en.wikipedia.org/wiki/Camel_case); that is, the first
    letter should be in lower case, and each new word should be
    capitalized, with no spaces or underscores in between the words.
-   Variables and methods should be descriptive of what the variable
    holds.
-   For loop counters should be something short such as `i`, `j`, or
    `k`. You may also use a descriptive, but still short, name for a for
    loop counter such as `row` or `col`

-   Method names should start with a verb (this includes boolean methods
    that start with the verb "is").

### Bad Code

The names of the variables are not descriptive, and the method is not
written as a verb or in camel case.

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `public`{.cpp .keyword .bold}
  2                                    `static`{.cpp .keyword .bold}
  3                                    `void`{.cpp .keyword .bold}
  4                                    `coolstuff(`{.cpp .plain}`int`{.cpp
  5                                    .color1 .bold} `x) {`{.cpp .plain}
  6                                    `    `{.cpp .spaces}`int`{.cpp
  7                                    .color1 .bold} `myvar = x;`{.cpp
  8                                    .plain}
                                       `    `{.cpp .spaces}`do`{.cpp
                                       .keyword .bold} `{`{.cpp .plain}
                                       `        `{.cpp
                                       .spaces}`System.out.print(myvar + `{
                                       .cpp
                                       .plain}`" "`{.cpp .string}`);`{.cpp
                                       .plain}
                                       `        `{.cpp
                                       .spaces}`myvar = (myvar + 7)%12;`{.c
                                       pp
                                       .plain}
                                       `    `{.cpp .spaces}`}`{.cpp .plain}
                                       `    `{.cpp .spaces}`while`{.cpp
                                       .keyword .bold}`(myvar != x);`{.cpp
                                       .plain}
                                       `}`{.cpp .plain}
  ------------------------------------ ------------------------------------

### Good Code

The method is now a verb that describes what it does, and its name and
all variables are written in camel case (assuming "halfstep" is one
word) and in descriptive language.

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `public`{.cpp .keyword .bold}
  2                                    `static`{.cpp .keyword .bold}
  3                                    `void`{.cpp .keyword .bold}
  4                                    `printCircleOfFifths(`{.cpp
  5                                    .plain}`int`{.cpp .color1 .bold}
  6                                    `halfstepInit) {`{.cpp .plain}
  7                                    `    `{.cpp .spaces}`int`{.cpp
  8                                    .color1 .bold}
                                       `halfstepCurr = halfstepInit;`{.cpp
                                       .plain}
                                       `    `{.cpp .spaces}`do`{.cpp
                                       .keyword .bold} `{`{.cpp .plain}
                                       `        `{.cpp
                                       .spaces}`System.out.print(halfstepCu
                                       rr + `{.cpp
                                       .plain}`" "`{.cpp .string}`);`{.cpp
                                       .plain}
                                       `        `{.cpp
                                       .spaces}`halfstepCurr = (halfstepCur
                                       r + 7)%12;`{.cpp
                                       .plain}
                                       `    `{.cpp .spaces}`}`{.cpp .plain}
                                       `    `{.cpp .spaces}`while`{.cpp
                                       .keyword
                                       .bold}`(halfstepCurr != halfstepInit
                                       );`{.cpp
                                       .plain}
                                       `}`{.cpp .plain}
  ------------------------------------ ------------------------------------

* * * * *

Documentation: Overview
--------------------------

All files must have comments near the top of the main program’s file
containing the following information: Author’s name, Assignment name,
Date, Class, Short description of the project. For complete information
on writing Java documentation, visit [this
link](http://www.ctralie.com/Teaching/CS173_S2020/www.oracle.com/technetwork/java/javase/tech/index-137868.html)
or [this
link](http://www.tutorialspoint.com/java/java_documentation.htm). As an
example, here's a comment at the top of a file

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `/**`{.cpp .comments}
  2                                    `* The Stack class represents a last
  3                                    -in-first-out stack of objects. `{.c
  4                                    pp
  5                                    .comments}
  6                                    `* @author  Chris Tralie CS 173`{.cp
                                       p
                                       .comments}
                                       `* @version 0.1, January 2020`{.cpp
                                       .comments}
                                       `* Note that this version is not thr
                                       ead safe.`{.cpp
                                       .comments}
                                       `*/`{.cpp .comments}
  ------------------------------------ ------------------------------------

* * * * *

Documentation: Inline code
-----------------------------

All variables (except for loop counters) must be documented. Do not
state the obvious. This clutters up your code and does not convey any
information to the reader.

### Bad Code

[?](#)

  --- ---------------------------------------------------------------------------------------------
  1   `int`{.cpp .color1 .bold} `numCounter;     `{.cpp .plain}`//counts numbers`{.cpp .comments}
  --- ---------------------------------------------------------------------------------------------

### Good Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `int`{.cpp .color1 .bold}
  2                                    `numCounter;     `{.cpp
                                       .plain}`// Keeps track of how many `
                                       {.cpp
                                       .comments}
                                       `                    `{.cpp
                                       .spaces}`// integers the user has en
                                       tered`{.cpp
                                       .comments}
  ------------------------------------ ------------------------------------

* * * * *

Documentation: Methods
-------------------------

All methods will have documentation including, but not limited to:

1.  Method summary
2.  Parameter descriptions
3.  Return value descriptions

These comments should appear above the method name in a particular
format, which makes it easy to automatically generate web pages
describing the code (for instance, see documentation for the [audio
code](https://algs4.cs.princeton.edu/code/javadoc/edu/princeton/cs/algs4/StdAudio.html)
we've been using, which was generated this way). In NetBeans, if you
type out the definition of the method and then type `/**` followed by
`ENTER`, it will automatically generate a correctly formatted comment,
which you can fill in with details. Below is an example (courtesy of
[Professor
Schilling](https://www.ursinus.edu/live/profiles/133-ann-marie-v-schilling))
of what it should look like:

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `/**`{.cpp .comments}
  2                                    ` `{.cpp
  3                                    .spaces}`* Returns an Image object t
  4                                    hat can then be painted on the scree
  5                                    n. `{.cpp
  6                                    .comments}
  7                                    ` `{.cpp
  8                                    .spaces}`* The url argument must spe
  9                                    cify an absolute {@link URL}. The na
  10                                   me`{.cpp
  11                                   .comments}
  12                                   ` `{.cpp
  13                                   .spaces}`* argument is a specifier t
  14                                   hat is relative to the url argument.
  15                                    `{.cpp
  16                                   .comments}
  17                                   ` `{.cpp .spaces}`* <p>`{.cpp
  18                                   .comments}
  19                                   ` `{.cpp
  20                                   .spaces}`* This method always return
  21                                   s immediately, whether or not the `{
  22                                   .cpp
  23                                   .comments}
  24                                   ` `{.cpp
                                       .spaces}`* image exists. When this a
                                       pplet attempts to draw the image on`
                                       {.cpp
                                       .comments}
                                       ` `{.cpp
                                       .spaces}`* the screen, the data will
                                        be loaded. The graphics primitives 
                                       `{.cpp
                                       .comments}
                                       ` `{.cpp
                                       .spaces}`* that draw the image will 
                                       incrementally paint on the screen. `
                                       {.cpp
                                       .comments}
                                       ` `{.cpp .spaces}`*`{.cpp .comments}
                                       ` `{.cpp
                                       .spaces}`* @param  url  an absolute 
                                       URL giving the base location of the 
                                       image`{.cpp
                                       .comments}
                                       ` `{.cpp
                                       .spaces}`* @param  name the location
                                        of the image, relative to the url a
                                       rgument`{.cpp
                                       .comments}
                                       ` `{.cpp
                                       .spaces}`* @return      the image at
                                        the specified URL`{.cpp
                                       .comments}
                                       ` `{.cpp
                                       .spaces}`* @see         Image`{.cpp
                                       .comments}
                                       ` `{.cpp .spaces}`*/`{.cpp
                                       .comments}
                                       `public`{.cpp .keyword .bold}
                                       `Image getImage(URL url, String name
                                       ) {`{.cpp
                                       .plain}
                                       `    `{.cpp
                                       .spaces}`Image image = null;`{.cpp
                                       .plain}
                                       `    `{.cpp .spaces}`try`{.cpp
                                       .keyword .bold} `{`{.cpp .plain}
                                       `        `{.cpp
                                       .spaces}`image = getImage(`{.cpp
                                       .plain}`new`{.cpp .keyword .bold}
                                       `URL(url, name));`{.cpp .plain}
                                       `    `{.cpp .spaces}`} `{.cpp
                                       .plain}`catch`{.cpp .keyword .bold}
                                       `(MalformedURLException e) {`{.cpp
                                       .plain}
                                       `        `{.cpp
                                       .spaces}`e.printStackTrace();`{.cpp
                                       .plain}
                                       `    `{.cpp .spaces}`}`{.cpp .plain}
                                       `    `{.cpp .spaces}`return`{.cpp
                                       .keyword .bold} `image;`{.cpp
                                       .plain}
                                       ` `{.cpp .spaces}`}`{.cpp .plain}
  ------------------------------------ ------------------------------------

* * * * *

Appropriate Loop Choices
---------------------------

Code will be graded on appropriate loop choice. Using a while where a
for loop is more appropriate will result in a deduction. You should use
a do while loop where appropriate. Breaking out of a loop for any
condition aside from the loop control will result in a deduction.

### Bad Code

Since the loop below starts at 0 and stops at 9, a for loop is much more
appropriate. Furthermore, the code uses a break statement, which can be
confusing.

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `int`{.cpp .color1 .bold}
  2                                    `i = 0;`{.cpp .plain}
  3                                    `int`{.cpp .color1 .bold}
  4                                    `sum = 0;`{.cpp .plain}
  5                                    `while`{.cpp .keyword .bold}
  6                                    `(`{.cpp .plain}`true`{.cpp .keyword
  7                                    .bold}`) {`{.cpp .plain}
  8                                    `    `{.cpp .spaces}`if`{.cpp
  9                                    .keyword .bold} `(i >= 10) {`{.cpp
                                       .plain}
                                       `        `{.cpp .spaces}`break`{.cpp
                                       .keyword .bold}`;`{.cpp .plain}
                                       `    `{.cpp .spaces}`}`{.cpp .plain}
                                       `    `{.cpp
                                       .spaces}`sum += Math.`{.cpp
                                       .plain}`pow`{.cpp .functions
                                       .bold}`(2, (`{.cpp
                                       .plain}`double`{.cpp .color1
                                       .bold}`)i);`{.cpp .plain}
                                       `    `{.cpp .spaces}`i++;`{.cpp
                                       .plain}
                                       `}`{.cpp .plain}
  ------------------------------------ ------------------------------------

### Good Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `int`{.cpp .color1 .bold}
  2                                    `sum = 0;`{.cpp .plain}
  3                                    `for`{.cpp .keyword .bold} `(`{.cpp
  4                                    .plain}`int`{.cpp .color1 .bold}
                                       `i = 0; i < 10; i++) {`{.cpp .plain}
                                       `    `{.cpp
                                       .spaces}`sum += Math.`{.cpp
                                       .plain}`pow`{.cpp .functions
                                       .bold}`(2, (`{.cpp
                                       .plain}`double`{.cpp .color1
                                       .bold}`)i);`{.cpp .plain}
                                       `}`{.cpp .plain}
  ------------------------------------ ------------------------------------

### Bad Code

Since the loop below starts at 0 and stops at 9, a for loop is much more
appropriate. Furthermore, the code uses a break statement, which can be
confusing.

* * * * *

As another example, the code below would be better stylistically in a do
while loop

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `int`{.cpp .color1 .bold}
  2                                    `choice = `{.cpp .plain}`rand`{.cpp
  3                                    .functions .bold}`.nextInt(4);`{.cpp
  4                                    .plain}
                                       `while`{.cpp .keyword .bold}
                                       `(choice==temp){`{.cpp .plain}
                                       `    `{.cpp .spaces}`choice = `{.cpp
                                       .plain}`rand`{.cpp .functions
                                       .bold}`.nextInt(4);`{.cpp .plain}
                                       `}`{.cpp .plain}
  ------------------------------------ ------------------------------------

### Good Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `int`{.cpp .color1 .bold}
  2                                    `choice = -1;`{.cpp .plain}
  3                                    `do`{.cpp .keyword .bold} `{`{.cpp
  4                                    .plain}
  5                                    `    `{.cpp .spaces}`choice = `{.cpp
                                       .plain}`rand`{.cpp .functions
                                       .bold}`.nextInt(4);`{.cpp .plain}
                                       `}`{.cpp .plain}
                                       `while`{.cpp .keyword .bold}
                                       `(choice==temp);`{.cpp .plain}
  ------------------------------------ ------------------------------------

* * * * *

Exiting Appropriately
------------------------

Ending the program anywhere except for the last line of the main will
result in a deduction. (In other words, no `exit(0)` in the middle of
your code)

* * * * *

The Break Command
--------------------

The `break` command should only appear in a `switch` statement, and not
in a loop.

* * * * *

The GOTO Command
-------------------

Do not use `goto` anywhere in your code! It is an artifact from older
programming languages and leads to [spaghetti
code](https://en.wikipedia.org/wiki/Spaghetti_code).

* * * * *

Positive Boolean Variable Names
-----------------------------------

To avoid confusion, boolean variable names should convey the positive
case. In other words `isReady`, `isValid`, `isProperTime` are good
Boolean variable names. Some not so good names are `readyCheck`,
`notValid`, `checkTime`.

* * * * *

Boolean Variable Comparisons
--------------------------------

Conditional checks must not compare booleans to `true` or false

Example 1:
----------

### Bad Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `if`{.cpp .keyword .bold}
  2                                    `((isValid == `{.cpp
  3                                    .plain}`true`{.cpp .keyword
                                       .bold}`) || (isReady == `{.cpp
                                       .plain}`false`{.cpp .keyword
                                       .bold}`)) {`{.cpp .plain}
                                       `    `{.cpp .spaces}`...`{.cpp
                                       .plain}
                                       `}`{.cpp .plain}
  ------------------------------------ ------------------------------------

### Good Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `if`{.cpp .keyword .bold}
  2                                    `(isValid || !isReady) {`{.cpp
  3                                    .plain}
                                       `    `{.cpp .spaces}`...`{.cpp
                                       .plain}
                                       `}`{.cpp .plain}
  ------------------------------------ ------------------------------------

Example 2:
----------

### Bad Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `// This code "toggles" a boolean va
  2                                    riable`{.cpp
  3                                    .comments}
  4                                    `// back and forth`{.cpp .comments}
  5                                    `if`{.cpp .keyword .bold}
  6                                    `(isToggled == `{.cpp
  7                                    .plain}`true`{.cpp .keyword
  8                                    .bold}`) {`{.cpp .plain}
                                       `    `{.cpp
                                       .spaces}`isToggled = `{.cpp
                                       .plain}`false`{.cpp .keyword
                                       .bold}`;`{.cpp .plain}
                                       `}`{.cpp .plain}
                                       `else`{.cpp .keyword .bold}
                                       `if`{.cpp .keyword .bold}
                                       `(isToggled == `{.cpp
                                       .plain}`false`{.cpp .keyword
                                       .bold}`) {`{.cpp .plain}
                                       `    `{.cpp
                                       .spaces}`isToggled = `{.cpp
                                       .plain}`true`{.cpp .keyword
                                       .bold}`;`{.cpp .plain}
                                       `}`{.cpp .plain}
  ------------------------------------ ------------------------------------

### Good Code

[?](#)

  --- ----------------------------------------
  1   `isToggled = !isToggled;`{.cpp .plain}
  --- ----------------------------------------

* * * * *

Breaking Up Long Boolean Statements
---------------------------------------

Long conditionals should not appear as `while` or `if` conditions. Use a
`boolean` variables for readability and self-documentation

### Bad Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `if`{.cpp .keyword .bold}
  2                                    `((value <10) || (value >45)) || (re
  3                                    sponse ==”t”) && ((season ==FALL) ||
                                        (season==SPRING))){`{.cpp
                                       .plain}
                                       `    `{.cpp .spaces}`...`{.cpp
                                       .plain}
                                       `};`{.cpp .plain}
  ------------------------------------ ------------------------------------

### Good Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `//check if price is ok, consumer ag
  2                                    rees, and time is right`{.cpp
  3                                    .comments}
  4                                    `boolean isReady =   ((value <10) ||
  5                                     (value >45)) `{.cpp
  6                                    .plain}
  7                                    `                    `{.cpp
  8                                    .spaces}`&& (response ==”t”) `{.cpp
                                       .plain}
                                       `                    `{.cpp
                                       .spaces}`&& ((season ==FALL) `{.cpp
                                       .plain}
                                       `                    `{.cpp
                                       .spaces}`|| (season==SPRING)));`{.cp
                                       p
                                       .plain}
                                       `if`{.cpp .keyword .bold}
                                       `(isReady){`{.cpp .plain}
                                       `    `{.cpp
                                       .spaces}`//do some stuff`{.cpp
                                       .comments}
                                       `};`{.cpp .plain}
  ------------------------------------ ------------------------------------

* * * * *

Robustness
--------------

All input must be checked. Bad input must be handled gracefully; code
must not crash on any inputs. Bad input must not be handled silently. If
the user gives bad input, they must be notified and given a choice to
re-enter or quit the program.

### Bad Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `// Code to convert a fraction to a 
  2                                    decimal`{.cpp
  3                                    .comments}
  4                                    `Scanner in = `{.cpp
  5                                    .plain}`new`{.cpp .keyword .bold}
  6                                    `Scanner(System.in);`{.cpp .plain}
  7                                    `System.out.print(`{.cpp
                                       .plain}`"Enter numerator: "`{.cpp
                                       .string}`);`{.cpp .plain}
                                       `double`{.cpp .color1 .bold}
                                       `num = in.nextDouble();`{.cpp
                                       .plain}
                                       `System.out.print(`{.cpp
                                       .plain}`"Enter denominator: "`{.cpp
                                       .string}`);`{.cpp .plain}
                                       `double`{.cpp .color1 .bold}
                                       `denom = in.nextDouble();`{.cpp
                                       .plain}
                                       `System.out.println(num/denom);`{.cp
                                       p
                                       .plain}
  ------------------------------------ ------------------------------------

### Good Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `// Code to convert a fraction to a 
  2                                    decimal`{.cpp
  3                                    .comments}
  4                                    `Scanner in = `{.cpp
  5                                    .plain}`new`{.cpp .keyword .bold}
  6                                    `Scanner(System.in);`{.cpp .plain}
  7                                    `double`{.cpp .color1 .bold}
  8                                    `num = 0, denom = 0;`{.cpp .plain}
  9                                    `do`{.cpp .keyword .bold} `{`{.cpp
  10                                   .plain}
  11                                   `    `{.cpp
  12                                   .spaces}`System.out.print(`{.cpp
  13                                   .plain}`"Enter numerator: "`{.cpp
  14                                   .string}`);`{.cpp .plain}
                                       `    `{.cpp
                                       .spaces}`num = in.nextDouble();`{.cp
                                       p
                                       .plain}
                                       `    `{.cpp
                                       .spaces}`System.out.print(`{.cpp
                                       .plain}`"Enter denominator: "`{.cpp
                                       .string}`);`{.cpp .plain}
                                       `    `{.cpp
                                       .spaces}`denom = in.nextDouble();`{.
                                       cpp
                                       .plain}
                                       `    `{.cpp .spaces}`if`{.cpp
                                       .keyword .bold}
                                       `(denom == 0) {`{.cpp .plain}
                                       `        `{.cpp
                                       .spaces}`System.out.println(`{.cpp
                                       .plain}`"Cannot have 0 in denominato
                                       r!"`{.cpp
                                       .string}`);`{.cpp .plain}
                                       `    `{.cpp .spaces}`}`{.cpp .plain}
                                       `}`{.cpp .plain}
                                       `while`{.cpp .keyword .bold}
                                       `(denom == 0);`{.cpp .plain}
                                       `System.out.println(num/denom);`{.cp
                                       p
                                       .plain}
  ------------------------------------ ------------------------------------

* * * * *

No Magic Numbers!
---------------------

A "magic number" is a number in the program that should be defined as a
final constant, especially if it's used more than once, since the
programmer only has to update it in one place to change all instances.

### Bad Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `double`{.cpp .color1 .bold}
  2                                    `Td = 44100/(440*Math.`{.cpp
  3                                    .plain}`pow`{.cpp .functions
  4                                    .bold}`(2, 1/12.0));`{.cpp .plain}
                                       `int`{.cpp .color1 .bold}
                                       `T = (`{.cpp .plain}`int`{.cpp
                                       .color1
                                       .bold}`)Math.round(Td);`{.cpp
                                       .plain}
                                        
                                       `int`{.cpp .color1 .bold}
                                       `N = (`{.cpp .plain}`int`{.cpp
                                       .color1
                                       .bold}`)(Math.round(44100*duration))
                                       ;`{.cpp
                                       .plain}
  ------------------------------------ ------------------------------------

### Good Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `// The sample rate`{.cpp .comments}
  2                                    `public`{.cpp .keyword .bold}
  3                                    `static`{.cpp .keyword .bold}
  4                                    `final `{.cpp .plain}`int`{.cpp
  5                                    .color1 .bold} `FS = 44100;`{.cpp
  6                                    .plain}
  7                                     
  8                                    `...`{.cpp .plain}
  9                                     
  10                                   `// Compute the period one halfstep 
  11                                   above a 440hz A`{.cpp
                                       .comments}
                                       `double`{.cpp .color1 .bold}
                                       `Td = FS/(440*Math.`{.cpp
                                       .plain}`pow`{.cpp .functions
                                       .bold}`(2, 1/12.0));`{.cpp .plain}
                                       `int`{.cpp .color1 .bold}
                                       `T = (`{.cpp .plain}`int`{.cpp
                                       .color1
                                       .bold}`)Math.round(Td);`{.cpp
                                       .plain}
                                        
                                       `// Compute the number of samples ov
                                       er a particular duration of seconds`
                                       {.cpp
                                       .comments}
                                       `int`{.cpp .color1 .bold}
                                       `N = (`{.cpp .plain}`int`{.cpp
                                       .color1
                                       .bold}`)(Math.round(FS*duration));`{
                                       .cpp
                                       .plain}
  ------------------------------------ ------------------------------------

* * * * *

Capitalizing Final Variables
--------------------------------

All final variables must be in all caps.

### Bad Code

`                                         public static final int secondsInDay = 24*3600;                                     `
\
\

### Good Code

`                                         public static final int SECONDS_IN_DAY = 24*3600;                                     `

* * * * *

Methods Returning At The End
--------------------------------

Methods may only return at the end of the method, not in the middle

### Bad Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `public`{.cpp .keyword .bold}
  2                                    `static`{.cpp .keyword .bold}
  3                                    `boolean isEven(`{.cpp
  4                                    .plain}`int`{.cpp .color1 .bold}
  5                                    `x) {`{.cpp .plain}
  6                                    `    `{.cpp .spaces}`if`{.cpp
                                       .keyword .bold}
                                       `(x % 2 == 0) {`{.cpp .plain}
                                       `        `{.cpp
                                       .spaces}`return`{.cpp .keyword
                                       .bold} `true`{.cpp .keyword
                                       .bold}`;`{.cpp .plain}
                                       `    `{.cpp .spaces}`}`{.cpp .plain}
                                       `    `{.cpp .spaces}`return`{.cpp
                                       .keyword .bold} `false`{.cpp
                                       .keyword .bold}`;`{.cpp .plain}
                                       `}`{.cpp .plain}
  ------------------------------------ ------------------------------------

### Good Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `public`{.cpp .keyword .bold}
  2                                    `static`{.cpp .keyword .bold}
  3                                    `boolean isEven(`{.cpp
  4                                    .plain}`int`{.cpp .color1 .bold}
  5                                    `x) {`{.cpp .plain}
  6                                    `    `{.cpp
  7                                    .spaces}`boolean result = `{.cpp
                                       .plain}`false`{.cpp .keyword
                                       .bold}`;`{.cpp .plain}
                                       `    `{.cpp .spaces}`if`{.cpp
                                       .keyword .bold}
                                       `(x % 2 == 0) {`{.cpp .plain}
                                       `        `{.cpp
                                       .spaces}`result = `{.cpp
                                       .plain}`true`{.cpp .keyword
                                       .bold}`;`{.cpp .plain}
                                       `    `{.cpp .spaces}`}`{.cpp .plain}
                                       `    `{.cpp .spaces}`return`{.cpp
                                       .keyword .bold} `result;`{.cpp
                                       .plain}
                                       `}`{.cpp .plain}
  ------------------------------------ ------------------------------------

* * * * *

Efficiently Written Code
----------------------------

Code must be efficient as possible without sacrificing readability. This
includes, but is not limited to chaining your if statements, using the
least amount of variable declarations as possible, and using the
smallest data type necessary. For instance, if the user is to answer
1,2,3,4 as a response, use an int, not a double.

* * * * *

Avoid Compound Method calls
-------------------------------

Compounding methods and parameters makes your code difficult to read and
debug, so split up method calls using variables when appropriate.

### Bad Code

[?](#)

  --- --------------------------------------------------------------------------------------------
  1   `int`{.cpp .color1 .bold} `myInt = Integer.parseInt(in.getLine().charAt(2));`{.cpp .plain}
  --- --------------------------------------------------------------------------------------------

### Good Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `String inputLine = in.getLine();`{.
  2                                    cpp
  3                                    .plain}
                                       `char`{.cpp .color1 .bold}
                                       `id = inputLine.charAt(2);`{.cpp
                                       .plain}
                                       `int`{.cpp .color1 .bold}
                                       `myInt = Integer.parseInt(id);`{.cpp
                                       .plain}
  ------------------------------------ ------------------------------------

* * * * *

Text Input Prompts
----------------------

Prompts must be meaningful and input must appear on the same line as the
prompt. There must be a space between the prompt and the input the user
gives.

### Bad Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `System.out.println(`{.cpp
  2                                    .plain}`"Enter something"`{.cpp
                                       .string}`);`{.cpp .plain}
                                       `int`{.cpp .color1 .bold}
                                       `x = in.nextInt();`{.cpp .plain}
  ------------------------------------ ------------------------------------

### Good Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `System.out.print(`{.cpp
  2                                    .plain}`"Please enter a prime number
                                       : "`{.cpp
                                       .string}`);`{.cpp .plain}
                                       `int`{.cpp .color1 .bold}
                                       `x = `{.cpp .plain}`int`{.cpp
                                       .color1 .bold}`.nextInt();`{.cpp
                                       .plain}
  ------------------------------------ ------------------------------------

* * * * *

Variable Scoping
--------------------

All variable declarations must be within the scope of a method unless
the professor gives permission to put a variable within the class scope.

### Bad Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `int`{.cpp .color1
  2                                    .bold}`[] refs = {3,28,7,4,9,6,11,8,
  3                                    5,10,7,12};`{.cpp
  4                                    .plain}
  5                                     
  6                                    `public`{.cpp .keyword .bold}
  7                                    `static`{.cpp .keyword .bold}
  8                                    `int`{.cpp .color1 .bold}
  9                                    `getWeekday(`{.cpp .plain}`int`{.cpp
  10                                   .color1 .bold} `year, `{.cpp
  11                                   .plain}`int`{.cpp .color1 .bold}
  12                                   `month, `{.cpp .plain}`int`{.cpp
  13                                   .color1 .bold} `day) {`{.cpp .plain}
  14                                   `    `{.cpp .spaces}`int`{.cpp
  15                                   .color1 .bold} `weekday = 0;`{.cpp
                                       .plain}
                                       `    `{.cpp .spaces}`int`{.cpp
                                       .color1 .bold}
                                       `ydoomsday=getDoomsdayYear(year);`{.
                                       cpp
                                       .plain}
                                       `    `{.cpp .spaces}`int`{.cpp
                                       .color1 .bold} `reference = 0;`{.cpp
                                       .plain}
                                        
                                       `    `{.cpp .spaces}`if`{.cpp
                                       .keyword
                                       .bold}`(isALeapYear(year);){`{.cpp
                                       .plain}
                                       `        `{.cpp
                                       .spaces}`refs[0]=4;`{.cpp .plain}
                                       `        `{.cpp
                                       .spaces}`refs[1]=29;`{.cpp .plain}
                                       `    `{.cpp .spaces}`}`{.cpp .plain}
                                       `    `{.cpp
                                       .spaces}`reference = refs[month-1];`
                                       {.cpp
                                       .plain}
                                        
                                       `    `{.cpp .spaces}`...`{.cpp
                                       .plain}
                                       `}`{.cpp .plain}
  ------------------------------------ ------------------------------------

### Good Code

[?](#)

  ------------------------------------ ------------------------------------
  1                                    `public`{.cpp .keyword .bold}
  2                                    `static`{.cpp .keyword .bold}
  3                                    `int`{.cpp .color1 .bold}
  4                                    `getWeekday(`{.cpp .plain}`int`{.cpp
  5                                    .color1 .bold} `year, `{.cpp
  6                                    .plain}`int`{.cpp .color1 .bold}
  7                                    `month, `{.cpp .plain}`int`{.cpp
  8                                    .color1 .bold} `day) {`{.cpp .plain}
  9                                    `    `{.cpp .spaces}`int`{.cpp
  10                                   .color1
  11                                   .bold}`[] refs = {3,28,7,4,9,6,11,8,
  12                                   5,10,7,12};`{.cpp
  13                                   .plain}
  14                                    
  15                                   `    `{.cpp .spaces}`int`{.cpp
                                       .color1 .bold} `weekday = 0;`{.cpp
                                       .plain}
                                       `    `{.cpp .spaces}`int`{.cpp
                                       .color1 .bold}
                                       `ydoomsday=getDoomsdayYear(year);`{.
                                       cpp
                                       .plain}
                                       `    `{.cpp .spaces}`int`{.cpp
                                       .color1 .bold} `reference = 0;`{.cpp
                                       .plain}
                                        
                                       `    `{.cpp .spaces}`if`{.cpp
                                       .keyword
                                       .bold}`(isALeapYear(year);){`{.cpp
                                       .plain}
                                       `        `{.cpp
                                       .spaces}`refs[0]=4;`{.cpp .plain}
                                       `        `{.cpp
                                       .spaces}`refs[1]=29;`{.cpp .plain}
                                       `    `{.cpp .spaces}`}`{.cpp .plain}
                                       `    `{.cpp
                                       .spaces}`reference = refs[month-1];`
                                       {.cpp
                                       .plain}
                                        
                                       `    `{.cpp .spaces}`...`{.cpp
                                       .plain}
                                       `}`{.cpp .plain}
  ------------------------------------ ------------------------------------
  
  
<script src="{{ site.baseurl }}/assets/js/jquery.min.js"></script>
<script src="{{ site.baseurl }}/assets/js/skel.min.js"></script>
<script src="{{ site.baseurl }}/assets/js/util.js"></script>
<script src="{{ site.baseurl }}/assets/js/main.js"></script>
<script type="text/javascript" src="{{ site.baseurl }}/assets/js/shCore.js"></script>
<script type="text/javascript" src="{{ site.baseurl }}/assets/js/shBrushJScript.js"></script>
<script type="text/javascript" src="{{ site.baseurl }}/assets/js/shBrushCpp.js"></script>
<script type="text/javascript" src="{{ site.baseurl }}/assets/js/shBrushMatlabSimple.js"></script>
<script type="text/javascript" src="{{ site.baseurl }}/assets/js/shBrushPython.js"></script>
<link type="text/css" rel="stylesheet" href="{{ site.baseurl }}/assets/css/shCoreDefault.css">
<script type="text/javascript">SyntaxHighlighter.all();</script>		
<script src="{{ site.baseurl }}/assets/js/polyfill.min.js"></script>
<script id="MathJax-script" async="" src="{{ site.baseurl }}/assets/js/tex-mml-chtml.js"></script>	            