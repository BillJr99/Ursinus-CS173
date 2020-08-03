---
layout: activity
permalink: /Activities/Boolean
title: "CS173: Intro to Computer Science - Boolean Expressions"
excerpt: "CS173: Intro to Computer Science - Boolean Expressions"

info:
  goals: 
    - To be able to write a boolean expression using variables of various types
  models:
    - model: |
        <div style="width: 100%; display: table; border-collapse:separate; border-spacing:5px;">
        <div style="width: 100%; display: table-row; background-color: black; color: white;">
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Type</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Purpose</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Example</strong>
            </div>
        </div>
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>&&</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                AND two booleans (compute true if both are true)
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>boolean b = false;</code>
                <br>
                <code>boolean x = true && b; // false</code>
            </div>
        </div>
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>||</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                OR two booleans (compute true if at least one is true)
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>boolean x = (true || false); // true</code>
            </div>
        </div>  
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>!</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                NEGATE a boolean
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>boolean x = !(true || false); // = !(true) = false</code>
            </div>
        </div>   
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>==</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                Check if two values are equal
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>boolean x = (10 == 5); // false</code>
            </div>
        </div>  
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>!=</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                Check if two values are not equal.  This is the same as <code>!(x == y)</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>boolean x = (10 != 5); // true</code>
            </div>
        </div>          
        </div>
      title: Writing and Invoking Functions to Re-Use Code Logic
      questions:
        - What is the result of <code>(a || b) && (c || d)</code> if <code>a = true</code>, <code>b = true</code>, <code>c = false</code>, <code>d = false</code>?
        - "<a href=\"https://en.wikipedia.org/wiki/De_Morgan%27s_laws\">DeMorgan’s Law</a> allows you to simplify a boolean expression by &quot;factoring out&quot; a negation, and flipping an AND to an OR (and vice-versa).  For example, <code>(!a && !b)</code> is equivalent to <code>!(a || b)</code>. The reverse procedure also works - negating the outside, negating each term on the inside, and flipping the operator: <code>!(a || b)</code> is equivalent to <code>(!a && !b)</code>.  Re-write <code>!(a && !b)</code> using DeMorgan’s Law."

tags:
  - boolean
  - expressions
  
---

