---
layout: exercise
permalink: /Modules/Strings/Exercise2
title: "CS173: Intro to Computer Science - Strings Revisited"
excerpt: "CS173: Intro to Computer Science - Strings Revisited"

info:
  points: 3
  instructions: "Implement the program below that converts a String to \"Pig Latin\" according to the rules at the bottom of the page."
  goals:
    - To iterate over <code>String</code> variables and return part-way through the string iteration.
    
canvasasmtid: "137450"
canvaspoints: 3
      
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let ans = feedbackString.split("-");
  correctcheck: |
    ans[0] === "ashtray" && ans[1] === "igpay" && ans[2] === "ilesmay" && ans[3] === "eggyay"
 
files:
  - filename: "PigLatin.java"
    name: piglatin
    ismain: false
    isreadonly: false
    isvisible: true
    code: |
        public class PigLatin {
            public static boolean isVowel(String input, int idx) {
                boolean result = false;

                if(input.toLowerCase().charAt(idx) == 'a' || 
                        input.toLowerCase().charAt(idx) == 'e' || 
                        input.toLowerCase().charAt(idx) == 'i' || 
                        input.toLowerCase().charAt(idx) == 'o' || 
                        input.toLowerCase().charAt(idx) == 'u') {
                    result = true;
                } else {
                    result = false;
                }
                
                return result;
            }
            
            public static int firstVowelLocation(String input) {
                /* TODO: fill this in.  Return the index i corresponding to the first 
                   position at which input.charAt(i) is a vowel */
            }
            
            public static String pigLatin(String input) {
                String result;
                
                int idx = firstVowelLocation(input);
                
                /* TODO: fill this in according to the two possibilities given in 
                   the rules at the bottom of the page. */
                
                return result;
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
                System.out.print(PigLatin.pigLatin("trash"));
                System.out.print("-");
                System.out.print(PigLatin.pigLatin("pig"));
                System.out.print("-");
                System.out.print(PigLatin.pigLatin("smile"));
                System.out.print("-");
                System.out.print(PigLatin.pigLatin("egg"));
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

## Rules

We will simplify the rules as follows:

* If a `String` starts with a vowel, simply append "yay" to the end of the `String`.
* Otherwise, modify the string so that all the letters of the `String` up to (but not including) the first vowel are moved to the end of the `String`.  Then, append "ay" to the end of the resulting `String`.

## Hints

Given a `String` variable (let's say it's called `str`):

* You can use the `str.substring(i)` method to return a `String` containing all characters in `str` from position `i` to the end of the `String`.  Don't forget that `String` indices are numbered starting from 0.
* You can use the `str.substring(i, j)` method to return a `String` containing all characters in `str` from position `i` up to (but not including) position `j` of the `String`.
* You can use the `+` operator to concatenate two `String` values (or their substrings, which are also just `String` values!).