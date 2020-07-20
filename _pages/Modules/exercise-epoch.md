---
layout: exercise
permalink: /Modules/EpochTime/Exercise
title: "CS173: Intro to Computer Science - Epoch Time Overflow Calculator"
excerpt: "CS173: Intro to Computer Science - Epoch Time Overflow Calculator"

info:
  prev: "./Module"
  instructions: "Modify the EpochTimeOverflow.java file to print the year when the Epoch overflow occurs."
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString;
  correctcheck: |
    parseInt(pos, 10) == 2038
 
files:
  - filename: "EpochTimeOverflow.java"
    name: epochtimeoverflow
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        public class EpochTimeOverflow {
            public static void main(String[] args) {
                final int MAX_INT = 2147483647;
                
                int epochStartYear = 1970;
            }
        }    

  - filename: "Excerpt from Main.java: body of main() function"
    ismain: true
    name: main
    isreadonly: true
    isvisible: false
    code: |
        EpochTimeOverflow.main(null);
        
---

The largest signed 32-bit integer that can be represented is `pow(2, 31) - 1 = 2147483647`.  This is because the sign requires one bit to encode, leaving 31 bits to represent the value.  The Unix operating system stores the current date and time by storing the number of seconds that have elapsed since a particular date, called the epoch.  This "epoch" date is January 1, 1970.  The Unix `time_t` data type has historically been a 32-bit signed integer (more recently, it is being expanded to a 64-bit value, for reasons that will become clear shortly!).  In this exercise \[[^1]\], you will compute the number of years represented by the maximum number of seconds that a 32-bit signed integer can store.  After adding this to the epoch start year of 1970, you will print out this value as the year in which a 32-bit Epoch counter will "overflow" and start counting upwards from the minimum 32 bit signed integer.  

Incidentally, the smallest signed 32 bit integer is `-2147483648`.  Notice that this value differs by 1 from the largest possible positive value shown above; that's because one of the `pow(2, 32)` binary values must represent 0, so there is an odd number of values remaining on the number line!.

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie)