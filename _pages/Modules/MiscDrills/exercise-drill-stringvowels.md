---
layout: exercise
permalink: /MiscDrills/StringVowels
title: "CS174: OOP - Drills - Vowel Counting"
excerpt: "CS174: OOP - Drills - Vowel Counting"

info:
  prev: "./ArrayInsert"
  next: "./ArrayMinIndex"
  instructions: "Fill in the method <code>countVowels</code> to count the number of vowels (both lowercase and uppercase, not including y or Y) in a string.  Recall that the method <code>charAt</code> of the <code>String</code> class returns a character at a particular index, and, like arrays, strings are zero-indexed.  For instance, if <p><code>String s = \"I love CS\";</code></p>, then <p><code>s.charAt(3)</code></p> returns the character <code>o</code>.<p>Recall also that the <code>length()</code> method of the <code>String</code> class returns the total number of characters in the string."
  goals:
    - To do proper string indexing
    - To use conditional statements appropriately
    - To keep track of auxiliary variables within loops
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("3.12.10")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("9.44.12")
      feedback: "Try again: It appears you are counting every single character as a vowel."     
    - incorrectcheck: |
        pos.includes("0.0.0")
      feedback: "Try again: It appears that you aren't updating the auxiliary variable to count the number of vowels, and it is always returning 0."     
 
files:
  - filename: "StringUtils.java"
    name: stringutils
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class StringUtils {
            

            /**
            * Count the number of vowels in a string, regardless
            * of case
            * 
            * @param s The string to examine
            * @return The number of vowels in the string
            */
            public static int countVowels(String s) {
              int numVowels = 0;
              // TODO: Fill this in
              return numVowels;
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
              String s1 = "I love CS";
              int vowels1 = StringUtils.countVowels(s1);
              String s2 = "The quick brown fox jumped over the lAzy dOg";
              int vowels2 = StringUtils.countVowels(s2);
              String s3 = "aEIOu  AeioU";
              int vowels3 = StringUtils.countVowels(s3);
              System.out.print(vowels1 + "." + vowels2 + "." + vowels3);
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
