---
layout: activity
permalink: /Activities/DataTypes
title: "CS173: Intro to Computer Science - Data Types"
excerpt: "CS173: Intro to Computer Science - Data Types"

info:
  goals: 
    - To identify the major components of a Java program, including a method and a class
    - To explain that binary data uses &quot;bits&quot; of <code>1&apos;s</code> and <code>0&apos;s</code> to represent data of various types, both numeric and textual
    - To identify primitive data structures and their uses
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
        - How might a computer represent a whole number using only 1 and 0 digits?  How do you use the decimal digits 0 through 9 to represent all whole numbers?
        - How might a computer represent a True/False boolean?
        - How might a computer represent the letter <code>&apos;A&apos;</code> or the word <code>&quot;Hi!&quot;</code>?
    - title: "Special Characters"
      model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                System.out.print("The most damaging phrase in the language is: \"We've always done it this way!\"");
                System.out.println(" -- Grace Hopper");
            }
        }
        ]]></script> 
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
      questions: 
        - The excerpt from the above interview with Admiral Grace Hopper includes a quotation.  How can you print quotation marks to the screen without Java interpreting them as the end of your <code>String</code>?
        - Notice the use of <code>System.out.print</code> and <code>System.out.println</code>.  What's the difference between these two statements?
        - How could you revise the above program to print the entire statement using only one line of code (in other words, only one call to <code>System.out.println</code>?
    - title: "Escape Characters"
      model: |
        <img src="../images/examples/helloworld_annotated.png" alt="Annotated Hello World Java program example">
      questions: 
        - What do you think the curly braces represent and enclose?
  reflective_prompts: 
    - What other kinds of data could you imagine a computer representing?

tags:
  - datatypes
  
---

