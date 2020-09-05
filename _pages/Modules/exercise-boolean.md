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
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("122.58")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("245.16")
      feedback: "Try again: don't forget to divide by 2!"    
    - incorrectcheck: |
        pos.includes("24.51")
      feedback: "Try again: don't forget to square the time variable!"       
    - incorrectcheck: |
        pos.includes("49.03")
      feedback: "Try again: don't forget to square the time variable, and divide by 2!"         
      
files:
  - filename: "Driver.java"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class Driver {
            public static void main(String[] args) {
                float diameter = 6.5;
                
                float pi = 3.14159;
                
                /* TODO: Print the circumference of this circle, which is pi * the diameter */
                
                /* The value should be 20.420335, which you can verify on your calculator.  
                   But you might get something different!  Why? */
                
                /* TODO: Write an if statement that checks if the circumference is "equal" 
                   to this value by checking if it is greater than a nearby value and smaller 
                   than a nearby value. */
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
