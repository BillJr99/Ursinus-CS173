---
layout: assignment
permalink: /Labs/AverageFunction
title: "CS173: Intro to Computer Science - Averaging Functions"
excerpt: "CS173: Intro to Computer Science - Averaging Functions"

info:
  coursenum: CS173
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
  readings:
    - rtitle: "Functions Activity"
      rlink: "../Activities/Functions"  
      
tags:
  - functions
  
---

In this lab, you will develop and use functions to modularize and re-use your code.  

## Background

Consider the [grading table of our course syllabus](../#grading).  It lists grading weights for each component of the course (for example, programming assignments).  To compute your course grade, you would first average all your programming assignment grades together, and all the other grade component averages.  To compute the assignment average <span>\\(\mu_{x}\\)</span>, take the sum of each of your <span>\\(n\\)</span> assignment scores <span>\\(x_{i}\\)</span>, and divide by the number of assignments, as follows:

<br><span>\\(\mu_{x} = \frac{\sum\limits_{i=1}^{n} x_{i}}{n}\\)</span><br>

For example, suppose your assignment grades are 100, 75, and 80.  Your average assignment grade is the equally-weighted average:

<div align="center">
<br><span>\((1.0 + 0.75 + 0.80) / 3 = ((1.0 * 0.333) + (0.75 * 0.333) + (0.80 * 0.333)) = 0.85\)</span> (or 85%)<br>
</div>

**Note that I converted each grade to a `double`; I did this by dividing each one by 100.0.  This ensures that I am using floating point division throughout my program, and not integer division, in my calculations!  I suggest you do this as well.  Before you `return` your result, you can multiply by 100.0 again so that your grade is on a scale from 0 to 100.**

Then, those averages are averaged - but not equally.  The weighted average is computed by multiplying each of your component averages by a weight <span>\\(w_{i}\\)</span>, given by the syllabus (for example, a 50% weight would be computed as 0.5 for that corresponding <span>\\(w_{i}\\)</span>):

<br><span>\\(\mu_{x} = \sum\limits_{i=1}^{n} w_{i} x_{i}\\)</span><br>

This is actually the same as the standard equally-weighted average, where <span>\\(w_{i}\\)</span> is <span>\\(\frac{1}{n}\\)</span>, giving equal weight to all the components.

For example, suppose assignments had a weight of 40%, and labs had a weight of 60%.  If your overall assignment grade is an 80%, and your overall lab grade is a 90%, your grade formula would be:

<div align="center">
<br><span>\(0.4 \times 0.8 + 0.6 \times 0.9 = 0.32 + 0.54 = 0.86\)</span> (or 86%)<br>
</div>

## Part 1: Computing a Course Grade from a Weighted Average

In this lab, you will create a program that assigns variable values to labs, assignments, etc., according to the syllabus grade breakdown.  Then, you will compute your average lab grade, average assignment grade, etc., using equal weighted averaging (by adding up all the grades and dividing by the number of grades).  Then, you will take those computed averages, and compute a **weighted average** of them, using a weighted average (by multiplying each score by the weight of that score, and adding those products together).  You will print out your final grade.  

**You can make up grades for these as an example, and it is fine to only consider labs and assignments.  Use a 60% weight for assignments and a 40% weight for labs (these are not the actual weights in our course, but will be fine for an example!).**

It is nice to be able to compute these averages without having to do so by hand, but you probably noticed how tedious is was to copy and paste, or re-write, your averaging code over and over again!  We can use functions to reduce this workload.

### Computing an Equally-Weighted Average of Individual Grades
Write a function `computeEqualAverage` that returns a `double`, and accepts `double`s for your individual grades.  Modify your program so that you replace your equal-weight averaging with calls to this function.  Pass your individual grades as parameters to this function.  For this example, let's suppose you have three grades to compute (and, thus, three `double` parameters to this function).  This function adds up the grades and divides by the number of grades.

This function goes outside of your `main()` function, but inside of your class curly braces, and will look like this:

```java
public static double computeEqualAverage(double grade1, double grade2, double grade3) {
    // compute the average of grade1, grade2, grade3 here, and return that value
}
```

Your formula should look something like this:

<div align="center">
<br><span>\((grade1 + grade2 + grade3) / 3.0\)</span><br>
</div>

### Computing a Weighted Average of these Averages
Now, write a function `computeWeightedAverage` that also returns a `double`, and accepts `double`s for your course averages as well as the weights (since there is a lab average and an assignment average, and each has a weight, you should have four `double` parameters to this function).  This function multiplies each grade by its corresponding weight, and adds the resulting products together.  Your formula should look something like this:

<div align="center">
<br><span>\(weight1 \times grade1 + weight2 \times grade2\)</span><br>
</div>

### Putting it all Together: Calling these Functions to Compute a Course Final Grade
Finally, write the body of your `main()` function to call the equal average function twice (once for assignments and once for labs), and then to pass those results as parameters to a call to the weight average function.  Specifically, you can call the `computeEqualAverage` function to obtain your assignment average and to obtain your lab average, and then call `computeWeightedAverage` to weight them.  For example, once your two functions (`computeEqualAverage` and `computeWeightedAverage`) are written, you could call them as follows:

```java
// suppose our assignment grades were 60, 90, and 80: you should get approximately 76.667 as the average
double assignmentAverage = computeEqualAverage(60, 90, 80); 

// suppose the lab grades were 80, 90, and 80: you should get approximately 83.333 as the average
double labAverage = computeEqualAverage(80, 90, 80); 

// the assignment weight is 60% and the lab weight is 40%.  You should get approximately 79.333 as the total grade.
double finalGrade = computeWeightedAverage(assignmentAverage, 0.6, labAverage, 0.4); 
```

## Merging the Averaging Functions into a Generalized Function
This program should be much shorter than if you had duplicated all the code to compute these averages!  However, there is still some redundancy.  The two average functions are still essentially the same algorithm and perhaps essentially the same code.

Write a function called `computeAverage` that returns a `double` and accepts the individual values as parameters, like the others.  This time, add individual `double` paramters for the weights.  You will have a total of 6 parameters: 3 grade parameters, and 3 weight parameters.  Replace your call to `computeWeightedAverage` with a call to this function, passing the appropriate weights.  If you are only using assignments and labs for your averages, you will only have four values to pass to `comptueAverage` rather than 6.  You can pass 0 for the third grade and weight parameter, which will give the last zero a weight of 0, having no effect.

Finally, replace your call to `computeEqualAverage` with a call to `computeAverage`, passing the appropriate weights there as well (what should the weights be when computing an equal-weight average?  **Hint**: the three weights should be the same!).

## Exporting your Project for Submission

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.