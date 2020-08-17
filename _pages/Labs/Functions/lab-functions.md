---
layout: assignment
permalink: /Labs/AverageFunction
title: "CS173: Intro to Computer Science - Modular Code with Functions"
excerpt: "CS173: Intro to Computer Science - Modular Code with Functions"

info:
  coursenum: CS173
  githubclassroom:
    clonelink: false
  points: 100
  goals:
    - To develop functions to abstract program concepts
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
  - functions
  - conditionals
  
---

In this lab, you will develop and use functions to modularize and re-use your code.  

Consider the [grading table of our course syllabus](../#grading).  It lists grading weights for each component of the course (for example, programming assignments).  To compute your course grade, you would first average all your programming assignment grades together, and all the other grade component averages.  To compute the assignment average <span>\(\mu_{x}\)</span>, take the sum of each of your <span>\(n\)</span> assignment scores <span>\(x_{i}\)</span>, and divide by the number of assignments, as follows:

<br><span>\(\mu_{x} = \frac{\sum\limits_{i=1}{n} x_{i}}{n}\)</span><br>

Then, those averages are averaged - but not equally.  The weighted average is computed by multiplying each of your component averages by a weight <span>\(w_{i}\)</span>, given by the syllabus (for example, a 50\% weight would be computed as 0.5 for that corresponding <span>\(w_{i}\)</span>):

<br><span>\(\mu_{x} = \sum\limits_{i=1}{n} w_{i} \times x_{i}\)</span><br>

This is actually the same as the standard equally-weighted average, where w_{i} is \frac{1}{n}, giving equal weight to all the components.

Create a program that assigns variable values to labs, assignments, etc., according to the syllabus grade breakdown.  Compute your average lab grade, average assignment grade, etc., using equal weighted averaging.

Then, take those computed averages, and compute a **weighted average** of them, using the weights in the syllabus.  Print out your final grade.

It is nice to be able to compute these averages without having to do so by hand, but you probably noticed how tedious is was to copy and paste, or re-write, your averaging code over and over again!  We can use functions to reduce this workload.

Write a function `computeEqualAverage` that returns a `double`, and accepts `double`s for your individual grades.  Modify your program so that you replace your equal-weight averaging with calls to this function.  Pass your individual grades as parameters to this function.

Now, write a function `computeWeightedAverage` that also returns a `double`, and accepts `double`s for your course averages.  Modify your program to replace your weighted average computation with a call to this function (again passing the average values as parameters).

This program should be much shorter!  However, there is still some redundancy.  The two average functions are still essentially the same algorithm and perhaps essentially the same code.

Write a function called `computeAverage` that returns a `double` and accepts the individual values as parameters, like the others.  This time, add individual `double` paramters for the weights.  Replace your call to `computeWeightedAverage` with a call to this function, passing the appropriate weights. 

Finally, replace your call to `computeEqualAverage` with a call to `computeAverage`, passing the appropriate weights there as well (what should the weights be when computing an equal-weight average?).