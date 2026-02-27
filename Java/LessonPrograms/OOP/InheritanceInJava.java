// Program: OOP Property - Inheritance in Java

class Person {

    String name;

    // Parent Constructor
    Person(String name) {
        this.name = name;
        System.out.println("Person Constructor Called");
    }

    void showRole() {
        System.out.println("I am a Person.");
    }
}

// ---------------- Child Class ----------------
class Student3 extends Person {

    int marks;

    // Constructor Chaining using super
    Student3(String name, int marks) {
        super(name);   // Calls parent constructor
        this.marks = marks;
        System.out.println("Student Constructor Called");
    }

    // Method Overriding
    @Override
    void showRole() {
        System.out.println("I am a Student.");
    }

    void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Marks: " + marks);
    }
}

public class InheritanceInJava {

    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== OOP PROPERTY: INHERITANCE ====================");
        System.out.println("""
Inheritance allows one class to acquire
properties and behaviors of another class.

Parent Class → Superclass
Child Class → Subclass

Syntax:
class Child extends Parent
""");


        // ---------------- Why Inheritance ----------------
        System.out.println("\n==================== WHY INHERITANCE? ====================");
        System.out.println("""
Inheritance is used for:
✔ Code Reusability
✔ Logical Hierarchy
✔ Reducing duplication
✔ Easy maintenance

Instead of rewriting common code,
child class reuses parent features.
""");


        // ---------------- Types of Inheritance ----------------
        System.out.println("\n==================== TYPES OF INHERITANCE IN JAVA ====================");
        System.out.println("""
Java supports:

✔ Single Inheritance
✔ Multilevel Inheritance
✔ Hierarchical Inheritance

Java does NOT support:
✘ Multiple inheritance using classes

(But possible using interfaces)
""");


        // ---------------- Object Creation ----------------
        System.out.println("\n==================== OBJECT CREATION ====================");
        Student3 s1 = new Student3("Amit", 90);

        s1.displayDetails();


        // ---------------- Method Overriding ----------------
        System.out.println("\n==================== METHOD OVERRIDING ====================");
        System.out.println("""
Method Overriding:
✔ Same method name
✔ Same parameters
✔ Defined in parent
✔ Re-defined in child

Allows runtime polymorphism.
""");

        s1.showRole();


        // ---------------- super Keyword ----------------
        System.out.println("\n==================== SUPER KEYWORD ====================");
        System.out.println("""
super keyword is used to:

✔ Call parent constructor
✔ Access parent variables
✔ Access parent methods

Example:
super(name);
""");


        // ---------------- Constructor Chaining ----------------
        System.out.println("\n==================== CONSTRUCTOR CHAINING ====================");
        System.out.println("""
Constructor chaining means:

✔ Child constructor calls parent constructor
✔ Happens using super()
✔ super() must be first statement

Execution Order:
1. Parent Constructor
2. Child Constructor
""");


        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD EXAMPLE ====================");
        System.out.println("""
Vehicle → Parent
Car → Child
Bike → Child

Common features:
✔ speed
✔ fuel

Specific features:
✔ gear system
✔ seating capacity

Inheritance models real-world hierarchy.
""");


        // ---------------- Access Rules ----------------
        System.out.println("\n==================== ACCESS RULES ====================");
        System.out.println("""
✔ Child class inherits public & protected members
✔ Private members are NOT directly accessible
✔ Child can override non-final methods
""");


        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Forgetting super() in constructor
✘ Trying multiple inheritance with classes
✘ Overriding with different method signature
✘ Accessing private parent variables directly
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Inheritance allows child to reuse parent code.
→ Achieved using extends keyword.
→ super calls parent constructor.
→ Constructor chaining ensures proper initialization.
→ Method overriding enables runtime behavior change.
→ One of the four main OOP pillars.
""");
    }
}