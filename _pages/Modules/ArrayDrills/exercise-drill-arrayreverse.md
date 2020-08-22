---
layout: exercise
permalink: /ArrayDrills/ArrayReverse
title: "CS174: OOP - Drills - Creating the reverse of an array"
excerpt: "CS174: OOP - Drills - Creating the reverse of an array"

info:
  prev: "./ArrayMean"
  next: "./ArrayInsert"
  instructions: "Fill in the method <code>getReverseArray</code> in <code>ArrayUtils.java</code> to return a new array which is the reverse of a given array.  For example, the array {0, 5, 2, 3} would turn into the array {3, 2, 5, 0}."
  goals:
    - To do proper array indexing
    - To use loops in concert with arrays
    - To allocate and populate new arrays
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("1,0,4,3,0,10,5,0.3,1,1,1,1,0,0")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("0,5,10,0,3,4,0,1.0,0,1,1,1,1,3")
      feedback: "Try again. You want to reverse the array, not just copy over the elements directly."
    - incorrectcheck: |
        pos.includes("undefined")
      feedback: "Try again. You are going out of bounds of the array!"
 
files:
  - filename: "ArrayUtils.java"
    name: arrayutils
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class ArrayUtils {
            public static int[] getReverseArray(int[] arr) {
              /** TODO: Fill in your code here to create the reverse array **/
              return {};
            }

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
                int[] arr0 = {0, 5, 10, 0, 3, 4, 0, 1};
                int[] arr0rev = ArrayUtils.getReverseArray(arr0);
                int[] arr1 = {0, 0, 1, 1, 1, 1, 3};
                int[] arr1rev = ArrayUtils.getReverseArray(arr1);
                ArrayUtils.printArray(arr0rev);
                System.out.print(".");
                ArrayUtils.printArray(arr1rev);
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
