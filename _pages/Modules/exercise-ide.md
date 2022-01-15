---
layout: exercise
permalink: /Modules/IDE/Exercise
title: "CS173: Intro to Computer Science - Introduction to the NetBeans IDE"
excerpt: "CS173: Intro to Computer Science - Introduction to the NetBeans IDE"

info:
  points: 3
  prev: "./Module2"
  instructions: "Modify the MyFirstProgram.java file to print hello to yourself (Hello followed by your name)."
  goals:
    - To become familiar with the basic structure of a Java program
    - To write a Java statement
    
canvasasmtid: "137417"
canvaspoints: 3
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.split(" ");
  correctcheck: |
    pos.length > 1 && pos[0].toLowerCase() === "hello"
  incorrectchecks:
    - incorrectcheck: |
        pos.length == 1
      feedback: "Try again: try printing a space in between the word Hello and your name!"       
 
files:
  - filename: "MyFirstProgram.java"
    name: myfirstprogram
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class MyFirstProgram {
            public static void main(String[] args) {
                System.out.println("Hello");
            }
        }    

  - filename: "Excerpt from Main.java: body of main() function"
    ismain: true
    name: main
    isreadonly: true
    isvisible: false
    code: |
        MyFirstProgram.main(null);
        
---
