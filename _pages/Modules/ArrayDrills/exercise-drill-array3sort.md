---
layout: exercise
permalink: /ArrayDrills/Array3Sort
title: "CS174: OOP - Drills - Array 3 Sort"
excerpt: "CS174: OOP - Drills - Array 3 Sort"

info:
  prev: "./ArrayInsert"
  next: "./ArrayMinIndex"
  instructions: "Create a static method <code>sort3Elements</code> that takes in 3 integers and returns a 3-element array containing those integers in sorted order.  For instance, if it receives the integers 7, 1, and 3, it should return the array <code>{1, 3, 7}</code>"
  goals:
    - To do proper array indexing
    - To allocate and populate new arrays
    - To use conditional statements appropriately
    - To properly define methods
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("1,3,7.1,8,9")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("7,3,1.9,1,8")
      feedback: "Try again: You put the elements in the array, but you didn't sort them."   
    - incorrectcheck: |
        pos.includes("7,3,1.9,8,1")
      feedback: "Try again: You put the elements in descending order instead of ascending order."   
    - incorrectcheck: |
        pos.includes("0,0,0")
      feedback: "Try again: It looks like you forgot to fill in the array you returned with elements."    
    - incorrectcheck: |
        pos.includes("arr is undefined")
      feedback: "Try again: It looks like you forgot to return the array."    
    - incorrectcheck: |
        pos.includes("not a function")
      feedback: "Try again: It looks like you either didn't define the requested function or you misspelled it."   
 
files:
  - filename: "ArrayUtils.java"
    name: arrayutils
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class ArrayUtils {
            

            /**
            * Prints out the elements of an array, separated by commas
            * 
            * @param arr The array to print
            */
            public static void printArray(int[] arr) {
              for (int i = 0; i < arr.length; i++) {
                System.out.print(arr[i]);
                if (i < arr.length-1) {
                  System.out.print(",");
                }
              }
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
              int[] arr1 = ArrayUtils.sort3Elements(7, 3, 1);
              int[] arr2 = ArrayUtils.sort3Elements(9, 1, 8);
              ArrayUtils.printArray(arr1);
              System.out.print(".");
              ArrayUtils.printArray(arr2);
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
