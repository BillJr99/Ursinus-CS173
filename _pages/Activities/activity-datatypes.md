---
layout: activity
permalink: /Activities/DataTypes
title: "CS173: Intro to Computer Science - Overview of a Computer Program and Data Types"


info:
  goals: 
    - To identify the major components of a Java program, including a method and a class
    - To explain that binary data uses &quot;bits&quot; of <code>1&apos;s</code> and <code>0&apos;s</code> to represent data of various types, both numeric and textual
    - To identify primitive data structures and their uses
    - To be able to create and compile a Java source file in a chosen development environment
  models:
    - title: "Hello World"
      model: |
        <img src="../images/examples/helloworld_annotated.png" alt="Annotated Hello World Java program example">
      questions: 
        - What do you think the curly braces represent and enclose?
    - title: "Your First Program"
      model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                // println prints a "line" to the string
                System.out.println("Hello World!");
                System.out.println("Have a great day.");
            }
        }
        ]]></script> 
      questions: 
        - What do you think the <code>//</code> characters represent?
    - title: Primitive Data Types
      model: |
        <a title="Hellbus / Public domain" href="https://commons.wikimedia.org/wiki/File:Odometer_rollover.jpg"><img width="512" alt="Odometer rollover" src="https://upload.wikimedia.org/wikipedia/commons/5/53/Odometer_rollover.jpg"></a>
        <br>      
        <div style="width: 100%; display: table; border-collapse:separate; border-spacing:5px;">
        <div style="width: 100%; display: table-row; background-color: black; color: white;">
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Type Name</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Use</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Example</strong>
            </div>
        </div>
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>int</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                Whole number numeric values
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>int participants = 40;</code>
            </div>
        </div>    
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>double</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                Fractional or decimal numeric values (these are called "floating point" values)
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>double price = 5.95;</code>
            </div>
        </div>        
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>boolean</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                True/False
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>boolean raining = false;</code>
            </div>
        </div>  
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>char</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                A single character
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>char grade = &apos;A&apos;;</code>
            </div>
        </div>     
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>String</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                Textual data
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>String name = &quot;Lee&quot;;</code>
            </div>
        </div>       
        </div>
      questions:
        - What is the data type of the value <code>&quot;Hello World!&quot;</code>?
        - Observe the odometer above.  What is the place value of each of the digits in a decimal system?  How would this odometer count if the only digits it could display were 1 and 0?  What would each place value be then?
        - How might a computer represent a whole number using only 1 and 0 digits?  How do you use the decimal digits 0 through 9 to represent all whole numbers?        
        - How might a computer represent a whole number using only 1 and 0 digits?  How do you use the decimal digits 0 through 9 to represent all whole numbers?
        - How might a computer represent a True/False boolean?
        - How might a computer represent the letter <code>&apos;A&apos;</code> or the word <code>&quot;Hi!&quot;</code>?
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
        
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit1-Getting-Started/topic-1-8-practice-coding.html
      title: Mixed-Up Coding Practice

tags:
  - datatypes
  
---

