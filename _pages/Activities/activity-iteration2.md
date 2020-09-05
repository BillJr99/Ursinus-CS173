---
layout: activity
permalink: /Activities/Iteration2
title: "CS173: Intro to Computer Science - Iteration"
excerpt: "CS173: Intro to Computer Science - Iteration"

info:
  next: ./Iteration3
  prev: ./Iteration

  goals: 
    - To be able to explain the uses of the <code>while</code> loop structure 
    - To be able to explain the uses of the <code>do</code> loop structure 
    - To be able to apply boolean expressions to iterative structures via the <code>while</code> loop
    - To be able to apply boolean expressions to iterative structures via the <code>do</code> loop    

  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-1-while-loops.html
      title: <code>while</code> Loops

  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-5-loop-analysis.html
      title: Loop Analysis
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/Exercises.html
      title: Iteration Review
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-8-practice-coding.html
      title: Iteration Practice Problems
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQselfDivisorA.html
      title: Self Divisors using the Modulus, Loops, and Conditionals
    - link: https://repl.it/community/classrooms/20700/assignments/146541
      title: Prime Checker
    - link: https://repl.it/community/classrooms/20700/assignments/146559  
      title: The Fibonacci Sequence
      
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
        - Modify this code to implement a <code>checkIfRaining()</code> function that generates a random number between 1 and 10, and returns <code>true</code> if the number is greater than 7 (and return <code>false</code> otherwise).
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>  
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
                    System.out.println(“Can you guess my number?”);
                    guess = input.nextInt(); // read an integer from the keyboard
                } while(guess != value);

                System.out.println(“You got it!”);
            }
        }
        ]]></script>        
      title: The <code>do</code> Loop with User Input
      questions: 
        - "Why isn’t the code example from the first model written as a <code>do</code> loop?  How might this result in telling someone to \"play outside\" while it is raining?"
tags:
  - iterations
  
---

