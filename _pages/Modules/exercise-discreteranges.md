---
layout: exercise
permalink: /Modules/DiscreteRanges/Exercise
title: "CS173: Intro to Computer Science - Introduction to Primitive Data Types and Discrete Ranges"
excerpt: "CS173: Intro to Computer Science - Introduction to to Primitive Data Types and Discrete Ranges"

info:
  points: 3
  instructions: "Modify the Driver.java file to correct a bug due to an integer overflow.  Specifically, choose a more appropriate data type for the variable being printed."
  goals:
    - To select data types appropriate to the range of data used in a program
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("2147483648") && !(pos.includes("-2147483648"))
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("-2147483648")
      feedback: "Try again: the <code>int</code> data type results in an integer overflow.  Try a different type!"    
      
files:
  - filename: "Driver.java"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class Driver {
            public static void main(String[] args) {
                /* TODO: Change this line - only this line needs to be modified! */
                int score = 2147483647;
                
                System.out.println("Your score is " + score);
                
                score = score + 1;
                
                System.out.println("Now your score is " + score);                
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
