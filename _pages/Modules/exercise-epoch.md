---
layout: exercise
permalink: /Modules/EpochTime/Exercise
title: "CS173: Intro to Computer Science - Epoch Time Overflow Calculator"
excerpt: "CS173: Intro to Computer Science - Epoch Time Overflow Calculator"

info:
  points: 3
  instructions: "Modify the EpochTimeOverflow.java file to print the year when the Epoch overflow occurs.  Since years are integers, you can use <code>Math.floor(x)</code> to convert round <code>x</code> down to the nearest whole number."
  goals:
    - To perform arithmetic using the Java programming language
  
canvasasmtid: "137429"
canvaspoints: 3
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString;
  correctcheck: |
    pos.trim() === "2038"
  incorrectchecks:
    - incorrectcheck: |
        pos.trim() === "2038.0962597349062"
      feedback: "Try again: don't forget to convert this value to an integer!"
    - incorrectcheck: |
        pos.trim() === "68.09625973490614"
      feedback: "Try again: don't forget to add this value to the epoch starting year, and convert your answer to an integer."
    - incorrectcheck: |
        pos.trim() === "68"
      feedback: "Try again: don't forget to add this value to the epoch starting year."
 
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

## Visual Debugging with Trace

It is often helpful to step through your program one line at a time to see which variables are being updated at each step of your algorithm.  You can load this problem in [Trace](https://www.learnwithtrace.com/problems/0ef85be/code), and can share your work with me in that environment using [these instructions](https://usebirch.notion.site/How-to-Share-a-Replay-in-Trace-77ecc722883b4a0a906aa3da69573c9a).

## Background
There was a lot of scare and hype leading up to the year 2000 because of the so-called ["Y2K Bug"](https://www.nationalgeographic.org/encyclopedia/Y2K-bug/). Early computers had severely limited storage space, so programmers used only 2 digits to store the year, and it was assumed that the full year would be 19XX, where XX where the two digits. But as the year 2000 approached, people realized that most software with this assumption would suddenly assume it was the year 1900, which is a particularly big problem, for example, in banking software that computes interest rates.

Due to the diligent work of countless programmers updating legacy software, this never materialized into a major crisis. However, there is an even bigger, more subtle problem lurking on the horizon. Another common scheme for storing time is so-called ["Unix Time"](https://en.wikipedia.org/wiki/Unix_time) or "Epoch Time." In this scheme, every timestamp is represented as an integer, which is the number of seconds that have elapsed since midnight on December 1, 1970. For example, the time and date of 11:59PM on Friday 2/21/2020, is `1582329540`. As you may recall, there are limits to the possible values that can be stored by different variable types. In particular, if one uses the a 32-bit integer `int` type in Java to store Unix time, this will lead to overflow within the next 20 years, and the time will suddenly jump negative back to the early 1900s. Thus, the problems will be very similar to the Y2K bug, though possibly more far-reaching (every embedded device in cars, planes, buildings, etc is at risk). I expect we will see an FDR-esque public works project to update infrastructure in the years leading up to this problem.

The largest signed 32-bit integer that can be represented is `Math.pow(2, 31) - 1 = 2147483647`.  This is because the sign requires one bit to encode, leaving 31 bits to represent the value.  The Unix operating system stores the current date and time by storing the number of seconds that have elapsed since a particular date, called the epoch.  This "epoch" date is January 1, 1970.  The Unix time data type has historically been a 32-bit signed integer (more recently, it is being expanded to a 64-bit value, for reasons that will become clear shortly!).  In this exercise \[[^1]\], you will compute the number of years represented by the maximum number of seconds that a 32-bit signed integer can store.  After adding this to the epoch start year of 1970, you will print out this value as the year in which a 32-bit Epoch counter will "overflow" and start counting upwards from the minimum 32 bit signed integer.  

Incidentally, the smallest signed 32 bit integer is `-2147483648`.  Notice that this value differs by 1 from the largest possible positive value shown above; that's because one of the `Math.pow(2, 32)` binary values must represent 0, so there is an odd number of values remaining on the number line!.

**NOTE:** A [similar problem](https://www.theverge.com/2019/3/8/18255847/gps-week-rollover-issue-2019-garmin-tomtom-devices-affected/) happens with GPS devices nearly ever 20 years (most recently in 2019), because they store the number of weeks elapsed since 1980 as a 10-bit unsigned integer. 

## What To Do
* Begin by converting `MAX_INT` from seconds into years.
* Round this value down to the nearest integer using the `Math.floor()` method.
* This is the number of years that can be counted in seconds in a standard `int` data type.  Add this to the starting year (a variable containing the  value 1970) to calculate the year in which this time measurement will overflow the `int` data type.

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie)