// Program: Logical & Bitwise Operators in Java (Detailed)

public class LogicalAndBitwiseOperators {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== LOGICAL & BITWISE OPERATORS ====================");
        System.out.println("""
Operators in Java help us perform decision-making and work with Boolean logic
as well as binary (bit-level) operations.

In this lesson, we will explore:
1. Logical Operators
2. Bitwise Operators (Introduction)

Logical operators work with boolean values.
Bitwise operators work with binary bits (0 and 1).

Let us explore each category with detailed examples.
""");


        // ---------------- 1. Logical Operators ----------------
        System.out.println("\n==================== 1. LOGICAL OPERATORS (Boolean Logic) ====================");
        System.out.println("""
Logical operators are used to combine two or more conditions
and return true or false.

Operators:
&& → Logical AND  (true ONLY if both are true)
|| → Logical OR   (true if at least one condition is true)
!  → Logical NOT  (reverses boolean)

Used mostly in conditions, loops, and decision-making.
""");

        int a = 10, b = 5, c = 10;
        System.out.println("Example Output:");
        System.out.println("(a == b) && (a == c) → " + ((a == b) && (a == c)));
        System.out.println("(a > b) || (b > c)  → " + ((a > b) || (b > c)));
        System.out.println("!(a == c)          → " + (!(a == c)));

        System.out.println("\nMore Examples:");
        boolean cond1 = (5 < 10);
        boolean cond2 = (20 == 30);
        System.out.println("cond1 = " + cond1 + ", cond2 = " + cond2);
        System.out.println("cond1 && cond2 → " + (cond1 && cond2));
        System.out.println("cond1 || cond2 → " + (cond1 || cond2));
        System.out.println("!cond2         → " + (!cond2));


        // ---------------- Short-Circuit Behavior ----------------
        System.out.println("\n==================== SHORT-CIRCUIT LOGICAL OPERATORS ====================");
        System.out.println("""
Short-circuit behavior:
In && and ||, if the first condition decides the result,
the second condition is NOT checked.

Example:
    (false && something) → second part NOT checked
    (true || something)  → second part NOT checked

Short-circuiting increases performance and avoids invalid checks.
""");

        System.out.println("Example Output:");
        System.out.println("(false && (10/0 == 0)) → does NOT crash (second ignored)");
        System.out.println("(true || (10/0 == 0))  → does NOT crash (second ignored)");


        // ---------------- 2. Bitwise Operators ----------------
        System.out.println("\n==================== 2. BITWISE OPERATORS (BINARY LEVEL) ====================");
        System.out.println("""
Bitwise operators operate on bits (0 and 1). They are used in:
✔ low-level programming
✔ encryption
✔ hardware communication
✔ embedded systems

Bitwise Operators:
&  → AND
|  → OR
^  → XOR (exclusive OR)
~  → NOT (bitwise complement)
<< → Left Shift
>> → Right Shift

We use decimal numbers but operations happen in binary.
""");

        int x = 5;   // 0101 in binary
        int y = 3;   // 0011 in binary

        System.out.println("Example Output:");
        System.out.println("x = " + x + " (0101), y = " + y + " (0011)");
        System.out.println("x & y  (AND) = " + (x & y));  // 0001 → 1
        System.out.println("x | y  (OR)  = " + (x | y));  // 0111 → 7
        System.out.println("x ^ y  (XOR) = " + (x ^ y));  // 0110 → 6


        // ---------------- Bitwise NOT ----------------
        System.out.println("\n==================== BITWISE NOT (~) ====================");
        System.out.println("""
Bitwise NOT (~) flips all bits (0 → 1, 1 → 0).
It also changes the sign due to 2's complement representation.

Example:
    ~x  (where x = 5) becomes -6

Binary:
x  =  0000 0101
~x =  1111 1010  (represents -6 in decimal)
""");

        System.out.println("Example Output:");
        System.out.println("~5 = " + (~5));


        // ---------------- Left & Right Shift ----------------
        System.out.println("\n==================== LEFT & RIGHT SHIFT ====================");
        System.out.println("""
Left Shift (<<) shifts bits to the left, multiplying the number by 2.
Right Shift (>>) shifts bits to the right, dividing the number by 2.

Example:
    5 << 1  → 10   (5 * 2)
    8 >> 1  → 4    (8 / 2)

""");

        System.out.println("Example Output:");
        System.out.println("5 << 1 = " + (5 << 1));
        System.out.println("8 >> 1 = " + (8 >> 1));
        System.out.println("10 << 2 = " + (10 << 2)); // 10 * 2^2 = 40
        System.out.println("20 >> 2 = " + (20 >> 2)); // 20 / 2^2 = 5


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Logical Operators:
   && (AND), || (OR), ! (NOT)
   ✔ Used with boolean values
   ✔ Used for conditions and decisions
   ✔ Short-circuits to optimize performance

→ Bitwise Operators:
   & | ^ ~ << >>
   ✔ Work at binary (bit) level
   ✔ Used in low-level programming

Understanding logical & bitwise operators is important
before learning conditions, loops, and binary operations.
""");
    }
}
