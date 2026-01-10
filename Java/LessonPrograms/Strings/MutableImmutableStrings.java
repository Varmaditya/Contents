// Program: Mutable & Immutable Strings and Comparison in Java

public class MutableImmutableStrings {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== MUTABLE & IMMUTABLE STRINGS ====================");
        System.out.println("""
In Java, strings behave differently compared to primitive data types.

One of the MOST IMPORTANT concepts to understand is:
✔ Immutability
✔ Mutability
✔ How strings are compared

These concepts affect:
✔ Performance
✔ Memory usage
✔ Program correctness
""");

        // ---------------- What is Immutability ----------------
        System.out.println("\n==================== WHAT IS IMMUTABILITY ====================");
        System.out.println("""
Immutability means:
✔ Once an object is created, it CANNOT be changed.

In Java:
✔ String objects are IMMUTABLE
✔ Any modification creates a NEW object
""");

        // ---------------- Immutable String Example ----------------
        System.out.println("\n==================== IMMUTABLE STRING EXAMPLE ====================");
        System.out.println("""
When we modify a String,
a new String object is created instead of changing the original.
""");

        String s = "Java";
        System.out.println("Original String: " + s);

        s = s.concat(" Programming");
        System.out.println("After modification: " + s);

        System.out.println("""
The original "Java" string was NOT changed.
A new String object was created.
""");

        // ---------------- Why String is Immutable ----------------
        System.out.println("\n==================== WHY STRING IS IMMUTABLE ====================");
        System.out.println("""
String is immutable for:
✔ Security (passwords, URLs)
✔ Thread safety
✔ Performance (String Constant Pool)
✔ Caching and reuse

Immutability prevents accidental data modification.
""");

        // ---------------- Mutable Strings ----------------
        System.out.println("\n==================== MUTABLE STRINGS ====================");
        System.out.println("""
Mutable strings CAN be changed after creation.

Java provides two mutable string classes:
✔ StringBuilder
✔ StringBuffer
""");

        // ---------------- StringBuilder ----------------
        System.out.println("\n==================== STRINGBUILDER ====================");
        System.out.println("""
StringBuilder:
✔ Mutable
✔ Faster
✔ Not thread-safe
✔ Used in single-threaded programs
""");

        StringBuilder sb = new StringBuilder("Java");
        System.out.println("Original StringBuilder: " + sb);

        sb.append(" Programming");
        System.out.println("After append: " + sb);

        // ---------------- StringBuffer ----------------
        System.out.println("\n==================== STRINGBUFFER ====================");
        System.out.println("""
StringBuffer:
✔ Mutable
✔ Thread-safe
✔ Slightly slower than StringBuilder
✔ Used in multi-threaded programs
""");

        StringBuffer sbf = new StringBuffer("Java");
        sbf.append(" Programming");
        System.out.println("StringBuffer result: " + sbf);

        // ---------------- String Comparison ----------------
        System.out.println("\n==================== STRING COMPARISON ====================");
        System.out.println("""
String comparison is a COMMON source of bugs.

Java provides TWO ways to compare strings:
✔ Using == operator
✔ Using equals() method
""");

        // ---------------- == Operator ----------------
        System.out.println("\n==================== == OPERATOR ====================");
        System.out.println("""
The == operator compares REFERENCES, not content.
""");

        String a1 = "Java";
        String a2 = "Java";
        String a3 = new String("Java");

        System.out.println("a1 == a2 : " + (a1 == a2));
        System.out.println("a1 == a3 : " + (a1 == a3));

        // ---------------- equals() Method ----------------
        System.out.println("\n==================== equals() METHOD ====================");
        System.out.println("""
equals() compares ACTUAL CONTENT of strings.
""");

        System.out.println("a1.equals(a2) : " + a1.equals(a2));
        System.out.println("a1.equals(a3) : " + a1.equals(a3));

        // ---------------- equalsIgnoreCase() ----------------
        System.out.println("\n==================== equalsIgnoreCase() ====================");
        System.out.println("""
equalsIgnoreCase() compares content
without considering letter case.
""");

        String x = "java";
        String y = "JAVA";

        System.out.println("x.equalsIgnoreCase(y): " + x.equalsIgnoreCase(y));

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Using == for content comparison
✘ Assuming String is mutable
✘ Overusing String instead of StringBuilder
✘ Ignoring performance impact
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ String is immutable.
→ StringBuilder and StringBuffer are mutable.
→ == compares references.
→ equals() compares content.
→ Choosing the right string type improves performance.

Understanding strings is CRITICAL in Java.
""");
    }
}
