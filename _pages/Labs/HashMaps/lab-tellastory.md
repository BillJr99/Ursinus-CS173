---
layout: assignment
permalink: /Labs/TellAStory
title: "CS173: Intro to Computer Science - Tell a Story with HashMaps"
excerpt: "CS173: Intro to Computer Science - Tell a Story with HashMaps"

info:
  coursenum: CS173
  githubclassroom:
    clonelink: "https://classroom.github.com/a/KW7gYBFu"
  points: 100
  goals:
    - To implement an arithmetic expression into executable code
    - To map variables to expression parameters
    - To identify and implement appropriate unit test cases
  rubric:
    - weight: 40
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 20
      description: Test Cases
      preemerging: Testing was performed outside of the unit test framework, or not performed at all
      beginning: Trivial test cases are provided in a unit test framework
      progressing: Test cases that cover some, but not all, boundary cases and branches of the program are provided
      proficient: Test cases that cover all boundary cases and branches of the program are provided
    - weight: 30
      description: Code Quality and Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide
      progressing: Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup)
      progressing: The program is submitted according to the directions with a minor omission or correction needed
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution

tags:
  - hashmaps
  - iteration
  
---

In this lab, you will use `HashMap`s to tell a dynamic story.  

Create a `HashMap` called `places` that define the different places you can go in your story.  These will map to a `String`.  The key `String` is the name of the place.  The second `String` (the value at that key) is a narration of your story upon entering that location.  Print this narration to the screen.

Create another `HashMap` called `moves` that gives a list of possible places one can go given the current room.  This will map to a value that is an array or an `ArrayList` of `String` values, each of which is a room key from the `places` array.  For example, `moves['courtyard']` would contain the value `'classroom'` if one can go to the classroom from the courtyard.  `courtyard` and `classroom` should each be a key in `moves` and in `places`. Print out the list of keys and the names of those locations (you can look them up in the `HashMap`).  

You should have at least 5 possible rooms, and at least 3 of those rooms should have a choice of at least 2 possible next locations.

The user will enter the next location, and you will loop until reaching the `end` key.  Add the following line to `build.gradle` to support reading `System.in` from NetBeans when using a Gradle project.

```
run.standardInput = System.in;
```

Finally, include a hash entry for `start` and `end` from which your story will begin and end.  Use an appropriate loop structure to terminate the story when the `end` key is reached.

The following template will help you get started:

```java
    public static void main(String[] args) {
        HashMap<String, String> places = new HashMap<String, String>();
        HashMap<String, String[]> moves = new HashMap<String, String[]>();

        // Create the list of rooms and narrations!
        places.put("start", "You are in a large room.");
        
        // What movements are possible between locations?  
        // There should be one key for every key in places above.
        String[] startMoves = {"start"}; // TODO: fix this to be a different set of rooms - it is an infinite loop if you can only go right back to start!
        moves.put("start", startMoves);
        
        String[] middleMoves = {"start", "end"};
        moves.put("middle", middleMoves);

        // Where are we starting the story?
        String currentRoom = "start";
        
        // TODO: write a loop that continues until currentroom is "end"
        // TODO: print out each room's story narration, and a list of possible moves from that room
        // TODO: then, prompt the user and read a string (scanner.nextLine()) that will be the next room, and repeat for that room!
        // Don't forget to print the ending story message at the end!
    }
```

Note that you should use a loop to scan over your keys to check which room you are in; that is, you should **not** have a separate `if` statement for every room that you are using!  You can loop over the keys in your `HashMap` like this:

```java
for (String room : places.keySet()) {
    // room will be the name of each room
    // and you can check if that's equal to the one the user input!
}
```

**In your README, include a graph (either a drawing or in text is fine!) that shows the progression of your rooms from one to the next.**

## Extra Credit (Up to 15%): Best Story Competition
Creativity is encouraged, but not required for a grade!  Let me know in your documentation if you'd like to demo your story to the class - I hope you do!  You will receive 7.5% extra credit for entering your submission, and the class will vote on their favorite story (the winner will receive an additional 7.5% extra credit).

## Extra Credit (10%): Conditional Rooms
Modify your program to have conditionals, in which your rooms print certain things depending on whether other conditions have been met.  For example, if you reach one room after visiting another, print something different in your story.