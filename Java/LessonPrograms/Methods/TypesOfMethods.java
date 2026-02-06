// Program: Types of Methods in Java

public class TypesOfMethods {

    // ---------------- 1. Void Method Without Parameters ----------------
    static void welcomeMessage() {
        System.out.println("Welcome to Java Programming!");
    }

    // ---------------- 2. Void Method With Parameters ----------------
    static void printSum(int a, int b) {
        int sum = a + b;
        System.out.println("Sum = " + sum);
    }

    // ---------------- 3. Method With Return Value and No Parameters ----------------
    static int getFixedNumber() {
        return 10;
    }

    // ---------------- 4. Method With Return Value and Parameters ----------------
    static int multiply(int x, int y) {
        return x * y;
    }

    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== TYPES OF METHODS IN JAVA ====================");
        System.out.println("""
In Java, methods can be classified based on:
✔ Whether they return a value
✔ Whether they accept parameters

Understanding these types helps you:
✔ Design clean programs
✔ Reuse logic efficiently
✔ Choose the right method structure
""");


        // ---------------- Classification of Methods ----------------
        System.out.println("\n==================== CLASSIFICATION OF METHODS ====================");
        System.out.println("""
Based on return type and parameters,
methods are commonly classified into:

1. Void methods
2. Methods with return value
3. Methods with parameters
4. Methods without parameters

We will explore each type with examples.
""");


        // ---------------- Void Methods ----------------
        System.out.println("\n==================== VOID METHODS ====================");
        System.out.println("""
Void methods:
✔ Do NOT return any value
✔ Use return type: void
✔ Perform an action (printing, displaying, updating)

Syntax:
    static void methodName() {
        // logic
    }
""");

        System.out.println("Calling a void method without parameters:");
        welcomeMessage();


        // ---------------- Void Method With Parameters ----------------
        System.out.println("\n==================== VOID METHOD WITH PARAMETERS ====================");
        System.out.println("""
These methods:
✔ Accept input values
✔ Perform operation
✔ Display result directly
✔ Do not send result back

Example:
    static void printSum(int a, int b)
""");

        System.out.println("Calling printSum(10, 20):");
        printSum(10, 20);


        // ---------------- Methods With Return Value ----------------
        System.out.println("\n==================== METHODS WITH RETURN VALUE ====================");
        System.out.println("""
These methods:
✔ Perform calculation
✔ Return result to caller
✔ Use return keyword
✔ Must specify return type

Syntax:
    static int methodName() {
        return value;
    }
""");

        int num = getFixedNumber();
        System.out.println("Returned value from getFixedNumber(): " + num);


        // ---------------- Method With Return Value and Parameters ----------------
        System.out.println("\n==================== RETURN TYPE + PARAMETERS ====================");
        System.out.println("""
These methods:
✔ Accept input
✔ Process data
✔ Return result

This is the MOST COMMON type of method.

Example:
    static int multiply(int x, int y)
""");

        int product = multiply(5, 4);
        System.out.println("Returned value from multiply(5, 4): " + product);


        // ---------------- Methods Without Parameters ----------------
        System.out.println("\n==================== METHODS WITHOUT PARAMETERS ====================");
        System.out.println("""
Methods without parameters:
✔ Do not require input
✔ Work on fixed or internal data
✔ Useful for constant tasks

Example:
    static int getFixedNumber()
""");


        // ---------------- Methods With Parameters ----------------
        System.out.println("\n==================== METHODS WITH PARAMETERS ====================");
        System.out.println("""
Methods with parameters:
✔ Accept external values
✔ Make methods flexible
✔ Allow reuse with different data

Example:
    multiply(2, 3)
    multiply(5, 7)
""");


        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD MAPPING ====================");
        System.out.println("""
Think of methods like devices:

1. Doorbell:
✔ No input
✔ No output
→ Void method without parameters

2. Calculator Display:
✔ Input numbers
✔ Shows result
→ Void method with parameters

3. ATM Balance Check:
✔ Returns balance
→ Method with return value
""");


        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Forgetting return statement in return-type method
✘ Returning wrong data type
✘ Ignoring returned value
✘ Using void when return is required
""");


        // ---------------- What Comes Next ----------------
        System.out.println("\n==================== WHAT COMES NEXT ====================");
        System.out.println("""
Now that you know method types,
next topics will include:

✔ Method overloading
✔ Passing arrays to methods
✔ Returning values from methods
✔ Scope of variables in methods
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Methods are classified by return type and parameters.
→ Void methods perform actions.
→ Return methods send data back.
→ Parameters make methods flexible.
→ Choosing correct method type improves design.

Methods are the building blocks of Java programs.
""");
    }
}
