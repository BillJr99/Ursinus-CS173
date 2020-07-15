---
layout: assignment
permalink: /Assignments/Iris
title: "CS173: Intro to Computer Science - The Iris Dataset"
excerpt: "CS173: Intro to Computer Science - The Iris Dataset"

info:
  coursenum: CS173
  githubclassroom:
    joinlink: https://classroom.github.com/classrooms/61290261-billmongan-cs173-fall20
    clonelink: false
  points: 100
  goals:
    - To use File I/O to read and process a text file dataset
    - To use arrays to process records of data 
    - To apply mathematical concepts in an algorithm
    - To tokenize string data using the split() function
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

tags:
  - strings
  - arrays
  - iteration
  - math
  
---

The [Iris Flower Dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) is a classic dataset proposed by [R. A. Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) to demonstrate the use of the Fisher Linear Discriminant, which is a classic instrument to separate and classify data.  

In this assignment, you will read the classic Iris dataset, and use information obtained about different types of flowers to predict what kind of flower an unknown specimen is knowing only its measured data values.  The dataset can be [downloaded](http://archive.ics.uci.edu/ml/datasets/Iris) and saved into your project directory.  On the [Iris download page](http://archive.ics.uci.edu/ml/datasets/Iris), click the `Data Folder` link, and then download the `iris.data` file.  The format of this file is a [Comma Separated Value (CSV)](https://en.wikipedia.org/wiki/Comma-separated_values) file, meaning that each token on a line is separated by a comma character (as opposed to spaces which we used earlier).  The first line is a header line, giving the labels for each column in the file (for example, whether the column contains lengths or widths of the flower petals).  This can be ignored; each subsequent line contains:

```
SepalLength,SepalWidth,PetalLength,PetalWidth,Classification
```

The lengths and widths are numeric values, and the classification is either `setosa`, `versicolor`, or `virginica`.  Given the sepal and petal widths and lengths, we can make a prediction about new types of flowers whose classification is unknown to us.  Generally, the more examples we have of each type of flower, the more accurate our prediction will be.

## Part 1: Reading the CSV File
Open the CSV file for reading.  Since it is a CSV file, a `BufferedReader` is a good choice, as we can read the text line-by-line.  Using the `split` function, you can obtain an array of values for each row.  This array will contain the sepal length, sepal width, petal length, petal width, and the known classification of that particular flower.  The `split` function accepts a `String` parameter representing the delimiter character on which to split.  For a CSV, that's the comma character.

## Part 2: Obtaining the Features
Using an `ArrayList`, gather all the sepal lengths, sepal widths, petal lengths, and petal widths by iterating over the text file and splitting each line.  If the classification is a `setosa` flower, store that in a separate array.  Similarly, use separate arrays for the `versicolor` and `virginica` flowers as well.  By the time you are finished reading the text file, you should have an array containing all the `setosa` petal lengths, one for all the `setosa` petal widths, and so on.

Compute the mean and variance of these arrays.  The formulas for the mean and variance are provided for your convenience:

Mean: <span>\\(\mu = \frac{\sum\limits_{i=1}^{n} x_{i}}{n}\\)</span><br>
Variance: <span>\\(\Sigma^{2} = \frac{\sum\limits_{i=1}^{n} ((x_{i}-\mu)^{2})\\)</span>

## Part 3: Classifying a New Flower
Using the Means you just computed, which we call our data featuress, we will try to determine the classification of an unknown flower.  Make up values for a flower based on the data that you see in the Iris data set.  Try to choose values that you know should align with one classification of flower over the others (that is, choose values close to the bunch of values for a particular type of flower); this way, you can check your work.  To classify our unknown flower, we will consider the means of the sepal lengths, sepal widths, petal lengths, and petal widths as points in 4-dimensional space.  Your unknown flower is also a point in 4-D space, and it is going to be closer to one of those mean points than it is to the others.  The means with the smallest distance is going to be our prediction.  From geometry, you may recall the Euclidean Distance as a measure of precisely this distance.  Here is the formula:

Euclidean Distance: <span>\\(d = \sqrt{(x_{petalLength}-\mu_{petalLength})^{2} + (x_{petalHeight}-\mu_{petalHeight})^{2} + (x_{petalLength}-\mu_{petalHeight})^{2} + (x_{sepalLength}-\mu_{sepalHeight})^{2}}\\)</span>

You will compute three of these Euclidean Distances: one using the means of the `setosa` flower, one using the means of the `versicolor` flower, and one using the means of the `virginica` flower.  `x` is your made up flower that you're looking to classify.

Print out all of your Euclidean Distances, and choose the flower corresponding to the smallest Euclidean Distance you calculated.  That is your prediction.  Change the values of your made up flower and see how you do predicting it!

## Part 4: Experimenting with the Data

### Classifying the Input Samples
Re-read each line of the Iris Dataset CSV file.  This time, pretend that you do not know the classification, and use those values as your "made up flower" to be classified.  In your program, compare your classification to the actual classification from the CSV, and print out your accuracy rate.

### Studying the Effect of More or Fewer Samples
What happens if you only read 10, 5, or 1 example of a `setosa` flower?  Modify your program to read only the first N rows of each of the flower types.  How well are you able to predict your flowers?  Use the accuracy rate you computed above, and graph your accuracy over N=1, 5, 10, and the whole dataset.

### Fisher Linear Discriminant
It is usually the case that adding more rows to our input data results in better classification (at least to a plateau).  However, it's not always the case that adding more columns ("features") to the dataset makes for better prediction.  If we use too many columns, our accuracy actually starts to decrease.  If we needed to remove some columns, how would we choose which columns to keep and which to remove?  Let's find out which column(s) are helping us classify the data the best.  We can do this by computing the Fisher Linear Discriminant (developed by Fisher, who also provided this classic Iris dataset).  

The key idea behind Fisher's Linear Discriminant is that data can be separated into classes if those classes have a relatively small variance, and the data between the classes have a relatively high variance.  Imagine two different coins (for example, an American quarter and an American dime).  The quarter has a large radius and weight compared to the dime.  If you looked at enough quarters and dimes, each one might have a slightly different radius and weight because of wear and tear, but generally, they would be close together, but the radius and weight of each dime would differ greatly from those of the quarter.

As you will learn in statistics, and implemented above in this assignment, the variance is a measure of the difference of the data elements to their overall mean.  Therefore, Fisher's idea can be expressed mathematically: 

<span>\\(FisherLDA \propto \frac{(\mu_{1} - \mu{2})^{2}}{\Sigma_{1}^{2} + Sigma_{2}^{2}}\\)</span>

The FisherLDA is large when the numerator is large and the denominator is small.  That is, when the difference of the means is large, and the sum of the variances is small.  This occurs when the means of the two classes differ greatly (like the dime and the quarter), while the variance of each is relatively small.

The Linear Discriminant function tells us how separable a feature is into two classes, and it only requires the mean and variance, which we have!  For each feature (the original arrays of the lengths/widths from the data set that you created in Part 2), compute the Linear Discriminant function for the following features:

1. The `setosa` sepal length *vs* the `versicolor` sepal length
2. The `setosa` sepal length *vs* the `versicolor` sepal length
3. The `setosa` sepal length *vs* the `virginicia` sepal length
4. The `setosa` sepal width *vs* the `versicolor` sepal width
5. The `setosa` sepal width *vs* the `versicolor` sepal width
6. The `setosa` sepal width *vs* the `virginicia` sepal width
7. The `setosa` petal length *vs* the `versicolor` petal length 
8. The `setosa` petal length *vs* the `versicolor` petal length 
9. The `setosa` petal length *vs* the `virginicia` petal length 
10. The `setosa` petal width *vs* the `versicolor` petal width
11. The `setosa` petal width *vs* the `versicolor` petal width 
12. The `setosa` petal width *vs* the `virginicia` petal width

At first glance, this seems like a lot of work!  Before you start writing code, remember that you can do this once, but implement the code in a function that accepts the two arrays as parameters.  Then, just call the functions with the right pair of arrays, and you're done!

Which column/feature (i.e., the "sepal length") best separates the `setosa` and the `versicolor` flowers?  Which column best separates the `setosa` and the `virginica` flowers?  Which column seems the best overall?  Do any columns appear to do a poor job separating any of the classes?  Which columns would you use for our approach?

## Extra Credit (10 Points)

For extra credit, remove the columns you selected based on the Linear Fisher Discriminant, and plot your new classification accuracies for N=1, 5, 10, and the whole dataset like you did in Part 4.  Did you sacrifice any classification accuracy (and how much, if so) by removing one or more columns with relatively low LDA score?