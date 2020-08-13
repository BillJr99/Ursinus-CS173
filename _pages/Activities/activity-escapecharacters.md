---
layout: activity
permalink: /Activities/EscapeCharacters
title: "CS173: Intro to Computer Science - Escape Characters"
excerpt: "CS173: Intro to Computer Science - Escape Characters"

info:
  prev: ./DataTypes
  
  goals: 
    - To identify the use of escape characters
    - To specify the manner in which escape characters are invoked
    - To apply escape characters where needed 
  models:
    - title: "Special Characters"
      model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                System.out.print("The most damaging phrase in the language is: \"We've always done it this way!\"");
                System.out.println(" -- Grace Hopper");
            }
        }
        ]]></script> 
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
      questions: 
        - The excerpt from the above interview with Admiral Grace Hopper includes a quotation.  How can you print quotation marks to the screen without Java interpreting them as the end of your <code>String</code>?
        - Notice the use of <code>System.out.print</code> and <code>System.out.println</code>.  What's the difference between these two statements?
        - How could you revise the above program to print the entire statement using only one line of code (in other words, only one call to <code>System.out.println</code>?
    - title: "Escape Characters"
      model: |
        <div style="width: 100%; display: table; border-collapse:separate; border-spacing:5px;">
        <div style="width: 100%; display: table-row; background-color: black; color: white;">
            <div style="display: table-cell; padding:5px; width:50%; background-color: black; color: white;">
                <strong>Escape Character</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:50%; background-color: black; color: white;">
                <strong>Use</strong>
            </div>
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:50%; ">
                <code>\'</code>
            </div>
            <div style="display: table-cell; padding:5px; width:50%; ">
                Single Quote
            </div>
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:50%; ">
                <code>\"</code>
            </div>
            <div style="display: table-cell; padding:5px; width:50%; ">
                Double Quote
            </div>
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:50%; ">
                <code>\n</code>
            </div>
            <div style="display: table-cell; padding:5px; width:50%; ">
                New Line
            </div>
        </div>
        <div style="width: 100%; display: table-row; ">
            <div style="display: table-cell; padding:5px; width:50%; ">
                <code>\t</code>
            </div>
            <div style="display: table-cell; padding:5px; width:50%; ">
                Tab
            </div>
        </div>
        </div>
      questions: 
        - What happens if you print an escape character?  Does the backslash actually print?
        - Why do you think we call these &quot;escape characters?&quot;
        - What escape character do you think prints a backslash to the screen?
        - How would you print the actual characters <code>\n</code> to the screen (i.e., not a newline character, but the actual backslash and n characters)? 
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit1-Getting-Started/topic-1-2-java-intro.html	
      title: Introduction to Java
  additional_practice:
    - link: https://practiceit.cs.washington.edu/problem/view/bjp5/chapter1/s10-Shaq
      title: Shaq
    - link: https://practiceit.cs.washington.edu/problem/view/bjp5/chapter1/s15-printlnSlashes
      title: Printing Slashes

tags:
  - datatypes
  
---

