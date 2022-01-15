---
layout: exercise
permalink: /Modules/MergeSort/Exercise
title: "CS173: Intro to Computer Science - Merge Sort"
excerpt: "CS173: Intro to Computer Science - Merge Sort"

info:
  points: 3
  prev: "./Module2"
  instructions: "Please fill in the while loop in the mergeSort method that performs the merging step.  Below is the majority of the code for merge sort, as well as some array utilities we wrote last lab. The main method fills in a random array, prints that array, calls the mergeSort method, and then prints the result. If you've done this properly, the resulting array will come back in sorted order."
  goals:
    - To implement the merge sort algorithm
    - To swap two variables in memory
    
canvasasmtid: ""    
canvaspoints: 3
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let arr1 = feedbackString.split("\n")[0].split(" ");
    let arr2 = feedbackString.split("\n")[1].split(" ");
    for (let i = 1; i < arr1.length; i++) {
        arr1[i-1] = parseInt(arr1[i]);
        arr2[i-1] = parseInt(arr2[i]);
    }
    arr1.length = arr1.length - 1;
    arr2.length = arr2.length - 1;
    arr1.sort(function(a, b){return a-b});
    console.log(arr1);
    console.log(arr2);
    let equal = true;
    for (let i = 0; i < arr1.length && equal; i++) {
        if (arr1[i] != arr2[i]) {
            equal = false;
        }
    }
  correctcheck: |
    equal
 
files:
  - filename: "MergeSort.java"
    name: mergesort
    ismain: false
    isreadonly: false
    isvisible: true
    code: |
        public class MergeSort {
            public static int MIN_LENGTH = 5;

            public static int[] mergeSort(int[] arr) {
                int[] result = {};
                if (arr.length < 5) {
                    result = ArrayUtilities.cloneArray(arr);
                    ArrayUtilities.insertionSort(result);
                }
                else {
                    result = new int[arr.length];
                    int halfway = (int)(arr.length / 2);
                    int[] list1 = ArrayUtilities.cloneArrayPart(arr, 0, halfway);
                    int[] list2 = ArrayUtilities.cloneArrayPart(arr, halfway, arr.length);
                    list1 = mergeSort(list1);
                    list2 = mergeSort(list2);
                    int i1 = 0;
                    int i2 = 0;
                    int i = 0;
                    while (i1 < list1.length && i2 < list2.length && i < result.length) {
                        // TODO: Fill this in
                        // if list1[i1] < list2[i2], then copy 
                        // list1[i1] over to result[i], move i1 over
                        // to the right by 1
                        
                        // otherwise, do the opposite
                        
                        i++;
                    }
                    while (i1 < list1.length) {
                        result[i] = list1[i1];
                        i1++;
                        i++;
                    }
                    while (i2 < list2.length) {
                        result[i] = list2[i2];
                        i2++;
                        i++;
                    }
                }
                return result;
            }    
        }
        
  - filename: "ArrayUtilities.java"
    name: arrayutilities
    ismain: false
    isreadonly: true
    isvisible: true
    code: |
        public class ArrayUtilities {
            /**
            * Create a random array of ints
            * @param N How many random numbers we want
            * @return An array with this many random numbers
            */
            public static int[] getRandomArray(int N) {
                int[] arr = new int[N];
                for (int i = 0; i < N; i++) {
                    arr[i] = (int)(Math.random()*2*N);
                }
                return arr;
            }

            /**
            * Print out the elements of an array separated by spaces
            * @param arr An array of ints
            */
            public static void printArray(int[] arr) {
                for (int i = 0; i < arr.length; i++) {
                    System.out.print(arr[i]);
                    if (i < arr.length - 1) {
                        System.out.print(" ");
                    }
                }
                System.out.println("");
            }

            /**
            * Copy over an array
            * @param arr An array of ints
            * @return A copy of this array
            */
            public static int[] cloneArray(int[] arr) {
               int[] copy = new int[arr.length];
               for (int i = 0; i < arr.length; i++) {
                   copy[i] = arr[i];
               }
               return copy;
            }

            /**
            * Take out a slice of the array starting at a particular index
            * and ending just before another index
            * @param arr
            * @param i1 Starting index
            * @param i2 One past our last index
            * @return 
            */
            public static int[] cloneArrayPart(int[] arr, int i1, int i2) {
               int N = i2 - i1;
               int[] slice = new int[N];
               for (int i = 0; i < N; i++) {
                   slice[i] = arr[i1+i];
               }
               return slice;
            }

            /**
            * Swap the element at index i for the element at index j
            * element at index j
            * @param arr An array of ints
            * @param i First index
            * @param j Second index
            */
            public static void swap(int[] arr, int i, int j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }

            /**
            * Implement the insertion sort algorithm to
            * sort the elements of an array in place
            * @param arr 
            */
            public static void insertionSort(int[] arr) {
                for (int i = 1; i < arr.length; i++) {
                    int j = i;
                    while (j >= 1 && arr[j] < arr[j-1]) {
                        swap(arr, j, j-1);
                        j--;
                    }
                }
            }
        }

  - filename: "Driver.java"
    name: driver
    ismain: false
    isreadonly: true
    isvisible: true
    code: | 
        public class Driver {
            public static void main(String[] args) {
                int[] arr = ArrayUtilities.getRandomArray(25);
                System.out.print("Original: ");
                ArrayUtilities.printArray(arr);
                arr = MergeSort.mergeSort(arr);
                System.out.print("Sorted: ");
                ArrayUtilities.printArray(arr);
            }
        }    

  - filename: "Excerpt from Main.java: body of main() function"
    ismain: true
    name: main
    isreadonly: true
    isvisible: false
    code: |
        Driver.main(null);
        
---

This exercise \[[^1]\] was developed by Prof. Tralie.

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie)