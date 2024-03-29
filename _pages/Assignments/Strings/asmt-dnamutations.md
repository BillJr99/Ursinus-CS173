---
layout: assignment
permalink: /Assignments/DNAMutations
title: "CS173: Intro to Computer Science - DNA Mutations"


info:
  coursenum: CS173
  points: 100
  goals:
    - To manipulate strings using the substring method
    - To apply string indexing in the context of iteration
    - To select and implement appropriate test cases to check boundary cases and potential off-by-one errors
    - To memory map strings on paper and to validate that mapping using the step debugger
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
    - rtitle: "Iteration Activity"
      rlink: "../Activities/Iteration"
    - rtitle: "Strings Activity"
      rlink: "../Activities/Strings"
    - rtitle: "Arrays Activity"
      rlink: "../Activities/Arrays"      
    - rtitle: "Testing Activity"
      rlink: "../Activities/Testing"
  questions:
    - "Given a <code>String</code> &quot;<code>Computing</code>&quot;, what beginning and ending indices would you pass to <code>substring</code> to retrieve the letters &quot;<code>put</code>&quot;?"
    - "Suppose you have a <code>String</code> <code>x = </code>&quot;<code>CS</code>&quot; and a String <code>y = </code>&quot;<code>173</code>&quot;.  How would you create a <code>String z</code> that combines the two strings to be <code>CS 173</code> without re-typing <code>CS</code> or <code>173</code>?"
    - "Suppose you have a <code>String x = </code>&quot;<code>hamburger</code>&quot;, and you wish to change it to &quot;<code>cheeseburger</code>&quot;.  What calls to <code>x.substring()</code> would allow you to do this?"

tags:
  - strings
  - arrays
  - iteration
  - testing
  - debugging
  
---

