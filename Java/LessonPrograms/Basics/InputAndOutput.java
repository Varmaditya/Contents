// Program: Input and Output in Java

import java.util.Scanner;

public class InputAndOutput {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== INPUT & OUTPUT IN JAVA ====================");
        System.out.println("""
Input and Output (I/O) are essential parts of any program.
Java provides simple ways to display output and read input from the user.

In this chapter, we will learn:
1. Output using System.out.print and System.out.println
2. Formatting output
3. Taking user input using Scanner
4. Difference between Scanner input and Command-Line Arguments
5. Common input mistakes beginners make

Let us explore each part in detail.
""");


        // ---------------- System.out.println ----------------
        System.out.println("\n==================== 1. OUTPUT USING System.out.println ====================");
        System.out.println("""
System.out.println → Prints text and moves to the next line.
System.out.print   → Prints text on the same line.

These methods are used to display messages, numbers, results, etc.

Example:
    System.out.println("Hello Java");
    System.out.print("A");
    System.out.print("B");

Output:
    Hello Java
    AB
""");

        System.out.println("Example Output:");
        System.out.println("Hello Java");
        System.out.print("A");
        System.out.print("B");
        System.out.println(); // next line


        // ---------------- Formatting Output ----------------
        System.out.println("\n==================== 2. FORMATTED OUTPUT ====================");
        System.out.println("""
Java supports formatted printing using printf().

Use %d for integers, %f for decimals, %s for strings, %c for characters.

Example:
    int marks = 90;
    System.out.printf("Marks: %d", marks);

printf does NOT move to next line unless we add \\n.
""");

        int marks = 90;
        System.out.println("Example Output:");
        System.out.printf("Marks: %d\n", marks);
        System.out.printf("Price: %.2f\n", 99.756);


        // ---------------- Scanner for Input ----------------
        System.out.println("\n==================== 3. TAKING INPUT USING Scanner ====================");
        System.out.println("""
Scanner is the most common way to take input in Java.
We create an object of Scanner and use methods to read data types.

Common methods:
• nextInt() → reads integer
• nextDouble() → reads decimal
• next() → reads a single word
• nextLine() → reads a full line
• nextBoolean() → reads true/false
• nextFloat(), nextLong(), nextByte(), etc.

Example:
    Scanner sc = new Scanner(System.in);
    int x = sc.nextInt();

Important:
Always import Scanner:
    import java.util.Scanner;
""");

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter an integer:");
        int num = sc.nextInt();
        System.out.println("You entered: " + num);


        // ---------------- Common Input Problem (nextLine issue) ----------------
        System.out.println("\n==================== 4. COMMON INPUT MISTAKE: nextLine() ISSUE ====================");
        System.out.println("""
Problem:
After using nextInt(), nextDouble(), nextFloat(), etc.,
a leftover newline '\\n' remains in the input buffer.

So when you call nextLine(), it captures that empty newline instead of actual input.

Solution:
Call an extra nextLine() to clear the buffer.

Example:
    sc.nextInt();
    sc.nextLine();  // clear leftover newline
    String name = sc.nextLine();
""");

        sc.nextLine(); // clearing leftover newline

        System.out.println("Enter a sentence (using nextLine):");
        String sentence = sc.nextLine();
        System.out.println("You entered: " + sentence);


        // ---------------- Command-Line Arguments ----------------
        System.out.println("\n==================== 5. COMMAND-LINE ARGUMENTS ====================");
        System.out.println("""
Command-line arguments are values passed from the terminal/command prompt
when running a Java program.

Syntax in terminal:
    java InputOutputInJava Hello 123

These values are stored in the 'args' array of main().

Example:
    public static void main(String[] args) {
        System.out.println(args[0]);  // Hello
        System.out.println(args[1]);  // 123
    }

Difference from Scanner:
• Scanner → input DURING program execution
• Command-line args → input BEFORE program starts
• Scanner allows interactive input; args do not
""");

        System.out.println("Example: Command-line arguments cannot be demonstrated here.");


        // ---------------- Common Input Errors ----------------
        System.out.println("\n==================== 6. COMMON INPUT ERRORS ====================");
        System.out.println("""
1. Trying to enter text when nextInt() expects a number → InputMismatchException
2. Forgetting to import Scanner → Compile error
3. Using nextLine() after nextInt() without clearing buffer
4. Using the wrong method for the wrong input type
5. Reading char incorrectly (should use next().charAt(0))

Good practice:
Always validate input and handle exceptions in real applications.
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ System.out.print / println are used to display output.
→ printf is used for formatted output.
→ Scanner helps read different types of user input.
→ nextLine() requires careful handling after numeric input.
→ Command-line arguments allow sending input before program execution.
→ Input errors mainly happen due to mismatched data types or Scanner misuse.

Understanding input & output is essential before writing interactive programs.
""");
    }
}
