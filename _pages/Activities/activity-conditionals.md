---
layout: activity
permalink: /Activities/Conditionals
title: "CS173: Intro to Computer Science - Conditionals"
excerpt: "CS173: Intro to Computer Science - Conditionals"

info:
  goals: 
    - To be able to write an <code>if</code> statement
    - To be able to write an <code>else</code> statement
    - To design boolean expressions for conditionals
    - To combine the <code>if</code> and <code>else</code> blocks to form conditionals that utilize the <code>else if</code> construct
    - To implement complex conditional statements using boolean expression operators
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public void canRunForPresident(int age) {
                if(age >= 35) {
                    System.out.println("You are old enough to run for President of the United States!");
                }
            }
            
            public static void main(String[] args) {
                canRunForPresident(38);
            }
        }
        ]]></script>     
      title: Conditionals for Selective Execution with <code>if</code> Statements
      questions:
        - Modify the above program to return a boolean that is true if a person can run for president, and false otherwise      
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public void canRunForPresident(int age) {
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
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void canRunForPresident2(int age) {
                if(age >= 18) {
                    System.out.println("You are old enough to vote!");
                    
                    if(age >= 35) {
                        System.out.println("... and you are old enough to run for President!");
                    } else {
                        System.out.println("... but not old enough to run for President!");
                    }
                } else {
                    System.out.println("You're too young to run for President, and too young to vote.");
                }
            }
            
            public static void canRunForPresident(int age) {
                if(age >= 35) {
                    System.out.println(“You are old enough to run for President of the United States!”);
                } else if(age >= 18) {
                    System.out.println(“You can’t run for President, but you are old enough to vote!”);
                } else {
                    System.out.println(“You’re too young to run for President, and too young to vote.”);
                }
            }
            
            public static void main(String[] args) {
                canRunForPresident(38);
                canRunForPresident2(21);
            }
        }
        ]]></script>         
      title: Creating a Waterfall of Possibilities by combining <code>else</code> and <code>if</code>
      questions:
        - Which code structure (<code>canRunForPresident</code> or <code>canRunForPresident2</code>) do you prefer and why?
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void canVoteButNotRunForPresident(int age) {
                if(age >= 18 && age <= 35) {
                    System.out.println(""); // What should we say here?
                }
            }
            
            public static void main(String[] args) {
                canVoteButNotRunForPresident(25);
            }
        }
        ]]></script>      
      title: "Compound <code>if</code> conditionals"
      questions: 
        - What text should go into the <code>println</code> statement to indicate whether the person can vote (at least age 18) but also is too young to run for president (at least age 35)?
        - Suppose we wished to <code>return</code> a <code>boolean</code> to <code>main()</code> indicating whether a person is old enough to vote but not old enough to run for President.  What modifications to the above code are needed?
        - "Consider the letter grade breakdown table on our <a href=\"../#grading\">course syllabus</a>.  Write a series of compound <code>if</code> statements that determines if your grade is an A+, an A, or an A-."
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>         
    - model: |
        <img src="../images/venn3.png" alt="Empty 3-way Venn Diagram">
      title: "Putting It All Together: Implementing a Venn Diagram"
      questions:
        - "Make up a 3-way <a href=\"https://en.wikipedia.org/wiki/Venn_diagram\">Venn Diagram</a> of your choosing; you can look one up on the Internet if you wish."
        - "Label the three large circles \"A\", \"B\", and \"C\".  In each of the 7 regions within the Venn Diagram, which elements are true and which are false?"
        - "Write a series of <code>if</code> statements that may use <code>else</code> and <code>else if</code> blocks that print out the different states of your Venn Diagram.  There are a few ways to go about this, so we will discuss and compare approaches as a class."
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-2-ifs.html
      title: The <code>if</code> Statement
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-3-if-else.html
      title: The <code>if</code>/<code>else</code> Statement
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-4-else-ifs.html
      title: <code>if</code>/<code>else if</code> Statements
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-5-compound-ifs.html 
      title: Compound <code>if</code> Statements
  additional_practice:
    - link: https://repl.it/community/classrooms/20700/assignments/146540
      title: Practice with Conditionals
    - link: https://repl.it/community/classrooms/20700/assignments/146545
      title: Even or Odd?
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/Exercises.html
      title: <code>if</code> Statements
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-10-practice-coding.html
      title: Code Practice with <code>if</code> Statements
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/APLine.html
      title: Using Class Functions
tags:
  - boolean
  - expressions
  - conditionals
  
---

