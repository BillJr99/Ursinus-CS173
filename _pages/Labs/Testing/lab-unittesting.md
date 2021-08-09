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
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup)
      progressing: The program is submitted according to the directions with a minor omission or correction needed
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution     

tags:
  - testing
  
---

In this lab \[[^1]\], you will practice with the unit testing framework JUnit within the NetBeans IDE.

## Unit Tests

Coming up with proper test cases is an important part of software engineering that, when done properly, saves everyone a huge headache. Good software testing frameworks allow the programmer to write a whole battery of tests that get applied every time the code is changed so that they don't have to manually input all of the tests every time.  In NetBeans, we have access to one such test framework known as JUnit, which runs a battery of tests completely separately from the main function.  You can create a test suite [in Netbeans](https://netbeans.org/kb/docs/java/junit-intro.html#Exercise_30) and write your tests there.  

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

## Exporting your Project for Submission

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie) and [Prof. Ann Marie Schilling](https://www.ursinus.edu/live/profiles/133-ann-marie-v-schilling)