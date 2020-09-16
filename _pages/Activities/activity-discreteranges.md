---
layout: activity
permalink: /Activities/DiscreteRanges
title: "CS173: Intro to Computer Science - Discrete Data Ranges"
excerpt: "CS173: Intro to Computer Science - Discrete Data Ranges"

info:
  goals: 
    - To explain that data types are discrete because they are represented by a finite number of computing bits
    - To explain that all data are represented computationally via binary values
    - To explain the relationship between a data type's bit size and its range
    - To explain why typed values take on discrete ranged values that can differ from data type to data type
  models:
    - model: |
        <div style="width: 100%; display: table; border-collapse:separate; border-spacing:5px;">
        <div style="width: 100%; display: table-row; background-color: black; color: white;">
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Type Name</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Number of Bits</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Number of Values that Can Be Stored</strong>
            </div>
        </div>
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>boolean</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                1 bit
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                2
            </div>
        </div>    
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>int</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                32 bits = 4 bytes
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <span>\(2^{32}\) = approximately 4 billion values</span>
                <br>
                Each additional bit doubles the number of values that can be stored: all the possible values with a <code>1</code> appended before them, plus all the possible values with a <code>0</code> appended before them!
            </div>
        </div>        
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>double</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                64 bits = 8 bytes
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <span>\(2^{64}\)</span> = approximately <span>\(18 \times 10^{18}\)</span> values</span>
            </div>
        </div>  
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>char</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                8 bits = 1 byte
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <span>\(2^{8}\)</span> = approximately 256 values
            </div>
        </div>     
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>String</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                1 byte per character (plus one additional byte at the end which contains the value <code>0</code>)
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                Each string is stored in memory with enough space to store all the characters plus the extra byte at the end.  In a way, a string holds only one value, made up of its characters.  We call strings <strong>immutable</strong> because we must create a new string to hold new textual data, rather than simply edit the original string variable.
            </div>
        </div>       
        </div>    
      title: Data Types are Discrete
      questions:
        - Why can’t a computer store data with an infinite number of possible values?
        - A boolean can hold only two values, because its single bit is either a 1 or a 0.  To what do these values correspond?
        - The <code>float</code> data type is a smaller version of the <code>double</code>; how many bits do you think a <code>float</code> uses?
        - Similarly, there is a larger version of the <code>int</code> data type called the <code>long</code>.  How many bits do you think this type uses, and how many values can it contain?
        - Which of the data types above has a variable rather than fixed length?  With this in mind, what do you think is the purpose of storing the extra <code>0</code> at the end of values of that type?  
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
        <!--
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
        -->
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
                Approximately <span>\(-1.797 \times 10^{308}\)</span> through <span>\(1.797 \times 10^{308}\)</span>, with approximately 15 significant digits of precision
            </div>            
        </div>         
        </div>    
      title: Data Types Have Ranges Because They Are Discrete
      questions:
        - The largest value a boolean can store is <code>1</code>, even though it is a single bit value that can hold two discrete values.  This is because a bit is needed to store the value <code>0</code>.  So a boolean’s largest value is not <span>\(2^{1}\)</span>, but actually <span>\(2^{1} - 1\)</span>.  What is the largest int value that a computer can store?
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
                Approximately <span>\(-3.402 \times 10^{38}\)</span> through <span>\(3.402 \times 10^{38}\)</span>, with approximately 6 significant digits of precision
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
                Approximately <span>\(-1.797 \times 10^{308}\)</span> through <span>\(1.797 \times 10^{308}\)</span>, with approximately 15 significant digits of precision
            </div>            
        </div>          
        </div>
      title: Larger Data Types Can Store More Values (Larger Values and More Precise Values)
      questions:
        - Fill in the blanks in the table above.              
        
  reflective_prompts: 
    - Numeric data types must hold not only positive values but also negative values.  What does this do to the number of positive values that can be represented by each type?  What are their ranges?

tags:
  - datatypes
  - expressions
  - math
  
---

