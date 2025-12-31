// Program: Relational & Unary Operators in Java

public class RelationalAndUnaryOperators {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== RELATIONAL & UNARY OPERATORS ====================");
        System.out.println("""
Operators help Java compare values, check conditions, and modify variables.

In this lesson, we will learn:
1. Relational (Comparison) Operators
2. Unary Operators (operate on a single operand)

Let us explore each with detailed examples.
""");


        // ---------------- 1. Relational Operators ----------------
        System.out.println("\n==================== 1. RELATIONAL OPERATORS ====================");
        System.out.println("""
Relational operators are used to compare two values.
They always return a boolean result: true or false.

Operators:
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to
==  Equal to
!=  Not equal to

Used in decision making, conditions, loops, logic, etc.
""");

        int a = 10, b = 7;
        System.out.println("Example Output:");
        System.out.println("a = " + a + ", b = " + b);
        System.out.println("a > b   → " + (a > b));
        System.out.println("a < b   → " + (a < b));
        System.out.println("a >= b  → " + (a >= b));
        System.out.println("a <= b  → " + (a <= b));
        System.out.println("a == b  → " + (a == b));
        System.out.println("a != b  → " + (a != b));


        // ---------------- Relational with char ----------------
        System.out.println("\n==================== RELATIONAL WITH char ====================");
        System.out.println("""
Characters have integer Unicode values, so relational comparison works on them too.

Example:
    'A' < 'B'  → true
    'Z' == 90  → false (because 'Z' = 90? No, it's 90 is 'Z'? Actually 'Z' = 90 is incorrect. 'Z' = 90+35? No this is wrong. 'Z'=90? Wrong.)

Correct:
    'A' = 65
    'B' = 66
    'Z' = 90

So relational comparisons depend on Unicode values.
""");

        System.out.println("Example Output:");
        System.out.println("'A' < 'B'  → " + ('A' < 'B'));
        System.out.println("'Z' > 'A'  → " + ('Z' > 'A'));
        System.out.println("'A' == 65  → " + ('A' == 65));


        // ---------------- 2. Unary Operators ----------------
        System.out.println("\n==================== 2. UNARY OPERATORS ====================");
        System.out.println("""
Unary operators work on a single operand.

Unary Operators:
+   Unary plus (usually ignored)
-   Unary minus (makes negative)
++  Increment (increase by 1)
--  Decrement (decrease by 1)
!   Logical NOT (reverses boolean)

Let us explore them in detail.
""");


        // ---------------- Unary Plus and Minus ----------------
        System.out.println("\n==================== UNARY PLUS & MINUS ====================");
        System.out.println("""
Unary plus does nothing, but unary minus changes the sign of a number.

Example:
    int x = 5;
    +x → 5
    -x → -5
""");

        int x = 5;
        System.out.println("Example Output:");
        System.out.println("x = " + x);
        System.out.println("+x = " + (+x));
        System.out.println("-x = " + (-x));


        // ---------------- Unary Increment & Decrement ----------------
        System.out.println("\n==================== UNARY INCREMENT & DECREMENT ====================");
        System.out.println("""
Increment and decrement change the value by 1.

++ → Increment
-- → Decrement

They have two forms:
1. Pre-increment (++x) → increases first, then uses value
2. Post-increment (x++) → uses value first, then increases
(Same logic for --)

Example:
    int n = 5;
    ++n → 6
    n++ → 6 (then n becomes 7)
""");

        int n = 5;
        System.out.println("Original n = " + n);
        System.out.println("++n (pre-increment)  = " + (++n)); // becomes 6
        System.out.println("n++ (post-increment) = " + (n++)); // uses 6, becomes 7
        System.out.println("After post-increment n = " + n);

        System.out.println("\nDecrement Example:");
        n = 10;
        System.out.println("Original n = " + n);
        System.out.println("--n (pre-decrement)  = " + (--n)); // becomes 9
        System.out.println("n-- (post-decrement) = " + (n--)); // uses 9, becomes 8
        System.out.println("After post-decrement n = " + n);


        // ---------------- Unary Logical NOT ----------------
        System.out.println("\n==================== UNARY LOGICAL NOT (!) ====================");
        System.out.println("""
Logical NOT (!) reverses a boolean value.

Example:
    boolean flag = true;
    !flag → false
""");

        boolean flag = true;
        System.out.println("Example Output:");
        System.out.println("flag = " + flag);
        System.out.println("!flag = " + (!flag));


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Relational Operators compare values and return boolean result.
   >, <, >=, <=, ==, !=  
→ They work with numbers, characters, and unicode values.

→ Unary Operators operate on a single operand.
   +, -, ++, --, !  
→ Increment & decrement have two forms: prefix and postfix.
→ Logical NOT reverses boolean values.

Relational + Unary operators are widely used in conditions and loops.
""");
    }
}
