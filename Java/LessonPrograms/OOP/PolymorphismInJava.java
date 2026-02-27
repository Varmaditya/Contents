// Program: OOP Property - Polymorphism in Java (Detailed)

class Animal {

    void makeSound() {
        System.out.println("Animal makes a sound.");
    }
}

// ---------------- Child Class 1 ----------------
class Dog extends Animal {

    // Method Overriding (Runtime Polymorphism)
    @Override
    void makeSound() {
        System.out.println("Dog barks.");
    }
}

// ---------------- Child Class 2 ----------------
class Cat extends Animal {

    @Override
    void makeSound() {
        System.out.println("Cat meows.");
    }
}

public class PolymorphismInJava {

    // ---------------- Method Overloading (Compile-time Polymorphism) ----------------
    static int add(int a, int b) {
        return a + b;
    }

    static double add(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== OOP PROPERTY: POLYMORPHISM ====================");
        System.out.println("""
Polymorphism means:
✔ One name
✔ Many forms

It allows an object to behave differently
based on context.

Java supports two types:
1. Compile-time Polymorphism
2. Runtime Polymorphism
""");


        // ==========================================================
        // 1️⃣ COMPILE-TIME POLYMORPHISM
        // ==========================================================

        System.out.println("\n==================== COMPILE-TIME POLYMORPHISM ====================");
        System.out.println("""
Compile-time Polymorphism is achieved using:
✔ Method Overloading

Decision is made at compile time.
""");

        int sum1 = add(10, 20);
        double sum2 = add(5.5, 4.5);

        System.out.println("add(10, 20) = " + sum1);
        System.out.println("add(5.5, 4.5) = " + sum2);

        System.out.println("""
Here:
✔ Same method name 'add'
✔ Different parameter types
✔ Compiler decides which method to call
""");


        // ==========================================================
        // 2️⃣ RUNTIME POLYMORPHISM
        // ==========================================================

        System.out.println("\n==================== RUNTIME POLYMORPHISM ====================");
        System.out.println("""
Runtime Polymorphism is achieved using:
✔ Method Overriding
✔ Inheritance
✔ Parent reference to child object

Decision is made at runtime.
""");

        Animal a;

        a = new Dog();
        a.makeSound();   // Calls Dog version

        a = new Cat();
        a.makeSound();   // Calls Cat version

        System.out.println("""
Here:
✔ Reference type = Animal
✔ Object type = Dog / Cat
✔ Method call decided at runtime
""");


        // ---------------- Why Polymorphism ----------------
        System.out.println("\n==================== WHY POLYMORPHISM? ====================");
        System.out.println("""
Polymorphism allows:
✔ Flexible code
✔ Loose coupling
✔ Code extensibility
✔ Dynamic behavior

New child classes can be added
without changing existing logic.
""");


        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD EXAMPLE ====================");
        System.out.println("""
Remote Control:

Press Power button →
✔ TV turns on
✔ AC turns on
✔ Projector turns on

Same action → Different behavior
This is polymorphism.
""");


        // ---------------- Compile-time vs Runtime ----------------
        System.out.println("\n==================== COMPILE-TIME vs RUNTIME ====================");
        System.out.println("""
COMPILE-TIME POLYMORPHISM:
✔ Method Overloading
✔ Faster
✔ Resolved during compilation

RUNTIME POLYMORPHISM:
✔ Method Overriding
✔ Dynamic Method Dispatch
✔ Resolved during execution
""");


        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Confusing overloading with overriding
✘ Changing method signature while overriding
✘ Not using inheritance for runtime polymorphism
✘ Assuming overloading happens at runtime
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Polymorphism means one name, many forms.
→ Compile-time polymorphism uses method overloading.
→ Runtime polymorphism uses method overriding.
→ Parent reference can refer to child object.
→ Enables flexible and scalable programs.

Polymorphism completes the 4 pillars of OOP.
""");
    }
}