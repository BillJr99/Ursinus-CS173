---
layout: exercise
permalink: /ArrayDrills/ArrayMinIndex
title: "CS174: OOP - Drills - Array Min Index"
excerpt: "CS174: OOP - Drills - Array Min Index"

info:
  prev: "./Array3Sort"
  instructions: "Create a static method <code>getMinIndex</code> takes in an array of doubles and returns the index of the minimum element in the array.  You must handle the following two special cases: <ol><li>If there are ties, it should return the lowest index among the ties</li><li>If the array is empty, your program should return 0 without crashing</li></ul>"
  goals:
    - To do proper array indexing
    - To use loops in concert with arrays
    - To keep track of multiple auxiliary variables in a loop
    - To properly define methods
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("2.1.0")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("undefined")
      feedback: "Try again: It looks like you're going out of bounds of the array somewhere."    
 
files:
  - filename: "ArrayUtils.java"
    name: arrayutils
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class ArrayUtils {
          // TODO: Add your method here
        }

  - filename: "Tester.java"
    name: tester
    ismain: false
    isreadonly: true
    isvisible: true
    code: | 
        public class Tester {
            public static void main(String[] args) {
                int[] arr0 = {3, 5, 0, 8, 0, 2};
                int min0 = ArrayUtils.getMinIndex(arr0);
                int[] arr1 = {9, -3, 4, -3, 2, 5, 3, 2};
                int min1 = ArrayUtils.getMinIndex(arr1);
                int[] arr2 = {};
                int min2 = ArrayUtils.getMinIndex(arr2);
                System.out.print(min0);
                System.out.print(".");
                System.out.print(min1);
                System.out.print(".");
                System.out.print(min2);
            }
        }    

  - filename: "Excerpt from Main.java: body of main() function"
    ismain: true
    name: main
    isreadonly: true
    isvisible: false
    code: |
        Tester.main(null);
        
---
