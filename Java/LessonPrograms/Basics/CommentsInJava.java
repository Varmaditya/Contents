// Program: Comments in Java

public class CommentsInJava {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== COMMENTS IN JAVA ====================");
        System.out.println("""
Comments are notes written inside a program to explain the code.
They are NOT executed by the Java compiler.

Why comments are used:
✔ To explain logic  
✔ To improve readability  
✔ To give instructions to other developers  
✔ To temporarily disable (ignore) some code  

Java provides THREE types of comments:
1. Single-line comment
2. Multi-line comment
3. Documentation comment
""");


        // ---------------- 1. Single-Line Comments ----------------
        System.out.println("\n==================== 1. SINGLE-LINE COMMENTS ====================");
        System.out.println("""
Single-line comments start with:
// 

Everything written after // on the same line is ignored by the compiler.

Usage:
→ Used for short explanations
→ Used to comment out a single line
Example:
    // This is a single-line comment
""");

        // Demonstration of single-line comments
        System.out.println("Example: Printing a message using single-line comments:");
        // This line prints a welcome message
        System.out.println("Hello from Java! (This line is explained using a single-line comment)");

        // The next line is commented out, so it will NOT run
        // System.out.println("This line is disabled and will not execute");

        System.out.println("Above: One line is commented out and does not execute.\n");


        // ---------------- 2. Multi-Line Comments ----------------
        System.out.println("\n==================== 2. MULTI-LINE COMMENTS ====================");
        System.out.println("""
Multi-line comments begin with:
    /*  
and end with:
    */

Everything written between these symbols is ignored.

Usage:
✔ To explain large concepts
✔ To disable multiple lines temporarily
✔ To add notes or instructions

Example:
    /*
       This is a
       multi-line comment
    */
""");

        // Demonstration of multi-line comment
        System.out.println("Example: Showing how a multi-line comment works:");

        /*
         The next print statement introduces multi-line comments.
         Multi-line comments can span across several lines.
         They are great for detailed explanations.
        */
        System.out.println("This message is explained using a multi-line comment.");

        // Multi-line comment disabling multiple lines:
/*
System.out.println("This line will not run.");
System.out.println("This line also will not run.");
*/
        System.out.println("Above: Two lines were disabled using a multi-line comment.\n");


        // ---------------- 3. Documentation Comments ----------------
        System.out.println("\n==================== 3. DOCUMENTATION COMMENTS ====================");
        System.out.println("""
Documentation comments are special comments used to generate official
Java documentation using the javadoc tool.

They begin with:
/**

and end with:
*/

Inside them, we use special tags such as:
✔ @author → Who created the code
✔ @version → Version number
✔ @return → What a method returns
✔ @param → Description of parameters

These comments are mostly used for professional Java development.

Example:
/**
 * This class performs calculations
 * @author John
 * @version 1.0
 */
""");

        // Demonstration: printing explanation of documentation comment usage
        System.out.println("Example: Documentation comments used for methods and classes.");
        System.out.println("Although not visible here, they help generate HTML documentation.\n");


        // ---------------- Real Program Example Using All Comments ----------------
        System.out.println("\n==================== REAL EXAMPLE USING ALL COMMENT TYPES ====================");

        System.out.println("""
Below is an example of a small code snippet (printed as text)
showing all three comment types working together:

---------------------------------------------
/**
 * This program adds two numbers.
 * @author Student
 */
public class Example {
    public static void main(String[] args) {

        // Declaring numbers
        int a = 10;  // first number
        int b = 20;  // second number

        /*
           Calculating sum:
           The result will be stored in 'sum'
        */
        int sum = a + b;

        System.out.println("Sum = " + sum);  // printing result
    }
}
---------------------------------------------
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Comments help explain and document code.  
→ Java provides 3 types of comments:

1. Single-line comment  
   // Used for short notes and disabling one line.

2. Multi-line comment  
   /* ... */ Used for long explanations or disabling multiple lines.

3. Documentation comment  
   /** ... */ Used with javadoc to create documentation.

Comments improve readability and make code easier to understand.
""");
    }
}
