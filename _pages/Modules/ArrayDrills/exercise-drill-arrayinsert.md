---
layout: exercise
permalink: /ArrayDrills/ArrayInsert
title: "CS174: OOP - Drills - Array Insert"
excerpt: "CS174: OOP - Drills - Array Insert"

info:
  prev: "./ArrayReverse"
  next: "./Array3Sort"
  instructions: "Modify the <code>insertElement</code> method in <code>ArrayUtils.java</code> to insert an element at a particular index.  For example, if you have the array <code>{0, 5, 4, 8, 2}</code> and you insert the element <code>1</code> at index <code>2</code>, you should create a new array with the elements <code>{0, 5, <b>1</b>, 4, 8, 2}</code>. <p><b>NOTE:</b> The tediousness of this seemingly simple operation is what motivates us to use other data structures such as an <code>ArrayList</code> or linked list."
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
    pos.includes("0,5,1,4,8,2.0,5,4,8,10,2.50,0,5,4,8,2")
  incorrectchecks:
    - incorrectcheck: |
        pos.length == 0
      feedback: "Try again: It looks like you're still returning the default empty array from the <code>insertElement</code> method. <p><b>Hint:</b> You should have two loops: one to copy the elements before the insertion index, and one to copy the elements after the insertion index</p>"    
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
            /**
            * Creates and returns a new array with "element" at the index "index," and
            * everything after the original index shifted over to the right by one
            *
            * @param arr The original array
            * @param index The index at which to place the new element.  Should be a value less
            *              than the length of the array
            * @param element The value of the new element
            * 
            * @return An array with the new element inserted
            */
            public static int[] insertElement(int[] arr, int index, int element) {
                /** TODO: Fill this in.  You should return
                * an int representing the number of zeroes in the
                * array arr
                */
                int[] newArray = {}; // This is a dummy value. You should change this
                return newArray;
            }

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
                int[] arr0 = {0, 5, 4, 8, 2};
                int[] result0 = ArrayUtils.insertElement(arr0, 2, 1);
                int[] result1 = ArrayUtils.insertElement(arr0, 4, 10);
                int[] result2 = ArrayUtils.insertElement(arr0, 0, 50);
                ArrayUtils.printArray(result0);
                System.out.print(".");
                ArrayUtils.printArray(result1);
                System.out.print(".");
                ArrayUtils.printArray(result2);
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
