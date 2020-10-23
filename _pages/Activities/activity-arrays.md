---
layout: activity
permalink: /Activities/Arrays
title: "CS173: Intro to Computer Science - Arrays"
excerpt: "CS173: Intro to Computer Science - Arrays"

info:
  next: ./Arrays2
  
  goals: 
    - To be able to explain that an array is an ordered collection of data
    - To be able to create an array and assign its elements
    - To be able to access an element from an array by its index

  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                int[] grades = new int[3];
                
                for(int i = 0; i < grades.length; i++) {
                    grades[i] = 90 + i;
                    System.out.println(grades[i]);
                }
            }
        }
        ]]></script>         
        <br>
        <img src="../images/examples/java-visualizer-array-int.png" alt="Java Visualizer Example of an Array" />
      title: Creating and Accessing Arrays
      questions:
        - What is the size of the <code>grades</code> array?
        - What are the indices of the <code>grades</code> array?
        - Why does the array use <code>.length</code>, when a String uses <code>.length()</code>, to report its size?
        
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/topic-6-1-array-basics.html
      title: Array Basics
          
tags:
  - arrays
  - classes  
---

