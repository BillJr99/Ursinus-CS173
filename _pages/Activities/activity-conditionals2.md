---
layout: activity
permalink: /Activities/Conditionals2
title: "CS173: Intro to Computer Science - Conditionals"
excerpt: "CS173: Intro to Computer Science - Conditionals"

info:
  prev: ./Conditionals
  next: ./Conditionals3
  
  goals: 
    - To be able to write an <code>if</code> statement
    - To be able to write an <code>else</code> statement
    - To design boolean expressions for conditionals
    - To implement complex conditional statements using boolean expression operators
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void canRunForPresident(int age) {
                if(age >= 35) {
                    System.out.println("You are old enough to run for President of the United States!");
                } else {
                    System.out.println("You're too young to run for President.");
                }
            }
            
            public static void main(String[] args) {
                canRunForPresident(38);
            }
        }
        ]]></script>     
      title: Conditionals for Selective Execution with <code>if</code>/<code>else</code> Statements
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-2-ifs.html
      title: The <code>if</code> Statement
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-3-if-else.html
      title: The <code>if</code>/<code>else</code> Statement
  additional_practice:
    - link: https://repl.it/community/classrooms/20700/assignments/146540
      title: Practice with Conditionals
    - link: https://repl.it/community/classrooms/20700/assignments/146545
      title: Even or Odd?

tags:
  - boolean
  - expressions
  - conditionals
  
---

