// Program: Variables and Constants in Java

public class VariablesAndConstants {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== VARIABLES & CONSTANTS ====================");
        System.out.println("""
Variables and constants are used to store data in a Java program.

- A VARIABLE is a container whose value can change during execution.
- A CONSTANT is a fixed value that cannot be changed once assigned.

Let us learn how to declare, initialize, and use variables and constants in Java.
""");


        // ---------------- Variables: Declaration ----------------
        System.out.println("\n==================== 1. VARIABLE DECLARATION ====================");
        System.out.println("""
Declaration means telling Java what kind of data (type) a variable will store.

Syntax:
    dataType variableName;

Examples:
    int age;
    double price;
    String name;

No value is stored yet. Memory is reserved for the variable.
""");

        System.out.println("Example Output:");
        System.out.println("Variables declared: int age; double price; String name;");


        // ---------------- Variables: Initialization ----------------
        System.out.println("\n==================== 2. VARIABLE INITIALIZATION ====================");
        System.out.println("""
Initialization means assigning a value to a variable for the first time.

Syntax:
    variableName = value;

Examples:
    age = 25;
    price = 199.99;
    name = \"Aditya\";

You can also declare and initialize in one line:
    int number = 100;
""");

        System.out.println("Example Output:");
        System.out.println("Initialized variables: age = 25, price = 199.99, name = Aditya");


        // ---------------- Using Variables ----------------
        System.out.println("\n==================== 3. USING VARIABLES ====================");
        System.out.println("""
Once declared and initialized, variables can be used in print statements
or in calculations (details of operators will come later).

Example:
    int a = 5;
    int b = 10;
    System.out.println(a);
    System.out.println(b);
""");

        int a = 5;
        int b = 10;
        System.out.println("Example Output:");
        System.out.println("a = " + a);
        System.out.println("b = " + b);


        // ---------------- Constants (final keyword) ----------------
        System.out.println("\n==================== 4. CONSTANTS (final KEYWORD) ====================");
        System.out.println("""
A CONSTANT is a variable whose value cannot be changed after initialization.

We use the keyword 'final' to create constants.

Syntax:
    final dataType CONSTANT_NAME = value;

Rules:
✔ Must be assigned a value only once.
✔ Written in UPPERCASE by convention.
✔ Attempting to change a final variable causes an error.

Examples:
    final int MAX_STUDENTS = 100;
    final double PI = 3.14159;
""");

        final int MAX_STUDENTS = 100;
        final double PI = 3.14159;

        System.out.println("Example Output:");
        System.out.println("Constant MAX_STUDENTS = " + MAX_STUDENTS);
        System.out.println("Constant PI = " + PI);


        // ---------------- Difference between Variable & Constant ----------------
        System.out.println("\n==================== 5. VARIABLE vs CONSTANT ====================");
        System.out.println("""
VARIABLE:
- Value can change.
- Declared normally without 'final'.

CONSTANT:
- Value CANNOT change once assigned.
- Declared using 'final'.
""");

        int changeable = 50;
        final int FIXED_VALUE = 500;

        System.out.println("Example Output:");
        System.out.println("Variable value initially: " + changeable);
        changeable = 60;
        System.out.println("Variable updated to: " + changeable);
        System.out.println("Constant value remains: " + FIXED_VALUE);


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Variables store changeable data.
→ Declaration: dataType variableName;
→ Initialization: variableName = value;
→ Use variables in print statements or expressions.
→ Constants are created using FINAL.
→ Constant values CANNOT change and use uppercase naming.

Mastering variables & constants is essential for all Java programs.
""");

    }
}
