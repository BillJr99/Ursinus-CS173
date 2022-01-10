---
layout: activity
permalink: /Activities/Classes
title: "CS173: Intro to Computer Science - Classes"
excerpt: "CS173: Intro to Computer Science - Classes"

info:
  next: ./Classes2
  
  goals: 
    - To be able to explain that classes provide methods and variables that represent complex nouns or ideas as a collection of data and functionality.
    - To be able to differentiate between a class and an object of that type.
    - To be able to invoke constructors using the <code>new</code> keyword.
    
  models:
    - model: |
       <img src="../images/examples/java-visualizer-book-classes.png" alt="Java Visualizer Class Overview of a Book Class"><br><small>Java Visualizer: <a href=https://cscircles.cemc.uwaterloo.ca/java_visualize>https://cscircles.cemc.uwaterloo.ca/java_visualize</a></small>
      title: Objects and Classes
      questions:
        - Consider the code example in the embedded frame, and the visualization of the class structures in the model.  What do you notice about the name of the class and the file in which it is saved?
        - What data does a <code>Book</code> contain?
        - How is each <code>Book</code> instantiated in <code>main()</code>?
        - Other editions of The Great Gatsby were released with 180 pages.  What would you change in the code to reflect this?
        - What would you write to print the author and title of each of these books? 
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaClassExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>   
    - model: Consider the program in the embedded frame.
      title: Static Methods
      questions:
        - What does the <code>static</code> keyword mean?
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaMovieClassExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
    - model: Consider the program in the embedded frame.
      title: Constructors
      questions:
        - What do you like better about this version of the program as opposed to the prior one?
        - What are the values of the underlying object variables (“fields”) title, author, and pages for the Book objects <code>b1</code>, <code>b2</code>, <code>b3</code>, and <code>b4</code>? 
        - What happens if you set <code>b3 = b2</code> and then manipulate the fields of <code>b2</code> or <code>b3</code>?
        - What do you think the <code>this</code> keyword means?
        - Why do you think we put underscore characters in the input parameters to the constructor, like <code>_pages</code>?     
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaConstructorExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
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
      title: Creating and Accessing Arrays of Objects
      questions:
        - What is the size of the <code>books</code> array?
        - What are the indices of the <code>books</code> array?
        - Why does the array use <code>.length</code>, when a String uses <code>.length()</code>, to report its size?
        - What is the advantage of allocating an array in a loop, when the book titles may need to be set individually?
        
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-1-objects-intro-turtles.html
      title: Objects   
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/Exercises.html
      title: Classes
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/Exercises.html
      title: Objects

tags:
  - classes
  
---

