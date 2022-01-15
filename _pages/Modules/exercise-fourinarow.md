---
layout: exercise
permalink: /Modules/FourInARow/Exercise
title: "CS173: Intro to Computer Science - Four in a Row"
excerpt: "CS173: Intro to Computer Science - Four in a Row"

info:
  points: 3
  instructions: "Modify the FourInARow.java file to return whether a given array contains a winning configuration.  Specifically, if any column has four consecutive items with the same value, they are a winner."
  goals:
    - To iterate over a 2-dimensional array
    
canvasasmtid: "137457"
canvaspoints: 3
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let ans = feedbackString.split("-");
  correctcheck: |
    ans[0] === "1" && ans[1] === "0" && ans[2] === "2"       
 
files:
  - filename: "FourInARow.java"
    name: fourinarow
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class FourInARow {
            public static int checkWinning(int[][] board) {
                // winner is 0 if there is no winner, 1 if team 1 wins, 
                // ... and 2 if team 2 wins.
                int winner = 0;

                // the counts are the number of consecutive entries for team 1,
                // ... or team 2 in a particular column
                int count1 = 0;
                int count2 = 0;

                // this outer loop counts over all the rows, and we would normally 
                // ... iterate across each row with the inner loop
                // ... but we want to loop down every column, so I'm switching the 
                // ... i and j indices so that we loop down each column instead!
                // the number of columns is board[0].length - the size of the first row
                // ... (we'll assume they're all the same, so we'll just pick the first one!)
                for(int j = 0; j < board[0].length; j++) {
                  // TODO: initialize count1 and count2 to 0 so that we have a 
                  // ... fresh count within each column

                  // now, loop down each of the columns to look for a winner
                  // the number of rows is board.length
                  for(int i = 0; i < board.length; i++) {
                    // TODO: if board[i][j] is 1, tally one for team1's count,  
                    // ... and similarly, if board[i][j] is 2, tally 1 for team2.
                    // ... BUT, also reset the other team's count to 0 (since they 
                    // ... can't be winning if they don't have 4 in a row!).
                    // ... what should you do in the "else" clause here, 
                    // ... if board[i][j] is 0?

                    // TODO: if count1 or count2 is 4, set winner to 1 (if count1 is 4), 
                    // ... or 2 (if count2 is 4)
                  }
                }

                return winner;                
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
                int[][] board1 = new int[][] {
                    { 0, 0, 1, 0 },
                    { 0, 2, 1, 1 },
                    { 0, 2, 1, 1 },
                    { 0, 2, 1, 1 }
                };
                
                int[][] board2 = new int[][] {
                    { 0, 0, 2, 0 },
                    { 0, 2, 1, 1 },
                    { 0, 2, 1, 1 },
                    { 0, 2, 1, 1 }
                };
                
                int[][] board3 = new int[][] {
                    { 0, 2, 2, 0 },
                    { 0, 2, 1, 1 },
                    { 0, 2, 1, 1 },
                    { 0, 2, 1, 1 }
                };                
                
                int winner1 = FourInARow.checkWinning(board1);
                int winner2 = FourInARow.checkWinning(board2);
                int winner3 = FourInARow.checkWinning(board3);
                              
                System.out.print(winner1 + "-" + winner2 + "-" + winner3);
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

In this exercise, you will fill in a function to determine the winner of a game of Four-in-a-Row.  A game board (a 2D array of `int`s) initially contains all `0`s.  Each player (team 1 and 2) places a value into a column of the game board, and it falls to the bottom of the board.  The game ends with a winner if the board contains four consecutive items down a column (only the vertical column - you don't need to worry about the rows or diagonals).  For example, this board represents a game won by team 2:

```java
int[][] board = new int[][] {
    { 0, 2, 2, 0 },
    { 0, 2, 1, 1 },
    { 0, 2, 1, 1 },
    { 0, 2, 1, 1 }
};     
```                