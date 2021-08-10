---
layout: assignment
permalink: /Labs/VennDiagram
title: "CS173: Intro to Computer Science - Venn Diagrams with Conditionals"
excerpt: "CS173: Intro to Computer Science - Venn Diagrams with Conditionals"

info:
  coursenum: CS173
  points: 100
  goals:
    - To use conditionals to solve problems enabling custom control flow
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
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
  readings:
    - rtitle: "Conditionals Activity"
      rlink: "../Activities/Conditionals"
      
tags:
  - conditionals
  
---

In this lab, you will use conditionals to alter your program's control flow (that is, flow from one line of code to the next).  We can use `if` statements to conditionally execute code, or to make a choice between two or more pieces of code to run.

## What to Do

Begin by drawing a [three-way Venn Diagram](https://www.educationworld.com/tools_templates/D_venn3_2) of your choice.  For example, [this Venn Diagram](https://www.buzzfeed.com/tessafahey/actor-venn-diagram) sorts characters by whether they have been in the Marvel Cinematic Universe, won an academic award, and/or performed on Broadway.  Whatever you choose, make sure at least one item fits into each category.  You can draw your diagram using software like Microsoft Paint or PowerPoint, or on paper and taking a picture.  Either way, be sure to submit it with your project!

Next, write a program that implements your Venn Diagram.  That is, write a series of `if/else if/else` statements, or nested `if` statements, that sets `boolean` variables representing each of the three main quadrants of your Venn Diagram, and prints to the screen where that person/place/thing fits into your Venn Diagram based on those `if` statements.  You can number the qudrants from 1 to 7, if you like, and print which quadrant results from the three `boolean` variables.

Finally, write a second version of your `if` statements, this time using nested `if` statements if you used an `if/else if/else` structure previously, or vice-versa.  Keep both versions in your program to submit!

## Exporting your Project for Submission

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.