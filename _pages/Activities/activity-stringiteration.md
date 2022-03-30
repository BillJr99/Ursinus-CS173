---
layout: activity
permalink: /Activities/Iteration/Strings
title: "CS173: Intro to Computer Science - Iteration over Strings"
excerpt: "CS173: Intro to Computer Science - Iteration over Strings"

info:
  goals: 
    - To be able to apply iteration and conditionals to a <code>String</code>

  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-3-strings-loops.html 
      title: <code>String</code> Loops 
    - link: https://towardsdatascience.com/hamilton-a-text-analysis-of-the-federalist-papers-e64cb1764fbf
      title: Performing Text Analysis on the Federalist Papers
     
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQstringScrambleA.html
      title: <code>String</code> Iteration    

  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {               
                String str = "Hello!";
                
                for(int i = 0; i < str.length(); i++) {
                    System.out.println("Give me a " + str.charAt(i));
                }
            }
        }
        ]]></script>     
      title: Looping over Each Character
      questions:
        - "What is the value of <code>str.length()</code>?"
        - Why does this loop not start at the initial value 1?  
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[       
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
      title: Iterative Algorithms Using the <code>String</code>
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
      questions:
        - "For what values of <code>i</code> will the character <code>&lsquo;t&rsquo;</code> be found in this <code>String</code>?  You may find the <a href=https://cscircles.cemc.uwaterloo.ca/java_visualize/>Java Visualizer</a> or your IDE debugger helpful."
        - "Write a function that accepts a <code>String x</code>, a <code>char c</code>, and an <code>int n</code>.  Return the index of the <code>n&rsquo;th</code> instance of the character <code>c</code> in the <code>String x</code>.  Use the <code>indexOf()</code> method in a loop."
        
tags:
  - iterations
  - strings
  
---

