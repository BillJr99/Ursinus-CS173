---
layout: assignment
permalink: /Labs/FinancialAidCalculator
title: "CS173: Intro to Computer Science - Financial Aid Calculator"
excerpt: "CS173: Intro to Computer Science - Financial Aid Calculator"

info:
  coursenum: CS173
  githubclassroom:
    clonelink: "https://classroom.github.com/a/f2o9Azh6"
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
  - conditionals
  
---

In this lab \[[^1]\], you will practice with `if` statements and `if/else` statements, as well as with unit tests with JUnit. It will also serve as a gentle introduction/sneak preview of methods.

A non-governmental organization got a large donation to help families in need, but they have so many families to help that they need a program to help automate calculating the amount of financial assistance for each family. The amount of aid depends both on the annual household income and the number of children in the family. The rules are as follows:

* If the annual household income is greater than $40,000, then no aid is provided.
* If the annual household income is between $30,000 (inclusive) and $40,000 (inclusive), then apply the following rules:
    * If the household has three or more children, provide $1,000 per child.
    * If the household has two or fewer children, provide $500 per child.
* If the annual household income is from $20,000 (inclusive) to $30,000 (not inclusive), then apply the following rules:
    * If the household has at least two children, then provide $1,500 per child.
    * If the household has only one child, then provide $2,000 total.
* If the annual household income is less than $20,000, then provide $2100 per child.

## Part 1: Soliciting User Input (15%)

Complete an input prompt asking the user to input an integer representing the number of kids who need assistance (this is by far the quicker part).

## Part 2: Financial Assistance Calculator (85%)

Fill in the method that computes the proper amount of assistance, following the rules above.

### Hints

It is possible to do this assignment with a single stream of if/else blocks that use boolean expressions, but you may instead want to do it with nested if statements in some of them (it's your choice). Recall that a nested if statement is a statement such as the following:

```java
if (a > b) {
    // Outer block
    if (c > d) {
        // Inner block 1
    }
    else {
        // Inner block 2
    }
}
```

In this example, we don't even check `c > d` unless `a > b` passes. Just for contrast, the way to get to inner block 1 without nested if statements is with a boolean expression:

```java
if (a > b && c > d) {
    // Inner block 1
}
```

## Part 3: Unit Tests

Coming up with proper test cases is an important part of software engineering that, when done properly, saves everyone a huge headache. Good software testing frameworks allow the programmer to write a whole battery of tests that get applied every time the code is changed so that they don't have to manually input all of the tests every time.  In NetBeans, we have access to one such test framework known as JUnit, which runs a battery of tests completely separately from the main function.  You can create a test suite [in Netbeans](https://netbeans.org/kb/docs/java/junit-intro.html#Exercise_30) and write your tests there.  To run the unit tests, right click on this file and select "run," as shown below:

![Running a Unit Test in NetBeans](../images/lab-financialaidcalculator/RunUnitTest.png)

The results of all of the tests will be shown in the console. For instance, for the default skeleton code, I provided two tests, and one of them fails:

![Viewing the Results of Running a Unit Test in NetBeans](../images/lab-financialaidcalculator/TestResults.png)

The reason for this behavior is as follows. By default, the code returns a "placeholder value" of $0.0 for all income levels and number of children. The first test has a high income that should receive zero aid, so this passes just fine. However, the second case has a mid level income of $35,000 with 5 kids, that should receive a total of $5,000 in aid by the rules above. In this case, the placeholder value of $0.0 is definitely not correct, so this second test will fail until you update your code.

To get full credit for this part of the assignment, **you must create enough unit tests so that every block of code you write is covered by at least one test**. The reference solution has 6 test cases, including the first two that are provided. The easiest way to create a new test case is to simply copy and paste the code for a test case that's already there (starting with `@Test` and continuing through the end curly brace `}` ) and to rename it and update the test values. **It is recommended that you do this as you are going along.** This will really help you when debugging, and it's a lot easier than inputting values into the console over and over again.

## Extra Credit (10%)

Print the money with commas in appropriate spots. For example, print $12,000 instead of $12000. You can assume that the amount of aid is less than a million dollars, so that you will need at most one comma.

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie) and [Prof. Ann Marie Schilling](https://www.ursinus.edu/live/profiles/133-ann-marie-v-schilling)