// Program: String Methods in Java (Detailed)

public class StringMethods {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== STRING METHODS IN JAVA ====================");
        System.out.println("""
In Java, String is a class.
This means Strings come with BUILT-IN METHODS.

String methods are used to:
✔ Get information about a string
✔ Extract parts of a string
✔ Compare strings
✔ Modify string content (by creating new strings)

In this program, we will study the MOST COMMON
and IMPORTANT String methods.
""");


        // ---------------- Sample String ----------------
        System.out.println("\n==================== SAMPLE STRING ====================");
        String text = "Java Programming";
        System.out.println("Sample String: \"" + text + "\"");


        // ---------------- length() ----------------
        System.out.println("\n==================== length() ====================");
        System.out.println("""
length() returns the total number of characters
in a string (including spaces).
""");

        System.out.println("Length of string: " + text.length());


        // ---------------- charAt() ----------------
        System.out.println("\n==================== charAt() ====================");
        System.out.println("""
charAt(index) returns the character
present at the given index.

Index starts from 0.
""");

        System.out.println("Character at index 0: " + text.charAt(0));
        System.out.println("Character at index 5: " + text.charAt(5));


        // ---------------- substring() ----------------
        System.out.println("\n==================== substring() ====================");
        System.out.println("""
substring() is used to extract a part of a string.

Forms:
1. substring(startIndex)
2. substring(startIndex, endIndex)

Note:
✔ startIndex is inclusive
✔ endIndex is exclusive
""");

        System.out.println("substring(5): " + text.substring(5));
        System.out.println("substring(0, 4): " + text.substring(0, 4));


        // ---------------- equals() ----------------
        System.out.println("\n==================== equals() ====================");
        System.out.println("""
equals() compares CONTENT of two strings.

It returns:
✔ true if content is same
✔ false if content is different
""");

        String s1 = "Java";
        String s2 = "Java";
        String s3 = new String("Java");

        System.out.println("s1.equals(s2): " + s1.equals(s2));
        System.out.println("s1.equals(s3): " + s1.equals(s3));


        // ---------------- equalsIgnoreCase() ----------------
        System.out.println("\n==================== equalsIgnoreCase() ====================");
        System.out.println("""
equalsIgnoreCase() compares strings
WITHOUT considering case.
""");

        String a = "java";
        String b = "JAVA";

        System.out.println("a.equalsIgnoreCase(b): " + a.equalsIgnoreCase(b));


        // ---------------- toLowerCase() ----------------
        System.out.println("\n==================== toLowerCase() ====================");
        System.out.println("""
toLowerCase() converts all characters
to lowercase.
""");

        System.out.println("Lowercase: " + text.toLowerCase());


        // ---------------- toUpperCase() ----------------
        System.out.println("\n==================== toUpperCase() ====================");
        System.out.println("""
toUpperCase() converts all characters
to uppercase.
""");

        System.out.println("Uppercase: " + text.toUpperCase());


        // ---------------- trim() ----------------
        System.out.println("\n==================== trim() ====================");
        System.out.println("""
trim() removes leading and trailing spaces.
""");

        String spaced = "   Hello Java   ";
        System.out.println("Before trim: \"" + spaced + "\"");
        System.out.println("After trim: \"" + spaced.trim() + "\"");


        // ---------------- contains() ----------------
        System.out.println("\n==================== contains() ====================");
        System.out.println("""
contains() checks whether a string
contains a specific sequence.
""");

        System.out.println("Contains \"Java\": " + text.contains("Java"));
        System.out.println("Contains \"Python\": " + text.contains("Python"));


        // ---------------- startsWith() & endsWith() ----------------
        System.out.println("\n==================== startsWith() & endsWith() ====================");
        System.out.println("""
startsWith() checks starting characters.
endsWith() checks ending characters.
""");

        System.out.println("Starts with \"Java\": " + text.startsWith("Java"));
        System.out.println("Ends with \"ming\": " + text.endsWith("ming"));


        // ---------------- indexOf() ----------------
        System.out.println("\n==================== indexOf() ====================");
        System.out.println("""
indexOf() returns the index of
first occurrence of a character or string.

Returns -1 if not found.
""");

        System.out.println("Index of 'P': " + text.indexOf('P'));
        System.out.println("Index of \"Program\": " + text.indexOf("Program"));


        // ---------------- lastIndexOf() ----------------
        System.out.println("\n==================== lastIndexOf() ====================");
        System.out.println("""
lastIndexOf() returns the index
of last occurrence.
""");

        String demo = "Java is easy. Java is powerful.";
        System.out.println("Last index of \"Java\": " + demo.lastIndexOf("Java"));


        // ---------------- replace() ----------------
        System.out.println("\n==================== replace() ====================");
        System.out.println("""
replace() replaces characters or strings
and returns a NEW string.
""");

        System.out.println("Replace Java with Python: " +
                text.replace("Java", "Python"));


        // ---------------- split() ----------------
        System.out.println("\n==================== split() ====================");
        System.out.println("""
split() divides a string into parts
based on a delimiter.
""");

        String sentence = "Java is easy to learn";
        String[] words = sentence.split(" ");

        System.out.println("Words after split:");
        for (String w : words) {
            System.out.println(w);
        }


        // ---------------- isEmpty() ----------------
        System.out.println("\n==================== isEmpty() ====================");
        System.out.println("""
isEmpty() checks whether string length is 0.
""");

        String empty = "";
        System.out.println("Is empty string empty? " + empty.isEmpty());


        // ---------------- String Immutability Reminder ----------------
        System.out.println("\n==================== STRING IMMUTABILITY ====================");
        System.out.println("""
All String methods DO NOT change original string.

They return NEW string objects.
""");

        System.out.println("Original text: " + text);


        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Using == instead of equals()
✘ Assuming methods modify original string
✘ Ignoring index boundaries
✘ Forgetting strings are immutable
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ String methods help manipulate and inspect text.
→ Strings are immutable.
→ equals() compares content.
→ substring() extracts parts.
→ split() breaks strings.
→ Case methods change letter casing.

String methods are used DAILY in Java programs.
""");
    }
}
