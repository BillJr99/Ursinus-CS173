---
layout: assignment
permalink: /Labs/FinancialAidCalculator
title: "CS173: Intro to Computer Science - Financial Aid Calculator"


info:
  coursenum: CS173
  points: 100
  goals:
    - To implement an arithmetic expression into executable code
    - To map variables to expression parameters
    - To identify and implement appropriate unit test cases
  rubric:
    - weight: 40
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 20
      description: Test Cases
      preemerging: Testing was performed outside of the unit test framework, or not performed at all
      beginning: Trivial test cases are provided in a unit test framework
      progressing: Test cases that cover some, but not all, boundary cases and branches of the program are provided
      proficient: Test cases that cover all boundary cases and branches of the program are provided
    - weight: 10
      description: Code Indentation and Spacing
      preemerging: Code indentation and spacing are generally inappropriate or inconsistent
      beginning: Code indentation or spacing are generally appropriate but inconsistent in a few isolated instances
      progressing: Code indentation or spacing are appropriate or consistent, with minor adjustments needed
      proficient: Code indentation and spacing are appropriate and consistent
    - weight: 10
      description: Code Quality
      preemerging: Prior code quality feedback and style guide standards are not reflected in the submitted code to a great extent
      beginning: Code quality conforms to several standards in the course Style Guide, and progress is demonstrated in improving code quality from prior feedback
      progressing: Code quality conforms to the standards in the course Style Guide to a great extent, with a few identified areas of improvement
      proficient: Code quality substantially conforms to the standards in the course Style Guide
    - weight: 10
      description: Code Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program; specifically, javadoc style comments are present for some functions
      progressing: Code documentation is present that re-states the explicit code definitions
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program; specifically, javadoc style comments are present for all functions
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided, or the README file submitted is blank
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions
  readings:
    - rtitle: "Expressions Activity"
      rlink: "../Activities/Expressions"  
    - rtitle: "Boolean Expressions Activity"
      rlink: "../Activities/Boolean"      
    - rtitle: "Conditionals Activity"
      rlink: "../Activities/Conditionals"  
    - rtitle: "Unit Testing Tutorial"
      rlink: "../NetBeans/JUnit"
    - rtitle: "Unit Testing Video Walkthrough"
      rlink: "../Modules/Testing/Module"
  questions:
    - "On paper, how much financial aid would a household receive if their income is $35,000 with one child?  What questions did you have to ask to determine which rule to apply, and how did you compute the amount once you had the correct rule?"      

tags:
  - testing
  - conditionals
  
---

In this lab \[[^1]\], you will practice with `if` statements and `if`/`else` statements, as well as with unit tests with JUnit. It will also serve as practice writing and calling functions (also known as "methods").

A non-governmental organization got a large donation to help families in need, but they have so many families to help that they need a program to help automate calculating the amount of financial assistance for each family. The amount of aid depends both on the annual household income and the number of children in the family. The rules are as follows:

* If the annual household income is greater than $40,000, then no aid is provided.
* If the annual household income is between $30,000 (inclusive) and $40,000 (inclusive), then apply the following rules:
    * If the household has three or more children, provide $1,000 per child.
    * If the household has two or fewer children, provide $500 per child.
