---
layout: activity
permalink: /Activities/Iteration
title: "CS173: Intro to Computer Science - Iteration"
excerpt: "CS173: Intro to Computer Science - Iteration"

info:
  goals: 
    - To be able to explain the uses of the different loop structures (<code>for</code>, <code>while</code>, and <code>do</code>)
    - To be able to apply boolean expressions to iterative structures via the <code>for</code>, <code>while</code>, and <code>do</code> loops
    - To be able to apply iteration and conditionals to a <code>String</code>

  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-2-for-loops.html
      title: <code>for</code> Loops
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-1-while-loops.html
      title: <code>while</code> Loops
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-4-nested-loops.html
      title: Nested Loops
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-3-strings-loops.html 
      title: String Loops 
     
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-5-loop-analysis.html
      title: Loop Analysis
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/Exercises.html
      title: Iteration Review
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-8-practice-coding.html
      title: Iteration Practice Problems
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQselfDivisorA.html
      title: Self Divisors using the Modulus, Loops, and Conditionals
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQstringScrambleA.html
      title: String Iteration    

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
        public class Main {
            public static void main(String[] args) {
                boolean raining = false;

                while(!raining) {
                    System.out.println("Play outside!");
                    raining = checkIfRaining(); // made up function!
                }
            }
        }
        ]]></script>        
      title: The <code>while</code> Loop
      questions:
        - Why isn’t this code example written as a do loop?  How might this result in telling someone to “play outside” while it is raining?
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
      title: The <code>while</code> Loop with User Input
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
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        import java.util.Scanner;
        
        public class Main {
            public static void main(String[] args) {
                String x = "test";
                
                boolean containsT = false;
                int numT = 0;
                
                for(int i = 0; i < x.length(); i++) {
                    if(x.charAt(i) == 't') {
                        containsT = true;
                        numT++;
                    }
                }
            }
        }
        ]]></script>     
      title: Iterative Algorithms Using the String
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
      questions:
        - "For what values of <code>i</code> will the character <code>'t'</code> be found in this <code>String</code>?  You may find the <a href=\"https://cscircles.cemc.uwaterloo.ca/java_visualize/\">Java Visualizer</a> or your IDE debugger helpful."
        
tags:
  - iterations
  - strings
  
---

