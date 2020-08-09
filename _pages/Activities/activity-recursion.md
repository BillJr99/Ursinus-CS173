---
layout: activity
permalink: /Activities/Recursion
title: "CS173: Intro to Computer Science - Recursion and Merge Sort"
excerpt: "CS173: Intro to Computer Science - Recursion and Merge Sort"

info:
  goals: 
    - To apply recursion to the sorting problem using <code>Merge Sort</code> and <code>Quicksort</code>
    - To identify a recursive base case
    - To implement recursive algorithms
  
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-6-sorting.html 
      title: Sorting
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/topic-10-1-recursion.html
      title: Recursion
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/topic-10-2-recursive-search-sort.html 
      title: Recursive Searching and Sorting  
      
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
        Quick Sort views the problem of sorting as a recursive one: sorting a large list is the same as sorting two smaller lists.  The problem gets smaller at each step as long as we learn the correct sorted position of one item at every step (just like with Selection Sort and Insertion Sort).    
        <br>
        <img src="https://www.geeksforgeeks.org/wp-content/uploads/gq/2014/01/QuickSort2.png" alt="Quicksort Diagram from geeksforgeeks">
      title: Efficient Sorting with Recursion - <code>Quicksort</code>
      questions:
        - The array is broken into two sub-problems at each step.  What do you notice about the elements in the left sub-problem and the elements in the right sub-problem?  How are they being &quot;partitioned&quot; into the two sub-arrays?
        - Notice that the problems aren’t always divided exactly into halves.  That’s because the algorithm is &quot;partitioning&quot; the values according to the last value of the array.  What would be the ideal choice of an element to &quot;partition&quot; around (this element is known as the &quot;pivot&quot;)?
        - The &quot;partition&quot; results in two sub-problems, with sub-arrays that include all the elements from the main problem, except for one.  Which element is left out, and why?
        - After each recursive iteration of Quick Sort, how many elements are placed into their correct position?  Where are they located?
        - Enter the code for <a href=https://www.geeksforgeeks.org/quick-sort/>Quick Sort</a> into the <a href=https://cscircles.cemc.uwaterloo.ca/java_visualize/#mode=edit>Java Visualizer</a> and execute it step-by-step.
        
    - model: |
        <a href=https://www.geeksforgeeks.org/merge-sort/>Merge Sort</a> views the problem of sorting as a recursive one: sorting a large list is the same as breaking the list in half, sorting each of those, and then "merging" them together as if they were a deck of cards being shuffled.
      title: Efficient Sorting with Recursion - <code>Merge Sort</code>
      questions:
        - What would the base case of <code>Merge Sort</code> be?  When might you stop splitting the array in half?
        - Given two sorted arrays, how would you go about merging them together?
        - Write the pseudocde for <code>Merge Sort</code> - there are exactly 3 steps (recursively calling the left half, followed by the right half, followed by a call to the merge step completed above).
        - What indices would you provide to sort the left half, right half, and merge steps at each recursive iteration? 
        - Enter the code for <a href=https://www.geeksforgeeks.org/merge-sort/>Merge Sort</a> into the <a href=https://cscircles.cemc.uwaterloo.ca/java_visualize/#mode=edit>Java Visualizer</a> and execute it step-by-step.        
  
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/rEasyMC.html
      title: Questions about Recursion
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/rMedMC.html
      title: Medium Difficulty Questions about Recursion
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/rHardMC.html 
      title: More Challenging Questions about Recursion
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/rBasePractice.html 
      title: Recursive Base Cases
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/recursionCodePractice.html 
      title: Recursion
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/topic-10-2-recursive-search-sort.html
      title:
    - link: Recursive Searching and Sorting https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/topic-10-1-recursion-day1.html#factorial-method
      title: Recursive Factorial Function
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/topic-10-1-recursion-challenge.html
      title: Recursion Tracing
      
  reflective_prompts:
    - How might you improve upon (reduce) the number of calls to <code>fib(2)</code> in the Fibonacci example?

tags:
  - recursion
  - sorting
  
---

