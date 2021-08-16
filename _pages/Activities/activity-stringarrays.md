---
layout: activity
permalink: /Activities/Arrays/Strings
title: "CS173: Intro to Computer Science - Arrays of Strings"
excerpt: "CS173: Intro to Computer Science - Arrays of Strings"

info:
  prev: ../Arrays2
    
  goals: 
    - To be able to print an array
    - "To split a String into an array using the <code>String.split()</code> method"

  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
            public static void printArray(String[] arr) { 
                for(int i = 0; i < arr.length; i++) {
                    System.out.print(arr[i]);
                    System.out.println(" ");
                }
                System.out.println();
            }

            public static void main(String[] args) {
                String str = "The quick brown fox jumped; it jumped over the dog.";
                String[] words = str.split(" ");
                printArray(words);
            }
        }
        ]]></script>         
      title: "Manipulating <code>String</code> Arrays"
      questions:
        - "What does the <code>split</code> function do?"
        - "When printing words, the period prints at the end of the final word.  How can we remove that?"
        - "How might you modify the call to <code>split</code> to separate on the semicolon?" 
        - "The spacing is not quite right when printing the sentence clauses; how can we fix that?"   
        - "Why was it necessary to print each element in the array using a loop?  Why not simply write <code>System.out.println(arr);</code>?"        
      
tags:
  - arrays
  - iteration
  
---

