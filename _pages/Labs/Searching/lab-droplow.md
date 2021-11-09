---
layout: assignment
permalink: /Labs/DropLowest
title: "CS173: Intro to Computer Science - Searching: Dropping the Lowest Score"
excerpt: "CS173: Intro to Computer Science - Searching: Dropping the Lowest Score"

info:
  coursenum: CS173
  points: 100
  goals:
    - To search an array using iterative approaches
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 30
      description: Code Quality and Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide
      progressing: Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide, and each function contains relevant and appropriate Javadoc documentation
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions
  readings:
    - rtitle: "ArrayList Activity"
      rlink: "../Activities/ArrayList"  
    - rtitle: "Iteration Activity"
      rlink: "../Activities/Iteration" 
  questions:
    - "Given an array containing the following values: <code>7, 8, 4, 2, 6, 5</code>, which index contains the smallest value?  What questions or comparisons did you have to ask to locate it?  What values did you have to keep track of?"
    - "Given an array containing the following values: <code>0, 8, 4, 2, 6, 5</code>, which index contains the smallest value?  What questions or comparisons did you have to ask to locate it?  What values did you have to keep track of?"
      
tags:
  - searching
  
---

In this lab, you will write and test functions to drop the lowest score in an `ArrayList<Double>` of test scores, and then return the average of the remaining items.

### Step 0: Creating an Array of Random Values
Since you'll be searching arrays for small items, it would be useful to have a function to generate an array of random values.  Write a function `generateRandomArray` that accepts an `int N` representing the desired size of the array.  You can create an `ArrayList` of `Double` values like this:

```java
ArrayList<Double> arr = new ArrayList<Double>(); // note the use of a capital D in the word Double
```

[Review](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html) the other `ArrayList` functions to determine how to add and remove items from the `ArrayList`.  In this function, write a loop to generate `N` random numbers and add them to your `ArrayList`.  For example, you can use your `ArrayList` as follows:

```java
arr.get(i) // this is equivalent to arr[i] for a traditional array
arr.add(x) // appends the value x - you'll use this one in your generateRandomArray function!
arr.remove(i) // remove the item at index i
arr.toString() // this lets you print the array values in a System.out.println statement!
arr.size() // this returns the number of elements in the array, which is equivalent to arr.length for a traditional array
```

Return the `ArrayList` you just created, and now you can generate random values from your `main` function!

### Step 1: Searching the Array for the Smallest Item
First, linearly search the array to find the index of the smallest item.  Remove the lowest item from the array, and print it.  You can print an `ArrayList` by calling `.toString()` on the `ArrayList` variable, and printing that.  

#### Finding the Item 
To find an item in an array, you can iterate over the array and use a conditional to check its value.

![Searching an array](../manim/output/ArraySearch.gif)

#### Finding the Smallest Item
Searching for the smallest item in an array is similar to searching an array, except that you don't have a specific key that you're looking for.  Instead, keep track of the smallest key value you've seen in the array so far, and update it if the current array item is smaller.  Choose an initial value for `key` that is so large that even the first item will seem smaller.

![Searching an array](../manim/output/ArraySearchLowest.gif)

Once you have found the smallest item, return its index to `main`, and remove the item from the `ArrayList` using that index.  **Question: why must your return statement be at the very end of this search function, and not anywhere else?**

**Hint:** You'll need initial values for the variables representing the smallest value and the position of the smallest value in the array.  One idea is to set these to the first position and value of the array, which would assume that the first value is the "one to beat."  **Which index (and value) correspond to the first element of the `ArrayList`?**

### Step 2: Counting the Number of Iterations
In addition, count the number of times your loop iterates to find the smallest item.  You can use an `int` counter that you increment each time you execute the loop.  Following the loop, print out the count of the number of times you execute inside a loop.

Put all of the above code into a function, and you will call that function from `main()`. 

### Step 3: Calling This Function and Plotting Your Results
Within `main()`, call this function several times, each with a different sized array.  You will plot the number of steps that were needed against the size of the array.  You can use a loop with a random number generator to generate scores.  I suggest creating a function that generates and returns an `ArrayList<Double>`, in which you pass the desired size of the array as a function parameter.  The function then uses a random number generator to fill the array and return it.  Then, you can call this from `main()` within a loop, so that you try it multiple times without having to copy and paste your code!

To plot your results, you can copy or type the iteration counts you receive into Microsoft Excel and generate a line graph.  Your first column will be the size of the array that you used, and your second column will be the number of iterations that were required to find the smallest element in that array.  Thus, your x-axis will be the size of the array, and your y-axis will be the number of iterations.  What do you notice about the shape and direction of this graph?

## Exporting your Project for Submission

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.
