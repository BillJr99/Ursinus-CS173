---
layout: exercise
permalink: /Modules/Conditionals/Exercise
title: "CS173: Intro to Computer Science - Introduction to Conditionals"
excerpt: "CS173: Intro to Computer Science - Introduction to to Conditionals"

info:
  points: 3
  instructions: "Modify the GradePrinter.java file to print the letter grade earned for a given final grade using an if statement, using our syllabus letter grade table."
  goals:
    - To use compound conditionals 
  
canvasasmtid: "137427"
canvaspoints: 3
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.split(/\r?\n/);
  correctcheck: |
    pos[0] === "A-" && pos[1] === "A+" && pos[2] === "B-" && pos.length < 9
  incorrectchecks:
    - incorrectcheck: |
        pos.length >= 9
      feedback: "Try again: your function should only print one line per call, since only one if/else statement should be true for each grade provided"      
      
files:
  - filename: "GradePrinter.java"
    name: myfile
    ismain: false
    isvisible: true
    isreadonly: false
    code: |
        public class GradePrinter {
            public static void printGrade(double grade) {
                /* TODO: fill this in by printing the letter grade
                   For example, if the grade is 92, you should:
                   System.out.println("A-");
                   
                   Use the syllabus to determine the correct letter 
                   grades for each grade range!
                   
                   You can assume that the grade variable contains the
                   number grade you're checking.  DO NOT create your own grade 
                   variable this time, as I'll automatically provide a few
                   to test your code from below.
                */
            }
        }
  - filename: "Driver.java"
    name: driver
    ismain: false
    isreadonly: true
    isvisible: true
    code: | 
        public class Driver {
            public static void main(String[] args) {
                GradePrinter.printGrade(89.75);
                GradePrinter.printGrade(96.9);
                GradePrinter.printGrade(82.99);
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
