---
layout: activity
permalink: /Activities/FileIO
title: "CS173: Intro to Computer Science - File I/O"
excerpt: "CS173: Intro to Computer Science - File I/O"

info:
  goals: 
    - To interface with the hard drive or console for user input
    - To catch exceptions and respond appropriately
    
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        import java.util.Scanner;
        
        public class Main {            
            public static String getText(String prompt, Scanner in) {
                System.out.println(prompt);
                String result = in.nextLine();
                return result;
            }
            
            public static void main(String[] args) {
                Scanner scanner = new Scanner(System.in);
                
                String name = getText("Enter your name:");
                
                System.out.println("Your name is: " + name);
            }
        }
        ]]></script>          
      title: "User Input with the <code>Scanner</code>"
      questions:
        - "What is <code>System.in</code>?"
        - "How would you use the <code>scanner</code> object to ask the user to enter their grade in the class; keep asking them to enter their grade until it is an A, B, C, D, or F."
        - "The <code>Scanner</code> class also includes a function called `nextInt` which returns a numeric value from the user.  Write a program to ask the user to pick a number from 1 to 10 (again, keep prompting them until the value is within this range!)"
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        import java.nio.file.Files;
        import java.nio.file.Paths;
        import java.io.IOException;
        
        public class Main {  
            public static String readFileBytes(String path) {
                byte[] result = new byte[1];
                result[0] = 0;
                
                try {
                    result = Files.readAllBytes(Paths.get(path));
                } catch(IOException e) {
                    System.err.println(e);
                }
                return result;
            }
            
            public static String readFileString(String path) {
                String result = "";
                try {
                    result = Files.readString(Paths.get(path));
                } catch(IOException e) {
                    System.err.println(e);
                }
                return result;
            }
            
            public static void main(String[] args) {
                String path = "test.txt";
                String contents = readFileString(path);
                byte[] byteContents = readFileBytes(path);
                System.out.println(contents);
            }
        }
        ]]></script>          
      title: User Input
      questions:
        - "What happens if a file path that doesn't exist (or that you don't have permission to open) is passed to <code>readFileString</code> or <code>readFileBytes</code>?"
        - "What is the difference between <code>readFileBytes</code> and <code>readFileString</code>?"
        
tags:
  - io
  - exceptions
  
---

