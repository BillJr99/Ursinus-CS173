---
layout: exercise
permalink: /Modules/Iteration/Exercise
title: "CS173: Intro to Computer Science - Introduction to Iteration"
excerpt: "CS173: Intro to Computer Science - Introduction to Iteration"

info:
  points: 3
  instructions: "Modify the Driver.java file to compute compound interest using a loop to compute the overall interest rate."
  goals:
    - To use iteration to compute a discrete value
    
canvasasmtid: "137444"
canvaspoints: 3
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("2.71456") || pos.includes("2.722014")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("2.722004")
      feedback: "Try again: you might be iterating once too many times; don't forget that initializing the variable counts as the first multiplication!" 
    - incorrectcheck: |
        pos.includes("2.613")
      feedback: "Try again: don't forget to compound daily instead of monthly!" 
    - incorrectcheck: |
        pos.includes("2.83")
      feedback: "Try again: don't forget to compound daily instead of monthly, and you might be iterating once too many times; initializing the variable counts as the first multiplication!" 
      
files:
  - filename: "Driver.java"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class Driver {
            public static void main(String[] args) {
                // balance = principal * totalInterestRate
                // totalInterestRate = totalInterestRate * compoundFactor, computed n*t times
                //   ... where compoundFactor = (1 + (rate / n))
                //       ... where t = periods (years), n = compoundTimesPerPeriod (times per year),
                //       ... and rate = annual interest rate (2% == 0.02)
                
                int principal = 1;                  // 1 dollar invested
                double interest = 1;                // at 100% interest
                int years = 1;                      // for 1 year
                
                /* TODO: Change this to compound daily */
                int compoundTimesPerYear = 12;      // compounded monthly
                
                double compoundFactor = 1 + (interest / compoundTimesPerYear);
                double totalInterestRate = compoundFactor;
                
                // iterate one fewer time because we initialized the variable above, which counts as one multiplication
                for(/* TODO: Fill this in */) { 
                    totalInterestRate = totalInterestRate * compoundFactor;
                }
                
                double finalBalance = principal * totalInterestRate;
                
                System.out.println(finalBalance);
                System.out.println(totalInterestRate);
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

## Fun With Limits

As your `compoundTimesPerYear` variable increases, your total balance approaches a certain famous constant: what is it?  
