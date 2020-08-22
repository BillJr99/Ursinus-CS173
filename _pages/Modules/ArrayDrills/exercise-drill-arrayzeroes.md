---
layout: exercise
permalink: /ArrayDrills/ArrayZeroes
title: "CS174: OOP - Drills - Counting Array Zeroes"
excerpt: "CS174: OOP - Drills - Counting Array Zeroes"

info:
  next: "./ArraySep"
  instructions: "Modify the <code>countZeroes</code> method in <code>ArrayZeroes.java</code> file to count the number of zeroes in an array (this is based on exercise 13 on page 266 of the Horstmann book <i>Java for Everyone</i>)."
  goals:
    - To do proper array indexing
    - To use loops in concert with arrays
    - To use logic inside of a loop
    - To declare accumulator variables outside of loops that are used in loops, but whose state persists beyond the loop
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("0.2.8.4")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("0.0.0.0")
      feedback: "Try again: It looks like you're still returning the default value of 0 from the <code>countZeroes</code> method"    
 
files:
  - filename: "ArrayZeroes.java"
    name: arrayzeroes
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class ArrayZeroes {
            public static int countZeroes(int[] arr) {
                /** TODO: Fill this in.  You should return
                * an int representing the number of zeroes in the
                * array arr
                */
                return 0;
            }
        }

  - filename: "Tester.java"
    name: tester
    ismain: false
    isreadonly: true
    isvisible: true
    code: | 
        public class Tester {
            public static void main(String[] args) {
                int[] arr0 = {};
                int zeroes0 = ArrayZeroes.countZeroes(arr0);
                int[] arr1 = {0, 5, 10, 0, 3, 4};
                int zeroes1 = ArrayZeroes.countZeroes(arr1);
                int[] arr2 = {0, 0, 1, 2, 4, 3, 4, 4, 0, 1, 2, 0, 3, 0, 0, 0, 2, 2, 4, 0};
                int zeroes2 = ArrayZeroes.countZeroes(arr2);
                int[] arr3 = {3, 13, 12,  3, 20, 17, 10, 17,  6,  1, 19, 10, 15,  9,  9, 13, 11, 8, 17,  0,  2,  1,  4, 10, 20,  5, 14,  5, 20, 17, 14, 17, 16,  5, 17, 14,  1, 17, 10, 14, 20, 20,  8, 10,  9,  9, 20,  8, 14,  4, 13, 9,  3, 11,  2,  8, 12,  1, 13,  9, 13,  1,  9, 14, 16, 15,  0,  9, 3,  5, 17,  2,  0, 12,  8,  7, 13, 15, 14,  7, 10, 11, 18, 19, 14, 20, 10,  2,  3, 10, 20,  3, 19,  8, 14, 11, 11,  5,  5,  0};
                int zeroes3 = ArrayZeroes.countZeroes(arr3);
                System.out.print(zeroes0 + "." + zeroes1 + "." + zeroes2 + "." + zeroes3);
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
