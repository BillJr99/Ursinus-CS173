---
layout: assignment
permalink: /Labs/Debugging
title: "CS173: Intro to Computer Science - Using the Debugger"
excerpt: "CS173: Intro to Computer Science - Using the Debugger"

info:
  coursenum: CS173
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

In this lab, you will practice using the debugger to identify and fix a bug in a piece of code.  

### Step 1: Download the Sample Project
Begin by downloading and opening [this NetBeans project](../files/lab-debugging/DebugSample.zip).  Once you open the project, it may be necessary to close and re-open NetBeans to refresh the project files.

This code attempts to compute the slope of the line connecting two Cartesian points.  Run the project.  You'll notice that the slope is 0, although this is incorrect.

### Step 2: "Breaking" or Pausing the Program at a Certain Point
Set a Line Breakpoint at line 25 of the code, and start the debugger until it breaks at this line.  **Hint**: you may wish to refer to our [debugger tutorial](../NetBeans/Debugging) for guidance on using the features of the debugger.  

### Step 3: Adding a "Watch" to Inspect Variable Values
When you run the debugger and it pauses ("breaks") somewhere in the code.  A pane appears at the bottom of the window indicating the variable types and values.  Here, you can inspect the values of the variables in your program at this point in the execution.  You can also add new watches.  Click to add a new watch, and enter `ydiff / xdiff` as the watch expression.  Note that you can even watch expressions, not just variables!

### Step 4: Fix the 2 Bugs!
What is the value of this watch, and what is its type?  Does its value make more sense given the context of its data type?  What happened to cause this program to fail, and what can be done to fix it?  **Hint**: you may wish to refer to our discussion of [Data Types, Operators, and Expressions](../Activities/Expressions).  Fix the data types of the `xdiff` and `ydiff` inputs so that they divide as floating point values, rather than as integers.

Make the needed repair, then stop and re-run the debugger.  Check the watch expression `ydiff / xdiff` again and verify that it is working correctly.

If you would like to re-run the debugger from the beginning, you can stop the current debugging session (because it might think you are still paused at a breakpoint!) using the stop toolbar button at the top of your window, as shown below.  Then, you can start the Debugger using the `Debug` menu like before!

![]({{ site.baseurl }}/images/netbeans/debugging/debug-stopdebugger.png)

You can submit this project as usual, by adding your README and exporting the project to a ZIP file for submission.

## Submission

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](http://www.billmongan.com/Ursinus-CS173-Spring2021/Modules/IDE/Module2) describing how to write a README for your project, and how to export it.

## Trivia

Did you know that the most copied StackOverflow code snippet (as of 2018) [contained a bug that was only fixed 9 years later](https://www.zdnet.com/article/the-most-copied-stackoverflow-java-code-snippet-contains-a-bug/)?