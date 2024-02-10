---
layout: activity
permalink: /Activities/NumberSystems
title: "CS173: Intro to Computer Science - Number Systems"


info:
  next: ./EscapeCharacters
  
  goals: 
    - To identify the number systems that represent common data types
    - To model colors according to their RGB encoding
    
  warmup: "What is the value of 255 in binary, and in hexadecimal?  How about 256?"  
  
  models:
    - model: |   
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/ASCII-Table-wide.svg/1280px-ASCII-Table-wide.svg.png" alt="ASCII Table from Wikipedia">
      title: ASCII Table
      questions:
        - What is the decimal representation for the character <code>'A'</code>?  How about the newline character <code>\n</code>?
        - What is the decimal representation for the character <code>'B'</code>?  How about the character <code>'b'</code>?  What is the difference between them?  
        - What is the difference between each corresponding capital and lowercase letter?
        - What is your name in ASCII decimal representation?  What is this in binary?
        - Write out the representation for the character <code>'B'</code> in binary, and also the character <code>'b'</code>.  How does their binary differ?
        - How do you think a <code>boolean isLowerCase(char x)</code> function might work?
        - "How large is an <code>int</code> variable in bits?  How does this compare to a <code>String</code>?"
        - "What are some ways we could specify the size of a <code>String</code>?  In other words, how can we know when the <code>String</code> is finished?"
    - model: |
        Visit this page: <a href="https://www.rapidtables.com/web/color/RGB_Color.html">https://www.rapidtables.com/web/color/RGB_Color.html</a>
      title: RGB Colors
      questions:
        - What three colors are used to define all colors on the color wheel?
        - What does every greyscale color have in common?
        - If you have one, what is the RGB value of your favorite color (or choose any color!)?  What is the  value of the red, green, and blue components in hexadecimal? What is the value in the "#" box for this color?
        - What is the largest and smallest value of red, green, and blue that you can have?
        - Given the number of possible reds, greens, and blues, how many total colors can we represent?
        - Including black and white, how many possible pure greyscale colors can we represent?
        - The complement of a color is the color computed whose red, green, and blue values would create white light when combined with the original color.  What mathematical expressions might compute the complement of a color defined in RGB?
      embed: |
        <iframe width="560" height="315" src="https://www.youtube.com/embed/3uzcN9PHZZs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        
reflective_prompts:
  - What can we do when choosing colors to better accommodate visually impaired or colorblind persons?
  
tags:
  - numbersystems
  - colors
  
---

