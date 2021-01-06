---
layout: assignment
permalink: /Labs/TellAStory
title: "CS173: Intro to Computer Science - Tell a Story with HashMaps"
excerpt: "CS173: Intro to Computer Science - Tell a Story with HashMaps"

info:
  coursenum: CS173
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

## Part 1: The Story
Create a `HashMap` called `places` that define the different places you can go in your story.  These will map to a `String`.  The key `String` is the name of the place.  The second `String` (the value at that key) is a narration of your story upon entering that location.  Print this narration to the screen.

Create another `HashMap` called `moves` that gives a list of possible places one can go given the current room.  This will map to a value that is an array or an `ArrayList` of `String` values, each of which is a room key from the `places` array.  For example, `moves["courtyard"]` would contain the value `"classroom"` if one can go to the classroom from the courtyard.  `courtyard` and `classroom` should each be a key in `moves` and in `places`. Print out the list of keys and the names of those locations (you can look them up in the `HashMap`).  

You should have at least 5 possible rooms, and at least 3 of those rooms should have a choice of at least 2 possible next locations.

**Does your end room need a moves transition to other rooms?  Why or why not?  (You could map it to an empty array if you wanted).**

The user will enter the next location, and you will loop until reaching the `end` key.  Before setting `currentRoom` to the user's next room choice (that they just entered via the `Scanner`), look up the 
`moves` `HashMap` corresponding to `currentRoom`.  This will give you an array of `String`s, with each 
`String` containing a room that you can move to from the current one.  Loop over each item of this array
and determine if the user's room entry is in the set of valid moves.  If the user's choice is not in the set of moves corresponding to the current room, continue to prompt them in a loop until they enter a valid choice.  You might wish to write a function
to assist you with this:

```public static boolean contains(String[] roomMoves, String val) {
    boolean result = false; // assume the value is not in the array, and try to find it
    
    // TODO: Loop over each String in roomMoves
    
        // TODO: if the array element is equal to val, set result to true
        
    return result;
}
```

Finally, include a hash entry for `start` and `end` from which your story will begin and end.  Use an appropriate loop structure to terminate the story when the `end` key is reached.

The following template will help you get started:

```java
    // Before you begin, put the following 1 line at the top of your program, under the "package" line
    // import java.util.HashMap
    
    public static void main(String[] args) {
        // If Java gives you a "redundant type arguments" warning, you can ignore it!
        HashMap<String, String> places = new HashMap<String, String>();
        HashMap<String, String[]> moves = new HashMap<String, String[]>();

        // TODO: Create the list of rooms and narrations! 
        // (Keep the start room, and be sure to add an end room!)
        places.put("start", "You are in a large room.");
        places.put("middle", "You are in another room."); // you are welcome to change this, it's just an example!
        
        // TODO: What movements are possible between locations?  
        // Add an array here for each room!
        // There should be one key for every key in places above.
        // Here is an example for the "start" room - it goes to a room
        // ... called "middle" or to a room called "start." 
        // ... You can decide and add more rooms or change them here.
        // Note that the name of the room must match the name of the room
        // ... you used in the places HashMap above!
        String[] startMoves = {"start", "middle"}; 
        moves.put("start", startMoves);
        
        // Here, my example "middle" room can move to the starting 
        // ... room or to the end room; again, this is just an example!
        // ... You should have one of these blocks for each of your 
        // ... places rooms that you defined above.
        String[] middleMoves = {"start", "end"}; 
        moves.put("middle", middleMoves);

        // Where are we starting the story?  (Leave this alone!)
        String currentRoom = "start";
        
        // TODO: write a loop that continues until currentRoom is "end"
        // What kind of loop do you need here?
            // TODO: inside that loop, print out each room's 
            // ... story narration, and a list of possible moves 
            // ... from that room
        
            // TODO: then, still inside the loop,
            // ... prompt the user and read a string (scanner.nextLine()) that 
            // ... will be the next room, and repeat for that room!
            
            // TODO: The room the user picks should be in the places.get(currentRoom) array,
            // ... so that only valid moves are made!  Once you get the array from the moves 
            // ... HashMap given current room user just entered, loop over that 
            // ... array of moves and determine if the "next room" that the user just entered
            // ... is in that array.  If it is not, loop and ask the user to enter a room again
            // ... until they enter a room that is in the currentRoom moves array.
        
        // TODO: Don't forget to print the ending story message at the end!
        // ... after your currentRoom loop terminates
    }
```

Note that you should use a loop to scan over your keys to check which room you are in; that is, you should **not** have a separate `if` statement for every room that you are using!  Instead, you can use the `.get(key)` method of a `HashMap` variable to get the corresponding value.  For example:

```java
String story = places.get(currentRoom);      // gets the story associated with a room
String[] nextSteps = moves.get(currentRoom); // gets the set of next moves the user can take
```

**What happens if you call `places.get` with a room that doesn't exist in your program?**

### For Additional Context: Checking String Equality
To check if two `String`s are equal, you can do this:

```java
// if they're equal
if(str1.equals(str2)) {

}

// if they're not equal
if(!str1.equals(str2)) {

}
```

### For Additional Context: Printing an Array
You won't be able to `System.out.println` an array - so you'll need to print each item in a loop.  For example:

```java
// assuming you have a String[] possibleMoves array
// you will modify this for your own variables, of course!
for(int i = 0; i < possibleMoves.length; i++) {
    System.out.println(possibleMoves[i]);
}
```

## Part 2: Graphing Your Story Rooms and Move Transitions

**In your README, include a graph (either a drawing or in text is fine!) that shows the progression of your rooms from one to the next.**

## Extra Credit (Up to 15%): Best Story Competition
Creativity is encouraged, but not required for a grade!  Let me know in your documentation if you'd like to demo your story to the class - I hope you do!  You will receive 7.5% extra credit for entering your submission, and the class will vote on their favorite story (the winner will receive an additional 7.5% extra credit).

## Extra Credit (10%): Conditional Rooms
Modify your program to have conditionals, in which your rooms print certain things depending on whether other conditions have been met.  For example, if you reach one room after visiting another, print something different in your story.

The `HashMap` does not tell you directly if you have visited a room - it just stores the data that goes with each room.  You can keep track of this in a number of ways: for example, with an integer that counts how many times you have visited a room.  Here's an example:

```java
// put this at the top of your program, 
// so that it initializes in the beginning of main()
int startRoomVisits = 0; 

// This goes in your loop, as you go from room to room!
if(currentRoom.equals("start")) {
    startRoomVisits = startRoomVisits + 1;
}
```

You can check these values inside your loop as well, and learn which room you have visited, and how many times you've been there (and what other rooms you've seen before).  If you have a lot of room, you might consider making an array or `HashMap` of these values to map them to the individual rooms for convenience!

## Submission

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](http://www.billmongan.com/Ursinus-CS173-Spring2021/Modules/IDE/Module2) describing how to write a README for your project, and how to export it.