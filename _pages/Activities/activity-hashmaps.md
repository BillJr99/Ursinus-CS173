---
layout: activity
permalink: /Activities/HashMaps
title: "CS173: Intro to Computer Science - HashMaps"
excerpt: "CS173: Intro to Computer Science - HashMaps"

info:
  goals: 
    - To identify the key-value relationship of the <code>HashMap</code>
    - To use generic data types with Generic container classes
    
  models:
    - model: |
       <a title="Larousse / Public domain" href="https://commons.wikimedia.org/wiki/File:Nouveau_Dictionnaire_Larousse_page.JPG"><img width="512" alt="Nouveau Dictionnaire Larousse page" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Nouveau_Dictionnaire_Larousse_page.JPG/512px-Nouveau_Dictionnaire_Larousse_page.JPG"></a> 
       <br>
       <a title="© 2010 by Tomasz Sienicki [user: tsca, mail: tomasz.sienicki at gmail.com] / CC BY (https://creativecommons.org/licenses/by/3.0)" href="https://commons.wikimedia.org/wiki/File:Telefonbog_ubt-1.JPG"><img width="512" alt="Telefonbog ubt-1" src="https://upload.wikimedia.org/wikipedia/commons/d/d3/Telefonbog_ubt-1.JPG"></a>
      title: "Data Maps"
      questions:
        - "Consider the dictionary and phone book above.  When you look something up in each of them, what are you looking up, and what are you looking <strong>for</strong>?  What are the data types?"
        - What are some ways that we make these lookups easier?  How are the data organized, and what part of the data is organized that way?  
        - A phone book maps ______ to ______, and a dictionary maps ______ to ______.
        - In computing, we tend to say that we map keys to values.  For the phone book and dictionary, what is the key, and what is the value?
    - model: |         
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[   
        import java.util.HashMap;
        
        public class Main {
           public static void main(String[] args) {
                HashMap<String, String> courses = new HashMap<String, String>;
                courses.put("CS173", "Prof. Mongan");
                courses.put("CS174", "Prof. Tralie");
                courses.put("CS274", "Prof. Schilling");
                
                System.out.println("CS173 is taught by: " + courses.get("CS173"));
                
                for(String key: courses.keySet()) {
                    System.out.println(key + " is taught by: " + courses.get(key));
                }
           }
        }
        ]]></script>       
      title: "The <code>HashMap</code>"
      questions:
        - What is different about the data type that defines the <code>HashMap</code> variable in this program?  What do the extra parameters mean?
        - What would you change in the program above to store the number of students enrolled in each course, instead of the instructor of each course?
        - What other types of data could you represent with a <code>HashMap</code>?
        - "Suppose you are developing a web browser that accesses web pages.  You want to <strong>cache</strong> the pages, so that you only access them once, to save on I/O, network calls, and your data plan.  How might a <code>HashMap</code> help you to do this?  What would be the key and the value?"
    - model: |         
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[   
        import java.util.HashMap;
        
        public class Main {
           public static void main(String[] args) {
                HashMap<String, HashMap<String, String>> browserCache = new HashMap<String, HashMap<String, String>>();
                
                HashMap<String, String> data = new HashMap<String, String>();
                data.put("date", "August 17, 2020");
                data.put("page", "<html><body>Hello!</body></html>");
                
                browserCache.put("www.ursinus.edu", data);
           }
        }
        ]]></script>       
      title: "A Complex <code>HashMap</code>"
      questions:
        - What is <code>browserCache</code> mapping?
        - What is the purpose of the additional <code>HashMap</code>?
        
tags:
  - hashmaps
  - containers
  
---

