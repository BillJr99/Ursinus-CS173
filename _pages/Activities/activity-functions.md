---
layout: activity
permalink: /Activities/Functions
title: "CS173: Intro to Computer Science - Functions"
excerpt: "CS173: Intro to Computer Science - Functions"

info:
  goals: 
    - To be able to call methods in various configurations (parameters, return values)
    - To be able to utilize the methods Math class in code
  models:
    - model: |
        <img src="../images/examples/functions_area.png" alt="Functions to Compute the Area of Shapes">
      title: Writing and Invoking Functions to Re-Use Code Logic
      questions:
        - Notice that functions have data types before their function names, just like variables do.  What is the return type of <code>circleArea()</code>?
        - Try running the sample program above in repl.it. 
        - Modify the program to write an additional function circleDiameter() that computes the diameter (<span>\(2 \times \pi \times r\)</span>) given the radius of the circle.  Call that function from main() and print the value.
        - Modify the program to write and call <code>triangleArea()</code> from <code>main()</code> and then print the area of a triangle whose dimensions you choose.
        - The Math class includes several useful math functions that you can call.  For example, <code>Math.pow(a, b)</code> will return the <code>double</code> value computed by <code>a</code> raised to the power of <code>b</code> (both <code>double</code> values).  Re-write <code>circleArea()</code> so that it computes the <code>radius</code> raised to the power of <code>2</code>, rather than multiplying it by itself.
        - The Math class also provides constants, so that you do not need to hard-code approximate values like we did with <code>3.14</code> for the value <span>\(\pi\)</span>.  Modify the program to use the constant <code>Math.PI</code> instead of <code>3.14</code>.
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>    
    - model: |
        <img src="../images/examples/functions_void.png" alt="void Function Examples">
      title: The <code>void</code> Keyword
      questions:
        - The <code>+</code> operator works on Strings as well as on numeric values.  &quot;Adding&quot; two strings together concatenates or combines them.  Re-write the <code>sayHello()</code> method so that it executes in just one <code>System.out.println()</code> statement.      
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
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
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit1-Getting-Started/topic-1-6-casting.html 
      title: Type Casting
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-3-methods-no-params.html
      title: Calling Functions with no Parameters
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-4-methods-with-params.html
      title: Calling Functions with Parameters
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-5-methods-return.html
      title: Function Return Values
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-9-Math.html
      title: Using the <code>Math</code> Class
tags:
  - functions
  - expressions
  
---

