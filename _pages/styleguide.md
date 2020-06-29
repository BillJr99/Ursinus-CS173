---
layout: default
permalink: /Style-Guide
title: "CS173: Intro to Computer Science - Style Guide"
excerpt: "CS173: Intro to Computer Science - Style Guide"

---

Style Guide
===========

As we've discussed and experienced, it's possible to write code that
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
rules.

All rules:
----------

* [Indentation/Brackets](#indentation)
* [Naming Conventions](#naming)
* [Documentation: Overview](#documentationoverview)
* [Documentation: Inline Code](#documentationinline)
* [Documentation: Methods](#documentationmethods)
* [Appropriate Loop Choices](#loopchoices)
* [Exiting Appropriately](#exiting)
* [The Break Command](#breaking)
* [The GOTO Command](#goto)
* [Positive Boolean Variable Names](#boolean)
* [Boolean Variable Comparisons](#booleancompare)
* [Breaking Up Long Boolean Statements](#booleanbreakup)
* [Robustness](#robustness)
* [No Magic Numbers!](#magicnumbers)
* [Capitalizing Final Variables](#finalcaps)
* [Methods Returning At The End](#methodsreturn)
* [Efficiently Written Code](#efficient)
* [Avoid Compound Method Calls](#compoundmethods)
* [Text Input Prompts](#textprompts)
* [Variable Scoping](#variablescoping)

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

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
                            for (int i = 0; i < 100; i++) {
                        if (i%2 == 0 && i%3 == 0)
                                System.out.println(i + " is divisible by 6");
            }
                    ]]></script>  

### Good Code

Here's a better version of the above example, in which brackets are
applied and aligned properly

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
                    for (int i = 0; i < 100; i++) {
                        if (i%2 == 0 && i%3 == 0) {
                            System.out.println(i + " is divisible by 6");
                        } 
                    }
                    ]]></script> 


<a name="naming"></a>

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

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    public static void coolstuff(int x) {
        int myvar = x;
        do {
            System.out.print(myvar + " ");
            myvar = (myvar + 7)%12;
        }
        while(myvar != x);
    }
]]></script>  

### Good Code

The method is now a verb that describes what it does, and its name and
all variables are written in camel case (assuming "halfstep" is one
word) and in descriptive language.

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    public static void printCircleOfFifths(int halfstepInit) {
        int halfstepCurr = halfstepInit;
        do {
            System.out.print(halfstepCurr + " ");
            halfstepCurr = (halfstepCurr + 7)%12;
        }
        while(halfstepCurr != halfstepInit);
    }
]]></script>

<a name="documentationoverview"></a>

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

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    /**
    * The Stack class represents a last-in-first-out stack of objects. 
    * @author  Chris Tralie CS 173
    * @version 0.1, January 2020
    * Note that this version is not thread safe.
    */ 
]]></script>

<a name="documentationinline"></a>

Documentation: Inline code
-----------------------------

All variables (except for loop counters) must be documented. Do not
state the obvious. This clutters up your code and does not convey any
information to the reader.

### Bad Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    int numCounter;  	//counts numbers
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    int numCounter; 	// Keeps track of how many 
                        // integers the user has entered
]]></script>

<a name="documentationmethods"></a>

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

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    /**
     * Returns an Image object that can then be painted on the screen. 
     * The url argument must specify an absolute {@link URL}. The name
     * argument is a specifier that is relative to the url argument. 
     * <p>
     * This method always returns immediately, whether or not the 
     * image exists. When this applet attempts to draw the image on
     * the screen, the data will be loaded. The graphics primitives 
     * that draw the image will incrementally paint on the screen. 
     *
     * @param  url  an absolute URL giving the base location of the image
     * @param  name the location of the image, relative to the url argument
     * @return      the image at the specified URL
     * @see         Image
     */
    public Image getImage(URL url, String name) {
        Image image = null;
        try {
            image = getImage(new URL(url, name));
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
        return image;
     }
]]></script>

<a name="loopchoices"></a>

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

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    int i = 0;
    int sum = 0;
    while (true) {
        if (i >= 10) {
            break;
        }
        sum += Math.pow(2, (double)i);
        i++;
    }
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    int sum = 0;
    for (int i = 0; i < 10; i++) {
        sum += Math.pow(2, (double)i);
    }
]]></script>

### Bad Code

As another example, the code below would be better stylistically in a do
while loop

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    int choice = rand.nextInt(4);
    while (choice==temp){
        choice = rand.nextInt(4);
    }
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    int choice = -1;
    do {
        choice = rand.nextInt(4);
    }
    while (choice==temp);
]]></script>

<a name="exiting"></a>

Exiting Appropriately
------------------------

Ending the program anywhere except for the last line of the main will
result in a deduction. (In other words, no `exit(0)` in the middle of
your code)

<a name="breaking"></a>

The Break Command
--------------------

The `break` command should only appear in a `switch` statement, and not
in a loop.

<a name="goto"></a>

The GOTO Command
-------------------

Do not use `goto` anywhere in your code! It is an artifact from older
programming languages and leads to [spaghetti
code](https://en.wikipedia.org/wiki/Spaghetti_code).

<a name="boolean"></a>

Positive Boolean Variable Names
-----------------------------------

To avoid confusion, boolean variable names should convey the positive
case. In other words `isReady`, `isValid`, `isProperTime` are good
Boolean variable names. Some not so good names are `readyCheck`,
`notValid`, `checkTime`.

<a name="booleancompare"></a>

Boolean Variable Comparisons
--------------------------------

Conditional checks must not compare booleans to `true` or false

Example 1:
----------

### Bad Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    if ((isValid == true) || (isReady == false)) {
        ...
    }
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    if (isValid || !isReady) {
        ...
    }
]]></script>

Example 2:
----------

### Bad Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    // This code "toggles" a boolean variable
    // back and forth
    if (isToggled == true) {
        isToggled = false;
    }
    else if (isToggled == false) {
        isToggled = true;
    }
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    isToggled = !isToggled;
]]></script>

