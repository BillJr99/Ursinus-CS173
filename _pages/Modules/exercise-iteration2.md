---
layout: exercise
permalink: /Modules/Iteration/Exercise2
title: "CS173: Intro to Computer Science - Iteration Revisited"
excerpt: "CS173: Intro to Computer Science - Iteration Revisited"

info:
  points: 3
  instructions: "Modify the Driver.java file to solve the 3x+1 problem using a loop and conditional."
  goals:
    - To use iteration to compute a discrete value
    - To use conditionals to make choices during each loop iteration
    
canvasasmtid: "107097"    
canvaspoints: 3
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.split();
  correctcheck: |
    pos[0] === "5" && pos[1] === "111" && pos[2] === "12"
      
files:
  - filename: "ThreeXPlusOne.java"
    name: threexplusone
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class ThreeXPlusOne {
            /* Given a number x, loop until x goes to 1.
               During each iteration, if x is even, divide it by 2.
               If it is odd, set x to 3 times x, plus 1.
               Return the number of iterations it took to solve. */
            public static int threeXPlusOne(int x) {
                /* TODO: Solve the three x plus one problem! */
                /* hint - use a loop and an if statement! */
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
                int ans1 = threeXPlusOne(5);
                int ans2 = threeXPlusOne(27);
                int ans3 = threeXPlusOne(17);
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

