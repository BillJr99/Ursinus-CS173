---
layout: activity
permalink: /Activities/Iteration/Do
title: "CS173: Intro to Computer Science - Iteration with the do Loop"


info:
  goals: 
    - To be able to explain the uses of the <code>do</code> loop structure 
    - To be able to apply boolean expressions to iterative structures via the <code>do</code> loop    

  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-5-loop-analysis.html
      title: Loop Analysis
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/Exercises.html
      title: Iteration Review
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-8-practice-coding.html
      title: Iteration Practice Problems
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQselfDivisorA.html
      title: Self Divisors using the Modulus, Loops, and Conditionals
      
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        import java.util.Scanner;
        
        public class Main {
            public static void main(String[] args) {
                int value = 7;
                int guess = -1;

                // Used to read the user’s input from the console
                Scanner input = new Scanner(System.in);

                do {
                    System.out.println("Can you guess my number?");
                    guess = input.nextInt(); // read an integer from the keyboard
                } while(guess != value);

                System.out.println("You got it!");
            }
        }
        ]]></script>        
      title: The <code>do</code> Loop with User Input
      questions: 
        - "Using this program structure as a template, write a program to ask the user to enter a menu option between 1 and 4.  Print out one of four different messages depending on the menu option they choose, and if they do not enter a number between 1 and 4, continue prompting them until they do so."
tags:
  - iterations
  
---

