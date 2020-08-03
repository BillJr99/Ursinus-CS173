---
layout: activity
permalink: /Activities/DataTypes
title: "CS173: Intro to Computer Science - Data Types and Escape Characters"
excerpt: "CS173: Intro to Computer Science - Data Types and Escape Characters"

info:
  goals: 
    - To identify the major components of a Java program, including a method and a class
    - To explain that binary data uses &quot;bits&quot; of <code>1&apos;s</code> and <code>0&apos;s</code> to represent data of various types, both numeric and textual
    - To identify primitive data structures and their uses
    - To identify the use of escape characters
    - To specify the manner in which escape characters are invoked
    - To apply escape characters where needed    
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
        <div style="width: 100%; display: table; border-collapse:separate; border-spacing:5px;">
        <div style="width: 100%; display: table-row; background-color: black; color: white;">
            <div style="display: table-cell; padding:5px; width:50%; background-color: black; color: white;">
                <strong>Escape Character</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:50%; background-color: black; color: white;">
                <strong>Use</strong>
            </div>
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:50%; ">
                <code>\'</code>
            </div>
            <div style="display: table-cell; padding:5px; width:50%; ">
                Single Quote
            </div>
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:50%; ">
                <code>\"</code>
            </div>
            <div style="display: table-cell; padding:5px; width:50%; ">
                Double Quote
            </div>
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:50%; ">
                <code>\n</code>
            </div>
            <div style="display: table-cell; padding:5px; width:50%; ">
                New Line
            </div>
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:50%; ">
                <code>\t</code>
            </div>
            <div style="display: table-cell; padding:5px; width:50%; ">
                Tab
            </div>
        </div>
        </div>
      questions: 
        - What happens if you print an escape character?  Does the backslash actually print?
        - Why do you think we call these &quot;escape characters?&quot;
        - What escape character do you think prints a backslash to the screen?
        - How would you print the actual characters <code>\n</code> to the screen (i.e., not a newline character, but the actual backslash and n characters)? 
    - model: |
        <div style="width: 100%; display: table; border-collapse:separate; border-spacing:5px;">
        <div style="width: 100%; display: table-row; background-color: black; color: white;">
            <div style="display: table-cell; padding:5px; width:25%; background-color: black; color: white;">
                <strong>Type Name</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; background-color: black; color: white;">
                <strong>Number of Bits</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; background-color: black; color: white;">
                <strong>Number of Values</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; background-color: black; color: white;">
                <strong>Range</strong>
            </div>            
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:25%; ">
                <code>boolean</code>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                1 bit
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                2
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                <code>0</code> or <code>1</code>
            </div>            
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:25%; ">
                <code>int</code>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                32 bits = 4 bytes
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                <span>\(2^{32}\)</span>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                <code>-2,147,483,648</code> through <code>2,147,483,647</code>
            </div>            
        </div> 
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:25%; ">
                <code>unsigned int</code>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                32 bits = 4 bytes
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                <span>\(2^{32}\)</span>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                <code>0</code> through <code>4,294,967,295</code>
            </div>            
        </div> 
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:25%; ">
                <code>double</code>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                64 bits = 8 bytes
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                <span>\(2^{64}\)</span>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                Approximately <code>-1.797 \times 10^{308}</code> through <code>1.797 \times 10^{308}</code>, with approximately 15 significant digits of precision
            </div>            
        </div>         
        </div>    
      title: Data Types Have Ranges Because They Are Discrete
      questions:
        - The largest value a boolean can store is 1, even though it is a single bit value that can hold two discrete values.  This is because a bit is needed to store the value 0.  So a boolean’s largest value is not 2^1, but actually 2^1 - 1.  What is the largest int value that a computer can store?
        - Why can the int data type store more negative values than positive values?
        - Suppose you required more precision than the 15 significant digits offered by the double type.  What would happen to the range if a double could provide more precision, and why?     
    - model: |
        <div style="width: 100%; display: table; border-collapse:separate; border-spacing:5px;">
        <div style="width: 100%; display: table-row; background-color: black; color: white;">
            <div style="display: table-cell; padding:5px; width:25%; background-color: black; color: white;">
                <strong>Type Name</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; background-color: black; color: white;">
                <strong>Number of Bits</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; background-color: black; color: white;">
                <strong>Number of Values</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; background-color: black; color: white;">
                <strong>Range</strong>
            </div>            
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:25%; ">
                <code>int</code>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                32 bits = 4 bytes
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                <span>\(2^{32}\)</span>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                <code>-2,147,483,648</code> through <code>2,147,483,647</code>
            </div>            
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:25%; ">
                <code>long</code>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                64 bits = 8 bytes
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                <strong>???</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                <strong>???</strong>
            </div>            
        </div>      
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:25%; ">
                <code>float</code>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                32 bits = 4 bytes
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                <strong>???</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                Approximately <code>-3.402 \times 10^{38}</code> through <code>3.402 \times 10^{38}</code>, with approximately 6 significant digits of precision
            </div>            
        </div>     
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:25%; ">
                <code>double</code>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                64 bits = 8 bytes
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                <span>\(2^{64}\)</span>
            </div>
            <div style="display: table-cell; padding:5px; width:25%; ">
                Approximately <code>-1.797 \times 10^{308}</code> through <code>1.797 \times 10^{308}</code>, with approximately 15 significant digits of precision
            </div>            
        </div>          
        </div>
      title: Larger Data Types Can Store More Values (Larger Values and More Precise Values)
      questions:
        - Fill in the blanks in the table above.            
  reflective_prompts: 
    - What other kinds of data could you imagine a computer representing?

tags:
  - datatypes
  
---

