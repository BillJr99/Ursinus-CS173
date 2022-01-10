---
layout: assignment
permalink: /Assignments/DebuggingTable
title: "CS173: Intro to Computer Science - Debugging Table"
excerpt: "CS173: Intro to Computer Science - Debugging Table"

info:
  coursenum: CS173
  points: 10
  contract:
    a: 
    - "At least five new entries are made into the Debugging Table"
    - "Each entry contains a description of the error, and a brief explanation about how to fix the error"
    - "At least 80% of the explanations on how to correct the errors are correct"
    b:
    - "At least three new entries are made into the Debugging Table"
    - "Each entry contains a description of the error, and a brief explanation about how to fix the error"
    - "At least 70% of the explanations on how to correct the errors are correct"
    c:
    - "At least two new entries are made into the Debugging Table"
    - "Each entry contains a description of the error, and a brief explanation about how to fix the error"
    - "A reasonable effort is made to describe how to fix each of the errors encountered, even if the explanation is incorrect"
    d:
    - "At least one new entry is made into the Debugging Table"
    - "The entries do not contain both a description of the error and a brief explanation about how to fix the error"
    
tags:
  - debuggingtable
  
---

## Debugging Table

Please submit to your class notebook your Debugging Table.  The Debugging Table is a list of errors, which you can write down or screen-shot, along with an explanation of the error and how you fixed it.  The format is up to you, but a reasonable entry might look like this:

```
Example.java:5: error: cannot find symbol
                System.out.println(y);
                                   ^
  symbol:   variable y
  location: class Example

I had initialized a variable x in the following example, but accidentally printed a variable called y.  
Since y didn't exist, the print statement on line 5 of my Example.java file failed.  
I changed this to print x instead, and it worked!

int x = 99;
System.out.println(y);
```

You should have one such entry for each new error that you encounter.