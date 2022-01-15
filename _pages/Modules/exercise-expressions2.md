---
layout: exercise
permalink: /Modules/Expressions/Exercise2
title: "CS173: Intro to Computer Science - Introduction to Primitive Data Types and Expressions Revisited"
excerpt: "CS173: Intro to Computer Science - Introduction to to Primitive Data Types and Expressions Revisited"

info:
  points: 3
  instructions: "Modify the Driver.java file to print the distance traveled by an object in free-fall for 5 seconds on Earth."
  goals:
    - To become familiar with the basic structure of a Java program
    - To write a Java statement
    - To declare a variable
    - To manipulate a variable with arithmetic statements

canvasasmtid: "137424"
canvaspoints: 3

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
                float g = 9.80665; // Gravitational Constant on Earth in m/s
                
                /* TODO: Declare a float variable representing the amount of time that 
                   an object fell due to gravity.  Set this variable to 5 seconds. */
                
                /* TODO: Print out the distance the object was in free-fall, which is (1/2) * g * time^2 */
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
