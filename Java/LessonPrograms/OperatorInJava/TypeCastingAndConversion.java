// Program: Type Conversion and Type Casting in Java

public class TypeCastingAndConversion {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== TYPE CONVERSION & TYPE CASTING ====================");
        System.out.println("""
In Java, different data types can be converted from one type to another.

There are two main concepts:
1. Type Conversion  (automatic / implicit)
2. Type Casting     (manual / explicit)

Related ideas:
- Widening & Narrowing conversions
- Type promotion in expressions
- Basic rules for safe casting

Let us understand each in detail.
""");


        // ---------------- 1. Widening Type Conversion (Implicit) ----------------
        System.out.println("\n==================== 1. WIDENING TYPE CONVERSION (IMPLICIT) ====================");
        System.out.println("""
Widening conversion means converting a smaller type to a larger type.
This is done AUTOMATICALLY by Java (no cast required).

Examples of widening:
    byte → short → int → long → float → double
    char → int → long → float → double

Because there is no data loss (in general), Java allows this automatically.

Example:
    int num = 10;
    double d = num;    // int to double (widening)
""");

        int num = 10;
        double d = num;  // implicit widening
        byte b = 100;
        int i = b;       // byte to int
        char ch = 'A';
        int chCode = ch; // char to int (Unicode code)

        System.out.println("Example Output (Widening):");
        System.out.println("int num = " + num);
        System.out.println("double d = num → " + d);
        System.out.println("byte b = " + b + " → int i = " + i);
        System.out.println("char ch = '" + ch + "' → int chCode = " + chCode);


        // ---------------- 2. Narrowing Type Casting (Explicit) ----------------
        System.out.println("\n==================== 2. NARROWING TYPE CASTING (EXPLICIT) ====================");
        System.out.println("""
Narrowing conversion means converting a larger type to a smaller type.
This can cause DATA LOSS or change in value.
Java does NOT allow this automatically. We must use EXPLICIT CASTING.

Examples of narrowing:
    double → float → long → int → short → byte
    int → char
    long → int

Syntax:
    targetType variable = (targetType) value;

Example:
    double x = 9.7;
    int y = (int) x;   // y becomes 9 (fractional part lost)
""");

        double x1 = 9.7;
        int y1 = (int) x1;       // fractional part lost
        int big = 130;
        byte small = (byte) big; // possible overflow

        System.out.println("Example Output (Narrowing):");
        System.out.println("double x1 = " + x1 + " → int y1 = (int)x1 → " + y1);
        System.out.println("int big = " + big + " → byte small = (byte)big → " + small);
        System.out.println("Note: 130 is outside byte range (-128 to 127), so value wraps around.");


        // ---------------- 3. Widening vs Narrowing Summary ----------------
        System.out.println("\n==================== 3. WIDENING vs NARROWING ====================");
        System.out.println("""
Widening (Safe, Automatic):
✔ Smaller type → Larger type
✔ No explicit cast required
✔ Little or no risk of data loss
Example:
    int → long → float → double

Narrowing (Risky, Manual):
✔ Larger type → Smaller type
✔ Explicit cast REQUIRED
✔ May lose data or cause overflow
Example:
    double → int
    int → byte
""");


        // ---------------- 4. Type Promotion in Expressions ----------------
        System.out.println("\n==================== 4. TYPE PROMOTION IN EXPRESSIONS ====================");
        System.out.println("""
When different data types are used in an expression,
Java automatically promotes them to a common type before evaluation.

Important rules:
1. All byte, short, and char are promoted to int in expressions.
2. If one operand is long → result is long.
3. If one operand is float → result is float.
4. If one operand is double → result is double.

Example:
    byte a = 10, b = 20;
    int c = a + b;  // a and b are promoted to int

    int x = 5;
    double y = 2.5;
    double z = x + y;  // x promoted to double
""");

        byte ba = 10, bb = 20;
        // byte bsum = ba + bb; // NOT allowed: ba+bb is int
        int bsum = ba + bb;

        int xi = 5;
        double yd = 2.5;
        double zd = xi + yd;

        System.out.println("Example Output (Type Promotion):");
        System.out.println("byte ba = " + ba + ", byte bb = " + bb);
        System.out.println("ba + bb stored in int bsum = " + bsum);
        System.out.println("int xi = " + xi + ", double yd = " + yd);
        System.out.println("xi + yd stored in double zd = " + zd);


        // ---------------- 5. Casting with char and int ----------------
        System.out.println("\n==================== 5. CASTING BETWEEN char AND int ====================");
        System.out.println("""
char stores Unicode values internally.
We can cast between char and int.

Example:
    char ch = 'A';         // Unicode 65
    int code = ch;         // implicit widening

    int n = 66;
    char c = (char) n;     // explicit narrowing
""");

        char ch1 = 'A';
        int code1 = ch1;          // widening
        int n1 = 66;
        char ch2 = (char) n1;     // narrowing to char

        System.out.println("Example Output:");
        System.out.println("char ch1 = '" + ch1 + "' → int code1 = " + code1);
        System.out.println("int n1 = " + n1 + " → char ch2 = (char)n1 → '" + ch2 + "'");


        // ---------------- 6. Type Casting Rules ----------------
        System.out.println("\n==================== 6. TYPE CASTING RULES ====================");
        System.out.println("""
Basic rules to remember:

1. Widening Conversion:
   ✔ Done automatically (implicit)
   ✔ No cast required
   ✔ Safer conversion
   Examples:
       int → long
       int → double
       char → int

2. Narrowing Conversion:
   ✔ Must use explicit cast
   ✔ May lose data or cause overflow
   Examples:
       double → int
       long → int
       int → byte

3. boolean cannot be cast to/from any other type.

4. In expressions:
   ✔ byte, short, char → promoted to int
   ✔ If double is present → entire expression becomes double
   ✔ If float is present (but no double) → result becomes float
""");


        // ---------------- 7. Combined Example ----------------
        System.out.println("\n==================== 7. COMBINED EXAMPLE ====================");
        System.out.println("""
Let us see a combined example using multiple types:

    byte  b  = 10;
    int   i  = 20;
    double d = 5.5;

    double result = b + i + d;

Explanation:
    b + i  → int (b promoted to int)
    int + d → double (int promoted to double)
    final result → double
""");

        byte bb1 = 10;
        int ii1 = 20;
        double dd1 = 5.5;
        double result = bb1 + ii1 + dd1;

        System.out.println("Example Output:");
        System.out.println("byte bb1 = " + bb1 + ", int ii1 = " + ii1 + ", double dd1 = " + dd1);
        System.out.println("bb1 + ii1 + dd1 = " + result + " (result is double)");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Type Conversion (implicit) happens automatically for widening conversions.
→ Widening: smaller → larger type (int → long → float → double).
→ Narrowing requires explicit casting and may lose data (double → int, int → byte).
→ Type promotion in expressions:
   - byte, short, char → promoted to int
   - mixed types → promoted to the largest type (long, float, double)
→ boolean is NOT compatible with numeric casting.
→ Always be careful with narrowing conversions to avoid unexpected results.

Understanding type conversion and casting is essential for correct arithmetic and expressions in Java.
""");
    }
}
