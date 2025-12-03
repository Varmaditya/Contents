// Program: Escape Sequences in Java

public class EscapeSequence {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== ESCAPE SEQUENCES IN JAVA ====================");
        System.out.println("""
Escape sequences are special character combinations used to format output.
They always begin with a BACKSLASH (\\).

They help in:
- Printing new lines
- Adding spaces (tabs)
- Printing quotes inside strings
- Printing special characters like backslash

Let us explore each escape sequence with examples.
""");

        // ---------------- \n (New Line) ----------------
        System.out.println("\n==================== 1. NEW LINE (\\n) ====================");
        System.out.println("""
The escape sequence \\n is used to move the cursor to the next line.
It helps in printing multiple lines cleanly.
""");

        System.out.println("Example Output:");
        System.out.println("Line 1\nLine 2\nLine 3");


        // ---------------- \t (Tab Space) ----------------
        System.out.println("\n==================== 2. TAB SPACE (\\t) ====================");
        System.out.println("""
The escape sequence \\t inserts a horizontal tab.
It is useful for aligning text in columns.
""");

        System.out.println("Example Output:");
        System.out.println("Name:\tAditya");
        System.out.println("Age:\t23");
        System.out.println("City:\tMumbai");


        // ---------------- \" (Double Quote) ----------------
        System.out.println("\n==================== 3. DOUBLE QUOTE (\\\") ====================");
        System.out.println("""
The escape sequence \\\" allows printing double quotes inside a string.
""");

        System.out.println("Example Output:");
        System.out.println("He said, \"Java is powerful!\"");


        // ---------------- \\ (Backslash) ----------------
        System.out.println("\n==================== 4. BACKSLASH (\\\\) ====================");
        System.out.println("""
To print a backslash, we use \\\\ because a single backslash starts an escape sequence.
""");

        System.out.println("Example Output:");
        System.out.println("This is a backslash: \\");


        // ---------------- Combining escape sequences ----------------
        System.out.println("\n==================== 5. COMBINED EXAMPLE ====================");
        System.out.println("""
We can combine multiple escape sequences to format complex output.
""");

        System.out.println("Example Output:");
        System.out.println("Start\n\tMiddle\n\t\tEnd");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Escape sequences help in formatting printed text.
→ \\n : New line
→ \\t : Tab space
→ \\\" : Double quote
→ \\\\ : Backslash
→ Can be combined to create structured output.

Understanding escape sequences improves readability of output.
""");

    }
}
