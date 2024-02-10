---
layout: activity
permalink: /Activities/Searching2
title: "CS173: Intro to Computer Science - Search Algorithms"


info:
  prev: ./Searching
  
  goals: 
    - To be able to search a list for a desired item.

  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-5-searching.html 
      title: Searching

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
        <br>
        <img src="../files/manim/output/ArraySearch.gif" alt="Searching an array">
      title: Searching
      questions:
        - What steps are required to find the index of an item in the array (say, the number <code>2</code>)?
        - Write Java-like pseudocode to implement a function to locate a value <code>k</code> in an array <code>A</code>.
        - How many iterations are required through the loop to find item <code>6</code>?  How about item <code>9</code>?
        - How many iterations are required through the loop to find the last item in a list of size <code>N</code>?

  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-5-searching.html
      title: Search Algorithms
      
tags:
  - searching
  - algorithms
  
---

