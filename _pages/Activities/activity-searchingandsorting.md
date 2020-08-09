---
layout: activity
permalink: /Activities/SearchingAndSorting
title: "CS173: Intro to Computer Science - Searching and Sorting"
excerpt: "CS173: Intro to Computer Science - Searching and Sorting"

info:
  goals: 
    - To be able to search a list for a desired item.
    - To be able to sort a list using the iterative sorting algorithms <code>Bubble Sort</code>, <code>Insertion Sort</code>, and <code>Selection Sort</code>
    - To be able to apply recursion to the search problem.

  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-5-searching.html 
      title: Searching
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-6-sorting.html 
      title: Sorting
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/topic-10-1-recursion.html
      title: Recursion
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/topic-10-2-recursive-search-sort.html 
      title: Recursive Searching and Sorting   

  models:
    - model: |
        <div style="width: 100%; display: table; border-collapse:separate; border-spacing:5px;">
        <div style="width: 100%; display: table-row; background-color: black; color: white;">
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>6</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>7</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>10</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>3</strong>
            </div>            
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>4</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>2</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>1</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>8</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>5</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>9</strong>
            </div>            
        </div>    
        </div>
        <br>
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
           public static void main(String[] args) {
                int[] A = { 6, 7, 10, 3, 4, 2, 1, 8, 5, 9 };
           }
        }
        ]]></script>        
      title: Searching
      questions:
        - What steps are required to find the index of an item in the array (say, the number <code>2</code>)?
        - Write Java-like pseudocode to implement a function to locate a value <code>k</code> in an array <code>A</code>.
        - How many iterations are required through the loop to find item <code>6</code>?  How about item <code>9</code>?
        - How many iterations are required through the loop to find the last item in a list of size <code>N</code>?
    - model: |
        <div style="width: 100%; display: table; border-collapse:separate; border-spacing:5px;">
        <div style="width: 100%; display: table-row; background-color: black; color: white;">
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>1</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>2</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>3</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>4</strong>
            </div>            
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>5</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>6</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>7</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>8</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>9</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:10%; background-color: black; color: white;">
                <strong>10</strong>
            </div>            
        </div>    
        </div>
        <br>
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
           public static void main(String[] args) {
                int[] A = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
           }
        }
        ]]></script>        
      title: Searching with Recursion
      questions:
        - Suppose you are playing the &quot;high-low&quot; game, in which you have to guess a number, and are told that the correct value is higher or lower than your guess.  What would be the best first guess, if you knew the value was between <code>1</code> and <code>10</code>?        
        - How do you know that a value will definitely be found in the right half of the array?  How about on the left half of the array?
        - Now, suppose you are playing the same "high-low" game, but instead of knowing the range of values you’re looking for, you know how big the array is that you’re searching.  You are still told whether your value is higher or lower than your guess.  Which element would you pick for your guess?  In mathematics, this element or value is known as the ______ of the list?
        - Try searching for the value <code>8</code>.  Write down which indices of the array you are searching within (initially <code>0</code> through <code>9</code>), and the index of your guess, at each step of the search, until you find the value <code>8</code>.  How many guesses were required?  How many guesses would have been required if the list was not sorted?
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        /* PSEUDOCODE */
        InsertionSort(int[] A) {
            // Take each element of the array, from left to right
            for(int i = 1; i < A.length; i++) {
                   int val = A[i];

                //… and put it into place in sorted order on the left side
                for(int j = i - 1; i >= 0; i--) {
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
        
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/ssEasyMC.html
      title: Iterative Sort (Insertion Sort, Selection Sort) Questions
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/ssHardMC.html
      title: Medium Difficulty Questions about Iterative Sort
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/ssMedMC.html
      title: More Challenging Questions about Iterative Sort
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-5-searching.html
      title: Search Algorithms
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-6-sorting.html
      title: Sorting Algorithms
      
tags:
  - searching
  - sorting
  - recursion
  
---

