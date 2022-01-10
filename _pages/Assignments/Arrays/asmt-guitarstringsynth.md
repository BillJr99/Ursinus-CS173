---
layout: assignment
permalink: /Assignments/GuitarStringSynth
title: "CS173: Intro to Computer Science - Guitar String Synthesier with the Karplus-Strong Algorithm"
excerpt: "CS173: Intro to Computer Science - Guitar String Synthesier with the Karplus-Strong Algorithm"

info:
  coursenum: CS173
  points: 100
  goals:
    - To implement an arithmetic expression into executable code
    - To map variables to expression parameters
    - To write code that interfaces with the computer audio interface
    - To manipulate arrays with audio data
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
    - rtitle: "Arrays Activity"
      rlink: "../Activities/Arrays"
    - rtitle: "Iteration Activity"
      rlink: "../Activities/Iteration"      
    - rtitle: "Conditionals Activity"
      rlink: "../Activities/Conditionals"      
      
tags:
  - math
  - arrays
  
---

In this assignment [\[[^1]\], \[[^2]\]], you will practice with arrays and loops in a fun application that involves digital audio.

[Download the skeleton code](../files/asmt-guitarstringsynth/GuitarStringSynth-master.zip) for this assignment.  In NetBeans, you can use the `File` menu, and select `Import Project` -> `From ZIP File` to select this file and open it.

You will be editing `src/guitarstring/GuitarString.java`.

