---
layout: exercise
permalink: /Modules/RTutorial/Exercise
title: "CS173: Intro to Computer Science - R"
excerpt: "CS173: Intro to Computer Science - R"

info:
  points: 0
  instructions: "Modify the R.java file to print Hello World to yourself."
  goals:
    - To write a program using the R programming language
  
canvasasmtid: ""
canvaspoints: 0
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString;
  correctcheck: |
    pos.trim() === "Hello World"
 
files:
  - filename: "R.java"
    name: r
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        print("Hello, world!")

  - filename: "Body of main() function"
    ismain: true
    name: main
    isreadonly: true
    isvisible: false
    code: ""
        
---
