// Program: Methods in Java

public class MethodsInJava {

    // ---------------- Example Method with No Parameters ----------------
    static void greet() {
        System.out.println("Hello! Welcome to Java methods.");
    }

    // ---------------- Method with Parameters ----------------
    static void displaySum(int a, int b) {
        int sum = a + b;
        System.out.println("Sum = " + sum);
    }

    // ---------------- Method with Return Value ----------------
    static int square(int num) {
        return num * num;
    }

    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== METHODS IN JAVA ====================");
        System.out.println("""
A method is a BLOCK OF CODE
that performs a specific task.

Methods help us:
✔ Organize code
✔ Avoid repetition
✔ Improve readability
✔ Reuse logic
""");


        // ---------------- What is a Method ----------------
        System.out.println("\n==================== WHAT IS A METHOD ====================");
        System.out.println("""
A method is:
✔ A named block of code
✔ Written once
✔ Called whenever needed

Example:
Instead of writing same code again and again,
we put it inside a method.
""");


        // ---------------- Why Use Methods ----------------
        System.out.println("\n==================== WHY USE METHODS ====================");
        System.out.println("""
Without methods:
✔ Code becomes long
✔ Repetition increases
✔ Difficult to debug

With methods:
✔ Code becomes modular
✔ Easy to test
✔ Easy to maintain
✔ Logic is reusable
""");


        // ---------------- Syntax of a Method ----------------
        System.out.println("\n==================== SYNTAX OF A METHOD ====================");
        System.out.println("""
General syntax:

returnType methodName(parameters) {
    // method body
}

Example:
static int add(int a, int b) {
    return a + b;
}

Parts:
✔ returnType → type of value returned
✔ methodName → name of method
✔ parameters → input values
✔ method body → logic
""");


        // ---------------- Calling a Method ----------------
        System.out.println("\n==================== CALLING A METHOD ====================");
        System.out.println("""
To use a method, we CALL it by its name.

If method has:
✔ No parameters → call directly
✔ Parameters → pass values
✔ Return value → store result
""");

        System.out.println("Calling greet() method:");
        greet();


        // ---------------- Parameters & Arguments ----------------
        System.out.println("\n==================== PARAMETERS & ARGUMENTS ====================");
        System.out.println("""
PARAMETERS:
✔ Variables defined in method declaration
✔ Act as placeholders

ARGUMENTS:
✔ Actual values passed during method call

Example:
Method definition:
    displaySum(int a, int b)

Method call:
    displaySum(10, 20)

Here:
a and b → parameters
10 and 20 → arguments
""");

        System.out.println("Calling displaySum(10, 20):");
        displaySum(10, 20);


        // ---------------- Return Values ----------------
        System.out.println("\n==================== RETURN VALUES ====================");
        System.out.println("""
Some methods RETURN a value.

✔ Return type must be specified
✔ return keyword sends value back
✔ Returned value can be stored or printed
""");

        int result = square(5);
        System.out.println("Returned value from square(5): " + result);


        // ---------------- Method Without Return ----------------
        System.out.println("\n==================== VOID METHODS ====================");
        System.out.println("""
If a method does NOT return anything,
we use return type: void

Example:
    static void greet() { ... }
""");


        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD MAPPING ====================");
        System.out.println("""
Think of methods like machines:

✔ Input → Parameters
✔ Processing → Method body
✔ Output → Return value

ATM Machine:
✔ Insert card → input
✔ Process → logic
✔ Cash → output
""");


        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Forgetting to call the method
✘ Mismatch between parameters & arguments
✘ Returning wrong data type
✘ Writing all code inside main()

Methods exist to KEEP main() clean.
""");


        // ---------------- What Comes Next ----------------
        System.out.println("\n==================== WHAT COMES NEXT ====================");
        System.out.println("""
Now that you understand method basics,
next topics will be:

✔ Method calling flow
✔ Method overloading
✔ Passing arrays to methods
✔ Returning arrays
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Methods are reusable blocks of code.
→ They reduce repetition.
→ Parameters accept input.
→ Arguments supply values.
→ Return values send results back.
→ main() is also a method.

Methods are the FOUNDATION of structured programming.
""");
    }
}
