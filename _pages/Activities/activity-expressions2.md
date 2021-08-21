---
layout: activity
permalink: /Activities/Expressions2
title: "CS173: Intro to Computer Science - Expressions"
excerpt: "CS173: Intro to Computer Science - Expressions"

info:
  next: ./EscapeCharacters
  prev: ./Expressions
  
  goals: 
    - To manipulate variables on paper
    - To explain that a variable holds a value at discrete points in time, and that updates to a variable replace the previous value
    
  models:
    - model: |
        As a group of 3, choose a whole number and pass it to the person to your left.  If the number is even, divide the number by 2, cross it out, and write that number down.  If it is odd, replace it with <code>3x + 1</code>.  Continue until the number is equal to 1.  
      title: Variable Updates
      questions:
        - How many steps did it take for your number to become 1?
        - What would you do if you wanted to keep better track of the number of steps?
        - What would you do if you wanted to keep track of all the intermediate values you encountered along the way?
    - model: |
        Suppose you are painting a room with four walls.  The walls should be painted in blue, and the ceiling should be painted in white.  The room is 8 feet tall, but there is molding around the perimeter of the ceiling which removes 4 paintable inches from the ceiling, and one half inch from the ceiling.  Using variables and primitive operations, list out the steps required to determine how much white and blue paint are required to paint the room.  Set variables to represent the width, height, number of walls, and so on.
      title: Defining Algorithms Using Arithmetic Expressions
      questions:
        - Solve this problem on your own, but present it to your small group and compare with their solutions.  How many different ways did your group come up with?  
        - Merge your solutions together as a team and present your approach to the class.  How did their approaches differ (and how were they similar)?
  
tags:
  - datatypes
  - expressions
  - math
  
---

## Trivia

This problem is part of the [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) which suggests that any value will eventually converge back to 1 after a finite number of iterations.  *We don't know if this is true!*
