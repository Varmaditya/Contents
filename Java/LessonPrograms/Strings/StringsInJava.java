// Program: Strings in Java

public class StringsInJava {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== STRINGS IN JAVA ====================");
        System.out.println("""
In real-world programs, we work with TEXT all the time.

Examples:
✔ Names
✔ Messages
✔ Addresses
✔ Passwords
✔ Emails

In Java, text data is handled using STRINGS.
""");

        // ---------------- What is a String ----------------
        System.out.println("\n==================== WHAT IS A STRING ====================");
        System.out.println("""
A String in Java is:
✔ A sequence of characters
✔ Used to store text
✔ Represented by the String class
✔ Enclosed within double quotes

Examples:
    "Hello"
    "Java Programming"
    "123ABC"
""");

        // ---------------- String as an Object ----------------
        System.out.println("\n==================== STRING AS AN OBJECT ====================");
        System.out.println("""
In Java, String is NOT a primitive data type.

It is:
✔ A class
✔ An object
✔ Part of java.lang package

This means:
✔ Strings have methods
✔ Strings have properties
✔ Strings behave differently than primitive types
""");

        // ---------------- Creating Strings ----------------
        System.out.println("\n==================== CREATING STRINGS ====================");
        System.out.println("""
There are TWO main ways to create strings in Java:

1. Using String Literal
2. Using new Keyword
""");

        // ---------------- String Literal ----------------
        System.out.println("\n==================== STRING LITERAL ====================");
        System.out.println("""
A string literal is created using double quotes.

Example:
    String s = "Java";

Characteristics:
✔ Stored in String Constant Pool (SCP)
✔ If same value exists, memory is shared
✔ More memory efficient
✔ Faster performance
""");

        String s1 = "Java";
        String s2 = "Java";

        System.out.println("String s1 = \"Java\"");
        System.out.println("String s2 = \"Java\"");
        System.out.println("s1 == s2 → " + (s1 == s2));

        // ---------------- new String() ----------------
        System.out.println("\n==================== USING new STRING() ====================");
        System.out.println("""
A string can also be created using the new keyword.

Example:
    String s = new String("Java");

Characteristics:
✔ Stored in Heap memory
✔ Always creates a new object
✔ No memory sharing
✔ Less memory efficient
""");

        String s3 = new String("Java");
        String s4 = new String("Java");

        System.out.println("String s3 = new String(\"Java\")");
        System.out.println("String s4 = new String(\"Java\")");
        System.out.println("s3 == s4 → " + (s3 == s4));

        // ---------------- Comparison Explanation ----------------
        System.out.println("\n==================== COMPARISON EXPLANATION ====================");
        System.out.println("""
The == operator compares REFERENCES, not content.

s1 == s2 → true
(both refer to same memory location in SCP)

s3 == s4 → false
(both refer to different objects in heap)

To compare CONTENT, we use equals() method
(which will be studied later).
""");

        // ---------------- Memory Concept (High-Level) ----------------
        System.out.println("\n==================== MEMORY CONCEPT (HIGH LEVEL) ====================");
        System.out.println("""
String Literal:
✔ Stored in String Constant Pool
✔ Reuses existing objects

new String():
✔ Stored in Heap memory
✔ Creates new object every time

This difference impacts:
✔ Memory usage
✔ Performance
""");

        // ---------------- When to Use What ----------------
        System.out.println("\n==================== WHEN TO USE WHICH ====================");
        System.out.println("""
Use String Literal:
✔ Most of the time
✔ When content is fixed
✔ For better performance

Use new String():
✔ When explicit object creation is required
✔ When working with security-sensitive data
""");

        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD MAPPING ====================");
        System.out.println("""
Examples:
✔ User name → String literal
✔ Error message → String literal
✔ Runtime-generated input → new String()

Strings are everywhere in Java programs.
""");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Using == to compare string content
✘ Creating unnecessary String objects
✘ Assuming String is primitive
✘ Ignoring memory behavior

Always remember:
✔ String is an object
✔ == compares references
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ String is a class used to store text.
→ Strings are objects, not primitives.
→ Can be created using literals or new keyword.
→ Literals are memory efficient.
→ new String() creates separate objects.

Strings are a CORE part of Java programming.
""");
    }
}
