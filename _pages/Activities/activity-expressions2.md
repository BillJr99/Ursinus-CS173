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
  
tags:
  - datatypes
  - expressions
  - math
  
---

## Trivia

This problem is part of the [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) which suggests that any value will eventually converge back to 1 after a finite number of iterations.  *We don't know if this is true!*
