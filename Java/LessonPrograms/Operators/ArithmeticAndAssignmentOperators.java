// Program: Arithmetic & Assignment Operators in Java

public class ArithmeticAndAssignmentOperators {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== ARITHMETIC & ASSIGNMENT OPERATORS ====================");
        System.out.println("""
Operators allow Java to perform mathematics and assign values to variables.

In this program, we study two important operator categories:
1. Arithmetic Operators  → used for mathematical calculations
2. Assignment Operators  → used to store/update values in variables

Let us understand both categories with detailed examples.
""");


        // ---------------- 1. Arithmetic Operators ----------------
        System.out.println("\n==================== 1. ARITHMETIC OPERATORS ====================");
        System.out.println("""
Arithmetic operators perform mathematical operations.

Available Arithmetic Operators:
+  Addition
-  Subtraction
*  Multiplication
/  Division
%  Modulus (Remainder)

Note:
• '/' for integers gives quotient
• '%' always gives remainder

Let us explore with examples:
""");

        int a = 20, b = 6;
        System.out.println("Example Output:");
        System.out.println("a = " + a + ", b = " + b);
        System.out.println("a + b  = " + (a + b));  // Addition
        System.out.println("a - b  = " + (a - b));  // Subtraction
        System.out.println("a * b  = " + (a * b));  // Multiplication
        System.out.println("a / b  = " + (a / b));  // Division
        System.out.println("a % b  = " + (a % b));  // Modulus (remainder)

        System.out.println("\nMore Examples:");
        System.out.println("5 + 3 = " + (5 + 3));
        System.out.println("15 - 4 = " + (15 - 4));
        System.out.println("7 * 5 = " + (7 * 5));
        System.out.println("22 / 4 = " + (22 / 4));
        System.out.println("22 % 4 = " + (22 % 4));


        // ---------------- Arithmetic with double ----------------
        System.out.println("\n==================== ARITHMETIC WITH DECIMALS ====================");
        System.out.println("""
Arithmetic operators also work with float and double values.

Example:
    double x = 10.5, y = 2.0;
""");

        double x = 10.5, y = 2.0;
        System.out.println("Example Output:");
        System.out.println("x = " + x + ", y = " + y);
        System.out.println("x + y = " + (x + y));
        System.out.println("x - y = " + (x - y));
        System.out.println("x * y = " + (x * y));
        System.out.println("x / y = " + (x / y));
        System.out.println("10.5 % 2.0 = " + (x % y)); // floating remainder


        // ---------------- Arithmetic with char ----------------
        System.out.println("\n==================== ARITHMETIC WITH CHAR ====================");
        System.out.println("""
Characters have numeric Unicode values and can participate in arithmetic.

Example:
    char c = 'A';
    c + 1  → 66 (because 'A' = 65)

""");

        char c = 'A';
        System.out.println("Example Output:");
        System.out.println("c = " + c);
        System.out.println("c + 1 = " + (c + 1));
        System.out.println("'Z' - 1 = " + ('Z' - 1));


        // ---------------- 2. Assignment Operators ----------------
        System.out.println("\n==================== 2. ASSIGNMENT OPERATORS ====================");
        System.out.println("""
Assignment operators assign values to variables.
They can also update values using +=, -=, *=, /=, %=

Basic Assignment:
    x = 10;  // store value

Compound Assignments:
    x += 5  → x = x + 5
    x -= 3  → x = x - 3
    x *= 2  → x = x * 2
    x /= 4  → x = x / 4
    x %= 3  → x = x % 3

Let us explore with a real example:
""");

        int num = 50;
        System.out.println("Initial num = " + num);

        num += 10;   // num = num + 10
        System.out.println("After num += 10  → " + num);

        num -= 5;    // num = num - 5
        System.out.println("After num -= 5   → " + num);

        num *= 2;    // num = num * 2
        System.out.println("After num *= 2   → " + num);

        num /= 5;    // num = num / 5
        System.out.println("After num /= 5   → " + num);

        num %= 3;    // num = num % 3
        System.out.println("After num %= 3   → " + num);


        // ---------------- Assignment with Strings ----------------
        System.out.println("\n==================== ASSIGNMENT WITH STRINGS ====================");
        System.out.println("""
Strings can use += to concatenate text.

Example:
    String msg = \"Hello\";
    msg += \" World\"; // Hello World
""");

        String msg = "Hello";
        msg += " Java";
        System.out.println("Example Output: " + msg);


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Arithmetic Operators perform mathematical operations: +, -, *, /, %
→ Arithmetic works with int, float, double, and char.
→ Assignment Operators store and update values.
→ Compound assignments (+=, -=, *=, /=, %=) modify variable values quickly.
→ Strings use += for concatenation.

Understanding arithmetic and assignment operators is essential for calculations in Java.
""");
    }
}
