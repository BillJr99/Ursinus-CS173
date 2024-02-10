---
layout: activity
permalink: /Activities/Arrays2
title: "CS173: Intro to Computer Science - Arrays"


info:
  prev: ./Arrays
  next: ./Arrays3
    
  goals: 
    - To be able to iterate over an array

  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
            public static void main(String[] args) {
                int[] arr = new int[10];
                
                int sum = 0;
                int i = 0;
                
                for(i = 0; i < arr.length; i++) {
                    arr[i] = 2 * i;
                }
                
                for(i = 0; i < arr.length; i++) {
                    sum = sum + arr[i];
                }
                
                System.out.println("Sum = " + sum);
            }
        }
        ]]></script>         
        <br>
        <img src="../images/examples/java-visualizer-arrayiterate.png" alt="Java Visualizer Example of an Array" />
      title: Iterating Over Arrays
      questions:
        - "How would you modify the program above to play a game of &quot;Duck-Duck-Goose&quot; -- that is, iterating through the array until a certain value is reached (say, <code>10</code>)?"
        
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/topic-6-2-traversing-arrays.html
      title: Traversing Arrays
    
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/ArrayPractice.html
      title: Array Practice
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/Exercises.html
      title: Questions about Arrays     
      
tags:
  - arrays
  - iteration
  
---