* If the annual household income is from $20,000 (inclusive) to $30,000 (not inclusive), then apply the following rules:
    * If the household has at least two children, then provide $1,500 per child.
    * If the household has only one child (don't forget to use `==` for this!), then provide $2,000 total.
    * If the household has no children, then no aid is provided.
* If the annual household income is less than $20,000, then provide $2,100 per child.

**Hint**: remember that numeric values in Java do not include the commas; these are only there for your reading convenience!  Also, make sure you don't return a negative value for aid if someone mistakenly reports a negative number of children (how can you check for this, and what should you calculate as the aid amount instead?)!

## Part 1: Soliciting User Input (15% of the Implementation Grade)

Create a new NetBeans project as usual.  In `main()`, complete an input prompt asking the user to input an integer representing the number of kids who need assistance (this is by far the quicker part).  You will pass these values to your `computeAssitance` function, and print the resulting financial assistance returned by `computeAssistance`.  Here is a [guide](https://www.w3schools.com/java/java_user_input.asp) on reading user input - consider the `nextDouble()` function which will read a number from the user keyboard and return a `double` variable for you to use, and the `nextInt()` function which returns an `int`.  For example:

```java
// don't forget to import java.util.Scanner; at the top (under the package line!)

// all the code below goes in your main() function

Scanner myScanner = new Scanner(System.in);

System.out.println("Enter Annual Income:");
double income = myScanner.nextDouble();
// do this again using nextInt() for numKids, which will be an int variable

// then, call your computeAssistance function, get the result, and print it!
```

## Part 2: Financial Assistance Calculator (85% of the Implementation Grade)

Create a method `double computeAssistance(double income, int numKids)`.  This function will go inside your class, along with your `main()` function.  Fill in the method that computes the proper amount of assistance, following the rules above.

Do not print anything in this function!  I suggest calculating the value of `assistanceAmount` in each `if` statement, and then you can use one single `return` statement at the bottom of the function to return that value.  See this example for the general layout.  You can print the result in your `main` function instead, and that way, you only have to write one print statement for the whole program.

```java
/** Compute the amount of financial assistance given to a family, 
 * given their income and number of children.
 * @param income The annual family income
 * @param numKids The number of children in the family
 * @return The amount of financial assistance in dollars and cents (a double)
 */
public static double computeAssistance(double income, int numKids) {
    double assistanceAmount = 0.0; // We'll start with $0 assistance as a placeholder value
    
    // Your code goes here; update assistanceAmount to the correct value according to the rules above
    // You can just update assistanceAmount inside the if statements, since we declared it at the top of this function.
    
    return assistanceAmount;
}
```

### Hints

It is possible to do this assignment with a single stream of `if`/`else` blocks that use boolean expressions, but you may instead want to do it with nested if statements in some of them (it's your choice). Recall that a nested if statement is a statement such as the following:

```java
if (a > b) {
    // Outer block
    if (c > d) {
        // Inner block 1
    }
    else {
        // Inner block 2
    }
} else {
    // Inner block 3
}
```

In this example, we don't even check `c > d` unless `a > b` passes. Just for contrast, the way to get to inner block 1 without nested if statements is with a boolean expression:

```java
if (a > b && c > d) {
    // Inner block 1
} else if(a > b) {
   // Inner block 2
} else {
   // Inner block 3
}
```

## Part 3: Unit Tests

Coming up with proper test cases is an important part of software engineering that, when done properly, saves everyone a huge headache. Good software testing frameworks allow the programmer to write a whole battery of tests that get applied every time the code is changed so that they don't have to manually input all of the tests every time.  In NetBeans, we have access to one such test framework known as JUnit, which runs a battery of tests completely separately from the main function.  You can create a test suite [in NetBeans](https://netbeans.org/kb/docs/java/junit-intro.html#Exercise_30) and write your tests there. 

**Before you begin, list the tests you'll need to write, and incldue this list in your README.  Specifically, which unit tests are needed to test all rules, including boundary cases and potential error values like a negative number of children or income?**

### Creating Unit Tests

Here is a guide on [creating unit tests in NetBeans using JUnit](../NetBeans/JUnit).  Follow it first to create a unit test class with functions to test your program.  You don't have to enter the code that you see there - that's for a test project that the tutorial walks through; instead, we'll give you test case code to use below right here on this lab page.

### Running Unit Tests

**To run the unit tests, right click on this unit test file (this is not the main class file that you normally edit in your project, but rather the unit test class file that you just created above!), and select `Test File`, as shown below (it may be called `Run File` as well, which is also fine!).**

![Running a Unit Test in NetBeans](../images/lab-financialaidcalculator/RunUnitTest.png)

The results of all of the tests will be shown in the console. For instance, for the default skeleton code, I provided two tests, and one of them fails:

![Viewing the Results of Running a Unit Test in NetBeans](../images/lab-financialaidcalculator/TestResults.png)

The reason for this behavior is as follows. By default, the code returns a "placeholder value" of $0.0 for all income levels and number of children. The first test has a high income that should receive zero aid, so this passes just fine. However, the second case has a mid level income of $35,000 with 5 kids, that should receive a total of $5,000 in aid by the rules above. In this case, the placeholder value of $0.0 is definitely not correct, so this second test will fail until you update your code.

The `assertEquals` functions takes three parameters: the expected answer, the actual answer from running the funciton, and a tolerance (how close you must get to the answer to be correct).  We want to be exact, so a third parameter of `0.0` is appropriate here.

**Note**: You may need to replace your import lines, if you see the word `jupiter` in them.  You can specify `JUnit 4` in the `Create/Update Tests` window when you create your tests (it's ok to re-create them if needed), and then delete the imports in your test file and replace them with these instead, if so:

```java
import org.junit.Test;
import static org.junit.Assert.*;
```

To get full credit for this part of the assignment, **you must create enough unit tests so that every block of code you write is covered by at least one test**. In other words, every `if` and `else` statement should be tested by at least one of your test cases, so create a `@Test` function with sample values that exercise every part of your code.  

If there is a `testMain` test, you can remove that.  It is only necessary to test the `computeAssistance` function, since `main` just obtains user input and then passes them to the `computeAssistance` function.  So these tests automatically run your function for you without asking for input!

The reference solution has 6 test cases, including the first two that are provided. The easiest way to create a new test case is to simply copy and paste the code for a test case that's already there (starting with `@Test` and continuing through the end curly brace `}` ) and to rename it and update the test values. **It is recommended that you do this as you are going along.** This will really help you when debugging, and it's a lot easier than inputting values into the console over and over again.

### Fixing Bugs with Unit Testing and the Debugger
Introduce an error into your program on purpose (like a mistake in the assistance amount formula).  Re-run your unit tests and see that at least one fails!  To fix it, set a breakpoint in your assistance function, and debug the proejct.  Type in your own values and step through to see where the bug occurs.  Fix it again, re-run your unit tests (and ensure they pass!), and describe what you did in your README.

## Extra Credit (10%)

Print the money with commas in appropriate spots. For example, print $12,000 instead of $12000. You can assume that the amount of aid is less than a million dollars, so that you will need at most one comma.  You may find [this guide](https://www.cs.colostate.edu/~cs160/.Summer16/resources/Java_printf_method_quick_reference.pdf) helpful, using a function called `System.out.printf`.

## Finishing Touches and Writeup 

Don't forget to test your program with several different inputs to help verify that things work the way you expect!  Think in terms of trying to break your program; if it's really hard to "trick" your program into getting the wrong answer, you've probably done a good job making your code robust.  

Also, check the [Style Guide](../Style-Guide) to make sure that you've written high quality code; make sure your code is "readable," well indented, uses good variable names, and includes good comments throughout the program.

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

### Exporting your Project for Submission

Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.  **Be sure to save your README file before exporting the project, so that your work is included in the submission!**

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie) and [Prof. Ann Marie Schilling](https://www.ursinus.edu/live/profiles/133-ann-marie-v-schilling)
