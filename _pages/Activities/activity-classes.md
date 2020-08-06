---
layout: activity
permalink: /Activities/Classes
title: "CS173: Intro to Computer Science - Classes"
excerpt: "CS173: Intro to Computer Science - Classes"

info:
  goals: 
    - To be able to explain that classes provide methods and variables that represent complex nouns or ideas as a collection of data and functionality.
    - To be able to differentiate between a class and an object of that type.
    - To be able to utilize wrapper classes (<code>Integer</code>, <code>Double</code>) to enable functionality upon the primitive types.
    - To be able to invoke constructors using the <code>new</code> keyword.
    - To be able to create constructors of various parameterizations.
    - To be able to compare two objects by their memory address, and by their underlying data through accessors or through an <code>equals()</code> method.
    - To be able to selectively protect and expose class data with the <code>public</code> and <code>private</code> keywords, and write accessors and mutators to interface with objects of the class.
    - To be able to write classes with an appropriate filename, level of abstraction, and encapsulation.
    
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
      title: Constructors
      questions:
        - What do you like better about this version of the program as opposed to the prior one?
        - What are the values of the underlying object variables (“fields”) title, author, and pages for the Book objects <code>b1</code>, <code>b2</code>, <code>b3</code>, and <code>b4</code>? 
        - What do you think the <code>this</code> keyword means?
        - Why do you think we put underscore characters in the input parameters to the constructor, like <code>_pages</code>?     
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaConstructorExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
    - model: |
        Consider the program in the embedded frame.  We protect class fields through <strong>encapsulation</strong>, which allows us to hide fields from manipulation by other classes or main().  In the prior examples, it is possible to set the number of pages of a book to be a negative value.  Using encapsulation, we can help ensure that fields are set correctly by enforcing preconditions, by marking fields and methods as <code>public</code> or <code>private</code>.
      title: Accessors and Mutators
      questions:
        - What does <code>private</code> mean?  
        - What happens if you try to access the variable directly, like <code>b1.pages = 10</code>?
        - Why do you think we call them accessor/getter and mutator/setter functions?
        - Why not just do things the old way and access the variable directly, rather than using accessors and mutators?
        - What does <code>public</code> and <code>private</code> mean?  
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaAccessorMutatorExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                Integer i1 = new Integer(5);
                Integer i2 = Integer.parseInt(“5”);
                Double d = new Double(3.14);
                Double pi = new Double(Math.PI);

                // compareTo returns 0 if equal, -1 if d is smaller, 1 if d is larger
                int comp = d.compareTo(pi); 
                int comp2 = i1.compareTo(i2);

                boolean equal = (i1 == i2);
            }
        }
        ]]></script>     
      title: Wrapper Classes
      questions:
        - What advantages do wrapper classes for primitive data types provide over simply using the primitives directly?
        - Why is <code>parseInt()</code> called on the class <code>Integer</code>, rather than on an object (like <code>i1</code>)?
        - We call the <code>parseInt()</code> function a _________ function, because it exists within a class context rather than a specific object instance.
        - What does <code>parseInt()</code> do?
        - What is the value of <code>comp</code> and <code>comp2</code>?  Why?
        - Compare the <code>Double d</code> to the <code>Double pi</code> in the example above.  Why is <code>3.14</code> less than <code>Math.PI</code>?
        - Why is <code>comp2</code> the value <code>0</code>?
        - Why is <code>equal</code> <code>false</code> in this example, when <code>i1</code> and <code>i2</code> have the same value <code>5</code>?
        - The <code>Integer</code> class has a static method <code>intValue()</code>.  How might you use that to compare the underlying field values of the Integer objects <code>i1</code> and <code>i2</code> in order to correct the line boolean <code>equal = (i1 == i2);</code>?    
        - Implement a method <code>boolean equals(Book _book)</code> that returns <code>true</code> if the title and author of <code>_book</code> is the same as the title and author of the Book object on which equals is called (in other words, <code>this</code>).
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaAccessorMutatorExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>         
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-1-objects-intro-turtles.html
      title: Objects
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-2-constructors.html
      title: Constructors
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-8-IntegerDouble.html
      title: The Wrapper Classes
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-7-comparing-objects.html 
      title: Comparing Objects
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/topic-5-1-parts-of-class.html
      title: Writing Classes
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/topic-5-2-writing-constructors.html 
      title: Writing Constructors
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/topic-5-4-accessor-methods.html
      title: Accessors
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/topic-5-5-mutator-methods.html
      title: Mutators
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/topic-5-6-writing-methods.html
      title: Methods
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/topic-5-8-scope-access.html 
      title: Scoping and Access
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/topic-5-7-static-vars-methods.html 
      title: The <code>static</code> Keyword    
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/Exercises.html
      title: Classes
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/Exercises.html
      title: Objects
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/FRQstepTracker.html
      title: Step Tracker Exercise
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/timeFRQ.html
      title: Time Class
  reflective_prompts:
    - How do you think encapsulation helps make things easier for other programmers to use our code?

tags:
  - classes
  
---

