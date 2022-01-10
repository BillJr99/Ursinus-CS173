---
layout: assignment
permalink: /Labs/ArrayAveraging
title: "CS173: Intro to Computer Science - Array Averaging"
excerpt: "CS173: Intro to Computer Science - Array Averaging"

info:
  coursenum: CS173
  points: 100
  goals:
    - To use arrays to store collections of values
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 10
      description: Code Indentation and Spacing
      preemerging: Code indentation and spacing are generally inappropriate or inconsistent
      beginning: Code indentation or spacing are generally appropriate but inconsistent in a few isolated instances
      progressing: Code indentation or spacing are appropriate or consistent, with minor adjustments needed
      proficient: Code indentation and spacing are appropriate and consistent
    - weight: 10
      description: Code Quality
      preemerging: Prior code quality feedback and style guide standards are not reflected in the submitted code to a great extent
      beginning: Code quality conforms to several standards in the course Style Guide, and progress is demonstrated in improving code quality from prior feedback
      progressing: Code quality conforms to the standards in the course Style Guide to a great extent, with a few identified areas of improvement
      proficient: Code quality substantially conforms to the standards in the course Style Guide
    - weight: 10
      description: Code Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program; specifically, javadoc style comments are present for some functions
      progressing: Code documentation is present that re-states the explicit code definitions
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program; specifically, javadoc style comments are present for all functions
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided, or the README file submitted is blank
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions
  readings:
    - rtitle: "Functions Activity"
      rlink: "../Activities/Functions"  
    - rtitle: "Conditionals Activity"
      rlink: "../Activities/Conditionals"  
    - rtitle: "Arrays Activity"
      rlink: "../Activities/Arrays"        

tags:
  - functions
  - conditionals
  - arrays
  
---

In this lab, you will develop and use arrays to simplify your computation over collections of data, so that you do not need to know how many data elements you are working with in order to develop a generalized algorithm.  

Consider the [grading table of our course syllabus](../#grading).  It lists grading weights for each component of the course (for example, programming assignments).  To compute your course grade, you would first average all your programming assignment grades together, and all the other grade component averages.  To compute the assignment average <span>\\(\mu_{x}\\)</span>, take the sum of each of your <span>\\(n\\)</span> assignment scores <span>\\(x_{i}\\)</span>, and divide by the number of assignments, as follows:

<br><span>\\(\mu_{x} = \frac{\sum\limits_{i=1}{n} x_{i}}{n}\\)</span><br>

Then, those averages are averaged - but not equally.  The weighted average is computed by multiplying each of your component averages by a weight <span>\\(w_{i}\\)</span>, given by the syllabus (for example, a 50% weight would be computed as 0.5 for that corresponding <span>\\(w_{i}\\)</span>):

<br><span>\\(\mu_{x} = \sum\limits_{i=1}{n} w_{i} \times x_{i}\\)</span><br>

This is actually the same as the standard equally-weighted average, where <span>\\(w_{i}\\)</span> is <span>\\(\frac{1}{n}\\)</span>, giving equal weight to all the components.

Create a program that assigns variable values to labs, assignments, etc., according to the syllabus grade breakdown.  Compute your average lab grade, average assignment grade, etc., using equal weighted averaging.

Then, take those computed averages, and compute a **weighted average** of them, using the weights in the syllabus.  Print out your final grade.

It is nice to be able to compute these averages without having to do so by hand, but you probably noticed how tedious is was to copy and paste, or re-write, your averaging code over and over again!  We can use functions to reduce this workload.

## Part 1: Equal Averages
Write a function `computeEqualAverage` that returns a `double`, and accepts an array of `double` for your individual grades.  Modify your program so that you replace your equal-weight averaging with calls to this function.  Pass your individual grades as an array parameter to this function.

Each time you return an equal average (for example, the equal average of your lab grades, the equal average of your assignment grades, and so on), insert those into an array called `courseAverages` that you will pass to `computeWeightedAverage` later.  You can create an array of a certain size like this in your `main()` function, and each of these will hold the result of one of your calls to `computeEqualAverage`:

`double[] averages = new double[4];`

where you know up-front that you will store 4 averages (for example, assignments, labs, projects, and attendance).  You have to specify how many elements you are storing up-front for now (we will improve upon this again later!).

Each time you call `computeEqualAverage`, store the result in one of these elements (for example, `averages[0] = computeEqualAverage(grades);` where `grades` is a `double[]`, an array of `double` values representing your collection of individual grades: `double[] grades`).

You can create a pre-initialized array of grades like this:

```java
double[] assignmentGrades = {90, 100, 80};
double[] labGrades = {95, 100, 85};
```

You can pass each of these to calls to `computeEqualAverage`, and assign the result to each index of `averages`, for example:

```java
averages[0] = computeEqualAverage(assignmentGrades);
// ... and so on
```

## Part 2: Weighted Averages
Now, write a function `computeWeightedAverage` that also returns a `double`, and accepts an array of `double` for your course averages, and an additional array of `double` to represent the weights.  Call this function passing the average array and a weights array as parameters.

## Finishing Touches and Writeup 

Don't forget to test your program with several different inputs to help verify that things work the way you expect!  Think in terms of trying to break your program; if it's really hard to "trick" your program into getting the wrong answer, you've probably done a good job making your code robust.  

Also, check the [Style Guide](../Style-Guide) to make sure that you've written high quality code; make sure your code is "readable," well indented, uses good variable names, and includes good comments throughout the program.

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

### Exporting your Project for Submission

Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.  **Be sure to save your README file before exporting the project, so that your work is included in the submission!**