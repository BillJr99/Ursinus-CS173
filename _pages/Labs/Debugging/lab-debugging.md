---
layout: assignment
permalink: /Labs/Debugging
title: "CS173: Intro to Computer Science - Using the Debugger"
excerpt: "CS173: Intro to Computer Science - Using the Debugger"

info:
  coursenum: CS173
  githubclassroom:
    clonelink: false
  points: 100
  goals:
    - To use the debugger to identify code bugs
  rubric:
    - weight: 15
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 15
      description: Code Quality and Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide
      progressing: Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide
    - weight: 70
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup)
      progressing: The program is submitted according to the directions with a minor omission or correction needed
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution

tags:
  - debugging
  
---

In this lab \[[^1]\], you will practice using the debugger to identify and fix a bug in a piece of code.  

Begin by downloading and opening [this NetBeans project](../files/labs-debugging/DebugSample.zip).  This code attempts to compute the slope of the line connecting two Cartesian points.  Run the project.  You'll notice that the slope is 0, although this is incorrect.

Set a Line Breakpoint at line 25 of the code, and start the debugger until it breaks at this line.  A pane appears at the bottom of the window indicating the variable types and values.  Here, you can inspect the values of the variables in your program at this point in the execution.  You can also add new watches.  Click to add a new watch, and enter `xdiff / ydiff` as the watch expression.  Note that you can even watch expressions, not just variables!

What is the value of this watch, and what is its type?  Does its value make more sense given the context of its data type?  What happened to cause this program to fail, and what can be done to fix it?

Make the needed repair, then stop and re-run the debugger.  Check the watch expression `xdiff / ydiff` again and verify that it is working correctly.

## Trivia

Did you know that the most copied StackOverflow code snippet (as of 2018) [contained a bug that was only recently fixed](https://www.zdnet.com/article/the-most-copied-stackoverflow-java-code-snippet-contains-a-bug/)?