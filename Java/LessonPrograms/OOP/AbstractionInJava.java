// Program: OOP Properties - Abstraction in Java

abstract class Vehicle {

    // Abstract method (no body)
    abstract void startEngine();

    // Concrete method
    void fuelType() {
        System.out.println("Vehicles use fuel to operate.");
    }
}

class Car extends Vehicle {

    // Implementing abstract method
    void startEngine() {
        System.out.println("Car engine starts with key ignition.");
    }
}

public class AbstractionInJava {

    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== OOP PROPERTY: ABSTRACTION ====================");
        System.out.println("""
Abstraction means:
✔ Hiding implementation details
✔ Showing only essential features

It focuses on:
✔ What an object does
✔ Not how it does it
""");


        // ---------------- What is Abstraction ----------------
        System.out.println("\n==================== WHAT IS ABSTRACTION ====================");
        System.out.println("""
In Java, abstraction is achieved using:
✔ Abstract classes
✔ Interfaces (later topic)

Abstract class:
✔ Can contain abstract methods
✔ Cannot be instantiated
""");


        // ---------------- Creating Object ----------------
        System.out.println("\n==================== USING ABSTRACTION ====================");
        Vehicle v = new Car();

        v.startEngine();
        v.fuelType();


        // ---------------- Why Abstraction ----------------
        System.out.println("\n==================== WHY ABSTRACTION ====================");
        System.out.println("""
Abstraction helps:
✔ Reduce complexity
✔ Improve security
✔ Provide clean design
✔ Hide sensitive logic
""");


        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD EXAMPLE ====================");
        System.out.println("""
Car Driver:
✔ Presses accelerator
✔ Does NOT know internal engine mechanics

User sees functionality,
but implementation is hidden.

That is abstraction.
""");


        // ---------------- Encapsulation vs Abstraction ----------------
        System.out.println("\n==================== ENCAPSULATION vs ABSTRACTION ====================");
        System.out.println("""
Encapsulation:
✔ Hides data

Abstraction:
✔ Hides implementation

Encapsulation protects data.
Abstraction simplifies complexity.
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Abstraction hides implementation details.
→ Achieved using abstract classes.
→ Cannot create object of abstract class.
→ Child class must implement abstract methods.
→ Makes code cleaner and more structured.
""");
    }
}