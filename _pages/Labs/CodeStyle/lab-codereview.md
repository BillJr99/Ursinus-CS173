---
layout: assignment
permalink: /Labs/CodeReview
title: "CS173: Intro to Computer Science - Code Style and Review"
excerpt: "CS173: Intro to Computer Science - Code Style and Review"

info:
  coursenum: CS173
  points: 100
  goals:
    - To identify good code style
    - To identify instances of code style that could be improved
    - To articulate the benefits of good and consistent coding style
  rubric:
    - weight: 60
      description: Partner Code Review Reports
      preemerging: At least one code review report is present, and the report lists at least one instance of code style and one area for improvement
      beginning: At least one code review report is present, and the report presents in detail at least two instances of code style and two areas for improvement
      progressing: At least two code review reports are present, and each report lists at least three meaningful instances of code style and three areas for improvement
      proficient: At least two code review reports are present, and each report presents in detail at least three meaningful instances of code style and three areas for improvement
    - weight: 30
      description: Code Revision
      preemerging: The code sample revision resulted in lower code quality than the original sample, but the program remained functional after the review
      beginning: The code sample was revised according to some of the feedback received, but the code revision was not an improvement to code style as identified by the reports
      progressing: The code sample was revised according to at least some of the feedback received
      proficient: The code sample was revised appropriately according to the feedback received
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions    

tags:
  - testing
  
---

In this lab, you will review a code sample from each partner in your group, identify good examples of [code style](../Style-Guide), and make recommendations for improvement.  When you receive these recommendations from each partner, implement them in your NetBeans project and submit your chosen project along with the report you received.

You will work in groups of three in this lab, so that each person will review the code of two other people, and receive feedback from two others as well.

## What to Do
Choose one of your recent NetBeans projects (a lab or an assignment), and exchange it with your partners, one-at-a-time.  You can do this by sharing your screen with them via a Zoom or Google Hangouts connection.  While your partner is reviewing your project, you can review theirs.

Write a report of at least one page for each partner's work, commenting on their coding style.  Use the style guide to inform your evaluation.  Specifically, you should highlight at least three items that were done well in terms of code readability and style, plus at least three items that could be improved.  You will be asked to make the changes from your partner's feedback, so the more detailed and specific you can be about what to do, the easier it will be for your partner (and, in turn, for you!).  

Some specific items you might seek to highlight include:

* **Indentation:** Is the use of indentation and curly braces ("brackets") consistent?  Do all code blocks (loops, conditionals, and functions) use brackets in the appropriate places?
* **Documentation:** It's important to comment your code so that there is a narrative for your reader to follow what has been implemented.  You should be able to read the code and understand each major step through its comments.  It is also important to comment each function with its purpose, input parameters, assumptions (for example, should one those parameters be a positive integer?), and return value.  
* **Control Flow:** Every non-void function should have **exactly one** `return` statement.  Set your return value throughout the function, and then return at the end.
* **Naming:** Is the capitalization of function and variable names consistent, and do those names make sense?  Single letter variable names are sometimes appropriate (like a `for` loop using `i` as its counter variable), but generally variable names should tell you something about what kind of value they take, and what its purpose is.
* **Testing:** Are test cases included with the project?  Do those test cases include a variety of inputs, including good boundary cases for the code being tested?  A good way to check for the quality of test cases is to ask yourself whether they seem to be trying to "break" the program, or "prove" that the program works.  We can't be sure that a program is perfect just because it passes some test cases, because it is not possible to test every possibility in every environment.  Because of this, it is good to think of yourself like a detective when it comes to writing test cases, and identifying as many different kinds of inputs as possible that will make the code fail.  You will write better functions if you can write them to pass those boundary tests.  Many developers even write their test cases **first** and then write the code itself; this is called [Test-Driven Development](https://en.wikipedia.org/wiki/Test-driven_development)!

When you are finished writing your reports, exchange each with the appropriate partner.  Each partner should take turns sharing their screen and allowing the other partners to discuss the code and their reports as a group together.

Remove the work you received from your partners when finished.

## A Word about Code Reviews

Sharing your code with others in a [code review](https://en.wikipedia.org/wiki/Code_review) for feedback can feel unnatural at first, since you are exposing your creative effort to others for their opinions.  Writing code is indeed a creative process, and it reveals something about the way each individual thinks about solving problems.  One important thing to remember is that the code review process does not exist to critique one's approach to problem solving; instead, the goal is to find bugs or vulnerabilities in that code, and to help elevate everyone's coding quality by discussing best practices as a group.  I remember learning programming the first time and wondering "am I really doing this correctly?"  Code review offers a peer review process that is intended not to critique your work, but rather to offer opportunities to elevate your code quality in ways you might not have considered before.  Computer Science and software development are collaborative disciplines and activities, and writing code that is easy to share with others benefits your team and your software's users.  Remember that it is not personal: it is about helping each other to make good code even better.

## Exporting your Project for Submission

When you're done, write a README for the project you modified that describes the revisions you made from the reports you received.  Also include the reports you wrote for your partners, and the reports that you received from them.  Be sure to save all your files before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.