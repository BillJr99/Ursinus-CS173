---
layout: assignment
permalink: /Labs/DropLowest
title: "CS173: Intro to Computer Science - Searching and Sorting: Dropping the Lowest Score"
excerpt: "CS173: Intro to Computer Science - Searching and Sorting: Dropping the Lowest Score"

info:
  coursenum: CS173
  githubclassroom:
    clonelink: "https://classroom.github.com/a/XWrevmFf"
  points: 100
  goals:
    - To search an array using iterative approaches
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

tags:
  - searching
  
---

In this lab, you will write and test functions to drop the lowest score in an array of `double` test scores, and then return the average of the remaining items.

First, linearly search the array and drop the lowest score.  Print out the count of the number of times you execute inside a loop - you can do this with an integer counter.

Try these functions for different sized arrays, and plot the number of steps that were needed.  You can use a loop with a random number generator to generate scores.
