---
layout: activity
permalink: /Activities/Iteration/While
title: "CS173: Intro to Computer Science - Iteration with the while Loop"
excerpt: "CS173: Intro to Computer Science - Iteration with the while Loop"

info:
  goals: 
    - To be able to explain the uses of the <code>while</code> loop structure 
    - To be able to apply boolean expressions to iterative structures via the <code>while</code> loop

  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-1-while-loops.html
      title: <code>while</code> Loops
      
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                boolean raining = false;

                while(!raining) {
                    double randVal = Math.random();
                    int minutes = (int) (randVal * 20);
                
                    System.out.println("Play outside for " + minutes + " minutes!");
                    raining = checkIfRaining(); // made up function!
                }
            }
        }
        ]]></script>        
      title: The <code>while</code> Loop
      questions:
        - "Draw a flow chart diagram as you did with the <code>if</code> statement in a <a href=\"../Conditionals3\">prior activity</a> ; this time, you can draw an arrow back to one of the flowchart elements to show the loop!"
        - Modify this code to implement a <code>checkIfRaining()</code> function that generates a random number between 1 and 10, and returns <code>true</code> if the number is greater than 7 (and return <code>false</code> otherwise).
        - "Develop an algorithm to determine if two <code>String</code> variables are equal."
        - "Develop a program to iterate over each character of a <code>String</code> and pass each character to a function that returns the letter's position in the alphabet (for example, the letter <code>a</code> would be position <code>0</code>."
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>  

tags:
  - iterations
  
---

