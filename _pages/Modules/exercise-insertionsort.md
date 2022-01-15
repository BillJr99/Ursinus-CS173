---
layout: exercise
permalink: /Modules/InsertionSort/Exercise
title: "CS173: Intro to Computer Science - Insertion Sort"
excerpt: "CS173: Intro to Computer Science - Insertion Sort"

info:
  points: 3
  prev: "./Module2"
  instructions: "Please fill in the swap method to swap arr[i] with arr[j]. Below is some of the code we wrote in the video to setup random arrays, as well as skeleton code for insertion sort. The main method fills in a random array, prints that array, calls the insertionSort method, and then prints the result. Once this method works properly, your insertion sort code will properly sort the array."
  goals:
    - To swap two variables in memory
    - To implement the insertion sort algorithm
    
canvasasmtid: "137466"
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
  - filename: "InsertionSort.java"
    name: insertionsort
    ismain: false
    isreadonly: false
    isvisible: true
    code: |
        public class InsertionSort {
            /**
            * Swap the element at index i for the element at index j
            * element at index j
            * @param arr An array of ints
            * @param i First index
            * @param j Second index
            */
            public static void swap(int[] arr, int i, int j) {
                // TODO: Fill this in
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
            * Check to see if two arrays are equal
            * @param arr1 First array
            * @param arr2 Second array
            * @return True if all of the elements are equal
            */
            public static boolean arraysEqual(int[] arr1, int[] arr2) {
                boolean equal = true;
                if (arr1.length == arr2.length) {
                    for (int i = 0; i < arr1.length && equal; i++) {
                        if (arr1[i] != arr2[i]) {
                            equal = false;
                        }
                    }
                }
                else {
                    equal = false;
                }
                return equal;
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
                InsertionSort.insertionSort(arr);
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

## Hints

* If you just say `arr[i] = arr[j]`, then that will do half of the swap, but now you've overwritten what `arr[i]` used to be, so you've lost the information you need to update `arr[j]`. Try creating a temporary variable to store the value in `arr[i]` before you overwite it with what's in `arr[j]`.

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie)