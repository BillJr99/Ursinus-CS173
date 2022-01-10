---
layout: activity
permalink: /Activities/Arrays3
title: "CS173: Intro to Computer Science - Arrays"
excerpt: "CS173: Intro to Computer Science - Arrays"

info:
  prev: ./Arrays2
  next: ./Arrays/Strings
    
  goals: 
    - To design and implement algorithms using arrays

  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
            public static void main(String[] args) {
                int[] arr1 = {1, 2, 3, 4, 5};
                int[] arr2 = {1, 2, 3, 4, 5, 6};
                
                // TODO: check that the arrays are the same length
                
                // TODO: determine the length of the smaller array
                
                // TODO: write a loop that iterates up to the length of the smaller array
                and checks if the two arrays contain the same values, one at a time
            }
        }
        ]]></script>         
      title: Array Equality Algorithm
      questions:
        - "Fill in the code in <code>main()</code> above to determine if two arrays contain the same values"
        - "Move this code into a function.  What should it return?  Print the result in <code>main()</code> and write javadoc for the function."
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>          
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
            /** Remove an item from an array.  Given an array and a position, return a 
              * new array without that item.
              * @param array the array from which to remove an item
              * @param index the index of the item to be omitted
              * @return a new array with all the items from the original array except for the one at the specified index position
              */
            public static int[] removeItem(int[] array, int index) {
                // TODO - fill this in!
                
                // hint: since you are removing one item from the array, 
                // and you know how big the original array was, you know how 
                // big your new array should be!
            }
            
            public static void printArray(int[] array) {
                // TODO - fill this in; print each item in the array 
                // on a single line on the screen!
            }
            
            public static void main(String[] args) {
                int[] arr1 = {1, 2, 3, 4, 5};
                
                int[] arr2 = removeItem(arr1, 2);
                
                printArray(arr2);
            }
        }
        ]]></script>         
      title: Array Manipulation Algorithm
      questions:
        - "Fill in the code in the two functions above."
        - "Write javadoc for the <code>printArray</code> function."
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>          
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        import java.util.Arrays;
        
        public class Main {
            public static void printArray(int[] array) {
                // TODO - fill this in; print each item in the array on a single line on the screen!
            }
            
            public static void main(String[] args) {
                int[] arr1 = {1, 2, 3, 2, 1};
                
                // Sort the array so that it contains {1, 1, 2, 2, 3}
                // This modifies the actual array contents, 
                // so there is no need to return a value here.
                Arrays.sort(arr1);
                
                // TODO - fill this in by printing out the unique elements of the array.  
                // For this example, you should print 1 2 3
                
                // Use the printArray code you wrote above!
                printArray(arr1);
            }
        }
        ]]></script>         
      title: Array Uniqueness Algorithm
      questions:
        - "Fill in the code in the two functions above."
        - "Write javadoc for the <code>printArray</code> function."
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>        
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/topic-6-2-traversing-arrays.html
      title: Traversing Arrays
    
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/ArrayPractice.html
      title: Array Practice
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/Exercises.html
      title: Questions about Arrays     
      
tags:
  - arrays
  - iteration
  
---

