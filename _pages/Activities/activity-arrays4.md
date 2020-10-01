---
layout: activity
permalink: /Activities/Arrays4
title: "CS173: Intro to Computer Science - Arrays"
excerpt: "CS173: Intro to Computer Science - Arrays"

info:
  prev: ./Arrays3
  
  goals: 
    - To be able to create, access, and iterate an <code>ArrayList</code>
    - To be able to explain that an <code>ArrayList</code> is a dynamic array that allows for expansion at runtime
    - To be able to dynamically grow and shrink an <code>ArrayList</code>
    - To use objects such as the <code>ArrayList</code> that accept templated/generic data types

  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
           public static void main(String[] args) {
              /* This is a class that encapsulates the behavior of an array,
                 but it grows as you add items on the fly. */
              ArrayList<String> arr = new ArrayList<String>(10);
              
              for(int i = 0; i < 10; i++) {
                String x = new String("Test #" + i);
                
                arr.add(x);
              }
              
              for(int i = 0; i < arr.size(); i++) {
                String x = arr.get(i);
                
                System.out.println(x);
              }
              
              arr.remove(arr.size() / 2);
              
              // This is called an Enhanced For Loop - a nice shortcut!
              for(String item: arr) {
                System.out.println(x);
              }
           }
        }
        ]]></script>       
      title: The <code>ArrayList</code>
      questions:      
        - What is the purpose of the <code>&lt;String&gt;</code> notation when creating the <code>ArrayList</code>?
        - What would be the effect of creating an <code>ArrayList</code> that stored another <code>ArrayList</code>?
        - What is the size of the <code>ArrayList</code> prior to calling <code>remove()</code>?  What is the size after the call?
        - Suppose a friend needed to remove every other element from an <code>ArrayList</code> (say, the ones with an even numbered index).  Looping for <code>i = 0</code> to <code>arr.size()</code>, they remove each element if <code>(i % 2 == 0)</code> but the wrong elements seem to be removed.  What happened, and what can we do instead?
        
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/topic-6-3-arrays-with-foreach.html 
      title: The Enhanced <code>for</code> Loop
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-1-arraylist-basics.html
      title: The <code>ArrayList</code>
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-2-arraylist-methods.html
      title: <code>ArrayList</code> Methods
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-3-arraylist-loops.html 
      title: Loops with the <code>ArrayList</code>
    
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/listPractice.html
      title: The <code>ArrayList</code>
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/listMedMC.html
      title: <code>ArrayList</code> Questions
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/listHardMC.html
      title: More Challenging Questions about the <code>ArrayList</code>
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/numberCubeA.html
      title: Number Cube
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/numberCubeB.html
      title: Number Cube (Longest Run)
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit8-2DArray/grayImageA.html
      title: Greyscale Images (Counting White Pixels)
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit8-2DArray/grayImageB.html
      title: Greyscale Images
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/horseBarnA.html
      title: Horse Barn
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/horseBarnB.html
      title: Horse Barn (Consolidation)
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/selfDivisorB.html
      title: Self Divisors
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/climbClubA.html
      title: Climbing Club
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/climbClubB.html
      title: Climbing Club (Sorted)
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/climbClubC.html
      title: Climbing Club (Distinct Names)
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/2016freeresponseQ4A.html
      title: String Formatter
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/2016freeresponseQ4B.html
      title: String Formatter (Gap Checker)
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit8-2DArray/routeCipherA.html
      title: Route Cipher
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit8-2DArray/routeCipherB.html
      title: Route Cipher with Encryption
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/soundA.html
      title: Sound
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/soundA.html
      title: Sound (Trim Silence)
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/cookieOrderA.html
      title: Cookie Order
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/cookieOrderB.html 
      title: Cookie Order with Removal       
      
tags:
  - arrays
  - arraylist
  - iteration
  - classes
  - containers 
  
---

