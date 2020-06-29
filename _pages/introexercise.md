---
layout: exercise
permalink: /Modules/IntroExercise
title: "CS173: Intro to Computer Science"
excerpt: "CS173: Intro to Computer Science"

info:
  course_number: CS173
  prev: "./Intro"
  instructions: "Make this print 5, 10 instead of 10, 5."
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: "http://www.billmongan.com"
  feedbackprocess: | 
    let a = 5;
  correctcheck: |
    true
 
files:
  - filename: "File.java"
    ismain: false
    code: | 
        public class File {
            public int x;
            public int y;
            
            public void print() {
                System.out.println(this.x + "," + this.y);
            }
        }
    
  - filename: "Main.java"
    ismain: true
    code: |
        File f = new File();
        f.x = 10;
        f.y = 5;
        f.print();
  
---
Welcome! 