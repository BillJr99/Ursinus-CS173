---
layout: activity
permalink: /Activities/Functions3
title: "CS173: Intro to Computer Science - Functions"
excerpt: "CS173: Intro to Computer Science - Functions"

info:
  next: ./Random
  prev: ./Functions2
  
  goals: 
    - To use functions with return values
    - To write javadoc comments for functions
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static double getCircleArea(double radius) {
                double rSquared = Math.pow(radius, 2);
                
                double result = Math.PI * rSquared;
                
                return result;
            }
            
            public static void main(String[] args) {
                // TODO: create a double variable
                
                // TODO: call the getArea function and store the result in your double variable
                
                // TODO: print that variable to the screen
            }
        }
        ]]></script>     
      title: Parameters and Return Values
      questions:
        - "Fill in the main function to compute the area of a circle."
        - "What would you modify to get the area of a circle with a different radius?"
        - "Write javadoc comments for the functions above."
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>   
        
tags:
  - functions
  - expressions
  
---

