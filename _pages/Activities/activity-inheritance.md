---
layout: activity
permalink: /Activities/Inheritance
title: "CS173: Intro to Computer Science - Inheritance"
excerpt: "CS173: Intro to Computer Science - Inheritance"

info:
  goals: 
    - To be able to explain the inheritance relationship among classes.
    - To be able to inherit from a superclass.
    - To be able to override a method from a superclass.
    - To be able to call <code>super()</code> in a constructor or method.
    - To be able to explain the difference between an interface, an abstract class, and a superclass.
    - To be able to inherit protected methods or fields from a superclass.
    
  models:
    - model: |
        <img src="../examples/inheritance-relationship.png" alt="Diagram of the Relationships between Inherited Classes">
      title: Inheritance Relationship
      questions:
        - Which items in the model are &quot;Vehicles?&quot;  Which are &quot;Homes?&quot;
        - What kinds of things do a car, truck, and motor home have in common?  What kinds of things do a motor home, townhouse, and apartment have in common?
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[  
        import java.util.Random;
        
        public interface Vehicle {
             // An interface shows how a program
             // Can interact with an object.
             // It defines common behaviors - no data/fields, just methods!
             
             public void unlock();
             
             public void lock();
             
             public void drive(int speed);
             
             // return a boolean if the vehicle is parked
             public boolean stop();
             
             public int getSpeed();
        }
        
        public interface Home {
            public int cook();
 
            public void makeBed();
        }

        public class Car implements Vehicle {
             int gear;
             boolean parked;
             int speed;
             boolean locked;
             
             public Car() {
               this.gear = 1; 
               this.parked = true;
               this.speed = 0;
               this.locked = true;
             }
             
             public int getSpeed() {
               return this.speed;
             }
             
             public void unlock() {
               this.locked = false;
             }
             
             public void lock() {
               this.locked = true;
             }
             
             public void drive(int speed) {
               if(this.parked == true) {
                 this.parked = false;
               }
             
               this.speed = speed;
               this.gear = this.speed / 10;
             }
             
             // return a boolean if the vehicle is parked
             public boolean stop() {
               this.speed = 0;
               this.gear = 1;
               return this.parked;
             }
        }

        public class MotorHome implements Vehicle, Home {
             int gear;
             boolean parked;
             int speed;
             boolean locked;
             boolean bedmade;
             
             public MotorHome() {
               this.gear = 1; 
               this.parked = true;
               this.speed = 0;
               this.locked = true;
               this.bedmade = true;
             }
             
             public void unlock() {
               this.locked = false;
             }
             
             public void lock() {
               this.locked = true;
             }
             
             public void drive(int speed) {
               if(this.parked == true) {
                 this.parked = false;
               }
             
               this.speed = speed;
               this.gear = this.speed / 5;
             }
             
             // return a boolean if the vehicle is parked
             public boolean stop() {
               this.speed = 0;
               this.gear = 1;
               return this.parked;
             }
             
             public int cook() {
               return 1; // yum?
             }
             
             public void makeBed() {
               this.bedmade = true;
             }
             
             public boolean isBedMade() {
               return this.bedmade;
             }
             
             public int getSpeed() {
               return this.speed;
             }
        }
         
        class Main {
             public static void main(String[] args) {
               Random r = new Random();
             
               Vehicle[] vehicles = new Vehicle[2];
             
               Car c = new Car();
               MotorHome m = new MotorHome();
             
               vehicles[0] = c;
               vehicles[1] = m;
             
               m.makeBed();
             
               for(Vehicle v: vehicles) {
                 v.drive(r.nextInt(50));
               }
             
               // Methods in the Interface can be called on variables whose type is just the interface, no matter what it really is!
               System.out.println("How fast is the car driving? " + vehicles[0].getSpeed());
             
               System.out.println("How about the Motor Home? " + vehicles[1].getSpeed());
             
               // Methods specific to a class can always be called from the object.
               System.out.println("Is the Motor Home bed made? " + m.isBedMade());
             }
        }
        ]]></script>
      title: Interfaces
      questions:
        - Does an <code>interface</code> define fields, methods, both, or neither?
        - What is the advantage of defining an <code>interface</code>?
        - When using an <code>interface</code>, it is sometimes still necessary to duplicate code.  Can you find an example of this in this Model?
        - Run this example in <a href=https://repl.it>repl.it</a>.  What must each file be named, and what code goes into which file?  When you click Run, what <code>javac</code> command executes (specifically, what files are compiled)? 
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>    
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[  
        import java.util.Random;
        
        public abstract class Vehicle {
             protected int gear;
             protected boolean parked;
             protected int speed;
             protected boolean locked;
             
             public Vehicle() {
               this.gear = 1;
               this.parked = true;
               this.speed = 0;
               this.locked = true;
             }
             
              public void drive(int speed) {
               if(this.parked == true) {
                 this.parked = false;
               }
               this.speed = speed;
             }
             
             // return a boolean if the vehicle is parked
             public abstract boolean stop();
             
             public int getSpeed() {
               return this.speed;
             }
             
             public void unlock() {
               this.locked = false;
             }
             
             public void lock() {
               this.locked = true;
             }
            }
            public interface Home {
             public int cook();
             
             public void makeBed();
        }

        public class Car extends Vehicle {
             public Car() {
               super();
             }
             
             public void drive(int speed) {
               super.drive(speed);
             
               this.gear = this.speed / 10;
             }
             
             // return a boolean if the vehicle is parked
             public boolean stop() {
               this.speed = 0;
               this.gear = 1;
               return this.parked;
            }
        }
        // Unlike interfaces, you can only extend a single class
        public class MotorHome extends Vehicle implements Home {
             private boolean bedmade;
             
             public MotorHome() {
               super();
               this.bedmade = true;
             }
             
             public void drive(int speed) {
               super.drive(speed);
             
               this.gear = this.speed / 5;
             }
             
             // return a boolean if the vehicle is parked
             public boolean stop() {
               this.speed = 0;
               this.gear = 1;
               return this.parked;
             }
             
             public int cook() {
               return 1; // yum?
             }
             
             public void makeBed() {
               this.bedmade = true;
             }
             
             public boolean isBedMade() {
               return this.bedmade;
             }
        }

        class Main {
             public static void main(String[] args) {
               Random r = new Random();
             
               Vehicle[] vehicles = new Vehicle[2];
             
               Car c = new Car();
               MotorHome m = new MotorHome();
             
               vehicles[0] = c;
               vehicles[1] = m;
             
               m.makeBed();
             
               for(Vehicle v: vehicles) {
                 v.drive(r.nextInt(50));
               }
             
               // Methods in the Interface can be called on variables whose type is just the interface, no matter what it really is!
               System.out.println("How fast is the car driving? " + vehicles[0].getSpeed());
             
               System.out.println("How about the Motor Home? " + vehicles[1].getSpeed());
             
               // Methods specific to a class can always be called from the object.
               System.out.println("Is the Motor Home bed made? " + m.isBedMade());
             }
        }

        ]]></script>    
      title: Inheriting from a Superclass, Abstract Methods, and <code>super()</code>
      questions:
        - How did each file change above by converting the <code>Vehicle</code> interface to a class?
        - By converting the <code>Vehicle</code> interface to a class, what can we now define in a <code>Vehicle</code> that we could not define in the <code>interface</code>?
        - You can implement an <code>interface</code>; what is the keyword to subclass a class?
        - From context, what do you think the abstract keyword means in the <code>Vehicle</code> class?
        - From context, what do you think the call to <code>super()</code> does?
        - Notice that some elements are scoped to be <code>public</code> and <code>private</code>, like before, but now some items are <code>protected</code>.  Which items are <code>protected</code>, and in which files do they reside?  What do you think this scope allows/disallows?      
      
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit9-Inheritance/topic-9-1-inheritance.html
      title: Inheritance
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit9-Inheritance/topic-9-5-hierarchies.html 
      title: Inheritance Hierarchies
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit9-Inheritance/topic-9-6-polymorphism.html 
      title: Polymorphism
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit9-Inheritance/topic-9-2-constructors.html
      title: Constructors with Inheritance
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit9-Inheritance/topic-9-3-overriding.html 
      title: Overriding Methods
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit9-Inheritance/topic-9-4-super.html
      title: The <code>super</code> Keyword
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit9-Inheritance/topic-9-7-Object.html 
      title: Object Inheritance
      
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit9-Inheritance/ooEasyMC.html
      title: Inheritance Questions
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit9-Inheritance/ooMedMC.html
      title: Medium Difficulty Inheritance Questions
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit9-Inheritance/ooHardMC.html 
      title: More Challenging Inheritance Questions
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit9-Inheritance/ooCodePractice.html
      title: implementing Subclasses
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit9-Inheritance/TrioA.html
      title: Cafeteria Manager
      
tags:
  - classes
  - inheritance
  
---

