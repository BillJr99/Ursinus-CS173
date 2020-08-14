---
layout: activity
permalink: /Activities/Iteration
title: "CS173: Intro to Computer Science - Iteration"
excerpt: "CS173: Intro to Computer Science - Iteration"

info:
  next: ./Iteration2
  
  goals: 
    - To be able to explain the uses of the <code>for</code> loop structure 
    - To be able to apply boolean expressions to iterative structures via the <code>for</code> loop

  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-2-for-loops.html
      title: <code>for</code> Loops
     
  additional_practice:
    - link: https://repl.it/community/classrooms/20700/assignments/146567
      title: Counting Practice
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-4-nested-loops.html
      title: Nested Loops      

  models:
    - model: |
        Conditionals can be used to repeatedly execute code.  There are three varieties of these “loops:” the for loop (which is useful when counting the number of iterations that are needed), the while loop (which is useful for executing until something is true), and the do loop (similar to the while loop, but it executes at least once and checks whether it should stop at the end of the loop, rather than at the beginning).    
        <br>
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                int i = 0;
                /* for(initial value; 
                        execute as long as this is true; 
                        what to do after each time through the loop) { … }
                */
                for(i = 0; i < 10; i++) {
                    System.out.println(i); // Counts from 0 to 9 and prints each
                }
            }
        }
        ]]></script>    
      title: The <code>for</code> Loop
      questions:
        - The code prints the numbers from 0 through 9.  Why doesn’t it also print the value 10?
        - What could you do to change this to print the values 0 through 10?  
        - What could you do to print the values 1 through 10?
        - What might you change in the code to print only the even values between 0 and 9, changing only the line beginning with for?
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        import java.util.Scanner;
        
        public class Main {
            public static void main(String[] args) {
                System.out.println("Each team gets 3 turns!");
                
                for(int i = 0; i < 10; i++) {
                    System.out.println("Team " + i);
                    for(int j = 0; j < 3; j++) {
                        System.out.println("Team " + i + " turn number " + j);
                    }
                }
            }
        }
        ]]></script>     
      title: Nested Loops
      questions:
        - How many times does the inner loop print statement execute?        
        
tags:
  - iterations
  
---

