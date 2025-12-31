// Program: while Loop in Java

import java.util.Scanner;

public class WhileLoop {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== WHILE LOOP IN JAVA ====================");
        System.out.println("""
The 'while' loop is a looping statement used when
the NUMBER OF ITERATIONS is NOT known in advance.

The loop keeps executing as long as the condition is TRUE.
Once the condition becomes false, the loop stops.

The while loop is called an ENTRY-CONTROLLED loop
because the condition is checked BEFORE execution.
""");

        // ---------------- Syntax ----------------
        System.out.println("\n==================== SYNTAX OF WHILE LOOP ====================");
        System.out.println("""
Syntax:

    while (condition) {
        // loop body
    }

Important points:
✔ Condition must be boolean
✔ Loop body executes only if condition is true
✔ Update must be handled inside loop body
""");

        // ---------------- Flow Explanation ----------------
        System.out.println("\n==================== FLOW OF WHILE LOOP ====================");
        System.out.println("""
Execution Flow:

START
 ↓
Check condition
 ↓
true  → Execute loop body
        ↓
        Update
        ↓
        Repeat condition check
false → Exit loop
""");

        // ---------------- Example 1: Print Numbers ----------------
        System.out.println("\n==================== EXAMPLE 1: PRINT NUMBERS ====================");
        System.out.println("""
Print numbers from 1 to 5.
""");

        int i = 1;

        while (i <= 5) {
            System.out.println("Number: " + i);
            i++;
        }

        System.out.println("Number printing completed.\n");

        // ---------------- Example 2: Sum of Numbers ----------------
        System.out.println("\n==================== EXAMPLE 2: SUM OF NUMBERS ====================");
        System.out.println("""
Calculate sum of numbers from 1 to n.
""");

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        int sum = 0;
        int num = 1;

        while (num <= n) {
            sum = sum + num;
            num++;
        }

        System.out.println("Sum = " + sum);
        System.out.println("Sum calculation completed.\n");

        // ---------------- Example 3: Reverse Counting ----------------
        System.out.println("\n==================== EXAMPLE 3: REVERSE COUNTING ====================");
        System.out.println("""
Print numbers from 10 to 1.
""");

        int r = 10;

        while (r >= 1) {
            System.out.println(r);
            r--;
        }

        System.out.println("Reverse counting completed.\n");

        // ---------------- Example 4: Password Retry Simulation ----------------
        System.out.println("\n==================== EXAMPLE 4: PASSWORD RETRY ====================");
        System.out.println("""
Repeat until correct password is entered.
""");

        sc.nextLine(); // clear buffer
        String password = "java123";
        String input = "";

        while (!input.equals(password)) {
            System.out.print("Enter password: ");
            input = sc.nextLine();
        }

        System.out.println("Access granted.\n");

        // ---------------- Example 5: Digit Count ----------------
        System.out.println("\n==================== EXAMPLE 5: DIGIT COUNT ====================");
        System.out.println("""
Count number of digits in a number.
""");

        System.out.print("Enter a number: ");
        int value = sc.nextInt();

        int count = 0;

        while (value != 0) {
            value = value / 10;
            count++;
        }

        System.out.println("Number of digits: " + count);
        System.out.println("Digit counting completed.\n");

        // ---------------- Comparison with for Loop ----------------
        System.out.println("\n==================== FOR vs WHILE ====================");
        System.out.println("""
for loop:
✔ Used when iterations are known
✔ Initialization, condition, update together

while loop:
✔ Used when iterations are unknown
✔ Condition-based repetition

Choose loop based on problem requirements.
""");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Forgetting update (causes infinite loop)
✘ Wrong condition logic
✘ Incorrect initialization
✘ Assuming loop executes at least once

Remember:
✔ Condition checked BEFORE execution
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ while loop repeats code while condition is true.
→ It is an entry-controlled loop.
→ Best used when iteration count is unknown.
→ Update must be handled manually.
→ Used in validations, retries, and dynamic loops.

Next topic: do-while loop.
""");

        sc.close();
    }
}
