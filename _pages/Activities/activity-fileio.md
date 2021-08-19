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
        - "The <code>Scanner</code> class also includes a function called `nextInt` which returns a numeric value from the user.  Write a program to ask the user to pick a number from 1 to 10 (again, keep prompting them until the value is within this range)!"
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        import java.nio.file.Files;
        import java.nio.file.Paths;
        import java.io.IOException;
        import java.io.FileNotFoundException;
        import java.io.File;
        import java.util.Scanner;
        
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
            
            public static void readLineByLine(String filePath) {
                try {
                    File input = new File(path);
                    Scanner scan = new Scanner(input);
                    
                    while(scan.hasNextLine()) {
                        String line = scan.nextLine();
                        System.out.println(line);
                    }
                } catch(FileNotFoundException e) {
                    System.err.println("Could not find the file!");
                }            
            }
            
            public static void main(String[] args) {
                String path = "test.txt";
                String contents = readFileString(path);
                byte[] byteContents = readFileBytes(path);
                System.out.println(contents);
                
                readLineByLine(path);
            }
        }
        ]]></script>          
      title: User Input
      questions:
        - "What happens if a file path that doesn't exist (or that you don't have permission to open) is passed to <code>readFileString</code> or <code>readFileBytes</code>?"
        - "What is the difference between <code>readFileBytes</code> and <code>readFileString</code>?"
        - "What do you think <code>try</code> and <code>throws</code> mean?"
        - "What do you think <code>System.err</code> does?"
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        /* Read a CSV file given its file path, and return an ArrayList of Strings, 
         * one String per line 
         */
        public static ArrayList<String> readTextFile(String filePath) {
            ArrayList<String> lines = new ArrayList<String>();
            
            try {
                BufferedReader br = new BufferedReader(new FileReader(filePath));
                String line;
                while((line = br.readLine()) != null) {
                    // only add the line if it has non-whitespace content
                    // strip() removes leading and trailing whitespace
                    if(line.strip().length() > 0) { 
                        lines.add(line);
                    }
                }
            } catch(IOException e) { // if an error occurs, do this!
                System.err.println("Error reading CSV file!");
                
                // System.err is like System.out but is used for errors
                // This allows us to separate program output from 
                // error output.
                e.printStackTrace(System.err);
            }
            
            return lines;
        }
        ]]></script>          
      title: "Reading All Lines of a Text File"
      questions:
        - "What do you think an array is?"
        - "Using the array, what do you think this function does that the <code>readLineByLine</code> function above does not do?"
        
tags:
  - io
  - exceptions
  
---

