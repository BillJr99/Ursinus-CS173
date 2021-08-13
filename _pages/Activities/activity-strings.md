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
        <img src="../manim/output/Substrings.gif" alt="Manim Strings Animation" />
        <br>      
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html" width="100%" height="700" scrolling="yes"></iframe>
      questions: 
        - What is the difference between <code>x = x.concat(y)</code> and <code>x = x + y</code> for <code>String</code> objects <code>x</code> and <code>y</code>?
        - "Rewrite the statement <code>String z = &quot;Cheese&quot; + &quot&Hamburger&quot;.substring(3);</code> using the <code>concat</code> function."
        - What is the difference between the two <code>indexOf()</code> methods given above? How do you know which version you are calling from a program?
        - What is the difference between the two <code>replace()</code> methods given above?  How do you know which version you are calling from a program?
        - You can compare two strings using <code>str1.equals(str2)</code>.  Why do you think <code>str1 == str2</code> won't work?
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
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

  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-6-strings.htm	
      title: Strings
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-7-string-methods.html
      title: String Methods

  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-12-practice-coding.html
      title: Coding with Objects
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQstringScrambleA.html
      title: <code>String</code> Manipulation
tags:
  - strings
  
---

