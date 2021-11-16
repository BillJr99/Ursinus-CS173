---
layout: assignment
permalink: /Labs/GridGame
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
    - weight: 30
      description: Code Quality and Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide
      progressing: Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
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
    - "What functions would you write to help you to solve this problem?"
    
tags:
  - arrays
  - 2darrays
  - fileio
  - strings
  
---

In this lab, you will represent a board game grid as a 2-dimensional array, and prompt two users to interact with the board game according to a set of rules.

To begin, prompt the user for the size of the board game.  Your board will be an `N` by `N` square, so the user can type in an integer value for `N`.  Next, loop over each of the back two rows of the board for the first player, and the front two rows for the second player, and ask them to enter the value of each piece, between 1 and 9, on the board.  The sum of the pieces on the board can be no more than `10*N` for each player.  So, if `N==8`, each player has up to 80 points to allocate to their 16 pieces on the board, so the board might look like this when set up:

```
9 6 4 1 2 3 4 2
5 7 6 8 4 3 8 8
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 
7 5 1 4 4 3 5 3
7 8 9 5 2 3 7 7
```

A value of 0 represents that the square is empty.

Do not allow the user to enter a value that is greater than the number of points they have remaining, and when a player reaches their total, stop adding pieces to the board for that player.

You might consider how to determine which square is occupied by which player: for example, you could use negative numbers to represent on player and positive for another, or you could add 10 to the value of each square occupied by the second player (just be sure to un-do these when inspecting the true value of the player's piece!).  A better solution would be to create a second 2D array, and store the player number (1, 2, or 0 for an empty square) in each grid location corresponding to a square occupied by that player.

Now, take turns moving pieces on the board.  Prompt each player for the row and column of the piece they wish to move.  They can move one square in any direction (including diagonals) so long as the destination square is empty or contains a piece belonging to the other player.  Prompt the user for which direction they wish to move, and if it is a valid move, update the board.  Ask them to try again if they choose a location that it outside of the board, or that currently belongs to one of their own pieces.

If the destination square belongs to the opposing player, decide which of the two pieces has the greater value.  The piece with the smaller value is discarded from the board, and the stronger piece's value becomes the sum of the two pieces.  So, if a piece with value 8 moves onto a square that belongs to a piece with value 6, the 6 piece is removed, and the remaining piece value becomes 14.  If there is a tie (for example, two pieces with value 5), do not make the move, and the player's turn ends.  The game ends when one player has no remaining pieces on the board, or when no possible moves can be made (check for each of these conditions after each turn, and print a message and quit when this occurs).  Print out which player has won the game, if there is a winner.

### Printing the Board
After every turn, print the board to the screen in a grid pattern (like the example above).  Remember that you cannot print an array directly, but rather you'll need to print each element one-by-one.  You can do this with a loop!  I suggest writing a function called `printBoard` that accepts the board and prints it to the screen.

### Reading the Board Placement from a File
Asking the users to type in their piece values at the beginning is a lot of work!  It would be better to read this information from a file.  Create a file `gameboard.txt` that contains the game board in the format below, and prompt the user to enter the filename to read.  Then, read that file, and set up the game board array by looping over the text in the file.  

```
9 6 4 1 2 3 4 2
5 7 6 8 4 3 8 8
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 
7 5 1 4 4 3 5 3
7 8 9 5 2 3 7 7
```

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

Refer to the [File I/O Activity](../Activities/FileIO) for details on reading a file using a `Scanner`.  You'll end up with a nested loop here: a `while` loop to read your file (one line at a time), and one loop to iterate over each of the values you obtained by calling `line.split()`.  The inner loop is a for loop, so you'll have a counter variable, and that will be helpful when setting your board array (for example, `board[x][y] = numericValue;`).  **Which of these indices (x or y) corresponds to your inner loop counter?**  The outer loop is a `while` loop, so you don't have a counter for that other index variable, but you can make your own, and increment it each time through the `while` loop.

#### Adding a File to Your Project
If you'd like to create a file, say, `board.txt`, and add it to your project, you can click on the `Files` tab above your project in NetBeans, then right click on your project folder, choose `New`, and `Other`.  In the window that appears, select `Other` and `Empty File` to create a blank text file.  When you click Next, it will ask you for a file name, where you can specify `board.txt` or a name of your choice!

### Extra Credit (10 Points): Custom Rules

For extra credit, create three additional rules for your game that pertain to the array, and implement them on the grid.  For example, pieces whose value is equal to a certain value can move more than one square at a time, or can jump over occupied squares, or wins if there is a tie, *etc*.  Write down which rules you impelemented in your README.

## Helpful Hints: Listing Your Helper Functions

Think about what functions will help you to complete this lab.  For example, you might have functions like these (and more!):

* `readBoard`: a function that takes in a filename (`String`), opens the file, reads it, and creates the board.  It returns an `int[][]` 2 dimensional array of `int`.
* `printBoard`: a function that takes in the board (`int[][]`) and prints it to the screen using a [nested loop](../Activities/2DArrays).
* `move`: a function that takes in the board, the `x` and `y` coordinate to be moved, and the direction to move, and returns the board with the updates made to move the piece.

## Exporting your Project for Submission

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.
