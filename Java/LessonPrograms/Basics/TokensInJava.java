// Program: Tokens in Java

public class TokensInJava {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== TOKENS IN JAVA ====================");
        System.out.println("""
Java programs are made up of small building blocks called TOKENS.
These are the smallest elements that have meaning in a Java program.

Java Tokens include:
1. Keywords
2. Identifiers
3. Literals
4. Symbols & Operators

Let us explore each one with examples.
""");

        // ---------------- Keywords ----------------
        System.out.println("\n==================== 1. KEYWORDS ====================");
        System.out.println("""
Keywords are reserved words in Java that have a special predefined meaning.
You CANNOT use them as variable names, class names, or identifiers.

Examples of keywords:
    class, public, static, void, int, double, if, else, return

→ These words tell Java how the program should behave.
""");

        // Demonstrating some common keywords through a simple example
        System.out.println("Example: In this line 'public class TokensInJava',");
        System.out.println(" - 'public' is a keyword");
        System.out.println(" - 'class' is a keyword");
        System.out.println(" - 'TokensInJava' is NOT a keyword (it's an identifier)");


        // ---------------- Identifiers ----------------
        System.out.println("\n==================== 2. IDENTIFIERS ====================");
        System.out.println("""
Identifiers are the names given to:
- classes
- methods
- variables
- objects

RULES for identifiers:
✔ Can contain letters, digits, underscore (_), dollar ($)
✔ Cannot start with a digit
✔ Cannot contain spaces
✔ Cannot use Java keywords
✔ Case-sensitive (Java, java, JAVA are different)

Examples:
    MyClass
    studentName
    _count
    $price
""");

        // Example: Showing valid identifiers
        System.out.println("Examples of VALID identifiers printed below:");
        System.out.println("MyClass, totalMarks, _value, $amount\n");


        // ---------------- Literals ----------------
        System.out.println("\n==================== 3. LITERALS ====================");
        System.out.println("""
Literals are fixed values written directly in the program.

Types of Literals:
1. Integer Literal → 10, 200, -55
2. Floating Literal → 3.14, -44.7, 0.0
3. Character Literal → 'A', 'z', '#'
4. String Literal → "Hello", "Java Programming"
5. Boolean Literal → true, false

These are NOT variables. These are constant values that appear in the code.
""");

        // Demonstration: Printing different literals
        System.out.println("Integer Literal: " + 10);
        System.out.println("Floating Literal: " + 3.14);
        System.out.println("Character Literal: " + 'A');
        System.out.println("String Literal: " + "Java is awesome");
        System.out.println("Boolean Literal: " + true);


        // ---------------- Symbols & Operators ----------------
        System.out.println("\n==================== 4. SYMBOLS & OPERATORS ====================");
        System.out.println("""
Symbols are special characters used for:
- grouping
- separating
- performing operations

Common symbols:
()   → parentheses
{}   → braces
[]   → brackets
;    → statement terminator
,    → separator
" "  → string quotes

OPERATORS perform actions such as:
1. Arithmetic → +  -  *  /  %
2. Relational → ==  !=  >  <  >=  <=
3. Logical → &&  ||  !
4. Assignment → =  +=  -=  *=

We will study these in detail later, but here is a simple demonstration.
""");

        // Demonstrating operators (only simple prints, no teaching operators deeply yet)
        System.out.println("Example Symbol: Semicolon ends this statement;");
        System.out.println("Example Operator: '+' is used for addition or combining strings.");
        System.out.println("Printing: \"Java\" + \" Language\" = " + "Java" + " Language");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Tokens are the smallest meaningful elements in a Java program.
→ Keywords: Reserved words (public, class, static, etc.)
→ Identifiers: Names for classes, methods, and variables.
→ Literals: Fixed values like numbers, characters, strings, true/false.
→ Symbols & Operators: Characters used for grouping and performing operations.

Understanding tokens is the first step to writing Java code correctly.
""");
    }
}
