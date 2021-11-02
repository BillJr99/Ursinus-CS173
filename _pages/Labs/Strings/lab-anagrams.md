---
layout: assignment
permalink: /Labs/Anagrams
title: "CS173: Intro to Computer Science - Anagram Solver"
excerpt: "CS173: Intro to Computer Science - Anagram Solver"

info:
  coursenum: CS173
  points: 100
  goals:
    - "To manipulate <code>String</code> variables"
  rubric:
    - weight: 40
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 20
      description: Test Cases
      preemerging: Testing was performed outside of the unit test framework, or not performed at all
      beginning: Trivial test cases are provided in a unit test framework
      progressing: Test cases that cover some, but not all, boundary cases and branches of the program are provided
      proficient: Test cases that cover all boundary cases and branches of the program are provided
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
    - rtitle: "File I/O Activity and Examples"
      rlink: "../Activities/FileIO"    
  questions:
    - "What functions do you need to write to solve this problem?  Before you begin, sketch them out first on paper or in a text file, and describe which functions you would call from <code>main</code> and in what order."
    
tags:
  - strings
  
---

In this lab, you will manipulate `String`s by computing all the anagrams of a given word in a dictionary.  We provide a [dictionary file](https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt) that you can download into your project and read into a `String`.  

## Part 1: Anagram Finder

Two words are anagrams if they contain the same letters.  For example, `bat` and `tab` are anagrams, because they each contain one letter `a`, one letter `b`, and one letter `t`.

Write a function that takes as parameters a file path and a `String` upon which to find anagrams.  [Read the dictionary file](../Activities/FileIO), one line at a time, and pass each line along with the `String` to a second function that returns `true` if the two words are anagrams, and `false` otherwise.  Print each word that is a matching anagram.

You can choose your approach for determining if two words are anagrams.  For example, you can loop over each character in each word, count the number of each character, and ensure they are equal across both `String`s.  If you are looking for a challenge, you can also sort the letters in each word, and the resulting `String`s should be equal (for example, both `bat` and `tab` sort to the same `String` `abt`).

## Part 2: Puzzle Solver

Next, write a new function that operates similarly to the anagram finder, but allows you to also specify a character and a position.  This function should accept a `String` representing your available characters, a character, and a position.  Find all words in the dictionary that are anagrams of your `String`, but with a specific character at a given position within the `String`.  Only print those anagram matches.

### Adding a File to your Project

When you save the dictionary file to your computer, you can go to NetBeans and choose the `File -> Open File` menu.  Choose the dictionary file.  If you then go to the `File -> Save As` menu, you can navigate to and double click on your project directory (this directory might be in your user home directory under a directory called `NetBeansProjects`).  After double clicking on your project directory, save your file under your project directory.  You can then open your file using the code below, and [read the file](../Activities/FileIO) as you normally would.

`File f = new File("words_alpha.txt");`

### A Word About the Dictionary File

Did you notice that you had to read the dictionary file twice (once for each part of the lab)?  **Why is this unfortunate, and what might we do differently in the future?**  You don't have to modify the program, but speculate in your README on a better approach that would allow us to only have to read the file a single time.

## Exporting your Project for Submission

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.
