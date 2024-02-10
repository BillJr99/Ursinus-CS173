---
layout: activity
permalink: /Activities/Strings
title: "CS173: Intro to Computer Science - Strings"


info:
  warmup: "Trace <a href=\"../Modules/Horstmann/Swap/Exercise\" target=\"_blank\">this algorithm</a> to swap two <code>int</code> variables."
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
    - title: <code>String</code> Manipulation with <code>substring</code>
      model: |
        <img src="../files/manim/output/Substrings.gif" alt="Manim String substring Animation" />
      questions: 
        - What is the difference between <code>x = x.concat(y)</code> and <code>x = x + y</code> for <code>String</code> objects <code>x</code> and <code>y</code>?
        - "Rewrite the statement <code>String z = &quot;Cheese&quot; + &quot;Hamburger&quot;.substring(3);</code> using the <code>concat</code> function."
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
    - title: <code>String</code> Searching with <code>indexOf</code>
      model: |
        <img src="../files/manim/output/StringIndexOf.gif" alt="Manim String indexOf Animation" />
      questions: 
        - What is the difference between the two <code>indexOf()</code> methods given above? How do you know which version you are calling from a program?
    - title: "More <code>String</code> Functions"
      model: |
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html" width="100%" height="700" scrolling="yes"></iframe>
        <br>
        <img src="../files/manim/output/StringReplace.gif" alt="Manim String replace Animation" />
      questions:
        - What is the difference between the two <code>replace()</code> methods given above?  How do you know which version you are calling from a program?
        - "Write a Java statement to replace &quot;Ham&quot; with &quot;Cheese&quot; in a <code>String</code> &quot;Hamburger&quot;"
    - title: "Working with <code>String</code>s"
      model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                String x = "Test";
                String y = new String("Test");
                
                if(x.equals(y)) {
                    System.out.println("x and y contain the same text!");
                }
                
                String z = "tan";
                System.out.println(z.substring(1, 2) + z.substring(0, 1));
            }
        }
        ]]></script> 
      questions: 
        - Why is it necessary to write <code>x.equals(y)</code> instead of <code>x == y</code> to check if two <code>String</code> objects contain the same text?       
        - What does the print statement output for the string <code>z</code>?
        - How might you print only the "est" characters from <code>x</code> using the <code>substring</code> method?
        - You can compare two strings using <code>str1.equals(str2)</code>.  Why do you think <code>str1 == str2</code> won't work?
        - "Java includes a <code>equalsIgnoreCase</code> function.  How do you think this works, using other functions that the <code>String</code> class provides?"
        - "Write a function that accepts two <code>String</code> parameters and returns true if the third character of each <code>String</code> is the same.  Be careful to check the length of each <code>String</code> first!"
        - "Using <code>String</code> methods, create a variable containing the word &quot;Book&quot; and the word &quot;keeper&quot;, and create the word &quot;Bookkeeper&quot; and &quot;Beekeeper&quot;.  There are multiple ways to do this!" 
        - "Read a String from the console, check that it is exactly a 5-letter word, and if so, convert it to upper-case.  Replace all the vowels with asterisks
Print the result!"
        - "Read a String from the console containing only the letters A, C, G, and/or T, and convert it to uppercase.  Replace the A's to T's, and all the T's to A's.  Replace the G's with C's and all the C's to G's."
        - "Challenge: there is a String function called matches that will check if a text pattern exists inside the String.    It returns a boolean (true if the pattern is found, false if not).  Use the matches function to see if any letter besides A, C, G, or T is in the String.  Here are some hints: <code>.*</code> means to search for any character (the <code>.</code> represents this) any number of times (the <code>*</code>).  You can check for a particular character using brackets like this: <code>[ACGT]</code> will match one character that is equal to A, C, G, or T.  Try searching for any number of characters, followed by a character in the alphabet other than A, C, G, or T, followed by any number of characters."

  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-6-strings.htm	
      title: Strings
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-7-string-methods.html
      title: String Methods
    - link: https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
      title: "String Javadoc Documentation Page"

  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-12-practice-coding.html
      title: Coding with Objects
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQstringScrambleA.html
      title: <code>String</code> Manipulation
tags:
  - strings
  
---

