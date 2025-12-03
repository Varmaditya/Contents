// Program: Data Types in Java

public class DataTypes {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== DATA TYPES IN JAVA ====================");
        System.out.println("""
Data types define the type of data a variable can store.

In Java, data types are mainly divided into:
1. Primitive Data Types
2. Non-Primitive (Reference) Data Types

Let us explore each category in detail.
""");


        // ---------------- Primitive Data Types ----------------
        System.out.println("\n==================== 1. PRIMITIVE DATA TYPES ====================");
        System.out.println("""
Primitive data types are the most basic data types in Java.
They store simple values directly in memory.

There are 8 primitive types:

1) byte    → 1 byte  → -128 to 127
2) short   → 2 bytes → -32,768 to 32,767
3) int     → 4 bytes → Most commonly used integer type
4) long    → 8 bytes → Larger integer values (suffix L needed)
5) float   → 4 bytes → Decimal numbers (suffix f needed)
6) double  → 8 bytes → Default decimal type
7) char    → 2 bytes → Single character ('A', '#')
8) boolean → 1 bit   → true/false
""");

        // Demonstrating primitive data types
        byte b = 10;
        short s = 200;
        int num = 5000;
        long bigNum = 123456789L;
        float f = 5.75f;
        double d = 99.99;
        char ch = 'J';
        boolean flag = true;

        System.out.println("Example Output:");
        System.out.println("byte b = " + b);
        System.out.println("short s = " + s);
        System.out.println("int num = " + num);
        System.out.println("long bigNum = " + bigNum);
        System.out.println("float f = " + f);
        System.out.println("double d = " + d);
        System.out.println("char ch = " + ch);
        System.out.println("boolean flag = " + flag);


        // ---------------- Non-Primitive / Reference Types ----------------
        System.out.println("\n==================== 2. NON-PRIMITIVE DATA TYPES ====================");
        System.out.println("""
Non-primitive data types are more complex.
They do NOT store actual value directly.
Instead, they store the memory ADDRESS (reference) of the object.

Common non-primitive types:
- String
- Arrays
- Classes
- Objects
- Interfaces

Characteristics:
✔ Start with uppercase (e.g., String, Integer)
✔ Can be NULL
✔ Can contain multiple values
✔ Have methods

Let us explore the most common ones.
""");


        // ---------------- String ----------------
        System.out.println("\n==================== 2.1 STRING ====================");
        System.out.println("""
String is a non-primitive type that stores a sequence of characters.

Example:
    String name = "Aditya";

Strings have built-in methods like:
    length(), toUpperCase(), charAt(), etc.
""");

        String name = "Aditya Varma";
        System.out.println("Example Output:");
        System.out.println("String name = " + name);
        System.out.println("Length of name = " + name.length());


        // ---------------- Arrays ----------------
        System.out.println("\n==================== 2.2 ARRAYS ====================");
        System.out.println("""
An array stores multiple values of the same data type.

Example:
    int[] marks = {90, 85, 88};

Arrays are objects in Java → non-primitive type.
""");

        int[] marks = {90, 85, 88};
        System.out.println("Example Output:");
        System.out.println("marks[0] = " + marks[0]);
        System.out.println("marks[1] = " + marks[1]);
        System.out.println("marks[2] = " + marks[2]);


        // ---------------- Objects ----------------
        System.out.println("\n==================== 2.3 OBJECTS ====================");
        System.out.println("""
Objects are created from classes.
They store data and have behaviors (methods).

Example:
    class Student { ... }
    Student s1 = new Student();

We will learn classes and objects in detail later.
""");

        System.out.println("Example Output:");
        System.out.println("Object example shown conceptually (no class used here).");


        // ---------------- Primitive vs Non-Primitive ----------------
        System.out.println("\n==================== 3. PRIMITIVE vs NON-PRIMITIVE ====================");
        System.out.println("""
PRIMITIVE:
- Store simple values
- Start with lowercase (int, double)
- Fixed size
- Faster

NON-PRIMITIVE:
- Store reference (address)
- Start with uppercase (String, Integer)
- Variable size
- Slower compared to primitives
- Have built-in methods
""");

        System.out.println("Example Output:");
        System.out.println("Primitive int value: " + num);
        System.out.println("Non-primitive String: " + name);


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Java data types are divided into Primitive & Non-Primitive.
→ Primitive (8 types): byte, short, int, long, float, double, char, boolean.
→ Non-primitive: String, arrays, classes, objects, interfaces.
→ Primitives store direct values; non-primitives store references.
→ Understanding data types is essential before working with variables and operations.
""");

    }
}
