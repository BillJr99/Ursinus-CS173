---
layout: activity
permalink: /Activities/Recursion
title: "CS173: Intro to Computer Science - Recursion"


info:
  next: ./Recursion2
  
  goals: 
    - To identify a recursive base case
    - To implement recursive algorithms
  
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/topic-10-1-recursion.html
      title: Recursion      
      
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
           public static int fibonacci(int n) {
                if(n <= 1) {    // Recursive alogirhtms need to know when to stop!
                    return 1;   // This is called the base case: fib(0) = fib(1) = 1
                } else {
                    return fibonacci(n-1) + fibonacci(n-2);
                }
           }
           
           public static void main(String[] args) {
                int ans = fibonacci(4);
                System.out.println(ans);
           }
        }
        ]]></script> 
        <br>
        <img src="../images/examples/fibonacci.png" alt="Diagram of Fibonacci Recursive Calls" />        
      title: Recursive Algorithms
      questions:
        - Notice that the algorithm &quot;starts over&quot; on a smaller part of the array after each guess.  This is a hallmark of a &quot;recursive algorithm.&quot;  They are like loops.  Do you think this approach requires more or less code to write than a non-recursive version?  Why or why not?
        - How many times did this algorithm compute <code>fib(2)</code>?
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
           public static int factorial(int n) {
                if(________) {               // What is the base case?
                    return ___;              // What gets returned by the base case?
                } else {
                    return ____ * _______;  // What is the recursive procedure?
                }
           }
           
           public static void main(String[] args) {
                int ans = factorial(4);
                System.out.println(ans);
           }
        }
        ]]></script>       
      title: Base Cases and Recursive Steps
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>       
      questions:
        - Fill in the base case and recusive call for the factorial function, and try running it!
        
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/rEasyMC.html
      title: Questions about Recursion
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/rBasePractice.html 
      title: Recursive Base Cases
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/recursionCodePractice.html 
      title: Recursion
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/topic-10-1-recursion-day1.html#factorial-method
      title: Recursive Factorial Function
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/topic-10-1-recursion-challenge.html
      title: Recursion Tracing
      
  reflective_prompts:
    - How might you improve upon (reduce) the number of calls to <code>fib(2)</code> in the Fibonacci example?

tags:
  - recursion
  - algorithms
  
---

