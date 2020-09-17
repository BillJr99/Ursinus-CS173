---
layout: activity
permalink: /Activities/Functions
title: "CS173: Intro to Computer Science - Functions"
excerpt: "CS173: Intro to Computer Science - Functions"

info:
  next: ./Random
  
  goals: 
    - To be able to call methods in various configurations (parameters, return values)
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            /* Return the area of a circle, given its radius
             * @param radius: the radius of the circle
             *        Precondition: radius >= 0
             * @return the area of the circle in square units of the radius
             */
            public static double circleArea(double radius) {
                double area = 3.14 * radius * radius;
                
                return area;
            }
            
            public static double triangleArea(double base, double height) {
                double area = 0.5 * base * height;
                
                return area;
            }
            
            public static void main(String[] args) {
                double r = 10.0;
                
                double a = circleArea(r);
                
                System.out.print("The area of the circle is: ");
                System.out.println(r);
            }
        }
        ]]></script>     
      title: Writing and Invoking Functions to Re-Use Code Logic
      questions:
        - What does <code>return</code> mean in the <code>circleArea</code> function above?
        - Notice that functions have data types before their function names, just like variables do.  What is the return type of <code>circleArea()</code>?
        - Try running the sample program above in repl.it. 
        - Modify the program to write an additional function circleDiameter() that computes the diameter (<span>\(2 \times \pi \times r\)</span>) given the radius of the circle.  Call that function from main() and print the value.
        - Modify the program to write and call <code>triangleArea()</code> from <code>main()</code> and then print the area of a triangle whose dimensions you choose.
        - The Math class includes several useful math functions that you can call.  For example, <code>Math.pow(a, b)</code> will return the <code>double</code> value computed by <code>a</code> raised to the power of <code>b</code> (both <code>double</code> values).  Re-write <code>circleArea()</code> so that it computes the <code>radius</code> raised to the power of <code>2</code>, rather than multiplying it by itself.
        - The Math class also provides constants, so that you do not need to hard-code approximate values like we did with <code>3.14</code> for the value <span>\(\pi\)</span>.  Modify the program to use the constant <code>Math.PI</code> instead of <code>3.14</code>.
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>    
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        import java.util.Scanner;
        
        public class Main {
            /* Print a greeting to a friend
               @param name: the name of the friend
             */
            public static void sayHello(String name) {
                System.out.print("Hello ");
                System.out.print(name);
                System.out.println("!");
            }
            
            /* Say Hello to the World */
            public static void sayHelloWorld() {
                System.out.println("Hello World!");
            }
            
            public static void main(String[] args) {
                Scanner scanner = new Scanner(System.in);
                
                System.out.print("Enter your name: ");
                String friend = scanner.nextLine();
                
                sayHello(friend);
                sayHello("friend");
                sayHelloWorld();
            }
        }
        ]]></script>  
      title: The <code>void</code> Keyword
      questions:
        - What does the <code>void</code> keyword mean as a return type?
        - What does it mean if a function does not have any parameters, like <code>sayHelloWorld()</code>?  For example, how do you call a function like this?
        - The <code>+</code> operator works on Strings as well as on numeric values.  &quot;Adding&quot; two strings together concatenates or combines them.  Re-write the <code>sayHello()</code> method so that it executes in just one <code>System.out.println()</code> statement.      
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>        

  reflective_prompts:
    - Notice the comments above the <code>circleArea</code> function.  What do you think a precondition means?
    - Write comments for the <code>triangleArea</code> function in a similar spirit to those of the <code>circleArea</code> function.
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit1-Getting-Started/topic-1-6-casting.html 
      title: Type Casting
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-3-methods-no-params.html
      title: Calling Functions with no Parameters
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-4-methods-with-params.html
      title: Calling Functions with Parameters
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-5-methods-return.html
      title: Function Return Values

tags:
  - functions
  - expressions
  
---

