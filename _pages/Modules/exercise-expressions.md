---
layout: exercise
permalink: /Modules/Expressions/Exercise
title: "CS173: Intro to Computer Science - Introduction to Primitive Data Types and Expressions"
excerpt: "CS173: Intro to Computer Science - Introduction to to Primitive Data Types and Expressions"

info:
  points: 3
  prev: "./Module2"
  instructions: "Modify the Driver.java file to compute and print the Energy of an object given its mass and the constant <code>c</code> (which is given to you in the program)."
  goals:
    - To become familiar with the basic structure of a Java program
    - To write a Java statement
    - To declare a variable
    - To manipulate a variable with arithmetic statements
  
canvasasmtid: "137422"
canvaspoints: 3
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("207000000000000000")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("690000000")
      feedback: "Try again: don't forget to square c with the Math.pow() method, or by multiplying by c twice!"    
    - incorrectcheck: |
        pos.includes("180000000000000000")
      feedback: "Try again: be sure to declare m as a float or double!"          
    - incorrectcheck: |
        pos.includes("1586999999")
      feedback: "Try again: you may have squared the mass value instead of the speed of light!"
      
files:
  - filename: "Driver.java"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class Driver {
            public static void main(String[] args) {
                /*  A constant representing the 
                    speed of light = 300000000, 
                    which can be typed as 3e8 for convenience
                    meaning "three times ten to the eighth" */
                final double C = 3e8; 

                /* TODO: 1. Declare a variable m for the mass 
                            of an object, and assign it the 
                            value 2.3.  Be sure to use the 
                            appropriate data type!
                         2. Compute the Energy (using 
                            Einstein's formula: E = MC^2)
                            ... note that C is a capital 
                            letter: variables are case 
                            sensitive, so you'll want to 
                            refer to it as C and not c in 
                            this program.
                         3. Print the value using 
                            System.out.println()
                */
                
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
