---
layout: activity
permalink: /Activities/Arrays
title: "CS173: Intro to Computer Science - Arrays"
excerpt: "CS173: Intro to Computer Science - Arrays"

info:
  next: ./Arrays2
  
  goals: 
    - To be able to explain that an array is an ordered collection of data, whether they be primitives or objects.
    - To be able to create an array and assign its elements
    - To be able to access an element from an array by its index

  models:
    - model: |
        Recall from our earlier examples that we had to create a separate Book object variable for each Book we wanted to create.  We can simplify things by creating a single variable that refers to the whole collection.  This is called an array.  They allow us to leverage loops to quickly iterate over a collection of values or objects.
        <br>
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Book {
            String title;
            String author;
            int pages;
            
            Book(String _title) {
                this.title = _title;
                this.author = "Unknown";
                this.pages = 0;
            }
        }
        
        public class Main {
            public static void main(String[] args) {
                Book[] books = new Book[3];
                
                for(int i = 0; i < books.length; i++) {
                    books[i] = new Book("Book Number " + i);
                    System.out.println(books[i].title);
                }
            }
        }
        ]]></script>         
        <br>
        <img src="../images/examples/java-visualizer-array.png" alt="Java Visualizer Example of an Array" />
      title: Creating and Accessing Arrays
      questions:
        - What is the size of the <code>books</code> array?
        - What are the indices of the <code>books</code> array?
        - Why does the array use <code>.length</code>, when a String uses <code>.length()</code>, to report its size?
        - What is the advantage of allocating an array in a loop, when the book titles may need to be set individually?
        
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/topic-6-1-array-basics.html
      title: Array Basics
          
tags:
  - arrays
  - classes  
---

