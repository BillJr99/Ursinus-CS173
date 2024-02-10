---
layout: activity
permalink: /Activities/Sorting2
title: "CS173: Intro to Computer Science - Sorting Algorithms"


info:  
  prev: ./Sorting
  
  goals: 
    - To be able to sort a list using additional iterative sorting algorithms (<code>Bubble Sort</code> and <code>Selection Sort</code>)

  models:      
    - model: |
        The benefits of a Binary Search algorithm required that we use a sorted list.  Given an unsorted array, we can sort it with an algorithm.
        <br><br>
        Selection Sort is similar to Insertion Sort, except that it searches the array for the smallest item, and inserts it on the left position.  It continues doing this, except that in step 2, it searches for the smallest item in the sub-array that starts at index <code>1</code> (instead of <code>0</code>, since that was the smallest element from the last step, and now we’re looking for the "second smallest element").  It continues to insert the "next smallest element" into the left position of the array, to the right of the ones it has inserted before.  So, the "second smallest" element goes in the "second position" from the left, and the "third smallest element" goes in the "third position from the left," and so on.  It "Selects" the smallest element that has yet to be sorted, and places it into the proper position.
        <br>
        <a title="Joestape89 / CC BY-SA (http://creativecommons.org/licenses/by-sa/3.0/)" href="https://commons.wikimedia.org/wiki/File:Selection-Sort-Animation.gif"><img width="64" alt="Selection-Sort-Animation" src="https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif"></a>
      title: <code>Selection Sort</code>
      questions: 
        - After each iteration of <a href=https://www.geeksforgeeks.org/selection-sort/>Selection Sort</a>, how many elements are in sorted order, and where are they located?
        - After each iteration, how many elements are still unsorted, and where are they located?
        - What is the pseudocode to find the smallest element in an array?
        - Modify this &quot;smallest element finder&quot; pseudocode into a function that finds the smallest element in an array, but with a parameter to indicate what positions to start and stop searching (<i>i.e.</i>, the starting and stopping indices).
        - What is the pseudocode to swap two elements in an array, given their indices?
        - Enter the code for <a href=https://www.geeksforgeeks.org/selection-sort/>Selection Sort</a> into the <a href=https://cscircles.cemc.uwaterloo.ca/java_visualize/#mode=edit>Java Visualizer</a> and execute it step-by-step.
    - model: |
        <a title="Swfung8 / CC BY-SA (https://creativecommons.org/licenses/by-sa/3.0)" href="https://commons.wikimedia.org/wiki/File:Bubble-sort-example-300px.gif"><img width="256" alt="Bubble-sort-example-300px" src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif"></a>
      title: <code>Bubble Sort</code>
      questions: 
        - Describe the execution of <a href=https://www.geeksforgeeks.org/bubble-sort/>Bubble Sort</a> in your own words.
      
tags:
  - searching
  - sorting
  - algorithms
  
---

