---
layout: activity
permalink: /Activities/Strings
title: "CS173: Intro to Computer Science - Strings"
excerpt: "CS173: Intro to Computer Science - Strings"

info:
  goals: 
    - To be able to explain that a <code>String</code> is a class that stores text and provides functionality that manipulates that text.
    - To be able to explain that a <code>String</code> is immutable, and that new memory is allocated for a <code>String</code> when it is modified.
    - To be able to create and manipulate a <code>String</code>.
    
    - To be able to invoke the <code>concat()</code>, <code>indexOf()</code>, <code>substring()</code> and <code>replace()</code> methods of a <code>String</code>.
  models:
    - title: "The <code>String</code>"
      model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                // These are equivalent
                // String x = "Test";
                String x = new String("Test");
                
                // So are these:
                x = "Another test";
                x = new String("Another test");
            }
        }
        ]]></script> 
      questions: 
        - Unlike re-assigning a primitive variable, assigning a variable to an object creates a new object.  A <code>String</code> is a class that allocates memory for and stores text. Since String text cannot be reassigned once it is allocated (and must be re-created instead), a <code>String</code> is called an <strong>immutable</strong> object.  Why can’t a <code>String</code> be re-assigned like an <code>int</code> or <code>double</code> can?
    - title: <code>String</code> Manipulation
      model: |
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#concat(java.lang.String)" width="100%" height="480" style="pointer-events:none;" scrolling="no"></iframe>
        <br>
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#indexOf(int)" width="100%" height="600" style="pointer-events:none;" scrolling="no"></iframe>
        <br>
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#indexOf(int,int)" width="100%" height="700" style="pointer-events:none;" scrolling="no"></iframe>
        <br>
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#replace(char,char)" width="100%" height="700" style="pointer-events:none;" scrolling="no"></iframe>
        <br>
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#replace(java.lang.CharSequence,java.lang.CharSequence)" width="100%" height="480" style="pointer-events:none;" scrolling="no"></iframe>
        <br>
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#substring(int,int)" width="100%" height="640" style="pointer-events:none;"></iframe>
      questions: 
        - What is the difference between <code>x = x.concat(y)</code> and <code>x = x + y</code> for <code>String</code> objects <code>x</code> and <code>y</code>?
        - What is the difference between the two <code>indexOf()</code> methods given above? How do you know which version you are calling from a program?
        - What is the difference between the two <code>replace()</code> methods given above?  How do you know which version you are calling from a program?
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        import java.util.Arrays;
        
        public class Main {
            public static void main(String[] args) {
                String x = "bat";
                String y = "tab";
                
                /* Sorting the letters in a string by converting the string 
                 * to an array of individual characters.
                 * https://www.geeksforgeeks.org/sort-a-string-in-java-2-different-ways/
                 */
                char xArray = x.toCharArray();
                char yArray = y.toCharArray();
                
                Arrays.sort(xArray); // xArray now contains "abt"
                Arrays.sort(yArray); // yArray now contains "abt"
                
                // Reconstruct the Strings from the sorted arrays
                String x = new String(xArray); // x now contains "abt"
                String y = new String(yArray); // y now contains "abt"
            }
        }
        ]]></script>     
      title: Palendrome Checker
      questions: 
        - Write a function that checks if two <code>String</code>s are equal, by checking them character by character.  
        - Use this comparison function to determine if two <code>String</code>s are palendromes of each other.  Two <code>String</code>s are panendromes if their sorted characters are equal to one another.
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-6-strings.htm	
      title: Strings
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-7-string-methods.html
      title: String Methods

  additional_practice:
    - link: https://repl.it/community/classrooms/20700/assignments/146459
      title: Printing the length of a <code>String</code>
    - link: https://repl.it/community/classrooms/20700/assignments/146544
      title: The <code>charAt</code> Method
    - link: https://repl.it/community/classrooms/20700/assignments/146534
      title: The <code>indexOf</code> Method
    - link: https://repl.it/community/classrooms/20700/assignments/146536
      title: Substrings
    - link: https://repl.it/community/classrooms/20700/assignments/146558
      title: <code>String</code> Methods Practice
    - link: https://repl.it/community/classrooms/20700/assignments/146561
      title: The <code>substring</code> method
    - link: https://repl.it/community/classrooms/20700/assignments/146555
      title: Testing for Substrings at the End of a <code>String</code>
    - link: https://repl.it/community/classrooms/20700/assignments/146553
      title: Testing for <code>String</code> Equality
    - link: https://repl.it/community/classrooms/20700/assignments/146570
      title: Reversing a <code>String</code>     
    - link: https://repl.it/community/classrooms/20700/assignments/146565
      title: Mixed Case
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-12-practice-coding.html
      title: Coding with Objects
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQstringScrambleA.html
      title: <code>String</code> Manipulation
    - link: https://repl.it/community/classrooms/20700/assignments/146564
      title: <code>String</code> Pluralizer
tags:
  - strings
  
---

