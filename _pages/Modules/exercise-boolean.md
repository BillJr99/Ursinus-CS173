---
layout: exercise
permalink: /Modules/Boolean/Exercise
title: "CS173: Intro to Computer Science - Introduction to Boolean Expressions"
excerpt: "CS173: Intro to Computer Science - Introduction to to Boolean Expressions"

info:
  points: 3
  instructions: "Modify the Driver.java file to determine if the circumference of a circle is approximately equal to a floating point value."
  goals:
    - To become familiar with the basic structure of a Java program
    - To write a Java statement
    - To declare a variable
    - To manipulate a variable with arithmetic statements
    - To write a compound boolean expression to verify a numeric range
    - To check the value of an imprecise floating point value
    - To explain that a floating point value is represented imprecisely with a discrete binary representation
  
canvasasmtid: "137425"  
canvaspoints: 3
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("20.420334999999998") && pos.includes("true")
      
files:
  - filename: "Driver.java"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class Driver {
            public static void main(String[] args) {
                /* Don't change these! */
                float diameter = 6.5;
                float pi = 3.14159;
                
                /* TODO: Declare a floating point variable circumference, 
                   and set it equal to pi * the diameter */
                
                /* TODO: Print the circumference of this circle */
                
                /* The true circumference is 20.420335, which you can verify on your calculator.  
                   But you might get something slightly different here!  Why? */
                
                /* TODO: Declare a boolean variable called isApproximatelyEqual, whose value is 
                   true if the circumference is "approximately equal" to 20.420335, by checking 
                   if it is greater than a nearby value like 20.42 and smaller than a nearby 
                   value like 20.43. */

                /* I'll print the value for you - don't change this! */
                System.out.println(isApproximatelyEqual);
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
