---
layout: assignment
permalink: /Labs/UnitTesting
title: "CS173: Intro to Computer Science - Unit Testing"
excerpt: "CS173: Intro to Computer Science - Unit Testing"

info:
  coursenum: CS173
  points: 100
  goals:
    - To design unit tests appropriate to a program
    - To implement unit tests in Java
    - To run test cases and interpret the report
    - To design unit tests for good code coverage and boundary input cases
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
    - weight: 30
      description: Code Quality and Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide
      progressing: Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions  

tags:
  - testing
  
---

In this lab, you will practice with the unit testing framework JUnit within the NetBeans IDE.

## Background: Unit Tests \[[^1]\]

Coming up with proper test cases is an important part of software engineering that, when done properly, saves everyone a huge headache. Good software testing frameworks allow the programmer to write a whole battery of tests that get applied every time the code is changed so that they don't have to manually input all of the tests every time.  In NetBeans, we have access to one such test framework known as JUnit, which runs a battery of tests completely separately from the main function.  You can create a test suite [in NetBeans](https://netbeans.org/kb/docs/java/junit-intro.html#Exercise_30) and write your tests there.  

## What to Do: Bug Hunt Challenge

Download the provided [NetBeans project](../files/lab-unittesting/UnitTestingSample.zip).  It contains several functions to perform various tasks.  Read the documentation for those functions carefully to understand what they are supposed to do.  Each function has a bug in it; you may be able to find each one by reading the code, but it is often easier to develop unit tests that expose particular code failures that you can fix.  For each function, identify test cases that might help you learn when the function would fail.  Write down your planned test case in your README and describe what you are looking to test (or what failure you are looking to expose) through that test.  Execute the unit tests, identify the bug(s), fix them, and re-run the tests until they pass.

### Creating Unit Tests 

Here is a guide on [creating unit tests in NetBeans using JUnit](../NetBeans/JUnit).  Follow it first to create a unit test class with functions to test your program.  You don't have to enter the code that you see there - that's for a test project that the tutorial walks through; instead, we'll give you test case code to use below right here on this lab page.

#### String Equality Test

When writing your `String` equality test cases, you will find that the unit tests provide default code that includes your parameters and expected return value, like this:

```java
String a = "";
String b = "";
boolean expResult = false;
```

This is because the function you are testing takes two `String` variables as parameters (`a` and `b`), and returns a `boolean`.  You can modify these to be two `String` values of your own, and the expected answer.  For example:

```java
String a = new String("Ursinus");
String b = new String("Ursinus");
boolean expResult = true;
```

This test should pass, but it will fail the first time you run it, because the function we are testing contains a bug.  Note that, for `String` parameters, I suggest creating a `new String` like in the example above.  Do not use:

```java
// don't do this!
String a = "Ursinus";
String b = "Ursinus";
boolean expResult = true;
```

... as this will merge the `String` variables `a` and `b` into a single location in memory (so the `==` operator will seem to pass these tests).

## Extra Credit (10%): New Code Samples
Do you have a code sample that you've written that you are willing to add to this lab project?  In your README, include the function that doesn't work correctly and a description of the bug, and we might share it (anonymously) in this lab for others to explore!

## Exporting your Project for Submission

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie) and [Prof. Ann Marie Schilling](https://www.ursinus.edu/live/profiles/133-ann-marie-v-schilling)
