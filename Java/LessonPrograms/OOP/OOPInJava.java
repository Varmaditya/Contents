// Program: Introduction to OOP in Java

class Students {

    // ---------------- Attributes (Instance Variables) ----------------
    String name;
    int age;

    // ---------------- Method ----------------
    void introduce() {
        System.out.println("Hello, my name is " + name + " and I am " + age + " years old.");
    }
}

public class OOPInJava {

    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== INTRODUCTION TO OOP IN JAVA ====================");
        System.out.println("""
OOP stands for Object-Oriented Programming.

It is a programming paradigm based on:
✔ Objects
✔ Classes
✔ Real-world modeling

Java is primarily an Object-Oriented Language.
""");


        // ---------------- Why OOP ----------------
        System.out.println("\n==================== WHY OOP? ====================");
        System.out.println("""
Without OOP:
✔ Code becomes messy
✔ Difficult to manage large systems
✔ Hard to reuse logic

With OOP:
✔ Code becomes modular
✔ Easy to maintain
✔ Real-world mapping becomes simple
✔ Better structure for large applications
""");


        // ---------------- OOP Principles ----------------
        System.out.println("\n==================== OOP Principles ====================");
        System.out.println("""
OOP is based on four fundamental principles:
• Encapsulation – Binding data and methods together inside a class and restricting direct access to data.
• Abstraction – Hiding internal implementation details and showing only essential features.
• Inheritance – Allowing one class to acquire properties and methods of another class.
• Polymorphism – Allowing the same method name to behave differently in different situations.
""");


        // ---------------- Real-Life Example ----------------
        System.out.println("\n==================== REAL-LIFE EXAMPLE ====================");
        System.out.println("""
Think about a CAR.

A Car has:
✔ Properties (color, model, speed)
✔ Behaviors (start, stop, accelerate)

In OOP:
✔ Properties → Variables
✔ Behaviors → Methods
✔ Car → Object
✔ Blueprint of car → Class
""");


        // ---------------- What is a Class ----------------
        System.out.println("\n==================== WHAT IS A CLASS ====================");
        System.out.println("""
A Class is a blueprint or template.

It defines:
✔ Attributes (variables)
✔ Methods (functions)

Example:
class Student {
    String name;
    int age;
}
""");


        // ---------------- What is an Object ----------------
        System.out.println("\n==================== WHAT IS AN OBJECT ====================");
        System.out.println("""
An Object is a real-world entity created from a class.

✔ Class → Blueprint
✔ Object → Real instance

Example:
Student s1 = new Student();
""");


        // ---------------- Creating Objects ----------------
        System.out.println("\n==================== CREATING OBJECTS ====================");
        System.out.println("""
Syntax for creating an object:

ClassName objectName = new ClassName();

Here:
✔ new keyword allocates memory
✔ Constructor initializes object
✔ Object gets its own copy of variables
""");

        Students s1 = new Students();
        Students s2 = new Students();


        // ---------------- Accessing Attributes ----------------
        System.out.println("\n==================== ACCESSING ATTRIBUTES ====================");
        System.out.println("""
We access attributes using dot operator.

Syntax:
objectName.variableName
""");

        s1.name = "Amit";
        s1.age = 20;

        s2.name = "Neha";
        s2.age = 22;

        System.out.println("Student 1 Name: " + s1.name);
        System.out.println("Student 1 Age: " + s1.age);

        System.out.println("Student 2 Name: " + s2.name);
        System.out.println("Student 2 Age: " + s2.age);


        // ---------------- Accessing Methods ----------------
        System.out.println("\n==================== ACCESSING METHODS ====================");
        System.out.println("""
We call methods using dot operator.

Syntax:
objectName.methodName();
""");

        s1.introduce();
        s2.introduce();


        // ---------------- Object Behavior ----------------
        System.out.println("\n==================== OBJECT BEHAVIOR ====================");
        System.out.println("""
Each object:
✔ Has its own copy of instance variables
✔ Can behave differently
✔ Is independent from other objects
""");


        // ---------------- Memory Concept ----------------
        System.out.println("\n==================== MEMORY CONCEPT ====================");
        System.out.println("""
When we create:
Student s1 = new Student();

✔ 's1' is reference variable
✔ Object is created in HEAP memory
✔ Instance variables belong to object
""");


        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD MAPPING ====================");
        System.out.println("""
Bank System:
✔ Class → BankAccount
✔ Object → Individual account
✔ Attributes → balance, accountNumber
✔ Methods → deposit(), withdraw()

OOP models real-world systems naturally.
""");


        // ---------------- Why OOP is Powerful ----------------
        System.out.println("\n==================== WHY OOP IS POWERFUL ====================");
        System.out.println("""
OOP allows:
✔ Code Reusability
✔ Scalability
✔ Maintainability
✔ Security (via encapsulation)
✔ Logical structure

Large systems (apps, games, banking software)
are built using OOP.
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ OOP is based on classes and objects.
→ Class is blueprint.
→ Object is instance of class.
→ Attributes store data.
→ Methods define behavior.
→ Objects are created using new keyword.
→ Dot operator accesses data and methods.

OOP is the foundation of Java.
""");
    }
}