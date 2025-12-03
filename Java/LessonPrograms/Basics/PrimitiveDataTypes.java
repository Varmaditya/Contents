// Program: Primitive Data Types in Java

import java.util.Scanner;

public class PrimitiveDataTypes {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // ---------------- Introduction ----------------
        System.out.println("\n==================== PRIMITIVE DATA TYPES ====================");
        System.out.println("""
Primitive data types are the MOST basic data types in Java.
There are exactly 8 primitive types. They store simple, fixed-size values.

Characteristics of Primitive Types:
✔ Store value directly (not a reference)
✔ Faster & memory-efficient
✔ Always lowercase (int, boolean, double)
✔ Have fixed size (defined by JVM)
✔ Cannot call methods on them

The 8 primitive types:
1. byte
2. short
3. int
4. long
5. float
6. double
7. char
8. boolean

Let us explore each one in detail.
""");

        // ---------------- byte ----------------
        System.out.println("\n==================== 1. byte ====================");
        System.out.println("""
byte → 1-byte integer type
Range: -128 to 127
Used when you want to save memory in large arrays.

Example:
    byte a = 100;
""");
        byte b1 = 100;
        System.out.println("Example Output: byte b1 = " + b1);

        System.out.print("Enter a byte value: ");
        byte userByte = sc.nextByte();
        System.out.println("You entered (byte): " + userByte);


        // ---------------- short ----------------
        System.out.println("\n==================== 2. short ====================");
        System.out.println("""
short → 2-byte integer type
Range: -32,768 to 32,767
Used for moderate-sized integers.

Example:
    short s = 30000;
""");
        short s1 = 30000;
        System.out.println("Example Output: short s1 = " + s1);

        System.out.print("Enter a short value: ");
        short userShort = sc.nextShort();
        System.out.println("You entered (short): " + userShort);


        // ---------------- int ----------------
        System.out.println("\n==================== 3. int ====================");
        System.out.println("""
int → 4-byte integer type
Range: -2,147,483,648 to 2,147,483,647
Most commonly used integer type.

Example:
    int marks = 95;
""");
        int i1 = 95;
        System.out.println("Example Output: int i1 = " + i1);

        System.out.print("Enter an int value: ");
        int userInt = sc.nextInt();
        System.out.println("You entered (int): " + userInt);


        // ---------------- long ----------------
        System.out.println("\n==================== 4. long ====================");
        System.out.println("""
long → 8-byte integer type
Used for very large numbers.
Must end with 'L' or 'l'.

Example:
    long population = 8000000000L;
""");
        long l1 = 8000000000L;
        System.out.println("Example Output: long l1 = " + l1);

        System.out.print("Enter a long value: ");
        long userLong = sc.nextLong();
        System.out.println("You entered (long): " + userLong);


        // ---------------- float ----------------
        System.out.println("\n==================== 5. float ====================");
        System.out.println("""
float → 4-byte decimal type
Stores up to 7 decimal digits (approx).
Must end with 'f' or 'F'.

Example:
    float price = 99.75f;
""");
        float f1 = 99.75f;
        System.out.println("Example Output: float f1 = " + f1);

        System.out.print("Enter a float value: ");
        float userFloat = sc.nextFloat();
        System.out.println("You entered (float): " + userFloat);


        // ---------------- double ----------------
        System.out.println("\n==================== 6. double ====================");
        System.out.println("""
double → 8-byte decimal type
Stores up to 15 decimal digits (approx)
Default type for decimal numbers.

Example:
    double salary = 55000.456;
""");
        double d1 = 55000.456;
        System.out.println("Example Output: double d1 = " + d1);

        System.out.print("Enter a double value: ");
        double userDouble = sc.nextDouble();
        System.out.println("You entered (double): " + userDouble);


        // ---------------- char ----------------
        System.out.println("\n==================== 7. char ====================");
        System.out.println("""
char → 2 bytes (stores a single Unicode character)
Enclosed in single quotes: 'A', '9', '$'

Example:
    char letter = 'J';

char also stores Unicode values:
    char unicodeChar = 65;   // 'A'
""");

        char c1 = 'J';
        char c2 = 65;
        System.out.println("Example Output:");
        System.out.println("char c1 = " + c1);
        System.out.println("char c2 (Unicode 65) = " + c2);

        System.out.print("Enter a single character: ");
        char userChar = sc.next().charAt(0);
        System.out.println("You entered (char): " + userChar);


        // ---------------- boolean ----------------
        System.out.println("\n==================== 8. boolean ====================");
        System.out.println("""
boolean → Stores ONLY true or false
Used in conditions and logical operations.

Example:
    boolean isJavaEasy = true;
""");
        boolean flag = true;
        System.out.println("Example Output: boolean flag = " + flag);

        System.out.print("Enter true or false: ");
        boolean userBoolean = sc.nextBoolean();
        System.out.println("You entered (boolean): " + userBoolean);


        // ---------------- Default Values ----------------
        System.out.println("\n==================== DEFAULT VALUES OF PRIMITIVES ====================");
        System.out.println("""
Primitive types have default values when used inside a class (as fields):
byte     → 0
short    → 0
int      → 0
long     → 0L
float    → 0.0f
double   → 0.0
char     → '\\u0000'  (null character)
boolean  → false

Note:
Variables inside MAIN do NOT get default values.
They MUST be initialized before use.
""");

        System.out.println("Default values cannot be shown here (need class fields).");


        // ---------------- Memory Sizes ----------------
        System.out.println("\n==================== MEMORY SIZE COMPARISON ====================");
        System.out.println("""
byte    → 1 byte
short   → 2 bytes
int     → 4 bytes
long    → 8 bytes
float   → 4 bytes
double  → 8 bytes
char    → 2 bytes
boolean → ~1 bit (depends on JVM)
""");

        System.out.println("These sizes are fixed by Java language specification.");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Java has exactly 8 primitive data types.
→ Used for storing simple values — fast and memory-efficient.
→ byte, short, int, long → whole numbers
→ float, double → decimal numbers
→ char → single Unicode character
→ boolean → true/false
→ Primitives store values directly (not references).
""");

        sc.close();
    }
}
