---
layout: assignment
permalink: /Labs/TellAStory/HashMap
title: "CS173: Intro to Computer Science - Tell a Story with HashMaps"


info:
  coursenum: CS173
  points: 100
  goals:
    - "To use a <code>HashMap</code> to associate keys with values"
    - To use a loop to input validated user data
    - To search an array for a value, and determine if that value is contained by the given array
    - To loop over and print values from an array
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 10
      description: Code Indentation and Spacing
      preemerging: Code indentation and spacing are generally inappropriate or inconsistent
      beginning: Code indentation or spacing are generally appropriate but inconsistent in a few isolated instances
      progressing: Code indentation or spacing are appropriate or consistent, with minor adjustments needed
      proficient: Code indentation and spacing are appropriate and consistent
    - weight: 10
      description: Code Quality
      preemerging: Prior code quality feedback and style guide standards are not reflected in the submitted code to a great extent
      beginning: Code quality conforms to several standards in the course Style Guide, and progress is demonstrated in improving code quality from prior feedback
      progressing: Code quality conforms to the standards in the course Style Guide to a great extent, with a few identified areas of improvement
      proficient: Code quality substantially conforms to the standards in the course Style Guide
    - weight: 10
      description: Code Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program; specifically, javadoc style comments are present for some functions
      progressing: Code documentation is present that re-states the explicit code definitions
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program; specifically, javadoc style comments are present for all functions
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided, or the README file submitted is blank
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions
  readings:
    - rtitle: "Strings Activity"
      rlink: "../Activities/Strings"  
    - rtitle: "Iteration Activity"
      rlink: "../Activities/Iteration"
    - rtitle: "HashMaps Activity"
      rlink: "../Activities/HashMaps"
  questions:
    - "What would happen if you tried to look up a room that does not exist in your <code>places</code> map?  Try it to be sure!"
    - "What would happen if you tried to look up a room called <code>middle</code> when your <code>places</code> map contains a room called <code>Middle</code> instead?  Try it to be sure!"
    
tags:
  - hashmaps
  - iteration
  - arrays
  - strings
  
---

In this lab, you will use `HashMap`s to tell a dynamic story.  

## Part 1: The Story
Create a `HashMap` called `places` that define the different places you can go in your story.  These will map to a `String`.  The key `String` is the name of the place.  The second `String` (the value at that key) is a narration of your story upon entering that location.  Print this narration to the screen.

Create another `HashMap` called `moves` that gives a list of possible places one can go given the current room.  This will map to a value that is an array or an `ArrayList` of `String` values, each of which is a room key from the `places` array.  For example, `moves.get("courtyard")` would contain the value `"classroom"` if one can go to the classroom from the courtyard.  `courtyard` and `classroom` should each be a key in `moves` and in `places`. Print out the list of keys and the names of those locations (you can look them up in the `HashMap`).  

Here is an example table illustrating what a `places` map might look like (note that each value is a `String`!):

|    key    |            value           |
|:---------:|:--------------------------:|
| start     | This is the starting room! |
| classroom | I am in a classroom!       |
| courtyard | Welcome to the courtyard!  |
| end       | The end!                   |

Here is an example table illustrating what a corresponding `moves` map might look like (note that each value here is a `String[]` array, and that the keys and values here are the same as the keys in the `places` map!):

|    key    |            value               |
|:---------:|:------------------------------:|
| start     | {"classroom", "courtyard"}     |
| classroom | {"start", "courtyard", "end"}  |
| courtyard | {"start", "classroom", "end"}  |
| end       | {}                             |

At the bottom of the page, you'll see a nice diagram illustrating this `moves` map.  **You should have at least 5 possible rooms, and at least 3 of those rooms should have a choice of at least 2 possible next locations.**

**Does your end room need a moves transition to other rooms?  Why or why not?  (You could map it to an empty array if you wanted).**

The user will enter the next location, and you will loop until reaching the `end` key.  Before setting `currentRoom` to the user's next room choice (that they just entered via the `Scanner`), look up the 
`moves` `HashMap` corresponding to `currentRoom`.  This will give you an array of `String`s, with each 
`String` containing a room that you can move to from the current one.  Loop over each item of this array
and determine if the user's room entry is in the set of valid moves.  If the user's choice is not in the set of moves corresponding to the current room, continue to prompt them in a loop until they enter a valid choice.  You might wish to write a function
to assist you with this:

```java
public static boolean contains(String[] roomMoves, String val) {
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

### Summary: What To Do
1. Create a `HashMap` of places that your story will contain.  This will map a room location to the story narrative that should display when the user arrives in that room.  You can lookup this map based on the `currentRoom` variable, and print the resulting value, to tell the story!
2. Create a `HashMap` of moves that maps each place in the array of places that you can move to next.  You'll print the contents of this array after you print the story narrative, to invite the user to input where to go next.  **Hint: the place names must match the ones you used in the first map of story places!  This is case sensitive, so if you call a place `dorm` in the first `HashMap`, you must call it `dorm` in this one, too.**
3. Allow the user to enter one of these places to go to next.  Make sure that place is in the array of places that you can go from the current room.  If the user enters a place that is not in the set of valid places, continue asking the user where to go next.  **What kind of loop should you use for this? Hint: this loop should go inside your outer story loop!**
4. Repeat steps 1 through 3 until `currentRoom` is equal to `end`.  **Hint: Don't forget to print the story message that goes with the `end` place!  You may need to print this outside of the loop, if your loop terminates as soon as the `currentRoom` variable becomes `end`.**

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
You won't be able to `System.out.println` an array - so you'll need to print each item in a loop.  If you print an array variable directly, you might see an output like this: `[I@76ed5528`.  This means that the variable is an integer array beginning at memory address `0x76ed5528`.  Instead, you should print each value of the array, one element at a time.  That's exactly what a loop is for! Here's how to do it:

```java
// assuming you have a String[] possibleMoves array
// you will modify this for your own variables, of course!
for(int i = 0; i < possibleMoves.length; i++) {
    System.out.println(possibleMoves[i]);
}
```

## Part 2: Graphing Your Story Rooms and Move Transitions

**In your README, include a graph (either a drawing or in text is fine!) that shows the progression of your rooms from one to the next.**

Here is an example diagram from my story example above:

![Story State Diagram](../images/lab-tellastory/state-diagram.png)

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

## Finishing Touches and Writeup 

Don't forget to test your program with several different inputs to help verify that things work the way you expect!  Think in terms of trying to break your program; if it's really hard to "trick" your program into getting the wrong answer, you've probably done a good job making your code robust.  

Also, check the [Style Guide](../Style-Guide) to make sure that you've written high quality code; make sure your code is "readable," well indented, uses good variable names, and includes good comments throughout the program.

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

### Exporting your Project for Submission

Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.  **Be sure to save your README file before exporting the project, so that your work is included in the submission!**