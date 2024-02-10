---
layout: activity
permalink: /Activities/Random
title: "CS173: Intro to Computer Science - Functions to Generate Random Numbers"


info:
  prev: ./Functions2
  
  goals: 
    - To be able to utilize the methods Math class in code
  models:
    - model: |
        <iframe src="https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html#random--" width="100%" height="480"></iframe>
      title: Generating pseudorandom numbers using <code>Math.random()</code>
      questions:
        - The <code>Math.random()</code> function takes no parameters, but returns a random number greater than or equal to <code>0</code>, and less than (but not equal to) <code>1</code>.  How can you use this to generate a random value between <code>0</code> and <code>10</code>?
        - Now, suppose you wish to generate a whole number <code>int</code> between <code>0</code> and <code>10</code>?  The <code>Math.round()</code> function rounds a <code>double</code> to the nearest <code>int</code> and returns it.  Convert your randomly generated value to an <code>int</code>.
        - "Alternatively, you can &quot;cast&quot; the <code>double</code> to an <code>int</code>, which converts the value by truncating the numbers after the decimal point (thus always rounding down).  For example: <code>int x = (int) 5.6; // x is now 5</code>. Try this instead with your randomly generated value to convert it from a <code>double</code> to an <code>int</code>."
        - You can use the <code>Math.max()</code> function, which accepts two numeric parameters and returns the largest of the two.  Using <code>Math.max()</code>, take your randomly generated <code>int</code>, and replace it with the value <code>1</code> if <code>1</code> is larger than your random number (if your random number is larger, choose that instead).
        - Write a function that generates a random number between <code>1</code> and <code>10</code> using the code you generated in the above questions.     
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>         

  reflective_prompts:
    - How do you think a computer might generate a random number?  Why do you think we call them pseudorandom numbers?
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-9-Math.html
      title: Using the <code>Math</code> Class
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit5-Writing-Classes/APLine.html
      title: Using Class Functions  
tags:
  - functions
  - expressions
  
---

