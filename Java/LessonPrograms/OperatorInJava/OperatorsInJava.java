// Program: Operators in Java

public class OperatorsInJava {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== OPERATORS IN JAVA ====================");
        System.out.println("""
Operators are special symbols that perform operations on variables and values.
They help in mathematical calculations, comparisons, decision-making, logic, and assignments.

Java Operators are classified into:
1. Arithmetic Operators
2. Assignment Operators
3. Relational (Comparison) Operators
4. Logical Operators
5. Unary Operators
6. Ternary Operator
7. Bitwise Operators (will be studied at intermediate level)

Let us explore each type in detail.
""");


        // ---------------- 1. Arithmetic Operators ----------------
        System.out.println("\n==================== 1. ARITHMETIC OPERATORS ====================");
        System.out.println("""
Arithmetic operators are used to perform mathematical calculations.

Operators:
+  (Addition)
-  (Subtraction)
*  (Multiplication)
/  (Division)
%  (Modulus or Remainder)

Example:
    int a = 10, b = 3;
    a + b  → 13
    a - b  → 7
    a * b  → 30
    a / b  → 3
    a % b  → 1
""");

        int a = 10, b = 3;
        System.out.println("Example Output:");
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        System.out.println("a / b = " + (a / b));
        System.out.println("a % b = " + (a % b));


        // ---------------- 2. Assignment Operators ----------------
        System.out.println("\n==================== 2. ASSIGNMENT OPERATORS ====================");
        System.out.println("""
Assignment operators assign values to variables.

Operators:
=    (Assign)
+=   (Add and assign)
-=   (Subtract and assign)
*=   (Multiply and assign)
/=   (Divide and assign)
%=   (Modulus and assign)

Example:
    int x = 5;
    x += 2  → x = x + 2  → 7
""");

        int x = 5;
        System.out.println("Example Output:");
        System.out.println("Original x = " + x);
        x += 2;
        System.out.println("After x += 2, x = " + x);


        // ---------------- 3. Relational Operators ----------------
        System.out.println("\n==================== 3. RELATIONAL OPERATORS ====================");
        System.out.println("""
Relational operators are used for comparison. They return true or false.

Operators:
>   (Greater than)
<   (Less than)
>=  (Greater than or equal to)
<=  (Less than or equal to)
==  (Equal to)
!=  (Not equal to)

Example:
    int a = 10, b = 3;
    a > b  → true
""");

        System.out.println("Example Output:");
        System.out.println("a > b  → " + (a > b));
        System.out.println("a < b  → " + (a < b));
        System.out.println("a == b → " + (a == b));
        System.out.println("a != b → " + (a != b));


        // ---------------- 4. Logical Operators ----------------
        System.out.println("\n==================== 4. LOGICAL OPERATORS ====================");
        System.out.println("""
Logical operators are used to combine multiple conditions.
They return true or false.

Operators:
&& → Logical AND  (Both conditions true)
|| → Logical OR   (At least one condition true)
!  → Logical NOT  (Reverses boolean value)

Example:
    (a > b) && (a == 10)  → true
""");

        System.out.println("Example Output:");
        System.out.println("(a > b) && (a == 10) → " + ((a > b) && (a == 10)));
        System.out.println("(a < b) || (a == 10) → " + ((a < b) || (a == 10)));
        System.out.println("!(a > b)              → " + (!(a > b)));


        // ---------------- 5. Unary Operators ----------------
        System.out.println("\n==================== 5. UNARY OPERATORS ====================");
        System.out.println("""
Unary operators operate on a single operand.

Operators:
+   (Positive)
-   (Negative)
++  (Increment)
--  (Decrement)
!   (Logical NOT)

Example:
    int n = 5;
    ++n  → 6  (pre-increment)
    n++  → 6 (then becomes 7)
""");

        int n = 5;
        System.out.println("Example Output:");
        System.out.println("Original n = " + n);
        System.out.println("++n (pre-increment) = " + (++n)); // becomes 6
        System.out.println("n++ (post-increment) = " + (n++)); // prints 6 then becomes 7
        System.out.println("After post-increment, n = " + n);


        // ---------------- 6. Ternary Operator ----------------
        System.out.println("\n==================== 6. TERNARY OPERATOR ====================");
        System.out.println("""
The ternary operator is a compact form of if-else.

Syntax:
    condition ? value_if_true : value_if_false;

Example:
    int age = 18;
    String result = (age >= 18) ? "Adult" : "Minor";
""");

        int age = 18;
        String result = (age >= 18) ? "Adult" : "Minor";
        System.out.println("Example Output: " + result);


        // ---------------- 7. Bitwise Operators ----------------
        System.out.println("\n==================== 7. BITWISE OPERATORS (INTRODUCTION) ====================");
        System.out.println("""
Bitwise operators operate on bits (0 and 1). They are used in low-level programming.

Operators:
&  → AND
|  → OR
^  → XOR
~  → NOT
<< → Left Shift
>> → Right Shift

We will learn bitwise operators in detail in intermediate-level Java.
""");

        System.out.println("Example Output (simple):");
        System.out.println("5 & 3 = " + (5 & 3));
        System.out.println("5 | 3 = " + (5 | 3));


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Operators perform actions on variables and values.
→ Arithmetic: +, -, *, /, %
→ Assignment: =, +=, -=, *=, /=, %=
→ Relational: >, <, >=, <=, ==, !=
→ Logical: &&, ||, !
→ Unary: ++, --, +, -, !
→ Ternary: condition ? true : false
→ Bitwise: & | ^ ~ << >> (will study later)

Operators are fundamental for calculations, logic, and decision-making in Java.
""");
    }
}
