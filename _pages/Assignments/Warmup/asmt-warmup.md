---
layout: assignment
permalink: /Assignments/Warmup
title: "CS173: Intro to Computer Science - Warmup"
excerpt: "CS173: Intro to Computer Science - Warmup"

info:
  coursenum: CS173
  officehourspoll: "https://doodle.com/poll/asqc86anp5k8mm86?utm_source=poll&utm_medium=link"
  class_notebook: "https://ursinuscollege365-my.sharepoint.com/personal/wmongan_ursinus_edu/Documents/Class%20Notebooks/CS173%20Fall%202021"
  class_notebook_name: "OneNote"
  chatname: "Microsoft Teams"
  submission: "We will complete this assignment using Teams, so there is no need to write up any documentation (as we will in future programming assignments) nor is it necessary to submit anything to Canvas.  It is fine to just follow the directions in each part and send me messages as appropriate!"
  testproject:
    ziplink: "../files/asmt-warmup/HW0-master.zip"
    zipfilename: "HW0-master.zip"
    zipdirname: "HW0-master"
  vpn: false
  points: 15
  
tags:
  - introduction
  
---

The purpose of this assignment is to get us set up for the course, both by getting to know each other better, and by setting up the software environment.

## Personal Survey (5 Pts)

I gave a couple of fun facts about myself in the class, but I want to get to know you all better. So please submit answers to the following questions as a private message to me on {{ page.info.chatname }}.

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
11. Please post a short introduction and a hello to the class on the Canvas Introductions discussion forum.  There is also a Water Cooler discussion group that you can use for social discussions as well!
12.  Finally, we will be sharing work with each other through electronic means.  To protect your privacy, you are welcome to use a pseudonym on your work in lieu of your name.  Let me know if you'd like to use a pseudonym on your assignments, and what name you'll use.

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

Once you click run, the code will run, and it will print a "magic number" inside of a terminal at the botton of the Netbeans window. **Please send me a new message letting me know the value of the magic number (5 pts)**. If you are having any trouble, please post to {{ page.info.chatname }}.

## Class Resources

### Class Notebook

We will use an electronic shared notebook throughout the class.  You'll be able to take notes there, see the whiteboard notes that I create, and respond to some reflective journal prompts throughout the course.  We'll use [{{page.info.class_notebook_name}}]({{ page.info.class_notebook }}), which you can access through this link.

{% if page.info.vpn %}
### VPN

You can access the Ursinus network remotely by using a Virtual Private Network (VPN).  This is a protocol and software package that connect your computer to the Ursinus network using your login and password, allowing you to access computers and resources (like library resources) that would normally require you to be physically located on the campus network.  Please follow [these](https://www.ursinus.edu/offices/information-technology/technology-support/hardware-and-software-help/remote-connections-and-vpn/) instructions to connect to the VPN.  When submitting class exercises, you will connect to the VPN so that we can authenticate and determine which student is completing which exercise.

**If you are planning to access course materials while off-campus, for example, if you are a commuting student, please install the VPN software per the instructiosn above on your computer.  I will request that you be given access to the VPN in the beginning of the semester, so you may not have access immediately on the first day.  If you find that you are unable to connect to the VPN the first time you need it for an assignment or exercise, contact techsupport@ursinus.edu and request to be given access to the VPN at that time.**
{% endif %}

## Syllabus (5pts)

Please take a moment to familiarize yourself with [the course syllabus]({{ site.baseurl }}). Then, **please send me a third and final message on {{ page.info.chatname }} with the answers to the following questions**

1.  True/False: If you choose to work with a buddy, you are allowed to look at your buddy's code and show them your code during labs
2.  True/False: If you choose to work with a buddy, you are allowed to look at your buddy's code and show them your code for regular assignments.
3.  True/False: You may look at a classmate's code during a regular assignment.
4.  True/False: Although I can work with my buddy on labs, we cannot email or copy each other's code directly, and our submissions should be substantially unique.
<!--4.  What happens if you show up after the lecture has already started?-->
4.  Where is the help room located?
<!--5.  Extra credit (+2) Send me a selfie of yourself inside of the help room.-->
