---
layout: assignment
permalink: /Labs/Words
title: "CS173: Intro to Computer Science - Words with Classmates"
excerpt: "CS173: Intro to Computer Science - Words with Classmates"

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
    - weight: 10
      description: Code Indentation and Spacing
      preemerging: Code indentation and spacing are generally inappropriate or inconsistent
      beginning: Code indentation or spacing are generally appropriate but inconsistent in a few isolated instances
      progressing: Code indentation or spacing are appropriate or consistent, with minor adjustments needed
      proficient: Code indentation and spacing are appropriate and consistent
    - weight: 10
      description: Code Quality
      preemerging: Prior code quality feedback and style guide standards are not reflected in the submitted code to a great extent
      beginning: Code quality conforms to several standards in the course Style Guide, and progress is demonstrated in improving code quality from prior feedback
      progressing: Code quality conforms to the standards in the course Style Guide to a great extent, with a few identified areas of improvement
      proficient: Code quality substantially conforms to the standards in the course Style Guide
    - weight: 10
      description: Code Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program; specifically, javadoc style comments are present for some functions
      progressing: Code documentation is present that re-states the explicit code definitions
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program; specifically, javadoc style comments are present for all functions
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided, or the README file submitted is blank
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

In this lab, you will manipulate `String`s by playing a game we will call "Words with Classmates" based on the [Wordle](https://www.powerlanguage.co.uk/wordle/) game.  

## Part 1: The Program

We provide a [dictionary file](https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt) that you can download into your project and read into a series of `String` variables, one line at a time.  [Read the dictionary file](../Activities/FileIO), one line at a time, and, for each word, if it is exactly 5 letters in length, use a random number generator to flip a coin and randomly select it with some probability.  If you get to the end of the file and haven't returned a word yet, return the last 5 letter word that you found.  Let's call this word your *secret word*.  You may wish to convert this `String` to an upper-case `String` to facilitate our comparisons later.

Print out five asterisk ("\*") characters to the screen to represent that the word has not yet been solved.  Give the player an opportunity to type in a 5-letter word as their guess.  For each letter in your guess, if the corresponding letter in the secret word is the correct letter and in the correct position in the secret word, print that correct letter to the screen in upper-case.  If the letter is in the secret word but not in the correct position as given in the guess, print this letter in lower-case.  If the letter is not in the secret word at all, print an asterisk.

Thus, if the secret word is `SAUCE`, and the user guesses `SIREN`, you would print `S**e*`, because the `S` in `SIREN` is in the correct position in the secret word `SAUCE`, but there is no `I`, `R`, or `N` in `SAUCE`, so asterisks would be printed in those positions, and the lower-case `e` gets printed in its position in the word `SIREN`, but in lower-case to indicate that it belongs somewhere else in the secret word.

Allow the user to guess up to 5 times.  

## Part 2: Customizing the Rules

Change the input variables to make your own rules to the game.  For example, perhaps you can use 6 letter words, or 6 letter guesses.  The best way to do this is to make sure that your parameter values (for example, 5 guesses, 5 letter words, and the probability of selecting a word from the dictionary file) are all variables or function parameters so that they can be customized easily.

## Part 3: Unit Tests

Add appropriate unit tests for all non-main functions that you write, and ensure that they pass!

### Adding a File to your Project

When you save the dictionary file to your computer, you can go to NetBeans and choose the `File -> Open File` menu.  Choose the dictionary file.  If you then go to the `File -> Save As` menu, you can navigate to and double click on your project directory (this directory might be in your user home directory under a directory called `NetBeansProjects`).  After double clicking on your project directory, save your file under your project directory.  You can then open your file using the code below, and [read the file](../Activities/FileIO) as you normally would.

`File f = new File("words_alpha.txt");`

## Finishing Touches and Writeup 

Don't forget to test your program with several different inputs to help verify that things work the way you expect!  Think in terms of trying to break your program; if it's really hard to "trick" your program into getting the wrong answer, you've probably done a good job making your code robust.  

Also, check the [Style Guide](../Style-Guide) to make sure that you've written high quality code; make sure your code is "readable," well indented, uses good variable names, and includes good comments throughout the program.

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

### Exporting your Project for Submission

Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.  **Be sure to save your README file before exporting the project, so that your work is included in the submission!**

## For Fun: Choosing the Most Informative Wordle Guess

Here is an interesting video from 3Blue1Brown describing the process by which one might select a Wordle guess that optimizes your chances of winning.  He talks about some background in Information Theory, which is a mechanism by which we can quantify how much information we get -- in other words, by how much we narrow down the possible answers given a guess.

<iframe width="560" height="315" src="https://www.youtube.com/embed/v68zYyaEmEA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
