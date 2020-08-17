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
        - How many calls would you make to `triangleArea` before you decide that it is "passing?"  What paramter inputs would you supply to those calls?
  models:
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
      questions:
        - What makes this a difficult function to test? 
        - What could we do to better facilitate testing a function like this?
        
reflective_prompts:
  - Suppose a friend suggests that you should be testing your software with every possible input to ensure that the code works.  Why is this impossible?  How should you strategize your unit tests instead?
  - What is more important, testing to show that our software works or testing to **identify** errors/bugs in the software?
  
tags:
  - testing
  - functions
  - conditionals
  
---

