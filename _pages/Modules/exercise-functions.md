---
layout: exercise
permalink: /Modules/Functions/Exercise
title: "CS173: Intro to Computer Science - Functions"
excerpt: "CS173: Intro to Computer Science - Functions"

info:
  prev: "./Module"
  points: 3
  instructions: "Write a function that computes one of the roots of a <a href=\"https://en.wikipedia.org/wiki/Quadratic_equation\">quadratic equation</a>.  In addition to multiplying b by itself, you can compute <code>b*b</code> using the <code>Math.pow()</code> method.  The <code>Math.sqrt()</code> method takes a <code>double</code> parameter, which is the number whose root should be computed, and returns the result as a <code>double</code>.  Now write a program that calls a method that you will write to compute the quadratic root, and then have <code>main()</code> print the root that you calculate."
  goals:
    - To write mathematical expressions in Java
    - To write a function that computes an expression and returns its result
    - To call a function from <code>main()</code> and use its return value
    
canvasasmtid: "137430"
canvaspoints: 3
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos === "3"        
 
files:
  - filename: "Driver.java"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class Driver {
            public static double quadraticRoots(int a, int b, int c) {
                // TODO write this function and return the result.
                // There are two roots (-b "+ or -" ...)
                // ... just compute -b + ...
            }
            
            public static void main(String[] args) {
                // Solving for a root of x in x^2 - x - 6
                double result = quadraticRoots(1, -1, -6);
                
                System.out.println(result);
            }
        }    

  - filename: "Excerpt from Main.java: body of main() function"
    ismain: true
    name: main
    isreadonly: true
    isvisible: false
    code: |
        Driver.main(null);
        
---

## Quadratic Formula

For reference, the quadratic formula is:

<span>\\[\frac{-b \pm \sqrt{(b^{2} - 4ac)}}{2a}\\]</span>

given an equation:

<span>\\[ax^{2} + bx + c = 0\\]</span>

In this exercise, you can simply compute one of the roots, as follows:

<span>\\[\frac{-b + \sqrt{(b^{2} - 4ac)}}{2a}\\]</span>
