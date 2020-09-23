---
layout: activity
permalink: /Activities/Conditionals
title: "CS173: Intro to Computer Science - Conditionals"
excerpt: "CS173: Intro to Computer Science - Conditionals"

info:
  next: ./Conditionals2
  
  goals: 
    - To be able to write an <code>if</code> statement
    - To be able to write an <code>else</code> statement
    - To design boolean expressions for conditionals
    - To implement complex conditional statements using boolean expression operators
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                int age = 38;
                
                if(age >= 35) {
                    System.out.println("You are old enough to run for President of the United States!");
                }
            }
        }
        ]]></script>     
      title: Conditionals for Selective Execution with <code>if</code> Statements
      questions:
        - Try running the above program for different ages (say, 18, 34, 35, and 36).
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                int age = 38;
                
                if(age >= 35) {
                    System.out.println("You are old enough to run for President of the United States!");
                } else {
                    System.out.println("You're too young to run for President.");
                }
            }
        }
        ]]></script>     
      title: Conditionals for Selective Execution with <code>if</code>/<code>else</code> Statements        
      questions:
        - Write and execute an <code>if</code>/<code>else</code> statement that determines if it is warm and not raining outside, and prints out whether or not it is appropriate to go outside.
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-2-ifs.html
      title: The <code>if</code> Statement
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-3-if-else.html
      title: The <code>if</code>/<code>else</code> Statement      
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/Exercises.html
      title: <code>if</code> Statements
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-10-practice-coding.html
      title: Code Practice with <code>if</code> Statements
    - link: https://repl.it/community/classrooms/20700/assignments/146540
      title: Practice with Conditionals
    - link: https://repl.it/community/classrooms/20700/assignments/146545
      title: Even or Odd?           

tags:
  - boolean
  - expressions
  - conditionals
  
---

