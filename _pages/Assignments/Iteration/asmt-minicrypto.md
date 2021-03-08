---
layout: assignment
permalink: /Assignments/MiniCrypto
title: "CS173: Intro to Computer Science - Public-Key Cryptography"
excerpt: "CS173: Intro to Computer Science - Public-Key Cryptography"

info:
  coursenum: CS173
  points: 100
  goals:
    - To relate the mathematics of modern encryption systems to applied principles of information hiding
    - To implement mathematical theory in the Java programming language
    - To apply library functionality from external jar files and build upon existing functionality
    - To implement algorithms that iterate over characters in a string and over elements in an array
  rubric:
    - weight: 60
      description: Algorithm Implementation
      preemerging: The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run
      beginning: The algorithm fails on the test inputs due to one or more minor issues
      progressing: The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation
      proficient: A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case
    - weight: 30
      description: Code Quality and Documentation
      preemerging: Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide
      beginning: Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide
      progressing: Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide
      proficient: Code is documented at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide
    - weight: 10
      description: Writeup and Submission
      preemerging: An incomplete submission is provided
      beginning: The program is submitted, but not according to the directions in one or more ways (for example, because it is lacking a readme writeup)
      progressing: The program is submitted according to the directions with a minor omission or correction needed
      proficient: The program is submitted according to the directions, including a readme writeup describing the solution    
  readings:
    - rtitle: "Strings Activity"
      rlink: "../Activities/Strings"
    - rtitle: "Iteration Activity"
      rlink: "../Activities/Iteration"      
      
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

## An Unplugged Activity
If you had to pass secret messages around the room, but had to do so by passing notes to the people immediately adjacent to you, how could you go about "securing" the messages so that only your partner at the other side of the room could read your note?  You and your partner would have to agree on some encoding for the message.  Many such encodings exist:

* [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
* [One-Time Pad](https://en.wikipedia.org/wiki/One-time_pad)
* [Linear Feedback Shift Register](https://en.wikipedia.org/wiki/Linear-feedback_shift_register)
* [The Enigma Machine](https://en.wikipedia.org/wiki/Enigma_machine)

One limitation is that you and your partner must agree upon the details of the encoding.  But how do you exchange that information?  You'd have to pass it through your neighbors again, and thus would not be a secret.  Public Key Cryptography provides us with mechanisms by which we can generate a key (a basis for an encoding), and make just enough information about it publicly available that others can use it to secure messages to us.  Everyone gets to see this information - it's enough to encrypt a message, but, amazingly, it's not enough to decrypt it!  Often, these cryptosystems are used to generate and send symmetric keys like the ones above, and this is the subject of secure [Key Exchange](https://en.wikipedia.org/wiki/Key_exchange) algorithms.

We need a scheme whereby the sender can know something public - everyone can know it!  Knowing the public part tells you nothing about how to decode a message, but actually allows you to encode the message for the recipient to secretly decode.  The secret is never shared, so it is never transmitted.  How can we do this?  The idea is to generate a piece of information that contains the mechanism for encryption and decryption, but in such a way that it is very difficult to extract that mechanism - this is akin to extracting the original ingredients from a stew.  For example, William Stanley Jevons proposed in 1874 that it is very difficult to identify two numbers that, when multiplied together, would result in [Jevons's Number: 8,616,460,799](https://en.wikipedia.org/wiki/William_Stanley_Jevons#Jevons's_number).  Given enough time, you might determine that the two numbers are 89,681 and 96,079 (which each happen to be prime numbers, so there are no other factors aside from Jevons's Number itself and 1); however, you could imagine this becoming more and more difficult as the target number gets larger and larger.  As another example, we could use difficult-to-compute graph algorithms like the [Vertex Cover](https://en.wikipedia.org/wiki/Vertex_cover) problem as shown in this [example](https://classic.csunplugged.org/wp-content/uploads/2014/12/unplugged-18-public_key_encryption_0.pdf).

Try sending a message to a classmate.  Every character in your word is a number, according to the American Standard Code for Information Interchange (ASCII) table below.  As a CS-Unplugged style example, come up with a set of 16 numbers that add up to one of your ASCII values, and put those numbers randomly on the map, labeling each vertex.  This is easy to break, though, since the original value is just the sum of these numbers!  Instead, take each vertex and its neighbors (there should be 4 nodes each), add up those numbers, and replace each vertex with that sum.  Erase or start a new map so that the original numbers can't be seen.  Give that resulting map to another student.  Can your classmate decode the message?  They should not be able to.  Now give it to the student with the private map (the solution to the vertex cover problem - which is difficult to compute, but gives the set of nodes that together touch all the other nodes exactly once).  That student adds up only the values on the larger vertices, which is the sum of the values of each node plus the nodes they touch (which is all of them, because they're the vertex cover nodes!), yielding the original ASCII value.  Your partner can easily decode the message.  This works by carefully constructing the map such that the highlighted vertices on the private map consist of the nodes that touch all vertices on the graph exactly once.  This can be a difficult problem to solve if it is not provided in advance.  It is breakable, though, using high school math techniques (systems of equations), in which t(i) = some partial sum of vertex values, knowing the summed values of the vertices and the neighbors on the map.  Nevertheless, it is a start.  We need another problem that is easy to set up but hard to break without the key.

![ASCII Table from Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/ASCII-Table-wide.svg/1280px-ASCII-Table-wide.svg.png)

### Another Example: The Knapsack Problem

A [similar exercise](https://nrich.maths.org/2199) can be accomplished with an actual cryptosystem using the [Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem).  This system was devised by Whitfield Diffie, Martin Hellman, and Ralph Merkle and is known as the [Merkle-Hellman Knapsack Cryptosystem](https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem).  It was broken by Adi Shamir, who is the "S" (along with Ron Rivest and Leonard Adleman) in the [RSA Cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) that we will explore in this assignment!  Diffie, Hellman, and Merkle also developed the [Diffie-Hellman Key Exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) algorithm (although they may not have been the first to do so) for exchanging keys over an insecure channel.

Try generating a public/private key and a message using the [Merkle Hellman Knapsack Cryptosystem](https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem#Example).

## Using the Product of Large Prime Numbers for Public and Private Keys
We will generate a public key (that we share with the public, like our map with the number sums filled in above), and a private key (that we keep to ourselves, like the solution to the Vertex Cover problem that extracts the secret meaning from our encrypted message), using the RSA Cryptosystem.  This system is based upon the product of two large prime numbers.  The private key relies on the idea that it is very difficult to obtain the original prime factors from these large products.  

Notice that many problems such as the map and the knapsack relied on modular arithmetic, using things that you've seen in school like "coprime" and "gcd."  Another difficult problem is factoring large numbers and finding large prime numbers.  How did we get the modular inverse of 588 mod 881?  It's because we made sure that they were coprime to each other.  Given numbers that don't have any factors (3 and 7, 9 and 25) in common, what's their gcd?  1 is the only number that divides them both.  This means that we can find a modular inverse of the one number mod the other number, because there exists a number <span>\\(r^{-1}\\)</span> (in this case, <span>\\(r^{-1}\\)</span> is known as the [Modular Inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse), not the traditional arithmetic inverse) such that <span>\\(rx = 1 (mod \; p)\\)</span>.

Some interesting relationships in mathematics (called [Fermat's Little Theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)) show us that when two numbers are coprime, we can compute the modular inverse of their product r: <span>\\(r^{-1} = r^{\phi(M) - 1} (mod \; M)\\)</span>.  <span>\\(\phi(M)\\)</span> is known as [Euler's Totient Function](https://en.wikipedia.org/wiki/Euler%27s_totient_function), and it is simply a count of the number of integers 1 <= k < M that are coprime to m.  <span>\\(\phi(24) = 8\\)</span> (because the totatives of 24 are 1,5,7,11,13,17,19,23).  So for r = 588 and q = 881, as in the [Knapsack Example](https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem#Example), we can compute the modular inverse of 588 (mod 881) as follows: <span>\\(588^{-1} = 588^{\phi(881)-1} (mod \; 881)\\)</span>.  Unfortunately, it is very difficult to compute <span>\\(\phi(M)\\)</span>, and therein lies the secret!  If you generate r by multiplying together two large prime numbers that you already know (this is why [finding large prime numbers](https://en.wikipedia.org/wiki/Largest_known_prime_number) is an interesting problem!), you can generate a number for which it is too difficult to compute Euler's Totient.  You can very easily compute the Totient with a loop that counts all values from 2 to C, and increments a counter if the greatest common divisor of each value and C is 1.  Thus, you (and probably only you) can compute the modular inverse of values mod <span>\\(M = \phi(C)\\)</span>.  

For now, we can look up <span>\\(\phi(881)\\)</span> on a website like [http://primefan.tripod.com/TotientAnswers1000.html](http://primefan.tripod.com/TotientAnswers1000.html), but it turns out that 881 is prime, meaning that no numbers greater than 1 other than itself divide into it.  So this means <span>\\(\phi(881) = (881 - 1) = 880\\)</span> (the other 880 numbers).  So <span>\\(588^{-1} = 588^{880-1} (mod \; 881) = 588^{879} (mod \; 881) = 588^{879} (mod \; 881)\\)</span>.  That's <span>\\(1.917e+2434 (mod \; 881)\\)</span>, or 442.  See how much easier that makes the problem above to solve?  Yet, it's harder for those that don't know the base number r and the modular inverse q, so we keep those secret.  Instead, we give our partner(s) enough information to generate encrypted values to us that we can decrypt using this approach.

To generate RSA keys, first select two prime numbers A (say, 47) and B (say, 71).  Normally, A and B should be very large -- a small map was easy to break, after all!  Multiply them together and call that <span>\\(C = AB = 47 \times 71 = 3337\\)</span>.  

Now compute <span>\\(\phi(C) = \phi(AB) = 3220\\)</span>, and call this number (the totient of C) M.  Pick an encryption key that is coprime to <span>\\(M = 3220\\)</span>.  There are mathematical ways of doing this (the [Extended Euclidean GCD Algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)), but let's just pick one since we're using small enough numbers -- how about 79.   Take my word for now that it is easy to do, especially with a computer.  Call this <span>\\(E = 79\\)</span>.

The decryption key is the modular inverse of the encryption key <span>\\(E  (mod \; 3220)\\)</span>.  Call this <span>\\(d = 79^{-1} = 79^{\phi(3220)-1} (mod \; 3220)\\)</span>.  Recall how to do this (keep in mind that 79 is coprime to M = 3220 -- what a great idea, because we can use our formula!).  So <span>\\(r^{-1} = r^{\phi(M) -1} (mod \; M)\\)</span> works.  According to [http://www25.brinkster.com/denshade/totient.html](http://www25.brinkster.com/denshade/totient.html), <span>\\(\phi(M) = 1056\\)</span>, but we could compute it.  So now we have <span>\\(79^{-1} = 79^{1056 - 1} (mod \; 3220) = 791055 (mod \; 3220) = 1019\\)</span>.

The encryption key <span>\\(C = 3337\\)</span> and <span>\\(e = 79\\)</span> make up the public key.  The private key is <span>\\(d = 1019\\)</span> and <span>\\(C = 3337\\)</span>.  If we want to send the value 688, we compute <span>\\(688^{79} (mod \; 3337) = 1570\\)</span>.  To decrypt it, take <span>\\(1570^{1019} (mod \; 3337) = 688\\)</span>.  It actually works the other way, too.  We can encrypt with the private key and decrypt with the public key.  It all works because of the modular properties of relatively prime numbers. They easily "undo" each other, but it's hard to reconstruct one number from the other.  

<details>
  <summary>But why would we ever want to do that?  What value would we gain by being the only person who could encrypt something (with our private key) that the whole world could decrypt (with our public key)?  (Click to reveal)</summary>
  
  The information would not be private, because anyone could decrypt it.  However, the public could be sure that you were the only person that could have generated that data.  If we submit a document, and an exact copy of the document encrypted with our private key, the public could decrypt it and verify that it matches the non-encrypted document we sent out.  This is the basis of a digital signature!
  
</details>

The idea is that 1019 is very difficult to find even knowing <span>\\(e = 79\\)</span> and <span>\\(C = 3337\\)</span>.  That's because we'd need to be able to factor 3337 into two numbers that, when one is subtracted from each and multiplied together, give 3220 -- such that 79 is relatively prime to that number.  If factoring was easy, we could try every number until we found it.  Luckily, it isn't so easy.   Still, cryptosystems are subject to attacks similar to those you do in the newspaper, and there are some tricks (padding, salting) to dealing with that.  What would you do?  Some devices like RSA keys generate RSA values every minute.  This is because we believe that even if these numbers can be factored, it would take more than a minute to do so, and thus the security maintained.

## RSAMath Library
The mathematics functions used in this assignment are provided in the jar file library [rsamath.jar]({{ site.baseurl }}/files/asmt-minicrypto/rsamath.jar).  First, download the jar to a location you'll remember.  To use this jar, after creating a Java project in NetBeans as usual, right-click on the project in your left project navigation pane (you can click the `Window` menu and select `Projects` if you don't see this), and click `Properties`, as shown:

![]({{ site.baseurl }}/images/netbeans/ProjectProperties.png)

Click the `Libraries` category on the left side of the window that appears.  Then click, the `+` sign next to the word `Classpath`, and click `Add JAR/Folder`, as shown:

![]({{ site.baseurl }}/images/netbeans/LibrariesAnt.png)

Finally, navigate to the jar file you downloaded earlier, and double click on it to add it to your project.  Click OK to close the window, and you're done!  

To see which functions are available in the RSAMath library, see the [Javadoc]({{ site.baseurl }}/files/asmt-minicrypto/doc/index.html).  The `RSAMath` class is implemented in the `cs4hs11.rsalibrary` package, which you can import in your program.  *The methods are not static, but you can create an `RSAMath` object and then call the functions on the resulting object.*  Here is a listing of the methods you'll find in this library:

![RSAMath Library Methods]({{ site.baseurl }}/images/asmt-minicrypto/javadocs.png)


## Step 1: Encrypting Characters Using A Public/Private Key that We Create

### Generate a Public/Private Key Pair
Write a function to generate a public and private key pair and print these to the screen.  Write a `main()` function to test this functionality.

A number N is prime if no number from 2 to N-1 divides evenly into it.  That is, <span>\\((N (mod \; k)) \ne 0\\)</span> for all <span>\\(k \in [2, N-1]\\)</span>.

Once you generate those prine numbers (let's call them A and B), you can generate your public key (E, C) and private key (D, C).  Recall that the value C is shared between the public and private key, and that E and C are made available to others so that they can encrypt data to you.  Your private key (D, C) is needed to decrypt those values, so you must keep the value D a secret!

To generate your public key:

1. Choose two prime numbers A and B.  Make these prime numbers at least 2 digits in length, but no more than 3 digits.  In practice, the values are much larger, but this is a demonstration.
2. Compute <span>\\(C = AB\\)</span>.
3. Compute <span>\\(M = \phi(C)\\)</span> using the `RSAMath.totient(C)` method.
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
long M = rsa.totient(C); 
long E = rsa.coprime(M);
```

### Encrypt Data Using a Public Key
Given a public key (E and C) as parameters, write a function to encrypt a given value, and return the encrypted value.  Print this value to the screen.

Here is an example:

![Encryption Example]({{ site.baseurl }}/images/asmt-minicrypto/encrypt.png)

The `RSAMath.endecrypt(X, E, C)` function will help you to do this, by encrypting the value X using the encryption key E and C.  

### Decrypt Data Using a Private Key
Similarly, accept a private key (D and C) as parameters, write another function to decrypt a given value, and return that decrypted value.  Print it to the screen as well.  

The procedure is similar to that used to encrypt a value.  The `RSAMath.endecrypt(X, D, C)` function will help you to do this, by encrypting the value X using the encryption key E and C.  

Here is an example:

![Decryption Example]({{ site.baseurl }}/images/asmt-minicrypto/decrypt.png)

<details>
  <summary>What do you notice about the encryption and decryption functions you just wrote?  (Click to reveal)</summary>
  
  They're exactly the same!  They only differ in the input parameters (what values are used for the keys).  This is because the mathematics results in the computation of the modular inverse of the value.  The same function can be used on two different problems!
  
</details>

### Test the Public/Private Key Pair by Encrypting and Decrypting Using Your Own Public and Private Key
Write test cases that encrypt values using your public key, and decrypt them using your private key, and assert that the final decrypted value matches your original input.  Also try encrypting with your private key and decrypting with your public key, to ensure that the keys are proper inverses of one another.

## Step 2: Communicating Secret Messages to a Partner Using Only Their Public Key
Now, write a program to accept your partner's public key, and your private key.  You can exchange keys via email, on Teams, or on the board.  Accept a String parameter, and for each character in the string, obtain its ASCII value and encrypt it with your partner's public key.  Send those encrypted values to your partner.

Your loop to obtain each character from the String will look something like this:

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

Given a set of integers that are values encrypted by your partner using your public key, write a program that decrypts each of those values (using a loop!) and decrypt to the original secret message.  Decide on a way to determine when you are finished so that you exit the loop nicely.  Write down how you decided to do this!  **For example, you can read each encrypted `int` value from the user keyboard using the `Scanner`, and enter a negative number to indicate that you have finished reading.  Continue reading and decrypting characters in a loop `while` the input is not negative!**

The procedure to do this is similar to that used to encrypt each character, except that the value to be decrypted is the encrypted value of the ASCII value used before, and the key is the private key (D, C) associated with the public key that was used to encrypt it.  You can cast the ASCII int value you obtain back to a char, and either print it or concatenate it with a `String`.  

**Hint: You will encrypt data using your partner's public key values `E` and `C`, and decrypt usnig your own private key values `D` and `C`.  The values of `C` will not be the same, since they are for two different keys (your partner's and your own)!**

When you decrypt a secret message using your own private key, you'll get back a `long`, as follows:

```java
long decrypted = RSAMath.endecrypt(encrypted, D, C);
```

You can convert the `long` back to a `char` for printing as follows:

```java
char decryptedChar = (char) decrypted;
```

## Step 3: Breaking Someone's Private Key Using Only Their Public Key
Going back through the RSA algorithm, how did you compute your private key from your public key?  Since they are modular inverses of one another, you could compute the modular inverse of your partner's public key (E and C) to obtain their private key D.  

<details>
  <summary>Why is this too difficult to do in practice?  (Click to reveal)</summary>
  
  You would need to know M, the Totient of C; this is equivalent to factoring the large prime number C, which is very difficult to do in practice.
  
</details>

Since these are small keys, you can compute <span>\\(M = \phi(C)\\)</span> directly, either by factoring C into its prime numbers A and B, or by computing the Totient of C directly (notice that these are essentially the same problem, since counting the values that are coprime to a number is effectively the same as searching for the two values that are not coprime - the factors A and B).    

Write and test a program to accept a public key.  To do this, compute your partner's private key from their public key, and test that you can obtain your own private key given your public key.  Print the private key to the screen and verify that it is correct with your partner.  This program should only accept E and C, the public key, as inputs.

Here is an example:

![Key Cracker]({{ site.baseurl }}/images/asmt-minicrypto/keycrack.png)

## Extra Credit (15 Points)

### Implement the RSAMath functions

Create your own versions of each of the functions in the RSAMath library given to you, and use those instead in your programs!

## Exporting your Project for Submission

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  In your README, answer any bolded questions presented on this page.  Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.  

## A Note About Export Controls

Some governments, including the United States, have [export controls on cryptographic technologies](https://en.wikipedia.org/wiki/Export_of_cryptography_from_the_United_States). 