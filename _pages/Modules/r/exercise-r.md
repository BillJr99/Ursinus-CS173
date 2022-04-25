---
layout: exercise-r
permalink: /Modules/R/TutorialExercise
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
    name: main
    ismain: true
    isreadonly: false
    isvisible: true
    code: | 
        print("Hello, world!")
        
---

<!-- Note: R Module Permalinks must be /Modules/R/ so that resources load
     with the following _config.yml directive:

        defaults:
          - scope:
              path: '_pages/Modules/R/'
            values:
              permalink: /Modules/R/
-->