---
layout: exercise
permalink: /Modules/TicTacToe/Exercise
title: "CS173: Intro to Computer Science - Tic-Tac-Toe"
excerpt: "CS173: Intro to Computer Science - Tic-Tac-Toe"

info:
  prev: "./Module"
  instructions: "Modify the TicTacToe.java file to return whether a given array contains a winning tic-tac-toe configuration."
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString;
  correctcheck: |
    pos.trim() === "true"
 
files:
  - filename: "TicTacToe.java"
    name: tictactoe
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class TicTacToe {
            public static boolean checkWinningTicTacToe(char[][] board) {

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
                    { "X", "O", "X", "-" },
                    { "O", "O", "X", "-" },
                    { "-", "-", "X", "-" },
                    { "-", "-", "X", "O" }
                };
                
                boolean isWinner1 = TicTacToe.checkWinningTicTacToe(board1);
                boolean isWinner2 = TicTacToe.checkWinningTicTacToe(board2);
                
                boolean bothWinners = isWinner1 && isWinner2;
                
                System.out.println(bothWinners);
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

Note that using this interface, it is necessary to compare char variables with double quotes instead of single quotes.  That is, to check if a variable `ch` is equal to the letter "X", you would write:

```java
if(ch == "X") { 
   // code to execute if true
}
```

You should use a loop in your submission.  To check your iteration, a test case is included that checks a 4x4 board for tic-tac-toe using the same rules as the standard 3x3 board (that is, that the whole column, row, or diagonal is filled with the same player's mark).  In other words, you are now searching for 4 marks in a row, but should use the same logic as you had written when using the 3x3 board.  

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie)