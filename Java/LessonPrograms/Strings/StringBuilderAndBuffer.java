// Program: StringBuilder & StringBuffer in Java (Detailed)

public class StringBuilderAndBuffer {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== STRINGBUILDER & STRINGBUFFER ====================");
        System.out.println("""
In Java, String objects are IMMUTABLE.
This causes performance issues when strings are modified frequently.

To solve this problem, Java provides:
✔ StringBuilder
✔ StringBuffer

These classes allow STRING MODIFICATION
without creating new objects.
""");

        // ---------------- Why Mutable Strings ----------------
        System.out.println("\n==================== WHY MUTABLE STRINGS ====================");
        System.out.println("""
Problem with String:
✔ Each modification creates a new object
✔ Memory wastage
✔ Slower performance in loops

Solution:
✔ Use mutable string classes
✔ Modify content without creating new objects
""");

        // ---------------- StringBuilder Introduction ----------------
        System.out.println("\n==================== STRINGBUILDER ====================");
        System.out.println("""
StringBuilder:
✔ Mutable
✔ Faster
✔ Not thread-safe
✔ Stored in heap memory
✔ Introduced in Java 1.5

Used when:
✔ String changes frequently
✔ Single-threaded programs
""");

        StringBuilder sb = new StringBuilder("Java");
        System.out.println("Initial StringBuilder: " + sb);

        // ---------------- append() ----------------
        System.out.println("\n==================== append() ====================");
        System.out.println("""
append() adds text to the existing object.
""");

        sb.append(" Programming");
        System.out.println("After append: " + sb);

        // ---------------- insert() ----------------
        System.out.println("\n==================== insert() ====================");
        System.out.println("""
insert(index, value) inserts data at given position.
""");

        sb.insert(5, "Language ");
        System.out.println("After insert: " + sb);

        // ---------------- replace() ----------------
        System.out.println("\n==================== replace() ====================");
        System.out.println("""
replace(start, end, value) replaces part of string.
""");

        sb.replace(0, 4, "JAVA");
        System.out.println("After replace: " + sb);


        // ---------------- delete() ----------------
        System.out.println("\n==================== delete() ====================");
        System.out.println("""
delete(start, end) removes characters.
""");

        sb.delete(5, 14);
        System.out.println("After delete: " + sb);

        // ---------------- reverse() ----------------
        System.out.println("\n==================== reverse() ====================");
        System.out.println("""
reverse() reverses the content.
""");

        sb.reverse();
        System.out.println("After reverse: " + sb);

        sb.reverse(); // restore original order

        // ---------------- capacity() ----------------
        System.out.println("\n==================== capacity() ====================");
        System.out.println("""
capacity() shows current storage capacity.
Default capacity = 16 + initial string length
""");

        StringBuilder cap = new StringBuilder("Hello");
        System.out.println("Capacity: " + cap.capacity());

        // ---------------- length() ----------------
        System.out.println("\n==================== length() ====================");
        System.out.println("""
length() returns number of characters.
""");

        System.out.println("Length: " + sb.length());

        // ---------------- charAt() ----------------
        System.out.println("\n==================== charAt() ====================");
        System.out.println("""
charAt(index) returns character at index.
""");

        System.out.println("Character at index 2: " + sb.charAt(2));

        // ---------------- setCharAt() ----------------
        System.out.println("\n==================== setCharAt() ====================");
        System.out.println("""
setCharAt(index, ch) modifies a character.
""");

        sb.setCharAt(0, 'j');
        System.out.println("After setCharAt: " + sb);

        // ---------------- StringBuffer Introduction ----------------
        System.out.println("\n==================== STRINGBUFFER ====================");
        System.out.println("""
StringBuffer:
✔ Mutable
✔ Thread-safe
✔ Synchronized
✔ Slower than StringBuilder
✔ Introduced in Java 1.0

Used when:
✔ Multiple threads modify same string
""");

        StringBuffer sbf = new StringBuffer("Java");
        sbf.append(" Programming");
        System.out.println("StringBuffer result: " + sbf);

        // ---------------- Comparison Summary Table ----------------
        System.out.println("\n==================== COMPARISON SUMMARY ====================");
        System.out.println("""
String:
✔ Immutable
✔ Safe and secure
✔ Slower for heavy modifications

StringBuilder:
✔ Mutable
✔ Fast
✔ Not thread-safe

StringBuffer:
✔ Mutable
✔ Thread-safe
✔ Slightly slower
""");

        // ---------------- When to Use What ----------------
        System.out.println("\n==================== WHEN TO USE WHAT ====================");
        System.out.println("""
Use String:
✔ When text does not change frequently
✔ For constants, messages, literals

Use StringBuilder:
✔ When frequent modifications are required
✔ In loops or performance-critical code

Use StringBuffer:
✔ In multi-threaded environments
""");

        // ---------------- Performance Insight ----------------
        System.out.println("\n==================== PERFORMANCE INSIGHT ====================");
        System.out.println("""
Using String in loops causes:
✔ Too many objects
✔ Slow execution

Using StringBuilder:
✔ Faster execution
✔ Better memory usage
""");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Using String in loops
✘ Using StringBuffer without multi-threading
✘ Confusing mutability rules
✘ Ignoring capacity behavior
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ StringBuilder and StringBuffer are mutable.
→ StringBuilder is faster but not thread-safe.
→ StringBuffer is thread-safe but slower.
→ Use StringBuilder for frequent modifications.
→ Use StringBuffer for multi-threaded safety.

Choosing the right string class matters.
""");
    }
}
