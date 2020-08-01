---
layout: activity
permalink: /Activities/DataTypes
title: "CS173: Intro to Computer Science - Data Types"
excerpt: "CS173: Intro to Computer Science - Data Types"

info:
  goals: 
    - To explain that binary data uses \"bits\" of `1\'s` and `0\'s` to represent data of various types, both numeric and textual
    - To identify primitive data structures and their uses
  models:
    - title: Primitive Data Types
      model: |
        <div style="width: 100%; display: table; border-collapse:separate; border-spacing:5px;">
        <div style="width: 100%; display: table-row;">
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
                `int`
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                Whole number numeric values
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                `int participants = 40;`
            </div>
        </div>    
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                `double`
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                Fractional or decimal numeric values (these are called "floating point" values)
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                `double price = 5.95;`
            </div>
        </div>        
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                `boolean`
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                True/False
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                `boolean raining = false;`
            </div>
        </div>  
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                `char`
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                A single character
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                `char grade = \'A\';`
            </div>
        </div>     
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                `String`
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                Textual data
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                `String name = \"Lee\";`
            </div>
        </div>       
        </div>
    questions:
      - What is the data type of the value `\"Hello World!\"`?
      - How might a computer represent a whole number using only 1 and 0 digits?  How do you use the decimal digits 0 through 9 to represent all whole numbers?
      - How might a computer represent a True/False boolean?
      - How might a computer represent the letter `\'A\'` or the word `\"Hi!\"`?
    
  reflective_prompt: What other kinds of data could you imagine a computer representing?

tags:
  - datatypes
  
---

