---
layout: exercise
permalink: /ArrayDrills/ArrayMean
title: "CS174: OOP - Drills - Printing array with commas"
excerpt: "CS174: OOP - Drills - Printing array with commas"

info:
  prev: "./ArraySep"
  instructions: "Fill in a method to compute the mean of an array of ints.  Note that even though the inputs are integers, their mean may be a decimal number!  For example, the mean of <code>{0, 5, 2, 4}</code> is <code>2.75</code>."  Finally, <i>if an empty array is passed to your method, you should return 0.0</i>.  Recall that this is referred to as a "boundary case" or "edge case" in testing.
  goals:
    - To do proper array accessing
    - To use loops in concert with arrays
    - To use logic inside of a loop
    - To declare accumulator variables outside of loops that are used in loops, but whose state persists beyond the loop
    - To use proper types
    - To practice handling boundary cases
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("2.875,1.0,0.0")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("2,")
      feedback: "Try again. Be careful to use a double variable to store your average!"  
    - incorrectcheck: |
        pos.includes("23")
      feedback: "Try again. Don't forget to divide by the number of elements in the array!" 
 
files:
  - filename: "ArrayUtils.java"
    name: arrayprinter
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class ArrayUtils {
            public static double getMean(int[] arr) {
              /** TODO: Fill in your code here to compute the mean **/
              return 0.0;
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
                System.out.print((double)ArrayUtils.getMean(arr0));
                System.out.print(",");
                int[] arr1 = {0, 0, 1, 1, 1, 1, 3};
                System.out.print((double)ArrayUtils.getMean(arr1));
                System.out.print(",");
                int[] arr2 = {};
                System.out.print((double)ArrayUtils.getMean(arr2));
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