[Nucleic Acid (NA) Sequences](https://en.wikipedia.org/wiki/Nucleic_acid_sequence) like DNA and RNA are organic chains of phosphates and sugars that encode that encode genetic information about living things.  These chains mutate in various ways through reproduction and as a result of cellular damage (for example, through UV from sunlight).  We represent the four DNA nucleotide bases as (A)denine, (C)ytosine, (G)uanine, and (T)hymine, using the letters A, C, G, and T, respectively.  An example DNA chain might be represented as AATCC.  Here is an example RNA chain from [Wikipedia](https://upload.wikimedia.org/wikipedia/commons/c/cd/RNA-codon.png) (which uses additional nucleotide bases such as (U)racil, represented by the letter U).

![An RNA Chain from Wikipedia](https://upload.wikimedia.org/wikipedia/commons/c/cd/RNA-codon.png)

In this assignment we will restrict ourselves to DNA bases A, C, G, and T.  Each of these bases has a complement, as follows:

* The complement of A is T (and vice-versa)
* The complement of C is G (and vice-versa)

A substring of DNA bases (for example, ACTG) might appear later in the chain in the form of its complement, in reverse.  That is, the complement of ACTG is TGAC (the A became a T, the C became a G, the T became an A, and the C became a G).  In this example, ACTG is referred to as a sense, and its reversed complement is called an antisense.  When we reverse TGAC, we obtain CAGT, and this is the antisense of the sense ACTG.  A DNA chain with this sense/antisense pattern might be represented as ACTG...CAGT (with zero or more additional bases occurring in the middle).

## Part 1: Detecting Differences in NA Chains
Given two strings, compute their percentage difference, character by character.  If the lengths are different, the difference of their lengths count as differences as well.  For example, "ACCG" and "ACTG" would differ by 25%, because 1 character is different out of the 4.  "ACCG" and "ACCGT" would differ by 20%, because 1 character is different out of a possible 5 (the length of the largest string).  This can be represented as a `double` (for example, 0.25 for 25%, and 0.2 for 20%).

## Part 2: Inserting a Chain
Given an NA chain string, an NA subchain, and a position, insert the subchain into the chain.  For example, `insert("ACCG", "TT", 2)` would return "ACTTCG" (recall that the indices start at 0, so the TT occupies position 3 and 4 in the string, which are indices 2 and 3.

## Part 3: Detecting an Antisense
Next, write a function to search one NA chain for the existence of an antisense.  As a parameter, pass the sense chain whose antisense you are searching for.  Return a boolean if you find it.  This function will need to call two other functions - one to compute the complement of the sense (the "antisense"), and next function to reverse that antisense chain string.  If you do those two things first, detecting the antisense becomes a simpler matter of searching one string for another.

### An Example
For example, `public static boolean detectAntisense(String chain, String sense)` should compute the complement of `sense`, reverse the variable `sense`, and then search for `sense` in `chain`.  As a specific example, 

`detectAntisense("ACATGCTATGTA", "ACAT");`

should compute the complement of the sense `ACAT` (which is `TGTA`), and then reverse it to obtain the antisense (which is `ATGT`).  Finally, return `true` if the antisense `ATGT` is found in the `chain` (which is `ACATGCTATGTA`) -- and in this case, it is (so we return `true`)!

You can use the string `indexOf()` method to search for one String inside another.  If `indexOf` returns `-1`, meaning you did not find the antisense in the chain, return `false`.  Otherwise, return `true`.

### Looping over a String
To loop over every character of a string, you can loop as follows:

```java
for(int i = 0; i < str.length(); i++) {
    System.out.println(str.charAt(i)); // as an example, this prints every character in the string!
}
```

Or, to loop backwards (for example, to reverse a `String`), you can try this:

```java
String reversed = "";
for(int i = str.length() - 1; i >= 0; i--) { // why str.length() - 1?
    reversed = reversed + str.charAt(i); // append to the new String, one character at a time
                                         // from the end to the beginning of the original String
}
```

When manipulating string indices, it is very important to avoid off-by-one errors.  For example, the `substring(start, end)` method starts at the index `start` but ends at the index `end - 1`, which can be confusing.  Compounding the confusion is that string indices start counting at 0, like most arrays do.  From the [javadoc documentation](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#substring(int,%20int)) for `substring`, we see that the `substring(1, 5)` of "smiles" is "mile".  

If you are looping through your string, take care to stop searching not only prior to the end of the string (as you normally would), but at the point at which the substring you are searching for would run past the end of the string.  For example, if you are searching for "ACC" in "CGCTG", you could stop searching once you reach the "T", because there is no room for "ACC" to fit there.  Your loop terminating condition will be a value less than `chain.length()`, where `chain` is the sequence you're searching within (i.e., "CGCTG") - **what should it be instead (hint: it is related to `subchain.length()`, where `subchain` is the sequence you're searching for, i.e. "ACC")?**

Prior to writing your code, draw a grid representing the string you're searching for, and number the indices from 0 to the length of the string.  Then draw a grid representing the chain you're searching within (again, from 0 to the length of that chain).  Step through the search procedure on paper so that you can see the indices that you'll be working with.  **How do your indices relate to the lengths of the source and target subchains?**  This will provide you the answers you need to implement your algorithm!

### Part 3, Step 1: Computing the Complement of an NA Sense
Given an NA chain string, return a new string representing its complement.  This should be a string of the same length as the original; however, each character should be replaced with its complement.  That is, all the A's should be switched to T's (and vice-versa), and all the C's should become G's (and vice-versa).  So, the sense `ACAT` becomes `TGTA`.

**Question: why do you need to return a new string?  Since strings are represented as arrays of characters, why can't you manipulate the input string paramter directly?  Even if you could, why do you think it is a good idea to create a new string anyway?**

### Part 3, Step 2: Reversing the NA Sense
Given an NA chain string, return a new string of the same length but with all the characters reversed.  That is, "ATCG" becomes "GCTA".  You will reverse the complement of the sense that you computed in Step 1.  So, in our example, `TGTA` (the complement of the sense `ACAT`) becomes `ATGT`.

### Part 3, Step 3: Compute an Antisense
Using the two functions you just wrote to compute the complement and the reverse of a chain, write a function to compute the antisense of a given NA chain.  To do this, compute the complement of the chain, and then reverse it.  To do this, simply call the function you wrote for Step 1 to compute the complement, passing it the sense (not the original chain, but the sense you're searching for; for example, if your primary function is `detectAntisense("ACATGCTATGTA", "ACAT");`, you would compute this on `ACAT`); then, call your Step 2 function to reverse the result.

### Part 3, Step 4: Find the Antisense
Finally, determine if the antisense is located inside the chain.  So, in our example, you would search for `ATGT` in `ACATGCTATGTA`, because the sense you are seeking is `ACAT`.  You can use the `chain.indexOf()` to help you here - feel free to look it up to see how it works!

## Part 4: Removing a Chain
Given an NA chain string and an NA subchain, remove all instances of the subchain from the chain.  For example, `remove("ACCGCC", "CC")` would return "AG".

Note that Java Strings now have a method `replaceAll` that will do this for you.  I definitely encourage you to use this.  However, you may notice that these helper methods don't always exist across many of the string operations we're exploring here.  So, there is significant value in practicing with string indexing.  For full credit on this problem, implement your own replacement algorithm to accomplish this without calling a `replace` or `replaceAll` string method.  However, it would be a good idea to write a unit test that compares your results to a call to `replaceAll`, and you should feel both free and encouraged to do so!

So, to do this, you will need to read the `String` one character at a time, and determine whether the substring is equal to your subsequence.  Append the character to your result `String` if they don't match, and advance your loop counter if they do match (so that you skip those characters).  Notice that I'm not asking you to remove the characters directly from the original `String`!  Although you could do this, you will have to do some extra work to update your loop counter if you make a change to the `String`.

**Question: for the sequence `ACCGCC`, replacing the subsequence `CC`, what pairs of characters do you need to compare to `CC`?  For example, you would first check `AC`, but then what are the rest, and what are their substring begin and end indices? List out each pair of characters, and their indices.  These should give you a hint about how your loop will work.**

## Part 5: Testing

Write unit tests for each part of this assignment.  You will need more than one test case per part.  Your test cases should include boundary conditions (for example, inserting or removing to the beginning, middle, and end of a string).  Your goal is to uncover errors with your test cases.  Because of 0-indexing, and off-by-one errors, an algorithm can appear to work fine as long as you manipulate the middle of a chain, but then break when you are dealing with the beginning or end.  Even I made an error while completing this assignment that was only uncovered when I tried to execute it at the end of a chain.  These mistakes are very easy to make, and you should assume that your code contains these bugs.  Think of testing like a game: your goal is to cause your software to break (that's how we identify bugs to fix and make our software more robust!).  

**Question: What test cases would you write in order to try to do that?**

## Finishing Touches and Writeup 

Don't forget to test your program with several different inputs to help verify that things work the way you expect!  Think in terms of trying to break your program; if it's really hard to "trick" your program into getting the wrong answer, you've probably done a good job making your code robust.  

Also, check the [Style Guide](../Style-Guide) to make sure that you've written high quality code; make sure your code is "readable," well indented, uses good variable names, and includes good comments throughout the program.

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

### Exporting your Project for Submission

Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.  **Be sure to save your README file before exporting the project, so that your work is included in the submission!**