---
layout: assignment
permalink: /Labs/TreasureHunt
title: "CS173: Intro to Computer Science - 2D Array Board Game"
excerpt: "CS173: Intro to Computer Science - 2D Array Board Game"

info:
  coursenum: CS173
  points: 100
  goals:
    - To represent and manipulate a grid of values in a 2D array
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
    - rtitle: "Arrays Activity"
      rlink: "../Activities/Arrays"     
    - rtitle: "2D Arrays Activity"
      rlink: "../Activities/2DArrays"          
    - rtitle: "File I/O Activity"
      rlink: "../Activities/FileIO" 
  questions:
    - "What additional functions would you write to help you to solve this problem?"
    
tags:
  - arrays
  - 2darrays
  - fileio
  
---

In this lab, you will create a text file representing a 2D grid, open and read that file into a 2D array, and then play a game with the user to search the array for hidden treasures within the text file.

## Background: Minesweeper
The rules of our game will be somewhat like the classic game Minesweeper, in which the user searches for hidden "mines" on a 2-dimensional grid by uncovering squares on the grid one-by-one.  When a square is uncovered, it either contains a "mine" or is empty.  If it contains a "mine," the game is lost.  If the mine is empty, a number is displayed on that square indicating how many "mines" are found on adjacent squares.  This is illustrated in the image below:

<a title="Brandenads, CC BY-SA 4.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Kmines_Expert_Game_with_Numbers_1-8.png"><img width="512" alt="Kmines Expert Game with Numbers 1-8" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Kmines_Expert_Game_with_Numbers_1-8.png/512px-Kmines_Expert_Game_with_Numbers_1-8.png"></a>

## What to Do

### Part 1: Creating a Game Board
Begin by creating a text file containing the treasures in your game.  To do this, create a file that represents a 2-dimensional grid, as shown below.  No specific size or shape is required, but this example represents an 8-by-8 grid.  Each entry is either a `1` or a `0`, indicating that the square contains a treasure, or does not.

```
0 1 1 0 0 1 0 1
0 0 0 0 0 0 1 0
1 0 0 0 1 0 0 0
0 0 0 1 0 0 0 0
0 0 0 0 0 0 1 1
1 0 0 1 0 1 1 1
0 0 0 0 1 0 0 0
1 0 0 1 0 1 0 0
```

Save this file into your project as `board.txt`.  

#### Adding a File to Your Project
If you'd like to create a file, say, `board.txt`, and add it to your project, you can click on the `Files` tab above your project in NetBeans, then right click on your project folder, choose `New`, and `Other`.  In the window that appears, select `Other` and `Empty File` to create a blank text file.  When you click Next, it will ask you for a file name, where you can specify `board.txt` or a name of your choice!

### Step 2: Reading the File into an Array
Begin by reading this file into your program.  Refer to the [File I/O Activity](../Activities/FileIO) for details on reading a file using a `Scanner`.  You'll end up with a nested loop here: a `while` loop to read your file (one line at a time), and one loop to iterate over each of the values you obtained by calling `line.split()`.

#### Splitting each Line of the File to Read Each Number within the File
You have a few options for reading the file, but I suggest reading the input one-line-at-a-time, and using the `String.split()` method to break each line into an array of its individual values.  You can split a String like this:

```java
String str = "The quick brown fox";
String[] words = str.split(" "); // words contains {"The", "quick", "brown", "fox"}
```

If your values are numeric (like they are in this lab!), you can convert each value to an `int` as follows:

```java
String str = "9 6 4 1 2 3 4 2"; // you will read this from your Scanner via a while loop!
String[] values = str.split(" ");
for(int i = 0; i < values.length; i++) {
  String value = values[i];
  int numericValue = Integer.parseInt(value);
  // you can set your array element to this value here
}
```

### Step 3: Play the Game
Prompt the user to enter an `x` and `y` position on the board.  Don't actually show the user the board contents!  Instead, print out a grid as follows:

* A star character for an unknown square
* For each uncovered square, print out a number representing how many adjacent squares contain a treasure tile
* A letter X for an uncovered tile that contains a treasure

Each time the user uncovers a treasure tile, award the user 100 points.  Each time the user uncovers a blank tile, award them 1 point.  The goal is to finish the game with as few points as possible (that is, lower scores are better!).

#### Determining the Location of the Treasure

There are several ways to solve this problem.  I suggest creating a second array of `int` values, with the same shape as your game board (that is, a 2D array with the same number of rows and columns as your board).  Let's call this new array your scoreboard.  Initially, set all the values inside this array to `-1`, which we will interpret to mean a square that has not been uncovered yet.  When the user uncovers a tile, check your original game board to see if it is a `0` or a `1`.  If it is a `1` (containing a treasure), set the corresponding position in the scoreboard to some value, let's say a `9`.  We'll use this value to mean that a treasure was uncovered.  Otherwise, the original board contained a `0`: when this happens, loop over the 8 squares adjacent to the uncovered square, and count how many of these squares contain a `1`.  This value can only be between `0` and `8` (which is why I chose `9` for the treasure square value, and `-1` for an unexplored square!).  Store this value on your scoreboard.

Then, when you print your board, you can just look at your scoreboard.  For each value in the scoreboard, if you see a `-1`, you can print a star character (meaning unexplored), if you see a value between `0` and `8`, you can print that number, and if you see a `9`, you can print a letter `X`.

Repeat this process until only treasure squares remain on the board.  You might write a function that checks if non-treasure squares remain uncovered, and return a `boolean` to let you know.  You will need your original board and your scoreboard: return `true` if there is at least one unexplored square on the scoreboard that still contains a `0` on the original board: your game loop will continue as long as this function returns `true`.

## Finishing Touches and Writeup 

Don't forget to test your program with several different inputs to help verify that things work the way you expect!  Think in terms of trying to break your program; if it's really hard to "trick" your program into getting the wrong answer, you've probably done a good job making your code robust.  

Also, check the [Style Guide](../Style-Guide) to make sure that you've written high quality code; make sure your code is "readable," well indented, uses good variable names, and includes good comments throughout the program.

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

### Exporting your Project for Submission

Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.  **Be sure to save your README file before exporting the project, so that your work is included in the submission!**
