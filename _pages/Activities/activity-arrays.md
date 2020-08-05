---
layout: activity
permalink: /Activities/Arrays
title: "CS173: Intro to Computer Science - Arrays"
excerpt: "CS173: Intro to Computer Science - Arrays"

info:
  goals: 
    - To be able to explain that an array is an ordered collection of data, whether they be primitives or objects.
    - To be able to create an array and assign its elements
    - To be able to access an element from an array by its index
    - To be able to iterate over an array
    - To be able to create, access, and iterate a 2D array
    - To be able to create, access, and iterate an ArrayList
    - To be able to explain that an ArrayList is a dynamic array that allows for expansion at runtime
    - To be able to dynamically grow and shrink an ArrayList
    - To use objects such as the <code>ArrayList</code> that accept templated/generic data types

  models:
    - model: |
        Recall from our earlier examples that we had to create a separate Book object variable for each Book we wanted to create.  We can simplify things by creating a single variable that refers to the whole collection.  This is called an array.  They allow us to leverage loops to quickly iterate over a collection of values or objects.
        <br>
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Book {
            String title;
            String author;
            int pages;
            
            Book(String _title) {
                this.title = _title;
                this.author = "Unknown";
                this.pages = 0;
            }
        }
        
        public class Main {
            public static void main(String[] args) {
                Book[] books = new Book[3];
                
                for(int i = 0; i < books.length; i++) {
                    books[i] = new Book("Book Number " + i);
                    System.out.println(books[i].title);
                }
            }
        }
        ]]></script>         
        <br>
        <img src="../images/examples/java-visualizer-array.png" alt="Java Visualizer Example of an Array" />
      title: Creating and Accessing Arrays
      questions:
        - What is the size of the <code>books</code> array?
        - What are the indices of the <code>books</code> array?
        - Why does the array use <code>.length</code>, when a String uses <code>.length()</code>, to report its size?
        - What is the advantage of allocating an array in a loop, when the book titles may need to be set individually?
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
            public static void main(String[] args) {
                int[] arr = new int[10];
                
                int sum = 0;
                int i = 0;
                
                for(i = 0; i < arr.length; i++) {
                    arr[i] = 2 * i;
                }
                
                for(i = 0; i < arr.length; i++) {
                    sum = sum + arr[i];
                }
                
                System.out.println("Sum = " + sum);
            }
        }
        ]]></script>         
        <br>
        <img src="../images/examples/java-visualizer-arrayiterate.png" alt="Java Visualizer Example of an Array" />
      title: Iterating Over Arrays
      questions:
        - "How would you modify the program above to play a game of &quot;Duck-Duck-Goose&quot; -- that is, iterating through the array until a certain value is reached (say, <code>10</code>)?"
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
           public static void main(String[] args) {
              int[][] mat1 = new int[10][10];
              int[][] mat2 = { { 1, 0 }, { 0, 1 } };
              
              // This is the length of the "outer vector" - the number of columns
              for(int i = 0; i < mat2.length; i++) {
                // This is the length of the "inner vector" - the number of rows
                for(int j = 0; j < mat2[i].length; j++) {
                    System.out.println(mat2[i][j]);
                }
              }
           }
        }
        ]]></script>         
        <br>
        <img src="../images/examples/java-visualizer-2darray.png" alt="Java Visualizer Example of a 2D Array" />
        <br>
        <img src="../images/examples/java-visualizer-2darrayidentity.png" alt="Java Visualizer Example of a 2D Array" />
      title: 2D Arrays and Traversals
      questions:
        - Run this code in the <a href=https://cscircles.cemc.uwaterloo.ca/java_visualize/#mode=edit>Java Visualizer</a>.  What is the output?
        - Re-draw the arrays <code>mat1</code> and <code>mat2</code> as a square grid. 
        - Is it possible to re-size these arrays if you need to add additional elements later?  If so, how, and if not, why not?
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
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/topic-6-1-array-basics.html
      title: Array Basics
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/topic-6-2-traversing-arrays.html
      title: Traversing Arrays
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/topic-6-3-arrays-with-foreach.html 
      title: The Enhanced <code>for</code> Loop
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-1-arraylist-basics.html
      title: The <code>ArrayList</code>
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-2-arraylist-methods.html
      title: <code>ArrayList</code> Methods
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit7-ArrayList/topic-7-3-arraylist-loops.html 
      title: Loops with the <code>ArrayList</code>
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit8-2DArray/topic-8-1-2D-arrays.html
      title: 2D Arrays
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit8-2DArray/topic-8-2-2D-array-loops.html
      title: Loops with 2D Arrays
         
  reflective_prompts:
    - How would you modify the above program to assign values to <code>mat1</code>, and then to multiply the two matrices together?  To multiply matrices, each cell of the result is equal to the products of each element of the corresponding column of <code>mat1</code> with each element of the corresponding row of <code>mat2</code>, added together.  A triply-nested loop with a sum is required.
    
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/ArrayPractice.html
      title: Array Practice
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit6-Arrays/Exercises.html
      title: Questions about Arrays
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit8-2DArray/Array2dCodePractice.html
      title: 2D Arrays
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
  
---

