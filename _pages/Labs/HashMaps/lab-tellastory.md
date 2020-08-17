---
layout: assignment
permalink: /Labs/TellAStory
title: "CS173: Intro to Computer Science - Tell a Story with HashMaps"
excerpt: "CS173: Intro to Computer Science - Tell a Story with HashMaps"

info:
  coursenum: CS173
  githubclassroom:
    clonelink: false
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
  - hashmaps
  - iteration
  
---

In this lab, you will use `HashMap`s to tell a dynamic story.  

Create a `HashMap` called `places` that define the different places you can go in your story.  These will map to an array of `String`s.  The first `String` is the name of the place.  The second `String` is a narration of your story upon entering that location.  Print this narration to the screen.

The remaining elements in your array will be Strings - the keys that you can go to from the current location.  Print out the list of keys and the names of those locations (you can look them up in the `HashMap`).  The user will enter the next location, and you will loop until reaching the `end` key.

Finally, include a hash entry for `start` and `end` from which your story will begin and end.  Use an appropriate loop structure to terminate the story when the `end` key is reached.

Creativity is encouraged, but not graded!  Let me know in your documentation if you'd like to demo your story to the class - I hope you do!