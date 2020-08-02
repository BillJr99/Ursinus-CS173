---
layout: assignment
permalink: /Assignments/Warmup
title: "CS173: Intro to Computer Science - Warmup"
excerpt: "CS173: Intro to Computer Science - Warmup"

info:
  coursenum: CS173
  officehourspoll: "https://www.when2meet.com/?9311271-8GY4a"
  testproject:
    ziplink: "../files/asmt-warmup/HW0-master.zip"
    zipfilename: "HW0-master.zip"
    zipdirname: "HW0-master"
  points: 15
  
tags:
  - introduction
  
---

The purpose of this assignment is to get us setup for the course, both by getting to know each other better, and by setting up the software environment.

## Personal Survey (5 Pts)

I gave a couple of fun facts about myself in the class, but I want to get to know you all better. So please submit answers to the following questions as a private message to me on GroupMe

1.  Your Name, Your Nickname (if applicable) / Preferred Pronouns
2.  What is your reason for taking the course? (Blunt honesty is perfectly fine here, if applicable)
3.  What are you majoring in / interested in majoring in?
4.  What do you think you might want to do after Ursinus?
5.  Have you had any experience with computer science / programming? (It's okay if you haven't!)
6.  What are you most excited about in this course?
7.  What are you the most worried about in this course?
8.  A fun fact about yourself
9.  Anything else you think I should know?
10.  Please attach **a headshot** picture to your message. I will use this to help get to know your name, but we will also use this in class to arrange groups.

## Web Poll for Office Hours

You will not be graded on this, but I want to setup my office hours so that everyone can make at least one of them. Please [click here]({{ page.info.officehourspoll }}) and select every block in which you can attend at least 30 minutes in your schedule. You may use a pseudonym or post anonymously if you wish.

## Software Environment (5 pts)

Please follow [the directions on the software page](../NetBeans) to install Netbeans and the CheckStyle plugin on your computer (alternatively, as stated on the software page, you may use Eclipse or IntelliJ). Once you have Netbeans installed, [click here]({{ page.info.testproject.ziplink }}) to download some code that we will use to test it. Save it somewhere on your computer that you know where to find it (the easiest way to do this in most browsers is to right click on the link and select "save as"). It is recommended that you make a folder that you use to place all of your {{ page.info.coursenum }} work in one place. As an example, I will create such a folder on my desktop named `{{ page.info.coursenum }}`, and I will copy the file I just downloaded into it. Next, you will want to _extract_ the contents of the file you just downloaded into the folder. For example, on Windows, I would right click on `{{ page.info.testproject.zipfilename }}` and click extract, and put the following into this dialog that pops up:

![]({{ site.baseurl }}/images/asmt-warmup/Extract.png)

Note that the default option is to extract to `{{ page.info.coursenum }}/{{ page.info.testproject.zipdirname }}`, but if you do this, it will create a folder within a folder (not the end of the world, but it makes things a little messy).

Next, open Netbeans and go to `File->Open Project` and navigate to the folder you just extracted. Then, open the project `{{ page.info.testproject.zipdirname }}`

![]({{ site.baseurl }}/images/asmt-warmup/OpenProject.png)

Next, expand `Source Packages -> hw0` and double click on `GoodCode.java`. Once you've done this, click the green play button (circled in red in the picture below) to compile and run the code.

![]({{ site.baseurl }}/images/asmt-warmup/GoodCode.png)

Once you click run, the code will run, and it will print a "magic number" inside of a terminal at the botton of the Netbeans window. **Please send me a new message letting me know the value of the magic number (5 pts)**. If you are having any trouble, please post to GroupMe.

## Syllabus (5pts)

Please take a moment to familiarize yourself with [the course syllabus]({{ site.baseurl }}). Then, **please send me a third and final message on GroupMe with the answers to the following questions**

1.  True/False: If you choose to work with a buddy, you are allowed to look at your buddy's code and show them your code during labs
2.  True/False: If you choose to work with a buddy, you are allowed to look at your buddy's code and show them your code for regular assignments.
3.  True/False: You may look at any classmate's code during a regular assignment.
4.  What happens if you show up after the lecture has already started?
5.  Where is the help room located?
6.  Extra credit (+2) Send me a selfie of yourself inside of the help room.
