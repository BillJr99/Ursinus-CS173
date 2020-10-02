---
layout: activity
permalink: /Activities/Functions2
title: "CS173: Intro to Computer Science - Functions"
excerpt: "CS173: Intro to Computer Science - Functions"

info:
  next: ./Random
  prev: ./Functions
  
  goals: 
    - To be able to call methods in various configurations (parameters, return values)
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            /* Given an integer value, multiply it by two and return that value
             * @param value: the value to multiply by two
             *        Precondition: an integer
             * @return the number that is twice the value of the input variable
             */
            public static int twice(int value) {
                int result = 2 * value;
                
                return result;
            }
            
            public static int thrice(int value) {
                int result = 3 * value;
                
                return result;
            }
            
            public static void main(String[] args) {
                int twoTimesSix = twice(6);
                int threeTimesFive = thrice(5);
                
                System.out.println("2 times 6 = " + twoTimesSix);
                System.out.println("3 times 5 = " + threeTimesFive);
            }
        }
        ]]></script>     
      title: Parameter Binding and Scope
      questions:
        - "Are the <code>value</code> variables in the <code>twice</code> and <code>thrice</code> functions the same variable, or different variables?  How about <code>result</code>?"
        - "How would you change the name of <code>value</code> to <code>inputValue</code>?"
        - "In this program, what value are we passing to the <code>twice</code> function?"

tags:
  - functions
  - expressions
  
---

