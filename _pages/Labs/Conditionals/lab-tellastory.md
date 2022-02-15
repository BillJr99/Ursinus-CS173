---
layout: assignment
permalink: /Labs/TellAStory/Conditionals
title: "CS173: Intro to Computer Science - Tell a Story with Conditionals"
excerpt: "CS173: Intro to Computer Science - Tell a Story with Conditionals"

info:
  coursenum: CS173
  points: 100
  goals:
    - To use conditionals to solve problems enabling custom control flow
    - To read user input from the console
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
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
    - rtitle: "Conditionals Activity"
      rlink: "../../Activities/Conditionals"
    
tags:
  - arrays
  - strings
  
---

In this lab, you will use conditionals to alter your program's control flow (that is, flow from one line of code to the next).  We can use `if` statements to conditionally execute code, or to make a choice between two or more pieces of code to run.  Then, you will use conditionals to create an narrate an interactive story.

## Part 1: Implementing a Venn Diagram

Begin by drawing a [three-way Venn Diagram](https://www.educationworld.com/tools_templates/D_venn3_2) of your choice.  For example, [this Venn Diagram](https://www.buzzfeed.com/tessafahey/actor-venn-diagram) sorts characters by whether they have been in the Marvel Cinematic Universe, won an academy award, and/or performed on Broadway.  Whatever you choose, make sure at least one item fits into each category.  You can draw your diagram using software like Microsoft Paint or PowerPoint, or on paper and taking a picture.  Either way, be sure to submit it with your project!

Next, write a program that implements your Venn Diagram.  That is, write a series of `if/else if/else` statements, or nested `if` statements, that sets `boolean` variables representing each of the three main quadrants of your Venn Diagram, and prints to the screen where that person/place/thing fits into your Venn Diagram based on those `if` statements.  You can number the qudrants from 1 to 7, if you like, and print which quadrant results from the three `boolean` variables.

### Hint: Nested versus Cascading `if` Staetments
If your `if` statements look like this:

```java
// this is a nested if statement
if(something) {
    if(somethingElse) {
        // do something
    }
}
```

you could also write it like this:

```java
// this is a cascading if statement
if(something && somethingElse) {
   // do something
}
```

#### `else/if` Statements

You can create your own "waterfall" of `else/if` statements using a shortcut notatation for the nested and cascading `if` statements above.  For example:

```java
double temperature = 50;

if(temperature > 90) {
  System.out.println("It's going to be hot out!");
} else if(temperature > 50) {
  System.out.println("It's going to be comfortable.");
} else if(temperature > 32) {
  System.out.println("It's above freezing!");
} else {
  System.out.println("It's freezing out!");
}
```

### Hint: Automatically Formatting Your Code

Using NetBeans, you can automatically format your code by going to the `Source` menu and choosing `Format`.  This will automatically align your curly braces and indent your code appropriately.  Please feel free to use this early and often as you write your code!

## Part 2: Using Conditionals to Tell a Story

Using `if` and `if/else` statements, write a program to tell an interactive story.  You can ask the user questions and have them enter their answer.  Depending on what they say, you can print one message or another in response to them.  You can be creative here!  Whatever you decide, your story should have **at least three opportunities** to enter a response (this could be a choice to walk from one room to another in your story, or to pick up an object, or to talk with someone, or take some action, *etc*).  At least once, your story should make a decision based on what the user just entered, and something else that has happened along the way.  In other words, you should have at least one compound `if` statement (using an `&&` or an `||`, a nested `if` statement, or a cascading `if` statement in your story.

### Reading User Input

Did you know that you can read values from the console window into variables?  You can read in all kinds of data types (numbers, text, and so on), which we'll explore later.  For now, here's how you can read in a `String` that the user can type in:

```java
// add this to the top of your program, under the line that starts with the word "package"
// import java.util.Scanner;

// and you can do this in main():
Scanner input = new Scanner(System.in);

System.out.println("What is your name?");
// this next line will pause to allow the user to type in something in the console window
// and whatever they type will go into the name variable when they hit <enter>!
String name = input.nextLine(); 

System.out.println("Your name is: " + name);
```

### Checking String Equality
To check if two `String`s are equal, you can do this:

```java
String str1 = "some string";
String str2 = "some other string";


// if they're equal
if(str1.equals(str2)) {

}

// if they're not equal
if(!str1.equals(str2)) {

}
```

For example:

```java
// add this to the top of your program, under the line that starts with the word "package"
// import java.util.Scanner;

// and you can do this in main():
Scanner input = new Scanner(System.in);

System.out.println("What is your name?");
// this next line will pause to allow the user to type in something in the console window
// and whatever they type will go into the name variable when they hit <enter>!
String name = input.nextLine();

if(name.equals("Bill")) {
    System.out.println("Hi, Bill!");
}
```

### Making an Interesting Story

You can add some depth to your story by setting a variable or two depending on the user's responses to your questions.  You can use those variables in `if` statements later, which will make it seem as though your story "remembered" the user's responses!

```java
// add this to the top of your program, under the line that starts with the word "package"
// import java.util.Scanner;

// and you can do this in main():
Scanner input = new Scanner(System.in);

System.out.println("What is your name?");
// this next line will pause to allow the user to type in something in the console window
// and whatever they type will go into the name variable when they hit <enter>!
String name = input.nextLine();

// Assume isBill is false, and then we can set it to true conditionally (if name is "Bill").
boolean isBill = false;
if(name.equals("Bill")) {
    isBill = true;
}

// later on...

if(isBill) {
    System.out.println("Earlier, you said your name is Bill!  It\'s nice to meet you.");
}
```

## Extra Credit (Up to 10%): Best Story Competition
Creativity is encouraged, but not required for a grade!  Let me know in your documentation if you'd like to demo your story to the class - I hope you do!  You will receive 5% extra credit for entering your submission, and the class will vote on their favorite story (the winner will receive an additional 5% extra credit).

## Finishing Touches and Writeup 

Don't forget to test your program with several different inputs to help verify that things work the way you expect!  Think in terms of trying to break your program; if it's really hard to "trick" your program into getting the wrong answer, you've probably done a good job making your code robust.  

Also, check the [Style Guide](../Style-Guide) to make sure that you've written high quality code; make sure your code is "readable," well indented, uses good variable names, and includes good comments throughout the program.

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

### Exporting your Project for Submission

Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.  **Be sure to save your README file before exporting the project, so that your work is included in the submission!**
