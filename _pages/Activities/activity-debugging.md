---
layout: activity
permalink: /Activities/Debugging
title: "CS173: Intro to Computer Science - Debugging"
excerpt: "CS173: Intro to Computer Science - Debugging"

info:
  goals: 
    - To use the NetBeans Debugger to step through and identify bugs in code
    
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        /*
         * To change this license header, choose License Headers in Project Properties.
         * To change this template file, choose Tools | Templates
         * and open the template in the editor.
         */
        package numbergame;

        /**
         *
         * @author bill
         */
        public class NumberGame {

            /**
             * @param args the command line arguments
             */
            public static void main(String[] args) {
                int value = 6;
                int year = 2021;
                int birthYear = 1982;
                
                double intermediate = value * 2;
                intermediate += 5;
                intermediate *= 50;
                intermediate -= 250;
                intermediate += year;
                intermediate -= birthYear;
                
                int ageThisYear = (int) (intermediate % 100);
                
                System.out.println(ageThisYear);
            }
            
        }
        ]]></script>   
      title: Using a Debugger to Trace Program Execution
      questions:
        - "Without using NetBeans, trace by hand through the program and update the values of each variable on paper."
        - "Add a watch on the <code>intermediate</code> variable."
        - "Set a breakpoint to stop the program at line 26."
        - "After running the program to line 26, step through the program one line of code at a time until you reach the end.  What variables change their values at each step, and to what values?"
        - "Write a program that uses a math formula incorrectly.  Exchange it with a partner, and use the debugger to try to find it.  As you step through the program, ask yourself what the next value should be, and then step once to check that you're right, until you find the mistake."
        
  readings:
    - rtitle: "Debugging Video"
      rlink: "../Modules/Debugger/Module"
    - rtitle: "NetBeans Debugging Tutorial"
      rlink: "../NetBeans/Debugging"  
    - rtitle: "Debugging in NetBeans"
      rlink: "http://www.cs.columbia.edu/~cmurphy/summer2008/1007/netbeans/7_debugging.html"
        
tags:
  - debugging  
---

