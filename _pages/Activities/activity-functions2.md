---
layout: activity
permalink: /Activities/Functions2
title: "CS173: Intro to Computer Science - Functions"
excerpt: "CS173: Intro to Computer Science - Functions"

info:
  next: ./Random
  prev: ./Functions
  
  goals: 
    - To be able to call methods in various configurations (parameters, return values)
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            /* Given an integer value, multiply it by two and return that value
             * @param value: the value to multiply by two
             *        Precondition: an integer
             * @return the number that is twice the value of the input variable
             */
            public static int twice(int value) {
                int result = 2 * value;
                
                return result;
            }
            
            public static int thrice(int value) {
                int result = 3 * value;
                
                return result;
            }
            
            public static void main(String[] args) {
                int twoTimesSix = twice(6);
                int threeTimesFive = thrice(5);
                
                System.out.println("2 times 6 = " + twoTimesSix);
                System.out.println("3 times 5 = " + threeTimesFive);
            }
        }
        ]]></script>     
      title: Parameter Binding and Scope
      questions:
        - "Are the <code>value</code> variables in the <code>twice</code> and <code>thrice</code> functions the same variable, or different variables?  How about <code>result</code>?"
        - "How would you change the name of <code>value</code> to <code>inputValue</code>?"
        - "In this program, what value are we passing to the <code>twice</code> function?"
        - "Create a variable in <code>main</code> and pass it to the <code>twice</code> function.  Can its value be changed by the <code>twice</code> function?  Why or why not?"
    - model: |
        <iframe height="600" style="width: 100%;" src="https://cscircles.cemc.uwaterloo.ca/java_visualize/iframe-embed.html?faking_cpp=false#data=%7B%22user_script%22%3A%22public%20class%20Main%20%7B%5Cn%20%20%20%20%2F*%20Given%20an%20integer%20value%2C%20multiply%20it%20by%20two%20and%20return%20that%20value%5Cn%20%20%20%20%20*%20%40param%20value%3A%20the%20value%20to%20multiply%20by%20two%5Cn%20%20%20%20%20*%20%20%20%20%20%20%20%20Precondition%3A%20an%20integer%5Cn%20%20%20%20%20*%20%40return%20the%20number%20that%20is%20twice%20the%20value%20of%20the%20input%20variable%5Cn%20%20%20%20%20*%2F%5Cn%20%20%20%20public%20static%20int%20twice(int%20value)%20%7B%5Cn%20%20%20%20%20%20%20%20int%20result%20%3D%202%20*%20value%3B%5Cn%20%20%20%20%20%20%20%20%20%5Cn%20%20%20%20%20%20%20%20return%20result%3B%5Cn%20%20%20%20%7D%5Cn%20%20%20%20%20%5Cn%20%20%20%20public%20static%20int%20thrice(int%20value)%20%7B%5Cn%20%20%20%20%20%20%20%20int%20result%20%3D%203%20*%20value%3B%5Cn%20%20%20%20%20%20%20%20%20%5Cn%20%20%20%20%20%20%20%20return%20result%3B%5Cn%20%20%20%20%7D%5Cn%20%20%20%20%20%5Cn%20%20%20%20public%20static%20void%20main(String%5B%5D%20args)%20%7B%5Cn%20%20%20%20%20%20%20%20int%20twoTimesSix%20%3D%20twice(6)%3B%5Cn%20%20%20%20%20%20%20%20int%20threeTimesFive%20%3D%20thrice(5)%3B%5Cn%20%20%20%20%20%20%20%20%20%5Cn%20%20%20%20%20%20%20%20System.out.println(%5C%222%20times%206%20%3D%20%5C%22%20%2B%20twoTimesSix)%3B%5Cn%20%20%20%20%20%20%20%20System.out.println(%5C%223%20times%205%20%3D%20%5C%22%20%2B%20threeTimesFive)%3B%5Cn%20%20%20%20%7D%5Cn%7D%22%2C%22options%22%3A%7B%22showStringsAsValues%22%3Atrue%2C%22showAllFields%22%3Afalse%7D%2C%22args%22%3A%5B%5D%2C%22stdin%22%3A%22%22%7D&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0&resizeContainer=true&highlightLines=true&rightStdout=true" frameborder="0" scrolling="yes"></iframe>
      title: The Java Visualizer
      questions:
        - "Step through the program above using the Forward button.  How many times does a <code>value</code> variable get declared, and in what frame each time?"
tags:
  - functions
  - expressions
  
---

