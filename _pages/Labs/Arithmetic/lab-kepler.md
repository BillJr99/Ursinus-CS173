---
layout: assignment
permalink: /Labs/Kepler
title: "CS173: Intro to Computer Science - Kepler's Third Law"


info:
  coursenum: CS173
  points: 100
  goals:
    - To implement an arithmetic expression into executable code
    - To map variables to expression parameters
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
      preemerging: An incomplete submission is provided, or the README file submitted is blank
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions
  readings:
    - rtitle: "Data Types Activity"
      rlink: "../Activities/DataTypes"
    - rtitle: "Expressions Activity"
      rlink: "../Activities/Expressions"      
  questions:
    - "What code is required to compute the value of <code>a</code> raised to the power of 3?"
    - "What code is required to compute the value of <code>Math.PI</code> raised to the power of 2?"
    - "What code is required to compute the denominator of Kepler's formula?"
    - "What code is required to compute the numerator of Kepler's formula?"
    - "What variables are different for each planet's computation?  Which variables are re-used for all planets?"
    
tags:
  - math
  
---

[Kepler's Third Law](https://en.wikipedia.org/wiki/Kepler's_laws_of_planetary_motion#Third_law_of_Kepler) relates the orbital period of a body around another body.  Due to gravitational forces, bodies in space are attracted to one another; objects in orbit continuously attract one another, forming an orbital pattern that we can predict.   In this lab \[[^1]\], you will compute the orbital period of the planets around the sun, given each planet's mass and length of its semi-major axis (the semi-major axis is half the length of the longest chord across the orbital ellipse).

The formula relating the orbital period `T` of a planet to its mass `m` and semi-major axis length `a` is:

<span>\\(T = \sqrt{\frac{4 \pi^{2} a^{3}}{G(M + m)}}\\)</span>

There are constants used in this formula, with values (given below) that you can plug into your program.  To use them, you can declare a constant variable as follows:

```java
final double VARIABLE_NAME = 123.456;
```

(note the use of the `final` keyword, which means that the assigned value cannot be changed, and the capital letters for the variable name, which quickly indicates to a programmer that the value is indeed a constant).

* <span>\\(M = 1.989 \times 10^{30} kg\\)</span> 
    * This is represented in Java as 1.989e30
* <span>\\(G = 6.6743015 \times 10^{-11} \frac{meters^{3}}{kg \times sec^{2}}\\)</span> 
    * This is represented in Java as 6.6743015e-11

The following table provides your inputs for the planetary mass and semi-major axis length, as well as an approximate length of the year on that planet in Earth Days (to help you check your output).  These are approximations, so your values might be a little different because we're rounding some values, but this should give you a rough idea of the values you'll get.

| Planet | m: Mass (kg) | a: Semi-major Axis Length (AU) | Approximate Length of Year (Earth Days) |
|-|-|-|-|
| Mercury | 3.285e23 | 0.38710 | 87.9693 |
| Venus | 4.867e24 | 0.72333 | 224.7008 |
| Earth | 5.972e24 | 1 | 365.2564 |
| Mars | 6.39e23 | 1.52366 | 686.9796 |
| Jupiter | 1.898e27 | 5.20336 | 4332.8201 |
| Saturn | 5.683e26 | 9.53707 | 10775.599 |
| Uranus | 8.681e25 | 19.1913 | 30687.153 |
| Neptune | 1.024e26 | 30.0690 | 60190.03 |
| Pluto  (a dwarf planet) | 1.309e22 | 39.4821 | 90600 |

## Converting Astronomical Units to Meters
Astronomical Units (AU) is a unit of measure approximately defined as the distance from the earth to the sun.  However, notice that the units in the constants above use meters.  In order to use the axis length value in your formula, you will need to convert the length from AU to meters.  One AU is approximately 149,597,870,700 meters, which we will represent as a double (since the value itself is larger than the maximum value of an `int`), so you can multiply the `AU` value in the table above by this value, as follows:

```java
final double metersPerAU = 1.49597870700e11;
double mercuryA = 0.38710;
mercuryA = mercuryA * metersPerAU; // no need to write double here, since we've already declared mercuryA as a double above!
```

## Some Arithmetic Expression Examples for Reference
Here is a coding example (unrelated to the lab, but for reference), to compute the average of two numbers, you might first add the two numbers, and then multiply by `0.5` (or divide by `2.0`), as follows:

```java
int x = 6;
int y = 12;
double average = 0.5 * (x + y);

```

To take the square root of a number `x`, you can use the `Math.sqrt(x)` function, and to raise a number `x` to a power `p`, you can use the `Math.pow(x, p)` function.  The constant <span>\\(\pi\\)</span> is provided to you as `Math.PI`.  `Math.sqrt(x)` and `Math.pow(x, p)` accept and return values of type `double`, and, similarly, `Math.PI` is a `double`.  For example, the code snippet below computes the area of a circle with radius `6` (note, this code will not appear in your lab directly; it's just an example!):

```java
double r = 6.0;
double rSquared = Math.pow(r, 2);
double area = Math.PI * rSquared;
double squareRootOfArea = Math.sqrt(area);
```

## Converting the Orbital Period from Seconds to Days
Just as you converted Astronomical Units (AU) to meters, Kepler's formula yields the orbital period in seconds.  In order to output the orbital period in Earth days, you will need to convert it by dividing the number of seconds by the number of seconds in an Earth day.  I recommend dividing the orbital period by the product of the number of hours in a day, times the number of minutes in an hour, times the number of seconds in a minute.  This will make your program easier to read and understand.

## What To Do
I strongly suggest computing the portions of this formula one item at a time, rather than implementing the entire formula as a single line of code.  Thus, I would compute the numerator separately from the denominator, then compute the square root of the quotient.  You might even compute the division first and then separately take the square root of it.  This keeps your code short and your arithmetic concise, and each of these makes your code easier to read, understand, and fix!

* First, begin by declaring a `final double` variable `M`, and setting it to the value `1.989e30`.
* Next, declare another `final double` variable `G`, with the value `6.6743015e-11`.
* Then, using the table above, declare `double` variables `m` and `a`, equal to the values in the table for one of the planets.  If you choose Venus, I suggest naming the variables `venusM` and `venusA`, so that you will know which ones are which later when computing the rest of the planetary orbits!
* Multiply `a` by `1.49597870700e11` to convert it from AU to meters.  Create a constant variable to represent the value `1.49597870700e11`, so that you can re-use this for each planet later.
* Implement Kepler's Formula to compute `T`, the orbital period in seconds.  I recommend computing each part of the formula as a separate variable to make the code easier to write (and to read!).  For example, you might create a variable whose value is `M + m` first, and then multiply that by `G`.  Another variable could hold the numerator, which you might set to `4` before multiplying itself by `Math.PI` squared, and multiply that again by a "cubed."  Then you can divide those two variables as a new variable, and take the square root of that resulting variable.  There are many correct ways of doing this, though, so you don't have to follow this plan exactly!  This is just one approach that you are welcome to use.
* Convert `T` from seconds to days by dividing by the number of seconds in a day.  If you'd like, you can do this by dividing by the number of seconds in a minute, then dividing that by the number of minutes in an hour, and then dividing that by the number of hours in a day.
* Print `T`, the orbital period in days.  You can check your work using the table above, which provides the approximate period in days for each planet.  Note that you should print the variable, so no quotes are used inside the print statement (otherwise it would just print the name of the variable as text!).  See the reading links at the top of this lab for an example of how to print!
* Repeat this process for the remaining planets, such that your program prints out all of the orbital periods when you run it.  For now, you can copy and paste your code and modify the variable values to do this, but we'll learn an easier way soon!
* Don't forget to comment your code to describe what you are doing using `//`, and write up a README describing what you have done to accompany your submission.  You can save your README file in your project directory.  
* When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.  

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie)
