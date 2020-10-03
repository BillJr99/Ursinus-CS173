---
layout: activity
permalink: /Activities/Testing
title: "CS173: Intro to Computer Science - Testing"
excerpt: "CS173: Intro to Computer Science - Testing"

info:
  goals: 
    - To be able to design test cases for unit testing a program
    - To design code modules for unit testing
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {            
            public static int triangleArea(int base, int height) {
                // Broken Code!
                return 1 / 2 * base * height;
            }
            
            public static void main(String[] args) {
                System.out.println(triangleArea(5, 2));
                System.out.println(triangleArea(3, -2));
            }
        }
        ]]></script>          
      title: Choosing Unit Tests
      questions:
        - What's wrong with this code? (there is more than one answer!)
        - How many calls would you make to <code>triangleArea</code> before you decide that it is "passing?"  What paramter inputs would you supply to those calls?
        - "Visit <a href=\"../NetBeans/JUnit\">this guide</a> and design a unit test for <code>triangleArea</code>.  You can just write the code in your notes: there is no need to compile or execute it now (we will do this in lab instead!)."
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        import java.util.Random;
        
        public class Main {            
            public static boolean isHeads() {
                Random rng = new Random();
                
                // Use the random number generator (rng)
                // to generate a value >= 0.0 and < 1.0
                double randomValue = rng.nextDouble();
                
                boolean result = false;
                if(randomValue > 0.5) {
                    result = true;
                } 
                
                return result;
            }
            
            public static void main(String[] args) {
                System.out.println(isHeads());
                System.out.println(isHeads());
            }
        }
        ]]></script>          
      title: Facilitating Unit Tests
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>       
      questions:
        - What makes this a difficult function to test? 
        - What could we do to better facilitate testing a function like this?
        - "Print the random number <code>randomValue</code> in the <code>isHeads</code> function when you compute it.  Then, call <code>rng.setSeed(100);</code> right before the call to <code>rng.nextDouble()</code>, and try running the program again.  What do you notice?"
        
reflective_prompts:
  - Suppose a friend suggests that you should be testing your software with every possible input to ensure that the code works.  Why is this impossible?  How should you strategize your unit tests instead?
  - What is more important, testing to show that our software works or testing to **identify** errors/bugs in the software?
  
tags:
  - testing
  - functions
  - conditionals
  
---

