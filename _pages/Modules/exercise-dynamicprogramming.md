---
layout: exercise
permalink: /Modules/DynamicProgramming/Exercise
title: "CS173: Intro to Computer Science - Dynamic Programming"
excerpt: "CS173: Intro to Computer Science - Dynamic Programming"

info:
  points: 3
  prev: "./Module2"
  instructions: "Your job below is to change the fib method so that it checks to see if a particular Fibonacci number has been saved in memory before trying to compute it. If it's already been saved, simply return what's in memory."
  goals:
    - To improve performance of a recursive algorithm by cacheing values via a Dynamic Program 

canvasasmtid: ""      
canvaspoints: 3
  
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let i1 = feedbackString.indexOf("fib(20) = 10946, counts = 39");
    let i2 = feedbackString.indexOf("fib(30) = 1346269, counts = 21"); 
  correctcheck: |
    i1 > -1 && i2 > -1 && i2 > i1
 
files:
  - filename: "Recursion.java"
    name: recursion
    ismain: false
    isreadonly: false
    isvisible: true
    code: |
        import java.util.HashMap;

        public class Recursion {
            private HashMap<Integer, Integer> fibMem;
            public static int counts = 0;
            
            public static void resetCounts() {
                counts = 0;
            }

            public Recursion() {
                fibMem = new HashMap<Integer, Integer>();
            }

            public int fib(Integer N) {
                counts++; // Keep this here so it counts correctly
                // TODO: If the result is already
                // in memory, do not compute it here.
                // Instead, get it from memory
                Integer result = 1;
                if (N > 1) {
                    result = fib(N-1) + fib(N-2);
                }
                fibMem.put(N, result);
                return result;
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
                Recursion r = new Recursion();
                
                int N = 20;
                Recursion.resetCounts();
                System.out.print("fib("+N+") = " + r.fib(N));
                System.out.println(", counts = " + Recursion.counts);
                
                N = 30;
                Recursion.resetCounts();
                System.out.print("fib("+N+") = " + r.fib(N));
                System.out.println(", counts = " + Recursion.counts);
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

In this exercise \[[^1]\], the main method computes `fib(20)` and `fib(30)`, and by default, it outputs the following stats:

* `fib(20) = 10946, counts = 21891`
* `fib(30) = 1346269, counts = 2692537`

But once you start using the memory properly, you'll get these stats instead, which are way more efficient

* `fib(20) = 10946, counts = 39`
* `fib(30) = 1346269, counts = 21`

In fact, now computing `fib(30)` takes even fewer than the 30 steps we would have done by hand, because we remembered some of the steps we did when computing `fib(20)` right before that.

## Hints

* Recall that to see if a key is in a HashMap `map`, you say `map.containsKey(key)`, which returns `true` if the key is in the map and `false` otherwise. So you'd want to check the memory by saying something like `fibMem.containsKey(N)`. You should use the result of this in an if statement
* Recall that to retrieve values from the hash map, you use the `get(key)` method.

[^1]: Developed by [Prof. Chris Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-j-tralie)