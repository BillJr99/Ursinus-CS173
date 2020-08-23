---
layout: activity
permalink: /Activities/DynamicProgramming
title: "CS173: Intro to Computer Science - Dynamic Programming"
excerpt: "CS173: Intro to Computer Science - Dynamic Programming"

info:
  goals: 
    - To explain the benefits of Dynamic Programming
    - To implement Dynamic Programming to improve the runtime performance of a given algorithm
  models:
    - model: |   
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void fibonacci(int n) {
                if(n <= 0) {
                    return 0;
                } else if(n <= 2) {
                    return 1;
                } else {
                    return fibonacci(n - 1) + fibonacci(n - 2);
                }
            }
            
            public static void main(String[] args) {
                System.out.println(fibonacci(5));
            }
        }
        ]]></script>  
      title: The Fibonacci Sequence
      questions:
        - Despite the concise code, what is inefficient about this approach to the Fibonacci sequence?
        - Try removing the recursive function calls: replace assignments or returns with array assignments, and write a loop instead.  
        - Is your loop solving the problem from the top-down or bottom-up?  That is, is your loop counting up or down, and why?  How is this similar or different from the recursive approach?
  
tags:
  - dynamicprogramming
  - recursion
  - iteration
  
---

