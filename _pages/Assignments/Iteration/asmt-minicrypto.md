---
layout: assignment
permalink: /Assignments/MiniCrypto
title: "CS173: Intro to Computer Science - Public-Key Cryptography"
excerpt: "CS173: Intro to Computer Science - Public-Key Cryptography"

info:
  coursenum: CS173
  points: 100
  goals:
    - To implement mathematical theory in the Java programming language
    - To apply library functionality from external jar files and build upon existing functionality
    - "To implement algorithms that iterate over characters in a <code>String</code> and over elements in an array"
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 10
      description: Code Indentation and Spacing
      preemerging: Code indentation and spacing are generally inappropriate or inconsistent
      beginning: Code indentation or spacing are generally appropriate but inconsistent in a few isolated instances
      progressing: Code indentation or spacing are appropriate or consistent, with minor adjustments needed
      proficient: Code indentation and spacing are appropriate and consistent
    - weight: 10
      description: Code Quality
      preemerging: Prior code quality feedback and style guide standards are not reflected in the submitted code to a great extent
      beginning: Code quality conforms to several standards in the course Style Guide, and progress is demonstrated in improving code quality from prior feedback
      progressing: Code quality conforms to the standards in the course Style Guide to a great extent, with a few identified areas of improvement
      proficient: Code quality substantially conforms to the standards in the course Style Guide
    - weight: 10
      description: Code Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program; specifically, javadoc style comments are present for some functions
      progressing: Code documentation is present that re-states the explicit code definitions
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program; specifically, javadoc style comments are present for all functions
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided, or the README file submitted is blank
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup or missing answers to written questions)
      progressing: The program is submitted according to the directions with a minor omission or correction needed, including a readme writeup describing the solution and answering nearly all questions posed in the instructions
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution and answering all questions posed in the instructions
  readings:
    - rtitle: "Mini Crypto Activity"
      rlink: "../Activities/MiniCrypto"
    - rtitle: "Strings Activity"
      rlink: "../Activities/Strings"
    - rtitle: "Iteration Activity: For Loops"
      rlink: "../Activities/Iteration/For"      
    - rtitle: "Iteration Activity: While Loops"
      rlink: "../Activities/Iteration/While"      
    - rtitle: "Iteration Activity: Do Loops"
      rlink: "../Activities/Iteration/Do"      
      
tags:
  - strings
  - iteration
  - numeric
  
---

This assignment is adapted from Prof. Mongan's assignments in communications and introductory cryptography \[[^1], [^2], [^3]\], and from the CS Unplugged Public Key Encryption lesson module \[[^4]\].

