---
layout: activity
permalink: /Activities/Conditionals3
title: "CS173: Intro to Computer Science - Conditionals"
excerpt: "CS173: Intro to Computer Science - Conditionals"

info:
  prev: ./Conditionals2
  
  goals: 
    - To be able to write an <code>if</code> statement
    - To be able to write an <code>else</code> statement
    - To design boolean expressions for conditionals
    - To combine the <code>if</code> and <code>else</code> blocks to form conditionals that utilize the <code>else if</code> construct
    - To implement complex conditional statements using boolean expression operators
    
  warmup: "How might you improve this <code>if</code> statement: <code>if(grade == 89.5) { ... }</code>?<br>How would you fix this one: <code>if(grade > 79.5 && < 90) { ... }</code>"  
  
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Driver {
            public static void main(String[] args) {
                boolean taxable = true;
                double tax = 0.06; // 6% tax rate
                double price = 9.99;

                // This code does not work!
                if(taxable) {
                  double total = price + price * tax;
                } else {
                  double total = price;
                }

                System.out.println("The total is: " + total);
            }
        }
        ]]></script>     
      title: Declaring Variables within a Conditional
      questions:
        - "What is wrong with the program above?  How can you fix it?"
        - "What would you say is the &quot;scope&quot; of the <code>total</code> variable?  In other words, in what code block is the variable defined for use?"
    - model: |
        <img src="../images/venn3.png" alt="Empty 3-way Venn Diagram">
      title: "Putting It All Together: Implementing a Venn Diagram"
      questions:
        - "Make up a 3-way <a href=\"https://en.wikipedia.org/wiki/Venn_diagram\">Venn Diagram</a> of your choosing; you can look one up on the Internet if you wish."
        - "Label the three large circles \"A\", \"B\", and \"C\".  In each of the 7 regions within the Venn Diagram, which elements are true and which are false?"
        - "Write a series of <code>if</code> statements that may use <code>else</code> and <code>else if</code> blocks that print out the different states of your Venn Diagram.  There are a few ways to go about this, so we will discuss and compare approaches as a class."
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>         
    - model: |
        <a title="P. Kemp, CC0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:If-Then-Else-diagram.svg"><img width="256" alt="If-Then-Else-diagram" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/If-Then-Else-diagram.svg/256px-If-Then-Else-diagram.svg.png"></a>
      title: "Using Flow Charts to Observe Conditional Program Flow"
      questions:
        - "Draw a flowchart diagram that illustrates the control flow of your Venn Diagram program."
        - "Draw a flowchart of a conditional that checks if your grade is within range for each letter grade in the class."
        
tags:
  - boolean
  - expressions
  - conditionals
  
---

