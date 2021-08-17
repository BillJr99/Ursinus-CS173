---
layout: activity
permalink: /Activities/Expressions
title: "CS173: Intro to Computer Science - Expressions"
excerpt: "CS173: Intro to Computer Science - Expressions"

info:
  next: ./Expressions2
  
  goals: 
    - To write statements that manipulate values of different numeric types
    - To manipulate variables in a Java program
    - To be able to apply operators appropriate to primitive data type values
    
  models:
    - model: |
        <div style="width: 100%; display: table; border-collapse:separate; border-spacing:5px;">
        <div style="width: 100%; display: table-row; background-color: black; color: white;">
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Operation</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Operator</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Examples</strong>
            </div>            
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:33%; ">
                Addition
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>+</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>int x = 6 + 4;</code>
                <br>
                <code>int y = x + 2;</code>
            </div>            
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:33%; ">
                Subtraction
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>-</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>float z = 3.1 - 5;</code>
            </div>            
        </div> 
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:33%; ">
                Multiplication
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>*</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>double x = 5.2 * 2;</code>
            </div>            
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:33%; ">
                Division
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>/</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>int idiv = 5 / 2; // returns 2</code>
                <br>
                <code>double fdiv = 5 / 2.0; // returns 2.5</code>
                <br>
                <code>double y = x / 2;</code>
            </div>            
        </div>   
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:33%; ">
                Modulus
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>%</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>int remainder = 5 % 2; // returns 1</code>
            </div>            
        </div> 
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:33%; ">
                Compound Increment
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>++</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>x++; // x = x + 1;</code>
            </div>            
        </div>     
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:33%; ">
                Compound Decrement
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>--</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>x--; // x = x - 1;</code>
            </div>            
        </div>            
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:33%; ">
                Compound Addition
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>+=</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>x += 5.5; // x = x + 5.5;</code>
            </div>            
        </div>            
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:33%; ">
                Compound Subtraction
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>-=</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>x -= 2; // x = x - 2;</code>
            </div>            
        </div>  
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:33%; ">
                Compound Multiplication
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>*=</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>x *= 10.1; // x = x * 10.1;</code>
            </div>            
        </div>         
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:33%; ">
                Compound Division
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>/=</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; ">
                <code>x /= y; // x = x / y;</code>
            </div>            
        </div>                 
        </div>    
      title: Manipulating Values with Operators
      questions:
        - "How are the values of <code>idiv</code> (the result of the integer division operation) and <code>fdiv</code> (the result of the floating point division operation) different and why?"
        - What would happen if you attempt to divide by 0?  Feel free to try this in the code window below!
        - Notice the result of dividing <code>x / 2</code> if <code>x</code> is an <code>int</code>?  How about if <code>x</code> is a <code>double</code> or a <code>float</code>?
        - Suppose you had to divide two integers, but you want the result to be stored as a floating point value.  How could you ensure that this happens (there are several possibilities!)?
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
        
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit1-Getting-Started/topic-1-4-assignment.html	
      title: Expressions and Assignments
      
  additional_practice: 
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit1-Getting-Started/topic-1-5-shortcutoperators.html
      title: Compound Assignment Operators
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit1-Getting-Started/Exercises.html
      title: Variables and Assignments
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit1-Getting-Started/topic-1-8-practice-coding.html
      title: Variables and Assignments Practice Coding Problems
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit1-Getting-Started/to
      title: Review of Variables and Assignments
      
  reflective_prompts:
    - "What is the binary representation of the integer value <code>48</code>?"
    - "What is the decimal representation of the binary value <code>01001</code>?"
tags:
  - datatypes
  - expressions
  - math
  
---

