---
layout: exercise
permalink: /Modules/Arrays/Exercise
title: "CS173: Intro to Computer Science - Nearest Value in an Array without Going Over"
excerpt: "CS173: Intro to Computer Science - Nearest Value in an Array without Going Over"

info:
  points: 3
  instructions: "Modify the Driver.java file to find the nearest value to a given value in an array, that is less than or equal to that value."
  goals:
    - To iterate over an array
    - To conditionally identify a specific array element by its index
  
canvasasmtid: "137454"
canvaspoints: 3
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let ans = feedbackString.split("-");
  correctcheck: |
    ans[0] === "1" && ans[1] === "2"
  incorrectchecks:
    - incorrectcheck: |
        ans[0] === "2" && ans[1] === "0"
      feedback: "Try again: You might want to use the absolute value of the difference, and only update the index and value if it is less than or equal to the target key!"
    - incorrectcheck: |
        ans[0] === "5" && ans[1] === "2"
      feedback: "Try again: You might want to use the absolute value of the difference!"
      
files:
  - filename: "ClosestValue.java"
    name: closestvalue
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class ClosestValue {
            /* Given an array of values, return the index 
               of the value that is closest to the key,
               but also less than or equal to the key. 
               Example: values = {3, 8, 6, 2, 4}
                        key = 7
                        return 2, because values[2] (6) is the nearest
                        value to the key (7) that is still smaller than 7. */
            public static int closestWithoutGoingOver(double[] values, double key) {
                /* TODO: initialize variables to represent the closest index (the result),
                         and the smallest difference you've seen so far.  For starters, 
                         set these to impossible values.  The index should be a value
                         that could never be an array index, like -1, and the smallest difference
                         should be a value so large that anything will seem smaller inside the loop. */
                
                    /* TODO: Loop over each item in values. */
                
                    /* TODO: for each value, calculate its difference from the key value */
                
                    /* TODO: If that difference is smaller than the smallest 
                         difference you've seen so far,
                         AND your value is less than or equal to key,
                         set the result to this index, and set the 
                         smallest difference you've seen to this difference value. */
                         
                /* TODO: return the closest index that you found */
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
                double[] arr1 = {3.2, 1.6, 100.3, 7.5, 1.8, 0.2};
                double key1 = 1.7;
                int ans1 = ClosestValue.closestWithoutGoingOver(arr1, key1);
                
                double[] arr2 = {3.2, 1.6, -6, -4, 0, 0.2};
                double key2 = -5;
                int ans2 = ClosestValue.closestWithoutGoingOver(arr2, key2);    

                System.out.print(ans1 + "-" + ans2);
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
