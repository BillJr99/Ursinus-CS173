---
layout: exercise
permalink: /Modules/ArrayLists/Exercise
title: "CS173: Intro to Computer Science - ArrayLists"
excerpt: "CS173: Intro to Computer Science - ArrayLists"

prev: "./Module2"

info:
  points: 3
  instructions: "Modify the Driver.java file to create an <code>ArrayList</code> containing all prime numbers between 0 and <code>n</code>."
  goals:
    - "To create and manipulate an <code>ArrayList</code>"
    - "To iterate over an <code>ArrayList</code>"
  
canvasasmtid: "137462"
canvaspoints: 3
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let ans = feedbackString.split("-");
  correctcheck: |
    ans[0] === "7" && ans[1] === "25"
      
files:
  - filename: "PrimeArray.java"
    name: primearray
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        import java.util.ArrayList;
        
        public class PrimeArray {
            public static boolean isPrime(int val) {
                for(int i = 2; i <= Math.sqrt(val); i++) {
                    if(val % i == 0) {
                        return false;
                    }
                }
                
                return true;
            }
            
            public static ArrayList<Integer> buildArrayOfPrimes(int n) {
                /* TODO: Create an ArrayList of Integer values */
                
                /* TODO: iterate from 2 to n */
                
                    /* TODO: if each number is prime, add it to the ArrayList */
                
                /* TODO: return the ArrayList */
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
                ArrayList<Integer> primes = PrimeArray.buildArrayOfPrimes(100);
                System.out.print(primes.get(3) + "-" + primes.size());
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
