---
layout: assignment
permalink: /Labs/Kepler
title: "CS173: Intro to Computer Science - Kepler's Third Law"
excerpt: "CS173: Intro to Computer Science - Kepler's Third Law"

info:
  coursenum: CS173
  githubclassroom:
    joinlink: https://classroom.github.com/classrooms/61290261-billmongan-cs173-fall20
    clonelink: false
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
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup)
      progressing: The program is submitted according to the directions with a minor omission or correction needed
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution

tags:
  - math
  
---

[Kepler's Third Law](https://en.wikipedia.org/wiki/Kepler's_laws_of_planetary_motion#Third_law_of_Kepler) relates the orbital period of a body around another body.  Due to gravitational forces, bodies in space are attracted to one another; objects in orbit continuously attract one another, forming an orbital pattern that we can predict.   In this lab \[[^1]\], you will compute the orbital period of the planets around the sun, given each planet's mass and length of its semi-major axis.

The formula relating the orbital period T of a planet to its mass m and semi-major axis length a is:

<span>\\(T = \sqrt{\frac{4 \pi^{2} a^{3}}{G(M + m)}}\\)</span>

There are constants used in this formula, with values (given below) that you can plug into your program.  To use them, you can declare a constant variable as follows:

```java
final double VARIABLE_NAME = 123.456
```

(note the use of the `final` keyword, which means that the assigned value cannot be changed, and the capital letters for the variable name, which quickly indicates to a programmer that the value is indeed a constant).

* <span>\\(M = 1.989 \times 10^{30} kg\\)</span> 
** This is represented in Java as 1.989e30
* <span>\\(G = 6.6743015 \times 10^{-11}\\) \frac{meters^{3}}{kg \times sec^{2}}</span> 
** This is represented in Java as 6.6743015e-11

The following table provides your inputs for the planetary mass and semi-major axis length, as well as an approximate length of the year on that planet in Earth Days (to help you check your output).

| Planet | Mass (kg) | Semi-major Axis Length (AU) | Approximate Length of Year (Earth Days) |
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

Astronomical Units (AU) is a unit of measure approximately defined as the distance from the earth to the sun.  However, notice that the units in the constants above use meters.  In order to use the axis length value in your formula, you will need to convert the length from AU to meters.  One AU is approximately 149,597,870,700 meters.

Similarly, the formula yields the orbital period in seconds.  In order to output the orbital period in years, you will need to convert it by dividing the number of seconds by the number of seconds in an Earth year.  

To take the square root of a number `x`, you can use the `Math.sqrt(x)` function, and to raise a number `x` to a power `p`, you can use the `Math.pow(x, p)` function.  The constant <span>\\(\pi\\)</span> is provided to you as `Math.PI`.

I strongly suggest computing the portions of this formula one item at a time, rather than implementing the entire formula as a single line of code.  Thus, I would compute the numerator separately from the denominator, then compute the square root of the quotient.  You might even compute the division first and then separately take the square root of it.  This keeps your code short and your arithmetic concise, and each of these makes your code easier to read, understand, and fix!

Similarly, when converting the resulting orbital period from seconds to years, I recommend dividing the orbital period by the product of the number of days in an Earth year times the number of hours in a day, times the number of minutes in an hour, times the number of seconds in a minute.  This will make your program easier to read and understand.

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie)