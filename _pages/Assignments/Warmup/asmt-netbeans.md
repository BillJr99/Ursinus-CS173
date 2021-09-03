---
layout: assignment
permalink: /Assignments/NetBeans
title: "CS173: Intro to Computer Science - Introduction to Java Programming with NetBeans"
excerpt: "CS173: Intro to Computer Science - Introduction to Java Programming with NetBeans"

info:
  coursenum: CS173
  points: 50
  goals:
    - To write and execute a Java program
    - To use the NetBeans Integrated Development Environment
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 30
      description: Code Quality and Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide
      progressing: Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions
  readings:
    - rtitle: "NetBeans Video Tutorial"
      rlink: "../Modules/IDE/Module" 
    - rtitle: "Data Types Activity"
      rlink: "../Activities/DataTypes"    
      
tags:
  - introduction
  
---

In this assignment, you will create a NetBeans Java project and write a small Java program.

## Creating a New Project in NetBeans
Each program you write will begin with a new project in the NetBeans software development environment.  Follow [these instructions](../NetBeans) to create a new Java project.

## Reviewing Your First Java Program
Your new project contains at least one file that will look something like this:

```java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package myprogram;

/**
 *
 * @author bill
 */
public class MyProgram {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
    }
    
}
```

The text inside comment blocks `/*` and `*/` are called comments.  These are lines where you can write anything you'd like - a description of what you're doing, or your name, etc.  They won't execute as part of your program, so they aren't code, per se.  They're just, as the name suggests, comments.  They can span multiple lines, as you can see in three places in the example above.  Another type of comment uses this format: `//`, and anything appearing on that line after the `//` comment marker is a comment.  These are just like the `/* ... */` comments, but only span a single line.  You can see one such comment in the code above.  The word `TODO` is not an official part of Java, but programmers like to make notes where they need to go back and write some code.  In this case, it's where your code will ultimately go.

Before we write any code, though, let's look at the structure of this program.  The first real line of code is right below the first comment.  It starts with the keyword `package`.  This essentially means that this is the name of the directory in which this source code file is saved inside your project.  Every project has a directory on your hard drive, under which you can find more directories with code inside.  This is useful if you have lots of source code files, so that you can organize them by what they do to make things easier for you to find.  In our course, we'll generally have only one of these, and so there won't be a need to change this.  On the left side of your NetBeans window, you should see the name of the package with a little yellow package icon.  These have to match exactly (even the upper-case and lower-case letters must be exactly the same), so it is generally a good idea to leave this alone.  The `package` for my project was called `myprogram`, but yours might be different - that's ok, as it's just a name: stick with yours!

Inside this `package` directory is your file.  In Java, we generally call each file a `class`, and these represent modules in which your programs will be written.  We can do more than just write code inside a class, but for now, that's all we need to get started.  The name of the class should, again, match the name of the file (letter case and all).  NetBeans should have done this for you automatically, so there is likely no need to change this.  In my example, you'll see that my class is called `MyProgram` on the line that reads `public class MyProgram`.  We'll talk about what `public` means another day: for now, we can say that it means that our code can be seen by all the other files in our project, if we had more code files.  On the left side of your NetBeans window, you should see your file (mine is called `MyProgram.java`; yours might be called something else, but it will end with `.java`) under the package directory we saw earlier.

Finally, inside your class is a function called `main`.  I know that `main` is inside your class, because there are curly braces `{` and `}` following `public class MyProgram` and at the very bottom of your file: the `public static void main(String[] args)` line is in-between those braces.  We even indent the function inside to help us visually confirm this.  We'll go over what each of the words `public`, `static`, and `void` mean later (along with the `String[] args`), but you can ignore them for now.  For the moment, `main` is the name of our function, and it's where we will write our program.  We can have more than one of these functions, but we'll just have one for now.  In fact, every program you write will have at least one function, and Java will always start by running whatever code is inside of your function called `main`.  So, you'll see one of these in every program that you write!  

## Writing Your First Java Program
For now, our `main` function is empty.  It has a single comment in it, reminding us to write our program there.  

If you were to replace the line:

```java
// TODO code application logic here
```

with

```java
System.out.println("Hello World!");
```

you could click the "Run" button (it's a green triangle pointing to the right around the middle of your toolbar at the top, or you can use the "Run"->"Run Project" menu), and you'd see the text "Hello World" appear at the bottom of your NetBeans window.  Let's try writing something more interesting.

Make a new line after your `System.out.println("Hello World!");` statement, but still inside the curly braces of your `main` function.  Now, we can write another line of code  that Java will execute right after printing "Hello World!" to the screen.  We generally run one line of code at a time.  For this example, we'll write a few lines of code to compute the area of a circle using the classic formula:
<br />
<span>\\(A = \pi r^{2}\\)</span>
<br />

There are a few different pieces here.  For example, we can see that we're going to have to "square" the radius by raising it to the power of 2, and then multiply it by <span>\\(\pi\\)</span>.  We'll write code to do these one step at a time.

### Declaring a Variable
Let's declare a **variable** called `radius` to represent the radius of the circle.  A variable is a label in your program that we can associate with a value.  The value can be a number, or text, or other things we'll see later; importantly, a variable's value can change over time as its name suggests.  We can direct our program to refer to that value at any time during the program, and can update it as we like.  This allows us to, for example, change the radius of the circle, without breaking the logic of our program.  In other words, we can compute the area of any circle, as long as we know what its radius is.

Write the following code in your project, right below the print statement we wrote earlier.

```java
double radius = 10.5;
```

A variable declaration generally consists of three things.  The first is the type of value we plan to store in the variable.  Numeric values that can have decimal places are called `double` values, so we'll use the word `double` here.  The second item is the name of the variable: `radius` (this can be just about anything we want, but it's a good idea to use a descriptive name!).  Finally, we use the equals sign to set this variable to a value.  Here, I'll use the value `10.5`, but you can put any number here that you'd like.  Later, you'll see how to obtain this value from the user via the keyboard or even a file on your disk!

### Computing the Area
Now that we have our formula and a value for the radius, we can compute the area using mathemtical expressions.  We need to square the radius, and we need to multiply that by <span>\\(\pi\\)</span>.  We can do either of these steps first, but let's square the radius first.  There is a function called `Math.pow` that takes a base `a` and a power `b`, and computes <span>\\(a^{b}\\)</span>.  We could use this to compute `Math.pow(radius, 2)`, and square the radius.  

How can we save that value for use later in our program?  We can assign it to a variable!  Write the following line of code below the line where you declared the `radius` variable earlier:

```java
double area = Math.pow(radius, 2);
```

Now, we have a variable called `area`, whose value will be a numeric `double` type, and its value will be whatever number was in the `radius` variable squared.

Next, we multiply this by <span>\\(\pi\\)</span>.  We could multiply it by `3.14`, but Java gives us a more precise value of <span>\\(\pi\\)</span> that we can use as a sort of built-in variable.  It's called `Math.PI`.  Our variable `area` already contains the value of the radius squared, so we can multiply the current value of `area` by `Math.PI` to compute the final area of our circle.  Here's the line of code that you can place below the `Math.pow` line you just wrote:

```java
area = area * Math.PI;
```

Note that the `*` character means multiplication in Java, and that we didn't need the word `double` this time.  We can leave out `double` because Java already knows that `area` is a `double` - we told it a few lines ago when we declared the variable!  If you type `double area = area * Math.PI`, you'll get an error letting you know this, and you can just remove the word `double` to fix it.

### Printing the Area to the Screen
We now know the area of our circle, but how do we display it to the user?  We saw the `System.out.println` function earlier, and we can print variables just like text.  Here's the code to put right below the line you just wrote:

```java
System.out.println(area);
```

Try running it!  You should see the text "Hello World!" followed by the area of your circle.

### Improving Our Output
It's nice to print a more friendly output to the user, so that they know what this number means.  Right before the `System.out.println(area);` line, try adding this line:

```java
System.out.println("The area is: ");
```

Running this program, you should see this print out before the area.  The only trouble is that they're on two different lines.  Modify the line you just wrote to this:

```java
System.out.print("The area is: ");
```

... and you should see "The area is: " followed by the area of your circle, all on one line.  With this in mind, what do you think the `ln` in `System.out.println` means?  What happens when you leave it off and simply write `System.out.print`?

Modify your program to print the following output using additional `System.out.print` and `System.out.println` statements:

```java
The area of the circle with radius 10.5 is: 346.3605881077468
```

## Exporting your Project for Submission

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it. 