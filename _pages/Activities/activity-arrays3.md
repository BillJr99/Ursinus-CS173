---
layout: activity
permalink: /Activities/Arrays3
title: "CS173: Intro to Computer Science - Arrays"
excerpt: "CS173: Intro to Computer Science - Arrays"

info:
  next: ./Arrays4
  prev: ./Arrays2

  goals: 
    - To be able to create, access, and iterate a 2D array

  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
           public static void main(String[] args) {
              int[][] mat1 = new int[10][10];
              int[][] mat2 = { { 1, 0 }, { 0, 1 } };
              
              // This is the length of the "outer vector" - the number of rows
              for(int i = 0; i < mat2.length; i++) {
                // This is the length of the "inner vector" - the number of columns
                for(int j = 0; j < mat2[i].length; j++) {
                    System.out.println(mat2[i][j]);
                }
              }
           }
        }
        ]]></script>         
        <br>
        <img src="../images/examples/java-visualizer-2darray.png" alt="Java Visualizer Example of a 2D Array" />
        <br>
        <img src="../images/examples/java-visualizer-2darrayidentity.png" alt="Java Visualizer Example of a 2D Array" />
      title: 2D Arrays and Traversals
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>  
      questions:
        - How would you describe a 2D array in terms of usual 1D arrays?
        - Does the first index indicate the row or the column of the 2D array?
        - How might you create a 3-dimensional array?
        - Run this code in the <a href=https://cscircles.cemc.uwaterloo.ca/java_visualize/#mode=edit>Java Visualizer</a>.  What is the output?
        - Re-draw the arrays <code>mat1</code> and <code>mat2</code> as a square grid. 
        - Is it possible to re-size these arrays if you need to add additional elements later?  If so, how, and if not, why not?
        - "Develop pseudocode to determine whether a 2D array is a &quot;magic array&quot;, in which the sum of each column and row of a square array is the same value.  A sample 3x3 magic array is: <code>[ 4, 9, 2, 3, 5, 7, 8, 1, 6 ]</code>."
        
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit8-2DArray/topic-8-1-2D-arrays.html
      title: 2D Arrays
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit8-2DArray/topic-8-2-2D-array-loops.html
      title: Loops with 2D Arrays
         
  reflective_prompts:
    - How would you modify the above program to assign values to <code>mat1</code>, and then to multiply the two matrices together?  To multiply matrices, each cell of the result is equal to the products of each element of the corresponding column of <code>mat1</code> with each element of the corresponding row of <code>mat2</code>, added together.  A triply-nested loop with a sum is required.
    
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit8-2DArray/Array2dCodePractice.html
      title: 2D Arrays  
      
tags:
  - arrays
  - iteration
  
---

