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
                char[][] board = new char[][] {
                    { "X", "O", "X" },
                    { "O", "X", "-" },
                    { "-", "-", "X" }
                };
                
                boolean isWinner = TicTacToe.checkWinningTicTacToe(board);
                
                System.out.println(isWinner);
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

In this exercise \[[^1]\], students will write a program that simulates a game of Tic-Tac-Toe. The Tic-Tac-Toe game is played on a 3x3 grid with two players who take turns. The first player marks moves with an X, and the second player marks moves with an O. The first player to form a horizontal, vertical, or diagonal sequence of three marks wins the game. Your program should check that a given board configuration is a winning board.

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie)