---
layout: exercise_python
permalink: "Python/Example_Quadratic"
title: "Python Example Module: Quadratic Formula"
excerpt: "Python Example Module: Quadratic Formula"
canvasasmtid: "95035"
canvaspoints: "3"
canvashalftries: 5

info:
  points: 3
  instructions: "Write a function that computes one of the roots of a <a href=\"https://en.wikipedia.org/wiki/Quadratic_equation\">quadratic equation</a>.  In addition to multiplying b by itself, you can compute <code>b*b</code> using the <code>b**</code> with the <code>**</code> operator.  The <code>math.sqrt()</code> method takes a single parameter, which is the number whose root should be computed, and returns the result.  Now complete the code to compute one of the roots of the quadratic formula"
  goals:
    - To write mathematical expressions in Python
    - To write a function that computes an expression and returns its result
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("3,1") || pos.includes("3.0,1.0")        
 
files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
         import math
         def get_quadratic_roots(a, b, c):
             """
             Compute the right root of of the quadratic equation
             f(x) = ax^2 + bx + c
             """
             return 0 # This is a default value

  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        # Run some tests on the method
        print(get_quadratic_roots(1, -1, -6), end=',')
        print(get_quadratic_roots(1, 0, -1))
        
---

## Quadratic Formula

For reference, the quadratic formula is:

<span>\\[\frac{-b \pm \sqrt{(b^{2} - 4ac)}}{2a}\\]</span>

given an equation:

<span>\\[ax^{2} + bx + c = 0\\]</span>

In this exercise, you can simply compute one of the roots, as follows:

<span>\\[\frac{-b + \sqrt{(b^{2} - 4ac)}}{2a}\\]</span>