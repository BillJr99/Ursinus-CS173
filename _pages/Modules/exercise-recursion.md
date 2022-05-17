---
layout: exercise
permalink: /Modules/Recursion/Exercise
title: "CS173: Intro to Computer Science - Recursion"
excerpt: "CS173: Intro to Computer Science - Recursion"

info:
  points: 3
  prev: "./Module"
  instructions: "Fill in the reverseString method below to recursively compute the string in reverse."
  goals:
    - To implement a recursive function call
    
canvasasmtid: "137468"
canvaspoints: 3
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let i1 = feedbackString.indexOf("olleh");
    let i2 = feedbackString.indexOf("desserts");
  incorrectchecks:
    - incorrectcheck: |
        editorText.includes("for") || editorText.includes("while")
      feedback: "Try again: don't forget to use recursion instead of any loops!  Your solution should not include a while or for loop."    
  correctcheck: |
    i1 > -1 && i2 > -1 && i2 > i1 && !editorText.includes("for") && !editorText.includes("while")
 
files:
  - filename: "Recursion.java"
    name: recursion
    ismain: false
    isreadonly: false
    isvisible: true
    code: |
        public class Recursion {
            /**
            * Given a string, return the reverse of it
            * Example) "hello", should return "olleh"
            * "o" + reverseString("hell")
            *    reverseString("hell") = "l" + reverseString("hel")
            *       reverseString("hel") = "l" + reverseString("he")
            *          reverseString("he") = "e" + reverseString("h")
            *            reverseString("h") = "h" + reverseString("")
            * @param s The input string
            * @return The reverse of s
            */
            public String reverseString(String s) {
                String result = "";
                if (s.length() > 0) {
                    // TODO: Fill this in as the last character
                    // plus the reverse of all but the last character
                    
                }
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
                Recursion r = new Recursion();
                System.out.println(r.reverseString("hello"));
                System.out.println(r.reverseString("stressed"));
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

In this exercise \[[^1]\], the main() method runs the code on "hello" and "stressed," and they should give "olleh" and "desserts," respectively (remember that when you're feeling stressed during finals week!).

## Hints
* Since s.length()-1 is the last index of a string s, the last character of s can be extracted with s.charAt(s.length()-1)
* Recall from chapter 2 that for a string s, s.substring(a, b) gives the substring of a string from index a to index b, not including b. So, for instance, if s = "stressed", then s.substring(0, 7) would yield the string "stresse". In this case, index 7 is the last index, but we don't include that index.
* If you get an error like too much recursion, this is the same as the stack overflow error we saw in the video. This probably means that the string you're calling recursively isn't actually decreasing in length, so you never reach the stopping condition of an empty string, and your code goes on forever. Check to make sure you're taking the right substring in your recursive call.

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie)