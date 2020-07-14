---
layout: default
permalink: /Assignments/MiniCrypto
title: "CS173: Intro to Computer Science - Public-Key Cryptography"
excerpt: "CS173: Intro to Computer Science - Public-Key Cryptography"

info:
  coursenum: CS173
  
tags:
  - strings
  - iteration
  - numeric
  
---

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# {{ page.title }} (100 Points)

This assignment is adapted from Prof. Mongan's assignments in communications and introductory cryptography \[[^1], [^2], [^3]\], and from the CS Unplugged Public Key Encryption lesson module \[[^4]\].

[^1]: William M. Mongan. 2012. An integrated introduction to network protocols and cryptography to high school students (abstract only). In Proceedings of the 43rd ACM technical symposium on Computer Science Education (SIGCSE ’12). Association for Computing Machinery, New York, NY, USA, 664. DOI:[https://doi.org/10.1145/2157136.2157364](https://doi.org/10.1145/2157136.2157364)
[^2]: William M. Mongan. 2011. Networking Applications, Protocols, and Cryptography with Java. Google CS4HS Workshop at the University of Pennsylvania, Philadelphia, PA.
[^3]: William M. Mongan. 2012. Networking Applications, Protocols, and Cryptography with Java. Tapia Workshop at the University of Pennsylvania, Philadelphia, PA.
[^4]: Bell, Witten, and Fellows. 1998. Computer Science Unplugged - Public Key Encryption. Available at [https://classic.csunplugged.org/public-key-encryption/](https://classic.csunplugged.org/public-key-encryption/)

The goals of this assignment are:
* To relate the mathematics of modern encryption systems to applied principles of information hiding
* To implement mathematical theory in the Java programming language
* To apply library functionality from external jar files and build upon existing functionality
* To implement algorithms that iterate over characters in a string and over elements in an array

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

Notice that many problems such as the map and the knapsack relied on modular arithmetic, using things that you've seen in school like "coprime" and "gcd."  Another difficult problem is factoring large numbers and finding large prime numbers.  How did we get the modular inverse of 588 mod 881?  It's because we made sure that they were coprime to each other.  Given numbers that don't have any factors (3 and 7, 9 and 25) in common, what's their gcd?  1 is the only number that divides them both.  This means that we can find a modular inverse of the one number mod the other number, because there exists a number <span>\(r^{-1}\)</span> (in this case, <span>\(r^{-1}\)</span> is known as the [Modular Inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse), not the traditional arithmetic inverse) such that <span>\(rx = 1 (mod p)\)</span>.

Some interesting relationships in mathematics (called [Fermat's Little Theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)) show us that when two numbers are coprime, we can compute the modular inverse of their product r: <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=r^{-1} = r^{\phi(m) -1} mod m">.  <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=\phi(m)"> is known as [Euler's Totient Function](https://en.wikipedia.org/wiki/Euler%27s_totient_function), and it is simply a count of the number of integers 1 <= k < m that are coprime to m.  <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=\phi(24) = 8"> because the totatives of 24 are 1,5,7,11,13,17,19,23).  So for r = 588 and q = 881, as in the [Knapsack Example](https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem#Example), we can compute the modular inverse of 588 (mod 881) as follows: <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=588^{-1} = 588^{\phi(881)-1} mod 881">.  Unfortunately, it is very difficult to compute <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=\phi(m)"> - and therein lies the secret!  If you generate r by multiplying together two large prime numbers that you already know (this is why [finding large prime numbers](https://en.wikipedia.org/wiki/Largest_known_prime_number) is an interesting problem!), you can generate a number for which it is too difficult to compute Euler's Totient.  But, the totient of a prime number p is (p-1), because every number larger than 1 except p is co-prime to it (because it's prime itself)!.  Thus, the totient of the product of two primes p and q is (p-1)(q-1) (because every number larger than 1 except for p and q is coprime to it!).  You can very easily compute the Totient, and, thus, you (and probably only you) can compute the modular inverse of values mod m = (p-1)(q-1).  

For now, we can look up <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=\phi(881)"> on a website like [http://primefan.tripod.com/TotientAnswers1000.html](http://primefan.tripod.com/TotientAnswers1000.html), but it turns out that 881 is prime, meaning that no numbers greater than 1 other than itself divide into it.  So this means <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=\phi(881) = (881-1) = 880"> (the other 880 numbers).  So <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=588^{-1} = 588^{880-1} mod 881 = 588^{879} mod 881"> That's 1.917e+2434 mod 881, or 442.  See how much easier that makes the problem above to solve?  Yet, it's harder for those that don't know the base number r and the modular inverse q, so we keep those secret.  Instead, we give our partner(s) enough information to generate encrypted values to us that we can decrypt using this approach.

To generate RSA keys, first select two prime numbers A (say, 47) and B (say, 71).  Normally, A and B should be very large -- a small map was easy to break, after all!  Multiply them together and call that C = A*B = 47*71 = 3337.  

Now compute <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=\phi(C) = \phi(AB) = (A-1)(B-1) = 46 * 70 = 3220">, and call this number (the totient of C) M.  Pick an encryption key that is coprime to M = 3220.  There are mathematical ways of doing this (the [Extended Euclidean GCD Algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)), but let's just pick one since we're using small enough numbers -- how about 79.   Take my word for now that it is easy to do, especially with a computer.  Call this E = 79.

The decryption key is the modular inverse of the encryption key E mod 3220.  Call this <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=d = 79^{-1} = 79^{\phi(3220)-1} mod 3220">.  Recall how to do this (keep in mind that 79 is coprime to M = 3220 -- what a great idea, because we can use our formula!).  So <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=r^{-1} = r^{\phi(M) -1} mod M"> works.  According to [http://www25.brinkster.com/denshade/totient.html](http://www25.brinkster.com/denshade/totient.html), <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=\phi(M) = 1056">, but we could compute it.  So now we have <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=79^{-1} = 79^{1056 - 1} mod 3220 = 791055 mod 3220 = 1019">.

The encryption key C = 3337 and e = 79 make up the public key.  The private key is d = 1019 and C = 3337.  If we want to send the value 688, we compute <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=688^{79} mod 3337 = 1570">.  To decrypt it, take <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=1570^{1019} mod 3337 = 688">.  It actually works the other way, too.  We can encrypt with the private key and decrypt with the public key.  It all works because of the modular properties of relatively prime numbers. They easily "undo" each other, but it's hard to reconstruct one number from the other.  

<details>
  <summary>But why would we ever want to do that?  What value would we gain by being the only person who could encrypt something (with our private key) that the whole world could decrypt (with our public key)?  (Click to reveal)</summary>
  
  The information would not be private, because anyone could decrypt it.  However, the public could be sure that you were the only person that could have generated that data.  If we submit a document, and an exact copy of the document encrypted with our private key, the public could decrypt it and verify that it matches the non-encrypted document we sent out.  This is the basis of a digital signature!
  
</details>

The idea is that 1019 is very difficult to find even knowing e = 79 and C = 3337.  That's because we'd need to be able to factor 3337 into two numbers that, when one is subtracted from each and multiplied together, give 3220 -- such that 79 is relatively prime to that number.  If factoring was easy, we could try every number until we found it.  Luckily, it isn't so easy.   Still, cryptosystems are subject to attacks similar to those you do in the newspaper, and there are some tricks (padding, salting) to dealing with that.  What would you do?  Some devices like RSA keys generate RSA values every minute.  This is because we believe that even if these numbers can be factored, it would take more than a minute to do so, and thus the security maintained.

## RSAMath Library
The mathematics functions used in this assignment are provided in the jar file library [rsamath.jar]({{ site.baseurl }}/files/rsamath/rsamath.jar).  To use this jar, after creating a Gradle Java project in Netbeans, add the following line inside the `dependencies` section of your `build.gradle` file:

```
compile fileTree(dir: 'libs', include: '*.jar')
```

If you do not have a dependencies section, you can add one as follows:

```
dependencies {
    compile fileTree(dir: 'libs', include: '*.jar')
}
```

Now, jar files added to the libs directory of your project will be available for use in your code.  You can download the [rsamath.jar]({{ site.baseurl }}/files/rsamath/rsamath.jar) file into a subdirectory of your project called `libs`.

To see which functions are available in the RSAMath library, see the [Javadoc]({{ site.baseurl }}/files/rsamath/doc/index.html).  The `RSAMath` class is implemented in the `cs4hs11.rsalibrary` package, which you can import in your program.  The methods are not static, so you can create an `RSAMath` object and then call the functions on the resulting object.  Here is a listing of the methods you'll find in this library:

![RSAMath Library Methods]({{ site.baseurl }}/images/asmt-minicrypto/javadocs.png)


## Step 1: Encrypting Characters Using A Public/Private Key that We Create

### Generate a Public/Private Key Pair
Write a function to generate a public and private key pair and print these to the screen.  Write a `main()` function to test this functionality.

Here is an example:

![Key Generator]({{ site.baseurl }}/images/asmt-minicrypto/genkey.png)

### Encrypt Data Using a Public Key
Given a public key (E and C) as parameters, write a function to encrypt a given value, and return the encrypted value.  Print this value to the screen.

Here is an example:

![Encryption Example]({{ site.baseurl }}/images/asmt-minicrypto/encrypt.png)

### Decrypt Data Using a Private Key
Similarly, accept a private key (D and C) as parameters, write another function to decrypt a given value, and return that decrypted value.  Print it to the screen as well.

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

Given a set of integers that are values encrypted by your partner using your public key, write a program that decrypts each of those values (using a loop!) and decrypt to the original secret message.  Decide on a way to determine when you are finished so that you exit the loop nicely.  Write down how you decided to do this!

## Breaking Someone's Private Key Using Only Their Public Key
Going back through the RSA algorithm, how did you compute your private key from your public key?  Since they are modular inverses of one another, you could compute the modular inverse of your partner's public key (E and C) to obtain their private key D.  

<details>
  <summary>Why is this too difficult to do in practice?  (Click to reveal)</summary>
  
  You would need to know <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=M = \phi(C)">, the Totient of C; this is equivalent to factoring the large prime number C, which is very difficult to do in practice.
  
</details>

Since these are small keys, you can compute <img style="vertical-align:middle" src="https://render.githubusercontent.com/render/math?math=M = \phi(C)"> directly, either by factoring C into its prime numbers A and B, and computing M = (A-1)(B-1), or by computing the Totient of C directly (notice that these are essentially the same problem, since counting the values that are coprime to a number is effectively the same as searching for the two values that are not coprime - the factors A and B).    

Write and test a program to accept a public key, and compute the private key.  Compute your partner's private key from their public key, and test that you can obtain your own private key given your public key.  This program should only accept E and C, the public key, as inputs.

Here is an example:

![Key Cracker]({{ site.baseurl }}/images/asmt-minicrypto/keycrack.png)

## Extra Credit (15 Points)

### Implement the RSAMath functions

Create your own versions of each of the functions in the RSAMath library given to you, and use those instead in your programs!

## Programming Rubric

|  | Pre-Emerging (<50%) | Beginning (50%) | Progressing (85%) | Proficient (100%) |
|-|-|-|-|-|
| Algorithm Implementation (60%) | The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run | The algorithm fails on the test inputs due to one or more minor issues | The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation | A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case |
| Code Quality and Documentation (30%) | Code commenting and structure are absent, or code structure departs significantly from best practice, and/or the code departs significantly from the style guide | Code commenting and structure is limited in ways that reduce the readability of the program, and/or there are minor departures from the style guide | Code documentation is present that re-states the explicit code definitions, and/or code is written that mostly adheres to the style guide | Code is documented at non-trivial points in a manner that enhances the readability of the program, and code is written according to the style guide |
| Writeup/Submission (10%) | An incomplete submission is provided | The program is submitted, but not according to the directions in one or more ways | The program is submitted according to the directions with a minor omission or correction needed | The program is submitted according to the directions, including a readme writeup describing the solution |