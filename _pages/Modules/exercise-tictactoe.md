---
layout: exercise
permalink: /Modules/TicTacToe/Exercise
title: "CS173: Intro to Computer Science - Tic-Tac-Toe"
excerpt: "CS173: Intro to Computer Science - Tic-Tac-Toe"

info:
  points: 3
  instructions: "Modify the TicTacToe.java file to return whether a given array contains a winning tic-tac-toe configuration."
  goals:
    - To iterate over a 2-dimensional array
    
canvasasmtid: ""    
canvaspoints: 3
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let ans = feedbackString.split("-");
  correctcheck: |
    ans[0] === "true" && ans[1] === "false"
 
files:
  - filename: "TicTacToe.java"
    name: tictactoe
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class TicTacToe {
            public static boolean checkWinningTicTacToe(char[][] board) {
                // return true if a winning tic-tac-toe board is given
                // for example, if the first element in any row is equal to the second element in that row, and also equal to the third element in that row.
                // ... the same logic is applied to every column, and to both diagonals of the board.
                
                // Use a loop to check each element of a row/column/diagonal.  The .length property of an array variable will be helpful in determining the bounds of (when to stop) the loop
            }
        }  

  - filename: "Driver.java"
    name: driver
    ismain: false
    isreadonly: true
    isvisible: true
    code: | 
        public class Driver {
            public static void main(String[] args) {
                char[][] board1 = new char[][] {
                    { "X", "O", "X" },
                    { "O", "X", "-" },
                    { "-", "-", "X" }
                };
                
                char[][] board2 = new char[][] {
                    { "X", "O", "X" },
                    { "O", "O", "-" },
                    { "-", "-", "X" }
                };
                
                boolean isWinner1 = TicTacToe.checkWinningTicTacToe(board1);
                boolean isWinner2 = TicTacToe.checkWinningTicTacToe(board2);
                              
                System.out.print(isWinner1 + "-" + isWinner2);
            }
        }         

  - filename: "Excerpt from Main.java: body of main() function"
    ismain: true
    name: main
    isreadonly: true
    isvisible: false
    code: |
        Driver.main(null);
        
---

In this exercise \[[^1]\], students will write a program that simulates a game of Tic-Tac-Toe. The Tic-Tac-Toe game is played on a 3x3 grid with two players who take turns. The first player marks moves with an X, and the second player marks moves with an O. The first player to form a horizontal, vertical, or diagonal sequence the same mark wins the game. In a 3x3 board, this is 3 such marks in a row.  Your program should check that a given board configuration is a winning board.

Note that using this interface, it is necessary to compare char variables with double quotes instead of single quotes (even though you will use single quotes in real Java code).  That is, to check if a variable `ch` is equal to the letter "X", you would write:

```java
if(ch == "X") { 
   // code to execute if true
}
```

You should use a loop in your submission.  To check your iteration, a test case is included that checks a 4x4 board for tic-tac-toe using the same rules as the standard 3x3 board (that is, that the whole column, row, or diagonal is filled with the same player's mark).  In other words, you are now searching for 4 marks in a row, but should use the same logic as you had written when using the 3x3 board.  

One way to go about this is to count how many X's and O's you find in a given row, column, or diagonal (three separate loops).  If the total number of X's or O's is equal to the length of that row, column, or diagonal, you can return `true`.  If, after all of these checks, you haven't found one of these winning conditions, return `false`.

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie)