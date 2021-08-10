---
layout: activity
permalink: /Activities/Recursion2
title: "CS173: Intro to Computer Science - Recursion"
excerpt: "CS173: Intro to Computer Science - Recursion"

info:
  prev: ./Recursion
  
  goals: 
    - To be able to apply recursion to the search problem
  
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/topic-10-2-recursive-search-sort.html 
      title: Recursive Searching and Sorting       
      
  models: 
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
  
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/rMedMC.html
      title: Medium Difficulty Questions about Recursion
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit10-Recursion/rHardMC.html 
      title: More Challenging Questions about Recursion

tags:
  - recursion
  
---

