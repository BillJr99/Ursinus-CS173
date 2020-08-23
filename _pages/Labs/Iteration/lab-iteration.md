---
layout: assignment
permalink: /Labs/MonteCarloPi
title: "CS173: Intro to Computer Science - Estimating Pi with Monte Carlo Simulation"
excerpt: "CS173: Intro to Computer Science - Estimating Pi with Monte Carlo Simulation"

info:
  coursenum: CS173
  githubclassroom:
    clonelink: "https://classroom.github.com/a/5lbeaWNk"
  points: 100
  goals:
    - To use iteration to solve problems while avoiding the need to write duplicate code
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
  - iteration
  - strings
  
---

In this lab, you will use iteration to help you avoid writing (and debugging, and fixing, and maintaining) the same code over and over again.  Specifically, we will estimate the value of <span>\(\pi\)</span> using iteratively generated random numbers.

Imagine a unit square with a circle inscribed.  The diameter of the circle is 1, since the length of a side of the unit square (in which the circle is inscribed) is 1.

**Question: what is the area of the square, and what is the area of the circle?**

Generate 10 pairs of random numbers (x and y coordinates) between 0 and 1.  Only some (or perhaps none!) of these points lie inside the circle, but all of these points lie inside the unit square.  The ratio of the points inside the circle to the points inside the square should approximate the ratio of the area of the circle to the area of the square, given enough points.

<span>\(\frac{A_{circle}}{A_{square}} = \frac{\pi \times r^{2}}{s^{2}}\)</span>

Since we're using a unit square with side length <span>\(s = 1\)</span>, we know that <span>\(r = 0.5\)</span>.  This gives us the following:

<span>\(\frac{A_{circle}}{A_{square}} = \frac{\pi \times 0.5^{2}}{1^{2}}\)</span><br>
<span>\(\frac{A_{circle}}{A_{square}} = \pi \times 0.25\)</span><br>

Amazingly, the ratio of data points inside the circle to those inside the square is <span>\(\frac{\pi}{4}\)</span>.  In fact, since every data point is inside the square (because x and y are both between 0 and 1), the percentage of data points inside the unit circle will approximate <span>\(\frac{\pi}{4}\)</span>.

We know that a point `(x, y)` lies within a unit circle if <span>\(x^{2} + y^{2} \leq 1\)</span>.  Thus, you can create a program with a function `estimatePi` that accepts a parameter that specifies the number of pairs of random numbers `(x, y)` to generate.  Return the percentage of those random pairs that lie within the unit circle.

Call this function for various numbers of iterations (for example, 10, 100, 1000, 10000, 100000, 1000000, and 10000000), and compute the error from the actual value of <span>\(\frac{\pi}{4}\)</span>.  Now, run it a second time: do the error values change?  If so, by how much?