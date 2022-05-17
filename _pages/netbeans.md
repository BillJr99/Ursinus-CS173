---
layout: default
permalink: /NetBeans
title: "CS173: Intro to Computer Science - NetBeans Software Environment"
excerpt: "CS173: Intro to Computer Science - NetBeans Software Environment"
    
---
# {{ page.title }}

This guide has been adapted from [Professor Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-tralie).

# Software Environment

We will be using the Java programming language in this class. The purpose of the class is not to become an expert in Java, but rather to use Java in the service of learning about other topics in computer science. To make this as easy as possible, we will start with an Integrated Development Environment (IDE) known as **Neatbeans**, which will make it easy to organize your projects and to run the code you write. It also has some nice tools to help you [debug]({{ site.baseurl }}#patienceanddebugging). 

Please visit these links to install the Java Development Kit (JDK) and NetBeans.  You will install the JDK first, and then NetBeans.  Most Windows and Linux users will want the **x64** downloads for each of these.

* [Java Development Kit](https://www.oracle.com/java/technologies/javase-downloads.html)
    * If you are prompted on the download page, you can select "JDK Download"
    * About halfway down the page are the download files.  You can choose the one that matches your operating system.  Most likely, it's the one that says "Windows x64 Installer" on Windows, or the one for MacOS if you are using a Mac.
    * You can find your download by opening a run dialog (Windows Key + R on Windows), typing "Downloads" in the box that appears, and hitting enter.  Double-clicking on the program you downloaded (the filename can be found on the webpage above) will start the process for you.
* [NetBeans](https://netbeans.apache.org/download/index.html)
    * If you are prompted on the download page, you can click "Download" under the "Apache NetBeans" heading.  The most recent version is generally fine.
    * It's OK if the version number is higher than the ones in the screenshots in this article, the windows and menus should be the same!

Here are a few notes to help you:

* You will need to allow the installer to make changes to your computer (the software is safe).
* It is fine to use the default location for NetBeans and the JDK.
* Please contact me if you have any difficulty installing or running NetBeans.

**NOTE:** You may also use [Eclipse](https://www.eclipse.org/downloads/packages/release/kepler/sr1/eclipse-ide-java-developers), [IntelliJ Idea](https://www.jetbrains.com/idea/download/), or the terminal (`javac` and `java`) if you are more comfortable with them, but the default option is Netbeans, and we will be working through examples in class and in labs with Netbeans.  Also, there is a [combined download of Java and NetBeans](https://www.oracle.com/technetwork/java/javase/downloads/jdk-netbeans-jsp-3413139-esa.html) in a single installer.  You are welcome to use this, but it is an older version of the software, so things might look a little different from the examples in class.

# Instructions for Creating NetBeans Projects 
<a name="newproject"></a>

To create a new project, first select `File->New Project`

![]({{ site.baseurl }}/images/netbeans/NewProject.png)

Then, select the projcet type "Java Application" under the "Java with Ant" section, and click Next

![]({{ site.baseurl }}/images/netbeans/JavaApplicationAnt.png)

Choose a location and a name for the project. You can uncheck the "Create Main Class" box unless, you want a file with an automatically generated file that runs when you click the play button for this project. But we're going to start from scratch in this example without a main

![]({{ site.baseurl }}/images/netbeans/ProjectNameAnt.png)

When you create a new project for the first time, NetBeans may prompt you to complete the installation of some software or to "resolve the project" (which configures it to run on your computer).  This is a one-time occurrence, if you even see this at all, and you can allow it to do so if asked.

Once the project has been created, you can make a new class by right clicking on default projects and clicking `New->Java Class`. This will create a new Java file with the name of the class you've chosen

![]({{ site.baseurl }}/images/netbeans/NewJavaClass.png)

Starting a new class like this without a package that you've chosen will create a completely empty class definition. We have to add some methods to it ourselves, including a main if we want it to do something when we right click on it and type "run." For now, we'll add a public static method that returns true if an integer is even and false otherwise:

![]({{ site.baseurl }}/images/netbeans/ClassWithMethod.png)

## Good Coding Style, Testing, Debugging, and Exporting Your Projects
We will use these tools later in the semester, so you can skip them the first time you're installing the software.  However, I'll include some guides here for when the time comes.

### Writing with Good Coding Style with Help from the CheckStyle NetBeans Plugin

Significant emphasis is placed upon [good coding style]({{ site.baseurl }}/Style-Guide) as we introduce the fundamental concepts of software development.  [Here is an article on using CheckStyle]({{ site.baseurl }}/NetBeans/CheckStyle), a plugin that will automatically scan your code as you write it and make recommendations about how to improve the quality of your code.

### Writing Test Cases

An important aspect of writing software is testing our code.  We will learn to do this during the class, and use the integrated unit test software built into Java and NetBeans. [Here is an article on using JUnit]({{ site.baseurl }}/NetBeans/JUnit), the unit testing framework.

### Using the Debugger

In addition to testing, NetBeans includes a debugger that can help identify errors in your code (especially when a test case fails!).  Here is an [article]({{ site.baseurl }}/NetBeans/Debugging) on using the NetBeans debugger for your projects.

### Exporting To Zip

If you want to export your whole project to a zip, go to `File->Export Project->To ZIP`

![]({{ site.baseurl }}/images/netbeans/ExportToZip.png)

Save your file with a `.zip` extension (that is, `MyProject.zip`).  You can click `Browse` on the export dialog to choose a location like your Desktop.

# Apporto
The NetBeans IDE software is also installed on Apporto, which can be reached from the cloud.  Here are [instructions](https://www.ursinus.edu/live/files/3550-apporto-instructionspdf) on how to access the software through Apporto.
