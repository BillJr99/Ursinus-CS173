---
layout: activity
permalink: /Activities/Sorting
title: "CS173: Intro to Computer Science - Search Algorithms"
excerpt: "CS173: Intro to Computer Science - Search Algorithms"

info:  
  next: ./Sorting2
  
  goals: 
    - To be able to sort a list using an iterative sorting algorithms (<code>Insertion Sort</code>)

  additional_reading:
    - link: ../Modules/Sorting/Modules/Sorting
      title: Sorting Module
    - title: "Interactive Demo of Insertion Sort"
      link: "https://mhyfritz.com/blog/2014/09/22/interactive-insertion-sort/"    
    - title: "Search Algorithms"
      link: "https://csawesome.runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-5-searching.html"  
    - title: "Sorting Algorithms"
      link: "https://csawesome.runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-6-sorting.html"       

  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        /* PSEUDOCODE */
        InsertionSort(int[] A) {
            // Take each element of the array, from left to right
            for(int i = 1; i < A.length; i++) {
                int val = A[i];

                //… and put it into place in sorted order on the left side
                for(int j = i - 1; j >= 0; j--) {
                    if(A[j] > val) {    // "duck-duck-goose" 
                        A[j+1] = A[j];  // if this isn’t the position,
                    }                   // slide the element that’s there 
                }                       // right to make room for it
         
               // The position has been found, either at the beginning 
               // of the list, or in the right place; insert it into
               // the space we’ve been sliding to make room for!
               A[j+1] = val;
            }
        }        
        ]]></script>
        <br>
        <a title="Swfung8 / CC BY-SA (https://creativecommons.org/licenses/by-sa/3.0)" href="https://commons.wikimedia.org/wiki/File:Insertion-sort-example-300px.gif"><img width="256" alt="Insertion-sort-example-300px" src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif"></a>
        <br>
        Consider the array defined in <a href="https://www.geeksforgeeks.org/insertion-sort/">this example</a>: [ 4, 3, 2, 10, 12, 1, 5, 6 ]
      title: <code>Insertion Sort</code>
      questions: 
        - Notice that the pseudocode for InsertionSort begins with <code>i = 1</code>, not <code>0</code>.  Why might this be?
        - After each iteration of the loop, how many elements of <code>A</code> are in sorted order?  Where are these elements located?
        - How many are not yet in sorted order, and where are these located?
        - If the inner <code>j</code> for loop goes all the way to index <code>0</code> without finding the key, what do we know about the value we’re inserting in this step?
        - What is the purpose of the line <code>A[j+1] = A[j]</code> inside the inner for loop?
        - Describe the execution of this algorithm in your own words.
        - Enter the code for <a href=https://www.geeksforgeeks.org/insertion-sort/>Insertion Sort</a> into the <a href=https://cscircles.cemc.uwaterloo.ca/java_visualize/#mode=edit>Java Visualizer</a> and execute it step-by-step.  
        - How many steps are required to execute this code on an array of size <code>10</code>?  In other words, how many times is the code inside the inner loop executed?  How does this count relate to the size of the array? 
        - Let's act it out!
        
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/ssEasyMC.html
      title: Iterative Sort (Insertion Sort) Questions
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/ssHardMC.html
      title: Medium Difficulty Questions about Iterative Sort
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/ssMedMC.html
      title: More Challenging Questions about Iterative Sort
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-6-sorting.html
      title: Sorting Algorithms
      
tags:
  - searching
  - sorting
  - algorithms
  
---