We will be using the `StdAudio` library from the Princeton [algs4cs](https://algs4.cs.princeton.edu/home/) repository. [View the documentation for this library here](https://algs4.cs.princeton.edu/code/javadoc/edu/princeton/cs/algs4/StdAudio.html).  These files are already imported into the project directly for you.

## Background: Digital Audio / Musical Notes
Sound is the result of pressure waves traveling through the air. Just as our ears pick up these pressure variations and send a signal to our brain, digital microphones/ADCs are designed to turn these variations into an array of pressure samples over time (in the discussion below, we often refer to "sample" and "array index" interchangeably). Digital audio is often sampled at 44100 samples per second, which we refer to as the **sample rate** (`FS`). This means that if we want to represent 2 seconds of audio, for instance, we need an array with 88200 samples (good thing we're using arrays and don't have to define 88200 individual variables!). The reason for this is that we need a sampling frequency that's at least twice the highest frequency we want to represent. Since the highest frequency humans can hear is around 20,000hz, 44100hz is adequate. (Another fun fact about this number is it is <span>\\(2^{2} 3^{2} 5^{2} 7^{2}\\)</span>.

We'll define `FS` as a constant, as follows:

```java
public static final int FS = 44100; // sample rate of 44.1 kHz
```

### Square Waves And Pitches
One property of our perception of audio is that if a sound repeats a pattern over and over again quickly enough, we hear it as a pitch, or musical note. For example, let's consider a "square wave." The code below is a snippet from SquareWave.java in the homework 5 package which generates this pattern. The pattern will repeat itself every T elements in the array. This is referred to as the period of the audio.

```java
/**
* 
* @param T The period of the square wave
* @param a The max/min value of the square wave
* @param duration The length in seconds of the wave
* @return An array containing a square wave
*/
public static double[] getSquareWave(int T, double a, double duration) {
    // Create enough samples to hold "duration" seconds of audio
    int N = (int)Math.round(duration*FS);
    double[] audio = new double[N];
    // Loop through and fill in the array with the 
    // square wave pattern that repeats every T samples
    for (int i = 0; i < N; i++) {
        if (i/(T/2) %2 == 0) {
            // The first half of the square pattern
            // is positive
            audio[i] = a;
        }
        else {
            // The second half of the square pattern
            // is negative
            audio[i] = -a;
        }
    }
    return audio;
}
```

For example, let's consider the audio we get from the following call to the method, where the period is 100 and the audio goes on for one second:

```java
double[] x = getSquareWave(100, 0.3, 1);
StdAudio.save("SquareWave100.wav", x);
```

The first 2000 samples of the array look like this:

![First 2000 samples of the audio file array with a period of 100](../images/asmt-guitarstringsynth/SquareWave100.svg)

and sounds like this:

<p>
<audio controls>
    <source src="../files/asmt-guitarstringsynth/SquareWave100.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio> 
</p>

If we shorten the period to 60, we obtain this instead:

```java
double[] y = getSquareWave(60, 0.3, 1);
StdAudio.save("SquareWave60.wav", y);
```
Notice how there are more repetitions packed together over the same same number of samples. This makes the audio goes up in pitch to a higher note (the F# above concert A).  Now, the first 2000 samples of the array look like this:

![First 2000 samples of the audio file array with a period of 60](../images/asmt-guitarstringsynth/SquareWave60.svg)

and sounds like this:

<p>
<audio controls>
    <source src="../files/asmt-guitarstringsynth/2SquareWaves.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio> 
</p>

We can mix these two sounds together into one composite sound by using the sumArrays method we wrote in class (which I've placed in a class called ArrayUtils in the skeleton code):

```java
double[] z = ArrayUtils.sumArrays(x, y);
StdAudio.save("2SquareWaves.wav", z);
```

which looks and sounds like this

![First 2000 samples of the audio file array with the previous two arrays summed](../images/asmt-guitarstringsynth/2SquareWaves.svg)

<p>
<audio controls>
    <source src="../files/asmt-guitarstringsynth/2SquareWaves.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio> 
</p>

### Pulse Tone Sinusoids
It's also possible to build sounds from sine waves, which we refer to as "pure tones." Given a sample rate `FS`, a period `T`, and an amplitude (loudness) `a`, the formula for the value in the array at index `i` is:

<span>\\(a \times sin(\frac{2 \pi i}{T})\\)</span>

For those who know trigonometry, you'll notice that this does indeed go through one period over `T` samples, since that will bring it from 0 to 2 <span>\\(\pi\\)</span>. The code to do this, which can be found in `Sinusoid.java` in the skeleton code, looks like this:

```java
/**
 * 
 * @param T The period of the sinusoid
 * @param a The amplitude of the sinusoid
 * @param duration The length in seconds of the wave
 * @return An array containing a sinusoid
 */
public static double[] getSinusoid(int T, double a, double duration) {
    int N = (int)Math.round(duration*FS);
    double[] audio = new double[N];
    for (int i = 0; i < N; i++) {
        audio[i] = a*Math.sin(2*Math.PI*(double)i/T);
    }
    return audio;
}
```

For example, let's consider the audio we get from the following call to the method, where the period is 100 and the audio goes on for one second:

```java
double[] x = getSinusoid(100, 0.8, 1);
StdAudio.save("Sinusoid100.wav", x);
```

The first 2000 samples of the array look like this

![First 2000 samples of the audio file array of a sinusoid with a period of 100](../images/asmt-guitarstringsynth/Sinusoid100.svg)

and the audio sounds like this (a concert A)

<p>
<audio controls>
    <source src="../files/asmt-guitarstringsynth/Sinusoid100.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio> 
</p>

If we shorten the period to 60

```java
double[] y = getSinusoid(60, 0.8, 1);
StdAudio.save("Sinusoid60.wav", y);
```

then the first 2000 samples look like this

![First 2000 samples of the audio file array of a sinusoid with a period of 60](../images/asmt-guitarstringsynth/Sinusoid60.svg)

As with the square wave, there are more repetitions packed together over the same same number of samples, which makes the audio go to a higher pitch

<p>
<audio controls>
    <source src="../files/asmt-guitarstringsynth/Sinusoid60.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio> 
</p>

## Main Programming Task: The Karplus-Strong Algorithm
The square waves and sinusoids sound a bit dull and unrealistic (although a real clarinet does sound a bit [like a square wave](https://pages.mtu.edu/~suits/clarinet.html)). But it is possible to make a very realistic plucked guitar sound with a surprisingly simple algorithm known as the [Karplus-Strong Algorithm](https://en.wikipedia.org/wiki/Karplus%E2%80%93Strong_string_synthesis), which is the starting point for [all of the digital synthesizers](https://en.wikipedia.org/wiki/Digital_waveguide_synthesis) used in the 80s and beyond. Your job in this assignment will be to implement the Karplus-Strong algorithm in several stages by filling in three methods in `GuitarString.java`.

### Part 1: Getting the Period (25%)

Most Western string orchestras tune to a "concert A," which goes through 440 periods in one second. If our audio is sampled at 44100 samples per second, this means that each period takes up about 100 samples (which we saw in the examples above). In each octave in the Western chromatic scale, there are 12 notes total. Going from one note to its adjacent note in order is called a halfstep. For example, a B is 2 halfsteps above A. The formula for determining the period for a particular note h halfsteps away from a concert A is:

<span>\\(T = \frac{FS}{440 \times 2^{\frac{h}{12}}}\\)</span>

For example, at a sample rate of 44100, a B which is 2 halfsteps above concert A has a period of:

<span>\\(T = \frac{44100}{440 \times 2^{\frac{2}{12}}} \approx 89.29\\)</span>

Notice how the period has gotten shorter, which indeed corresponds to an increase in pitch, as we saw in the square/sinusoid examples.

It is also possible for the halfstep to be negative, in which case the formula yields a period longer than 100, for a pitch lower than 440. For example, for a G two halfsteps below concert A, the formula yields:

<span>\\(T = \frac{44100}{440 \times 2^{\frac{-2}{12}}} \approx 112.5\\)</span>

Your first task is to implement this equation in the `getPeriod(int halfStep)` method in `GuitarString.java`. You should round the period you return to the nearest integer.

#### Hints
* Be sure you're using the correct types here, and cast if you have to! In particular, `h/12` should be a decimal number.
* Use the `Math.pow()` function to raise a number to a power.
* Use the `Math.round()` function to round to the nearest integer.

### Part 2: Random Samples (25%)
The next step of the algorithm consists of coming up with some "random noise," which sounds like static. In the context of the Karplus Strong algorithm, this can be thought of as randomly stimulating the string with a pluck. To do this, you will complete the method:

```java
public static void fillRandomSamples(double[] arr, int numSamples)
```

This method should fill in the first `numSamples` indices of the array `arr` with random samples between -1.0 and 1.0. As a corner case, if the user asks for more samples than the capacity of the array, **you should fill at most the length of the array**.

For example, if you make an array that's one second long (FS samples long) and fill the entire array with noise, the code would look like this:

```java
double[] samples = new double[FS];
fillRandomSamples(samples, FS);
StdAudio.play(samples);
```

And the audio would sound like "static":

<p>
<audio controls>
    <source src="../files/asmt-guitarstringsynth/noise.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio> 
</p>

If you were to plot the first 2000 samples of the array, they would look something like this (though the answer would be slightly different every time since the numbers are random)

![First 2000 samples of the audio file array of random noise](../images/asmt-guitarstringsynth/noise.svg)

#### Hints
* You can make use of Java's function `Math.random()`, which returns a random number between 0.0 and 1.0.
* How can you manipulate this random number to become a value between 0.0 and 2.0?  Then, you can further manipulate the value to be a number between -1.0 and 1.0.

### Part 3: The Final Plucked Sound (50%)

Now it's time to tie everything together to get our wonderful plucked sound. You will be filling in the method:

```java
public static double[] getPluckedSound(int note, double duration, double decay)
```

The steps are as follows:
1. Given a note, find its period `T` to the nearest integer by using your method that computes the period. **You've made a function do to this already, so you should call that function!**
2. Create an array with enough samples to hold `duration` seconds audio.  How many elements does this array need?  It depends on the duration and the number of samples per second (also known as the sample rate or frequency): **you have both of these!**
3. Fill in the first `T` samples with random noise **using your noise method**.
4. Process all of the rest of the samples one by one in order, starting at index `T`. Each value should be the average of the two adjacent samples `T` indices back multiplied by a factor of `decay`. For example, if you're at index 150 and your period is 100, you should average samples at indices 50 and 51. This simulates a traveling wave over a string of length `T` that decays and dampens "low frequencies" first, and is referred to as a "digital waveguide."

For example, if your code works properly, then the following call to your method will play a guitar string at a concert A:

```java
StdAudio.play(getPluckedSound(0, 0.5, 0.98));
```

which sounds like this

<p>
<audio controls>
    <source src="../files/asmt-guitarstringsynth/KarplusStrongConcertA.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio> 
</p>

If we plot the first 2000 values of the array, we can see it starts with totally random noise in the first 100 samples, but then it gradually evens out to a periodic sound that decays over time:

![Karplus Strong Concert A](../images/asmt-guitarstringsynth/KarplusStrongConcertA.svg)

By default, the `main` function in `GuitarString.java` plays the first 24 halfsteps in sequence, which is two octaves of the chromatic scale. If your code is working properly and you run the `main`, you should hear the following sound:

<p>
<audio controls>
    <source src="../files/asmt-guitarstringsynth/ChromaticProgression.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio> 
</p>

### Extra Credit (25 Points)
As extra credit, you should fill in the method `playFile`, which loads in and plays a bunch of notes in sequence from a text file. The text file contains a bunch of lines with comma separated values for `halfstep,duration,decay`. For example, the "Happy Birthday" song contains the following sequence of 25 notes:

```
0,0.35,0.98
0,0.15,0.98
2,0.5,0.98
0,0.5,0.98
5,0.5,0.98
4,1,0.98
0,0.35,0.98
0,0.15,0.98
2,0.5,0.98
0,0.5,0.98
7,0.5,0.98
5,1,0.98
0,0.35,0.98
0,0.15,0.98
12,0.5,0.98
9,0.5,0.98
5,0.5,0.98
4,0.5,0.98
2,1,0.98
10,0.35,0.98
10,0.15,0.98
9,0.5,0.98
5,0.5,0.98
7,0.5,0.98
5,0.5,0.98
```

If you copy and paste this into a file called `HappyBirthday.txt`, you can run:

```java
playFile("HappyBirthday.txt");
```

#### Hints
* If you have a String `s` of comma-separated values, then `s.split(",")` will return an array of Strings that are on either side of the commas. For instance, `"11,12,13".split(",")` will return the array `{"11", "12", "13"}`. You will then need to convert each to the correct type. The function `Integer.parseInt(string)` will convert a string to an integer, and the function `Double.parseDouble(string)` will convert a string to a double.
* Then, from within `playFile`, you can call `getPluckedSound` and pass these three values as parameters to play each note of the song!

## Finishing Touches and Writeup 

Don't forget to test your program with several different inputs to help verify that things work the way you expect!  Think in terms of trying to break your program; if it's really hard to "trick" your program into getting the wrong answer, you've probably done a good job making your code robust.  

Also, check the [Style Guide](../Style-Guide) to make sure that you've written high quality code; make sure your code is "readable," well indented, uses good variable names, and includes good comments throughout the program.

When you're done, write a README for your project, and save all your files, before exporting your project to ZIP.  **In your README, answer any bolded questions presented on this page.**  In addition, write a few paragraphs describing what you did, how you did it, and how to use your program.  If your program requires the user to type something in, describe that here.  If you wrote functions to help solve your problem, what are they, and what do they do?  Imagine that you are giving your program to another student in the class, and you want to explain to them how to use it.  What would you tell them?  Imagine also that another student had given you the functions that you wrote for your program: what would you have wished that you knew about how to call those functions?

### Exporting your Project for Submission

Here is a [video tutorial](../Modules/IDE/Module2) describing how to write a README for your project, and how to export it.  **Be sure to save your README file before exporting the project, so that your work is included in the submission!**

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie)
[^2]: Adapted from [Princeton COS126 course](https://www.cs.princeton.edu/courses/archive/spring19/cos126/assignments/guitar-hero/)
