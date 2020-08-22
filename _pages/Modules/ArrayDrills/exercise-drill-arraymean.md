---
layout: exercise
permalink: /ArrayDrills/ArrayMean
title: "CS174: OOP - Drills - Computing the mean of arrays"
excerpt: "CS174: OOP - Drills - Computing the mean of arrays"

info:
  prev: "./ArraySep"
  next: "./ArrayReverse"
  instructions: "Fill in a method to compute the mean of an array of ints.  Note that even though the inputs are integers, their mean may be a decimal number!  For example, the mean of <code>{0, 5, 2, 4}</code> is <code>2.75</code>.  Finally, <i>if an empty array is passed to your method, you should return 0.0</i>.  Recall that this is referred to as a <i>boundary case</i> or <i>edge case</i> in testing."
  goals:
    - To do proper array indexing
    - To use loops in concert with arrays
    - To declare accumulator variables outside of loops that are used in loops, but whose state persists beyond the loop
    - To use proper types
    - To handle boundary cases
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("2.875.1.0")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("2.")
      feedback: "Try again. Be careful to use a double variable to store your average!"  
    
    - incorrectcheck: |
        pos.includes("23")
      feedback: "Try again. Don't forget to divide by the number of elements in the array!" 

    - incorrectcheck: |
        pos.includes("0.0.0")
      feedback: "Try again. It seems like you're still returning the default value of 0 for all of your arrays!" 

    - incorrectcheck: |
        pos.includes("NaN")
      feedback: "Try again. It appears you may be dividing by zero somewhere.  Be careful that you handle the case properly when there are no elements in the array!"
 
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
                double mean0 = (double)ArrayUtils.getMean(arr0);
                int[] arr1 = {0, 0, 1, 1, 1, 1, 3};
                double mean1 = (double)ArrayUtils.getMean(arr1);
                int[] arr2 = {};
                double mean2 = (double)ArrayUtils.getMean(arr2);
                System.out.print(mean0 + "." + mean1 + "." + mean2);
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
