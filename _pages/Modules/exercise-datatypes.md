---
layout: exercise
permalink: /Modules/DataTypes/Exercise
title: "CS173: Intro to Computer Science - Introduction to Primitive Data Types"
excerpt: "CS173: Intro to Computer Science - Introduction to to Primitive Data Types"

info:
  prev: "./Module"
  instructions: "Modify the Driver.java file to compute and print the Energy of an object given its mass and the constant c (which is given to you in the program)."
  goals:
    - To become familiar with the basic structure of a Java program
    - To write a Java statement
    - To declare a variable
    - To manipulate a variable with arithmetic statements
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("")
 
files:
  - filename: "Driver.java"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class Driver {
            public static void main(String[] args) {
                double c = 3e8; // A constant representing the speed of light

                /* TODO: 1. Declare a variable m for the mass of an object, and assign it the value 2.3.  Be sure to use the appropriate data type!
                         2. Compute the Energy (using Einstein's formula: E = mc^2)
                         3. Print the value using System.out.println
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
