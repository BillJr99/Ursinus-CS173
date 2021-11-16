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
        - "The <code>Scanner</code> class also includes a function called <code>nextInt</code> which returns a numeric value from the user.  Write a program to ask the user to pick a number from 1 to 10 (again, keep prompting them until the value is within this range)!"
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        import java.nio.file.Files;
        import java.nio.file.Paths;
        import java.io.IOException;
        import java.io.FileNotFoundException;
        import java.io.File;
        import java.util.Scanner;
        
        public class Main {  
            public static void readLineByLine(String filePath) throws FileNotFoundException {
                File input = new File(filePath);
                Scanner scan = new Scanner(input);

                while(scan.hasNextLine()) {
                    String line = scan.nextLine();
                    System.out.println(line);
                }           
            }
            
            public static void main(String[] args) {
                String path = "test.txt";
                
                try {
                  readLineByLine(path);
                } catch(FileNotFoundException e) {
                  System.err.println("File not found!");
                  e.printStackTrace();
                }
            }
        }
        ]]></script>          
      title: User Input
      questions:
        - "What do you think <code>try</code> and <code>throws</code> mean?"
        - "What happens if a file path that doesn't exist (or that you don't have permission to open) is passed to your function?  Try it and find out!"
        - "What do you think <code>System.err</code> does?"
        
tags:
  - io
  - exceptions
  
---

