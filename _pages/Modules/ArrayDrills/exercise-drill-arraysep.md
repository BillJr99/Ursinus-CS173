---
layout: exercise
permalink: /ArrayDrills/ArraySep
title: "CS174: OOP - Drills - Printing array with commas"
excerpt: "CS174: OOP - Drills - Printing array with commas"
canvasasmtid: "95024"
canvaspoints: "2"
canvashalftries: 5

info:
  prev: "./ArrayZeroes"
  next: "./ArrayMean"
  instructions: "Declare a void method <code>printArray</code> in the <code>ArrayPrinter</code> class.  This method should take an array of ints, and it should then print out the elements of the array separated by commas (this is useful, since printing out an array by default in Java just gives its memory address).  For example, the array <code>{0,5,2,4}</code> should be printed out as <b>0, 5, 2, 4</b>.  Note how there is no comma or space at the end of the output string."
  goals:
    - To declare a public static method to some specification
    - To do proper array indexing
    - To use loops in concert with arrays
    - To use logic inside of a loop
    - To use the <code>System.out.print</code> method properly
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("0, 5, 10, 0, 3, 4.0, 0, 1, 2, 4, 3, 4.")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("0, 5, 10, 0, 3, 4,") || pos.includes("0, 0, 1, 2, 4, 3, 4,")
      feedback: "Try again. Be careful not to include a comma at the end!"
    
    - incorrectcheck: |
        pos.includes("0,5,10,0,3,4") || pos.includes("0,0,1,2,4,3,4")
      feedback: "Try again. Be sure to include spaces after commas!"    
 
files:
  - filename: "ArrayPrinter.java"
    name: arrayprinter
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class ArrayPrinter {
            /** TODO: Declare your method here **/
        }

  - filename: "Tester.java"
    name: tester
    ismain: false
    isreadonly: true
    isvisible: true
    code: | 
        public class Tester {
            public static void main(String[] args) {
                int[] arr0 = {0, 5, 10, 0, 3, 4};
                ArrayPrinter.printArray(arr0);
                System.out.print(".");
                int[] arr1 = {0, 0, 1, 2, 4, 3, 4};
                ArrayPrinter.printArray(arr1);
                System.out.print(".");
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
