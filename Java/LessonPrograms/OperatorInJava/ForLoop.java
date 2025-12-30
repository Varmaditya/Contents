// Program: for Loop in Java

import java.util.Scanner;

public class ForLoop {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== FOR LOOP IN JAVA ====================");
        System.out.println("""
The 'for' loop is a looping statement used when
the NUMBER OF ITERATIONS is KNOWN in advance.

It is commonly used to:
✔ repeat tasks a fixed number of times
✔ iterate over ranges of values
✔ process sequences step-by-step

The for loop is compact and easy to read.
""");

        // ---------------- Syntax ----------------
        System.out.println("\n==================== SYNTAX OF FOR LOOP ====================");
        System.out.println("""
Syntax:

    for (initialization; condition; update) {
        // loop body
    }

Parts of for loop:
✔ initialization → executed ONCE at start
✔ condition → checked before every iteration
✔ update → executed after each iteration
""");

        // ---------------- Flow Explanation ----------------
        System.out.println("\n==================== FLOW OF FOR LOOP ====================");
        System.out.println("""
Execution Flow:

START
 ↓
Initialization
 ↓
Condition check
 ↓
true  → Execute loop body
        ↓
        Update
        ↓
        Repeat condition
false → Exit loop
""");

        // ---------------- Example 1: Print Numbers ----------------
        System.out.println("\n==================== EXAMPLE 1: PRINT NUMBERS ====================");
        System.out.println("""
Print numbers from 1 to 5.
""");

        for (int i = 1; i <= 5; i++) {
            System.out.println("Number: " + i);
        }

        System.out.println("Number printing completed.\n");


        // ---------------- Example 2: Print Even Numbers ----------------
        System.out.println("\n==================== EXAMPLE 2: EVEN NUMBERS ====================");
        System.out.println("""
Print even numbers from 1 to 10.
""");

        for (int i = 2; i <= 10; i += 2) {
            System.out.println(i);
        }

        System.out.println("Even numbers printed.\n");

        // ---------------- Example 3: Sum of Natural Numbers ----------------
        System.out.println("\n==================== EXAMPLE 3: SUM OF NUMBERS ====================");
        System.out.println("""
Calculate sum of numbers from 1 to n.
""");

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        int sum = 0;

        for (int i = 1; i <= n; i++) {
            sum = sum + i;
        }

        System.out.println("Sum = " + sum);
        System.out.println("Sum calculation completed.\n");

        // ---------------- Example 4: Multiplication Table ----------------
        System.out.println("\n==================== EXAMPLE 4: MULTIPLICATION TABLE ====================");
        System.out.println("""
Display multiplication table of a number.
""");

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        for (int i = 1; i <= 10; i++) {
            System.out.println(num + " x " + i + " = " + (num * i));
        }

        System.out.println("Table printed.\n");

        // ---------------- Example 5: Reverse Counting ----------------
        System.out.println("\n==================== EXAMPLE 5: REVERSE COUNTING ====================");
        System.out.println("""
Print numbers from 10 to 1.
""");

        for (int i = 10; i >= 1; i--) {
            System.out.println(i);
        }

        System.out.println("Reverse counting completed.\n");

        // ---------------- Example 6: Using for Loop with Condition ----------------
        System.out.println("\n==================== EXAMPLE 6: CONDITIONAL LOOP ====================");
        System.out.println("""
Print numbers divisible by 3 from 1 to 30.
""");

        for (int i = 1; i <= 30; i++) {
            if (i % 3 == 0) {
                System.out.println(i);
            }
        }

        System.out.println("Divisibility check completed.\n");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Infinite loop due to wrong condition
✘ Incorrect update expression
✘ Off-by-one errors
✘ Forgetting braces for multiple statements

Always verify:
✔ Initialization
✔ Condition
✔ Update
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ for loop is used when iterations are known.
→ Combines initialization, condition, and update.
→ Widely used for counting and ranges.
→ Efficient and readable looping structure.

Next topic: while loop.
""");

        sc.close();
    }
}
