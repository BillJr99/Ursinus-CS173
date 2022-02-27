---
layout: activity
permalink: /Activities/Functions3
title: "CS173: Intro to Computer Science - Functions"
excerpt: "CS173: Intro to Computer Science - Functions"

info:
  next: ./Random
  prev: ./Functions2
  
  warmup: "First, write an if statement to tell if room temperature is between 70 and 74 degrees (you can print out a message saying whether or not it is in this range).  Then, migrate this to a function that accepts the temperature as a parameter, and call this function at least twice from <code>main()</code>.  Next, add a second parameter to this function to represent the humidity, and display a separate message indicating whether it is within a range of 30 and 50 percent.  Finally, modify your function to return a <code>boolean</code> if both conditions are met.  How might you use this logic to control a thermostat device?"
  
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
        <iframe height="800px" width="100%" src="https://learnwithtrace.com/playground/code?files=eyJ2ZXJzaW9uIjowLCJmaWxlcyI6W3sidmVyc2lvbiI6MCwiZmlsZW5hbWUiOiJNYWluLmphdmEiLCJkaXJlY3RvcnkiOiJzcmMvbWFpbi9qYXZhL3RyYWNlIiwiY29udGVudHMiOiJwYWNrYWdlIHRyYWNlO1xuXG5wdWJsaWMgY2xhc3MgTWFpbiB7XG4gICAgcHVibGljIHN0YXRpYyBkb3VibGUgZ2V0Q2lyY2xlQXJlYShkb3VibGUgcmFkaXVzKSB7XG4gICAgICAgIGRvdWJsZSByU3F1YXJlZCA9IE1hdGgucG93KHJhZGl1cywgMik7XG4gICAgICAgICBcbiAgICAgICAgZG91YmxlIHJlc3VsdCA9IE1hdGguUEkgKiByU3F1YXJlZDtcbiAgICAgICAgIFxuICAgICAgICByZXR1cm4gcmVzdWx0O1xuICAgIH1cbiAgICAgXG4gICAgcHVibGljIHN0YXRpYyB2b2lkIG1haW4oU3RyaW5nW10gYXJncykge1xuICAgICAgICAvLyBUT0RPOiBjcmVhdGUgYSBkb3VibGUgdmFyaWFibGVcbiAgICAgICAgIFxuICAgICAgICAvLyBUT0RPOiBjYWxsIHRoZSBnZXRBcmVhIGZ1bmN0aW9uIGFuZCBzdG9yZSB0aGUgcmVzdWx0IGluIHlvdXIgZG91YmxlIHZhcmlhYmxlXG4gICAgICAgICBcbiAgICAgICAgLy8gVE9ETzogcHJpbnQgdGhhdCB2YXJpYWJsZSB0byB0aGUgc2NyZWVuXG4gICAgfVxufVxuIiwiZWRpdGFibGUiOnRydWV9XX0%253D&language=JAVA" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>   
        
tags:
  - functions
  - expressions
  
---