[^1]: William M. Mongan. 2012. An integrated introduction to network protocols and cryptography to high school students (abstract only). In Proceedings of the 43rd ACM technical symposium on Computer Science Education (SIGCSE ’12). Association for Computing Machinery, New York, NY, USA, 664. DOI:[https://doi.org/10.1145/2157136.2157364](https://doi.org/10.1145/2157136.2157364)
[^2]: William M. Mongan. 2011. Networking Applications, Protocols, and Cryptography with Java. Google CS4HS Workshop at the University of Pennsylvania, Philadelphia, PA.
[^3]: William M. Mongan. 2012. Networking Applications, Protocols, and Cryptography with Java. Tapia Workshop at the University of Pennsylvania, Philadelphia, PA.
[^4]: Bell, Witten, and Fellows. 1998. Computer Science Unplugged - Public Key Encryption. Available at [https://classic.csunplugged.org/public-key-encryption/](https://classic.csunplugged.org/public-key-encryption/)

## RSAMath Library
The mathematics functions used in this assignment are provided in the jar file library [rsamath.jar]({{ site.baseurl }}/files/asmt-minicrypto/rsamath.jar).  First, download the jar to a location you'll remember.  To use this jar, after creating a Java project in NetBeans as usual, right-click on the project in your left project navigation pane (you can click the `Window` menu and select `Projects` if you don't see this), and click `Properties`, as shown:

![]({{ site.baseurl }}/images/netbeans/ProjectProperties.png)

Click the `Libraries` category on the left side of the window that appears.  Then click, the `+` sign next to the word `Classpath`, and click `Add JAR/Folder`, as shown:

![]({{ site.baseurl }}/images/netbeans/LibrariesAnt.png)

Finally, navigate to the jar file you downloaded earlier, and double click on it to add it to your project.  Click OK to close the window, and you're done!  

To see which functions are available in the RSAMath library, see the [Javadoc]({{ site.baseurl }}/files/asmt-minicrypto/doc/index.html).  The `RSAMath` class is implemented in the `cs4hs11.rsalibrary` package, which you can import in your program.  *If you get an error indicating that the RSAMath methods are not static, you can create an `RSAMath` object and then call the functions on the resulting object.*  Here is a listing of the methods you'll find in this library:

![RSAMath Library Methods]({{ site.baseurl }}/images/asmt-minicrypto/javadocs.png)


## Step 1: Encrypting Characters Using A Public/Private Key that We Create

### Generate a Public/Private Key Pair
Write a function to generate a public and private key pair and print these to the screen.  Write a `main()` function to test this functionality.

A number N is prime if no number from 2 to N-1 divides evenly into it.  That is, <span>\\((N (mod \; k)) \ne 0\\)</span> for all <span>\\(k \in [2, N-1]\\)</span>.

Once you generate those prime numbers (let's call them A and B), you can generate your public key (E, C) and private key (D, C).  Recall that the value C is shared between the public and private key, and that E and C are made available to others so that they can encrypt data to you.  Your private key (D, C) is needed to decrypt those values, so you must keep the value D a secret!

To generate your public key:

1. Choose two prime numbers A and B.  Make these prime numbers at least 2 digits in length, but no more than 3 digits.  In practice, the values are much larger, but this is a demonstration.
2. Compute <span>\\(C = AB\\)</span>.  Since the ASCII table contains 128 entries (numbered 0 through 127), C should be larger than 127, so that all these characters can be represented.  If you send messages with characters from the extended ASCII table, C should be greater than 255.
3. Compute <span>\\(M = \phi(C)\\)</span> by computing `(A-1)*(B-1)`.  This will be equal to the result of the `RSAMath.totient(C)` method if your values of A and B are prime.
4. Compute E, a value co-prime to M.  The `RSAMath.coprime(M)` method can help you do this.
5. Compute D, the modular inverse of <span>\\(E (mod \; M)\\)</span>.  The `RSAMath.mod_inverse(E, M)` method can help you do this.

Here is an example:

![Key Generator]({{ site.baseurl }}/images/asmt-minicrypto/genkey.png)

So, to get started, you can compute `E` as follows:

```java
// do this import at the very top
// import cs4hs11.rsalibrary.RSAMath;

long A; // assign this to a prime number, perhaps from the Scanner or by computing one via a function
long B; // assign this to a prime number, perhaps from the Scanner or by computing one via a function
long C = A*B;

RSAMath rsa = new RSAMath();
long M = (A-1)*(B-1); // equal to rsa.totient(C), but much easier to compute! 
long E = rsa.coprime(M);
```  

## Step 2: Communicating Secret Messages to a Partner Using Only Their Public Key
Now, write a program to accept your partner's public key, and your private key.  You can exchange keys via email, on Teams, or on the board.  Accept a `String` parameter, and for each character in the `String`, obtain its ASCII value and encrypt it with your partner's public key.  Send those encrypted values to your partner.

### Encrypting a Message to Your Partner Using Their E and C Key Values

Given a public key (E and C) as parameters, write a function to encrypt a given value, and return the encrypted value.  Print this value to the screen.

Here is an example:

![Encryption Example]({{ site.baseurl }}/images/asmt-minicrypto/encrypt.png)

The `RSAMath.endecrypt(X, E, C)` function will help you to do this, by encrypting the value X using the encryption key E and C.

Your loop to obtain each character from the String will look something like this:

```java
String msg = "This is a secret message!";
int i = 0;
while(i < msg.length()) {
    // get each character from the string - the first one will be the letter T, followed by h, and so on...
    char x = msg.charAt(i); 
    
    // TODO: encrypt this character and print the encrypted value to the screen
    
    i = i + 1;
}
```

If you'd like a shortcut, you can also write the above code using a `for` loop!  Notice how it combines the initial value of `i`, the stopping value `i < msg.length()`, and the increment instruction `i = i + 1`:

```java
String msg = "This is a secret message!";
for(int i = 0; i < msg.length(); i++) {
    // get each character from the string - the first one will be the letter T, followed by h, and so on...
    char x = msg.charAt(i); 
    
    // TODO: encrypt this character and print the encrypted value to the screen
}
```

Each encrypted value X will be the ASCII value of each character in a String.  You can iterate over the characters of the string, and obtain a char value representing each character in the loop.  A char is really an integer whose value is the ASCII value of that character.  So, you can obtain the numeric ASCII value of the character by casting the `char` to a `long` (a `long` is a whole number like an `int`, but it is double the size of an `int`):

`long asciiX = (long) x; // where c is a char`

### Decrypting a Message from Your Partner Using Your D and C Key Values

Similarly, accept a private key (D and C) as parameters, write another function to decrypt a given value, and return that decrypted value.  Print it to the screen as well.  

The procedure is similar to that used to encrypt a value.  The `RSAMath.endecrypt(X, D, C)` function will help you to do this, by encrypting the value X using the encryption key E and C.  

Here is an example:

![Decryption Example]({{ site.baseurl }}/images/asmt-minicrypto/decrypt.png)

<details>
  <summary>What do you notice about the encryption and decryption functions you just wrote?  (Click to reveal)</summary>
  
  They're exactly the same!  They only differ in the input parameters (what values are used for the keys).  This is because the mathematics results in the computation of the modular inverse of the value.  The same function can be used on two different problems!
  
</details>

Given a set of integers that are values encrypted by your partner using your public key, write a program that decrypts each of those values (using a loop!) and decrypt to the original secret message.  Decide on a way to determine when you are finished so that you exit the loop nicely.  Write down how you decided to do this!  **For example, you can read each encrypted `long` value from the user keyboard using the `Scanner`, and enter a negative number to indicate that you have finished reading.  Continue reading and decrypting characters in a loop `while` the input is not negative!**

The procedure to do this is similar to that used to encrypt each character, except that the value to be decrypted is the encrypted value of the ASCII value used before, and the key is the private key (D, C) associated with the public key that was used to encrypt it.  You can cast the ASCII value you obtain as a `long` back to a char, and either print it or concatenate it with a `String`.  

**Hint: You will encrypt data using your partner's public key values `E` and `C`, and decrypt usnig your own private key values `D` and `C`.  The values of `C` will not be the same, since they are for two different keys (your partner's and your own)!**

When you decrypt a secret message using your own private key, you'll get back a `long`, as follows:

```java
long decrypted = RSAMath.endecrypt(encrypted, D, C);
```

You can convert the `long` back to a `char` for printing as follows:

```java
char decryptedChar = (char) decrypted;
```

### Test the Public/Private Key Pair by Encrypting and Decrypting Using Your Own Public and Private Key
Write test cases that encrypt values using your public key, and decrypt them using your private key, and assert that the final decrypted value matches your original input.  Also try encrypting with your private key and decrypting with your public key, to ensure that the keys are proper inverses of one another.

## Step 3: Breaking Someone's Private Key Using Only Their Public Key
Going back through the RSA algorithm, how did you compute your private key from your public key?  Since they are modular inverses of one another, you could compute the modular inverse of your partner's public key (E and C) to obtain their private key D.  

**Why is this too difficult to do in practice, when the key values are much larger?**

Since these are small keys, you can compute the Totient of C (<span>\\(M = \phi(C)\\)</span>) directly, or by computing <span>\\(M = (A-1)(B-1)\\)</span>.  Notice that these are essentially the same problem, since counting the values that are coprime to a number is effectively the same as searching for the two values that are not coprime - the factors A and B.    

Write and test a program to accept a public key.  To do this, compute your partner's private key from their public key, and test that you can obtain your own private key given your public key.  Print the private key to the screen and verify that it is correct with your partner.  This program should only accept E and C, the public key, as inputs.

Here is an example:

![Key Cracker]({{ site.baseurl }}/images/asmt-minicrypto/keycrack.png)

## Summary

As a summary, here is what to do.  You might want to write separate programs (projects) for each of these, and export and submit each of them.  It's up to you!

* Generate a key to share with the class.  Share your `E` and `C` public key with the class, but keep your `D` private key value a secret that you will use later!
* Use someone else's public key (`E` and `C`) to encrypt a secret message to them, one character at a time.  You can loop over the characters of a `String` to do this.  Share your encrypted numeric values with that person.
* When someone shares a message with you, use your own private key (`D` and `C`) to decrypt them to characters, one by one, and print them to the screen.  What message did you get?  Note that this `C` is different than the one you used to encrypt something to your classmate in the prior step: you used their `C` value instead!  Here, you are using your own value of `C`.
* Take someone's public key (`E` and `C`) and compute `M` and `D` from it.  Did it match their private key?  Why is this hard to do with actual public keys on the internet?

## Extra Credit (15 Points)

### Implement the RSAMath functions

Create your own versions of each of the functions in the RSAMath library given to you, and use those instead in your programs!

## Finishing Touches and Writeup 

Don't forget to test your program with several different inputs to help verify that things work the way you expect!  Think in terms of trying to break your program; if it's really hard to "trick" your program into getting the wrong answer, you've probably done a good job making your code robust.  

Also, check the [Style Guide](../Style-Guide) to make sure that you've written high quality code; make sure your code is "readable," well indented, uses good variable names, and includes good comments throughout the program.

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

### Exporting your Project for Submission

Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.  **Be sure to save your README file before exporting the project, so that your work is included in the submission!**

## A Note About Export Controls

Some governments, including the United States, have [export controls on cryptographic technologies](https://en.wikipedia.org/wiki/Export_of_cryptography_from_the_United_States). 
