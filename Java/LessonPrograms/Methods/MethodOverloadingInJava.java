// Program: Method Overloading in Java

public class MethodOverloadingInJava {

    // ---------------- Overloaded Methods: Same Name, Different Parameters ----------------

    // Method 1: No parameters
    static void display() {
        System.out.println("Display method with NO parameters");
    }

    // Method 2: One parameter
    static void display(int a) {
        System.out.println("Display method with ONE parameter: " + a);
    }

    // Method 3: Two parameters
    static void display(int a, int b) {
        System.out.println("Display method with TWO parameters: " + (a + b));
    }

    // Method 4: Different parameter types
    static void display(double a) {
        System.out.println("Display method with DOUBLE parameter: " + a);
    }

    // ---------------- Overloading with Return Type ----------------
    static int calculate(int a, int b) {
        return a + b;
    }

    static double calculate(double a, double b) {
        return a * b;
    }

    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== METHOD OVERLOADING IN JAVA ====================");
        System.out.println("""
Method Overloading allows multiple methods
to have the SAME NAME but DIFFERENT PARAMETERS.

It helps Java programs:
✔ Look clean
✔ Be readable
✔ Be intuitive
✔ Handle similar operations easily
""");


        // ---------------- What is Method Overloading ----------------
        System.out.println("\n==================== WHAT IS METHOD OVERLOADING ====================");
        System.out.println("""
Method Overloading means:
✔ Same method name
✔ Different parameter list

Java decides which method to call
based on the arguments passed during method call.
""");


        // ---------------- Why Method Overloading is Needed ----------------
        System.out.println("\n==================== WHY METHOD OVERLOADING IS NEEDED ====================");
        System.out.println("""
Without method overloading:
✔ We need different method names for same operation
✔ Code becomes confusing
✔ Poor readability

With method overloading:
✔ Same logical operation uses same method name
✔ Code is easier to understand
✔ Programs feel natural to read
""");


        // ---------------- Simple Example ----------------
        System.out.println("\n==================== SIMPLE OVERLOADING EXAMPLE ====================");
        System.out.println("""
Consider a display() method.

We want:
✔ display()
✔ display(int)
✔ display(int, int)

Instead of multiple names,
we overload the same method.
""");

        display();
        display(10);
        display(10, 20);
        display(5.5);


        // ---------------- Rules of Method Overloading ----------------
        System.out.println("\n==================== RULES OF METHOD OVERLOADING ====================");
        System.out.println("""
RULE 1: Method name MUST be same

RULE 2: Parameter list MUST be different
    ✔ Number of parameters
    ✔ Type of parameters
    ✔ Order of parameters

RULE 3: Return type ALONE is NOT sufficient
    ✘ Cannot overload only by changing return type

RULE 4: Overloading happens at COMPILE TIME
""");


        // ---------------- Overloading with Parameter Count ----------------
        System.out.println("\n==================== OVERLOADING BY PARAMETER COUNT ====================");
        System.out.println("""
Example:
✔ display()
✔ display(int)
✔ display(int, int)
""");


        // ---------------- Overloading with Parameter Type ----------------
        System.out.println("\n==================== OVERLOADING BY PARAMETER TYPE ====================");
        System.out.println("""
Example:
✔ display(int)
✔ display(double)
""");


        // ---------------- Overloading with Parameter Order ----------------
        System.out.println("\n==================== OVERLOADING BY PARAMETER ORDER ====================");
        System.out.println("""
Example:
✔ method(int, double)
✔ method(double, int)

(Types are same but order is different)
""");


        // ---------------- Return Type Rule ----------------
        System.out.println("\n==================== RETURN TYPE RULE ====================");
        System.out.println("""
THIS IS IMPORTANT:

✘ Method overloading CANNOT be done
   by changing return type only.

Example (INVALID):
    int add(int a, int b)
    double add(int a, int b)
""");


        // ---------------- Overloading with Return Value (Valid Case) ----------------
        System.out.println("\n==================== OVERLOADING WITH RETURN TYPE (VALID) ====================");
        System.out.println("""
Return type CAN change
ONLY IF parameter list is different.
""");

        int sum = calculate(5, 3);
        double product = calculate(2.5, 4.0);

        System.out.println("calculate(5, 3) returns: " + sum);
        System.out.println("calculate(2.5, 4.0) returns: " + product);


        // ---------------- Compile-Time Polymorphism ----------------
        System.out.println("\n==================== COMPILE-TIME POLYMORPHISM ====================");
        System.out.println("""
Method overloading is also called:
✔ Compile-time Polymorphism

Because:
✔ Method call is resolved at compile time
✔ Based on method signature
""");


        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD MAPPING ====================");
        System.out.println("""
Calculator Example:
✔ add(2, 3)
✔ add(2.5, 3.5)
✔ add(2, 3, 4)

Same operation → Different inputs → Same method name
""");


        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Trying to overload by return type only
✘ Confusing overloading with overriding
✘ Same parameter list accidentally
✘ Assuming runtime decision

Remember:
Overloading is compile-time.
""");


        // ---------------- What Comes Next ----------------
        System.out.println("\n==================== WHAT COMES NEXT ====================");
        System.out.println("""
Next topics after method overloading:

✔ Passing arrays to methods
✔ Returning arrays from methods
✔ Method calling flow (stack concept)
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Method overloading allows same method name with different parameters.
→ Improves readability and usability.
→ Parameter list must differ.
→ Return type alone cannot overload methods.
→ Overloading happens at compile time.

Method overloading makes Java code elegant and flexible.
""");
    }
}
