---
layout: exercise
permalink: /Modules/Functions/Exercise
title: "CS173: Intro to Computer Science - Functions"
excerpt: "CS173: Intro to Computer Science - Functions"

info:
  points: 3
  instructions: "test"
  goals:
    - To write mathematical expressions in Java
    - To write a function that computes an expression and returns its result
    - To call a function from <code>main()</code> and use its return value
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("3")        
 
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