<a name="booleanbreakup"></a>

Breaking Up Long Boolean Statements
---------------------------------------

Long conditionals should not appear as `while` or `if` conditions. Use a
`boolean` variables for readability and self-documentation

### Bad Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    if ((value <10) || (value >45)) || (response ==”t”) && ((season ==FALL) || (season==SPRING))){
        ...
    };
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    //check if price is ok, consumer agrees, and time is right
    boolean isReady = 	((value <10) || (value >45)) 
                        && (response ==”t”) 
                        && ((season ==FALL) 
                        || (season==SPRING)));
    if (isReady){
        //do some stuff
    };
]]></script>

<a name="robustness"></a>

Robustness
--------------

All input must be checked. Bad input must be handled gracefully; code
must not crash on any inputs. Bad input must not be handled silently. If
the user gives bad input, they must be notified and given a choice to
re-enter or quit the program.

### Bad Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    // Code to convert a fraction to a decimal
    Scanner in = new Scanner(System.in);
    System.out.print("Enter numerator: ");
    double num = in.nextDouble();
    System.out.print("Enter denominator: ");
    double denom = in.nextDouble();
    System.out.println(num/denom);
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    // Code to convert a fraction to a decimal
    Scanner in = new Scanner(System.in);
    double num = 0, denom = 0;
    do {
        System.out.print("Enter numerator: ");
        num = in.nextDouble();
        System.out.print("Enter denominator: ");
        denom = in.nextDouble();
        if (denom == 0) {
            System.out.println("Cannot have 0 in denominator!");
        }
    }
    while (denom == 0);
    System.out.println(num/denom);
]]></script>

<a name="magicnumbers"></a>

No Magic Numbers!
---------------------

A "magic number" is a number in the program that should be defined as a
final constant, especially if it's used more than once, since the
programmer only has to update it in one place to change all instances.

### Bad Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    double Td = 44100/(440*Math.pow(2, 1/12.0));
    int T = (int)Math.round(Td);

    int N = (int)(Math.round(44100*duration));
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    // The sample rate
    public static final int FS = 44100;

    ...
    
    // Compute the period one halfstep above a 440hz A
    double Td = FS/(440*Math.pow(2, 1/12.0));
    int T = (int)Math.round(Td);

    // Compute the number of samples over a particular duration of seconds
    int N = (int)(Math.round(FS*duration));
]]></script>

<a name="finalcaps"></a>

Capitalizing Final Variables
--------------------------------

All final variables must be in all caps.

### Bad Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    public static final int secondsInDay = 24*3600;
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    public static final int SECONDS_IN_DAY = 24*3600;
]]></script>
                                

<a name="methodsreturn"></a>

Methods Returning At The End
--------------------------------

Methods may only return at the end of the method, not in the middle

### Bad Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    public static boolean isEven(int x) {
        if (x % 2 == 0) {
            return true;
        }
        return false;
    }
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    public static boolean isEven(int x) {
        boolean result = false;
        if (x % 2 == 0) {
            result = true;
        }
        return result;
    }
]]></script>

<a name="efficient"></a>

Efficiently Written Code
----------------------------

Code must be efficient as possible without sacrificing readability. This
includes, but is not limited to chaining your if statements, using the
least amount of variable declarations as possible, and using the
smallest data type necessary. For instance, if the user is to answer
1,2,3,4 as a response, use an int, not a double.

<a name="compoundmethods"></a>

Avoid Compound Method calls
-------------------------------

Compounding methods and parameters makes your code difficult to read and
debug, so split up method calls using variables when appropriate.

### Bad Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    int myInt = Integer.parseInt(in.getLine().charAt(2));
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    String inputLine = in.getLine();
    char id = inputLine.charAt(2);
    int myInt = Integer.parseInt(id);
]]></script>

<a name="textprompts"></a>

Text Input Prompts
----------------------

Prompts must be meaningful and input must appear on the same line as the
prompt. There must be a space between the prompt and the input the user
gives.

### Bad Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    System.out.println("Enter something");
    int x = in.nextInt();
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    System.out.print("Please enter a prime number: ");
    int x = int.nextInt();
]]></script>

<a name="variablescoping"></a>

Variable Scoping
--------------------

All variable declarations must be within the scope of a method unless
the professor gives permission to put a variable within the class scope.

### Bad Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    int[] refs = {3,28,7,4,9,6,11,8,5,10,7,12};

    public static int getWeekday(int year, int month, int day) {
        int weekday = 0;
        int ydoomsday=getDoomsdayYear(year);
        int reference = 0;

        if(isALeapYear(year);){
            refs[0]=4;
            refs[1]=29;
        }
        reference = refs[month-1];

        ...
    }
]]></script>

### Good Code

<script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
    public static int getWeekday(int year, int month, int day) {
        int[] refs = {3,28,7,4,9,6,11,8,5,10,7,12};

        int weekday = 0;
        int ydoomsday=getDoomsdayYear(year);
        int reference = 0;

        if(isALeapYear(year);){
            refs[0]=4;
            refs[1]=29;
        }
        reference = refs[month-1];

        ...
    }
]]></script>
  
  
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