---
layout: exercise
permalink: /Modules/Strings/Exercise
title: "CS173: Intro to Computer Science - Strings"
excerpt: "CS173: Intro to Computer Science - Strings"

info:
  points: 3
  instructions: "Write a function that checks if two <code>String</code>s are equal, by checking them character by character.  Loop over all characters up to the length of the string, and obtain each character using the <code>str1.charAt(i)</code> or the <code>str1.substring(i, i+1)</code> method (and <code>str2.charAt(i)</code> or the <code>str2.substring(i, i+1)</code>, for the other string, as well)."
  goals:
    - "To iterate over <code>String</code> variables."

canvasasmtid: "137447"
canvaspoints: 3
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let ans1 = feedbackString.split("\n")[0].toLowerCase();
    let ans2 = feedbackString.split("\n")[1].toLowerCase();
    let ans3 = feedbackString.split("\n")[2].toLowerCase();
    let ans4 = feedbackString.split("\n")[3].toLowerCase();
    let ans5 = feedbackString.split("\n")[4].toLowerCase();
    let ans6 = feedbackString.split("\n")[5].toLowerCase();
  correctcheck: |
    ans1 === "true" && ans2 === "false" && ans3 === "false" && ans4 === "false" && ans5 === "false" && ans6 === "false"
 
files:    
  - filename: "CompareStrings.java"
    name: comparestrings
    ismain: false
    isreadonly: false
    isvisible: true
    code: |
        public class CompareStrings {
            /**
             * Compare the strings str1 and str2, character by character, 
             * and return true if they are equal and the same size.
             * @param str1 The first string to compare
             * @param str2 The second string to compare
             * @return true if the strings are equal, false if not      
             */
            public static boolean compare(String str1, String str2) {
                // TODO: If str1.length() is not equal to str2.length(), return false
            
                // TODO: Loop over each character and check that str1.charAt(i) equals str2.charAt(i).  
                // ... If not, return false
                // ... Hint: stop your loop at the smaller of the two string lengths (use Math.min() for this)!
                
                return true;
            }
        }
  - filename: "Driver.java"
    name: driver
    ismain: false
    isreadonly: true
    isvisible: true
    code: | 
        public class Driver {
            public static void checkEqual(String x, String y) {
                boolean isEqual = CompareStrings.compare(x, y);
                
                System.out.println(isEqual);
            }
                
            public static void main(String[] args) {
                String x = "bat";
                String y = "bat";
                checkEqual(x, y);

                String a = "testing";
                String b = "debugging";
                checkEqual(a, b);
                
                String c = "bat";
                String d = "cat";
                checkEqual(c, d);  

                String s = "computer";
                String t = "science";
                checkEqual(s, t);    

                String u = "bat";
                String v = "bar";
                checkEqual(u, v);  
                
                String e = "book";
                String f = "bookkeeper";
                checkEqual(e, f); 
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
