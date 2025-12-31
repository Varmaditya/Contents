// Program: Control Statements in Java (break and continue)

import java.util.Scanner;

public class ControlStatements {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== CONTROL STATEMENTS IN JAVA ====================");
        System.out.println("""
Control statements are used to ALTER the normal flow
of loop execution.

They allow a program to:
✔ Stop a loop completely
✔ Skip an iteration
✔ Exit execution early

In Java, the main loop control statements are:
1. break
2. continue
""");

        // ---------------- break Statement ----------------
        System.out.println("\n==================== BREAK STATEMENT ====================");
        System.out.println("""
The 'break' statement is used to TERMINATE a loop immediately.

When break is executed:
✔ Control exits the loop
✔ Remaining iterations are skipped
✔ Execution continues after the loop

break is commonly used:
✔ When a condition is satisfied
✔ When searching for a value
✔ To stop infinite loops
""");

        // ---------------- Example 1: break in for Loop ----------------
        System.out.println("\n==================== EXAMPLE 1: break IN for LOOP ====================");
        System.out.println("""
Stop loop when number equals 5.
""");

        for (int i = 1; i <= 10; i++) {
            if (i == 5) {
                break;
            }
            System.out.println("Number: " + i);
        }

        System.out.println("Loop stopped using break.\n");

        // ---------------- Example 2: break in while Loop ----------------
        System.out.println("\n==================== EXAMPLE 2: break IN while LOOP ====================");
        System.out.println("""
Stop loop when correct password is entered.
""");

        Scanner sc = new Scanner(System.in);
        String password = "java123";

        while (true) {
            System.out.print("Enter password: ");
            String input = sc.nextLine();

            if (input.equals(password)) {
                break;
            }
            System.out.println("Incorrect password. Try again.");
        }

        System.out.println("Access granted.\n");

        // ---------------- continue Statement ----------------
        System.out.println("\n==================== CONTINUE STATEMENT ====================");
        System.out.println("""
The 'continue' statement is used to SKIP the current iteration
and move to the next iteration of the loop.

When continue is executed:
✔ Current iteration stops
✔ Loop condition is rechecked
✔ Loop continues normally

continue does NOT terminate the loop.
""");

        // ---------------- Example 3: continue in for Loop ----------------
        System.out.println("\n==================== EXAMPLE 3: continue IN for LOOP ====================");
        System.out.println("""
Skip printing number 5.
""");

        for (int i = 1; i <= 10; i++) {
            if (i == 5) {
                continue;
            }
            System.out.println("Number: " + i);
        }

        System.out.println("Iteration skipped using continue.\n");

        // ---------------- Example 4: continue in while Loop ----------------
        System.out.println("\n==================== EXAMPLE 4: continue IN while LOOP ====================");
        System.out.println("""
Skip even numbers and print only odd numbers.
""");

        int num = 0;

        while (num < 10) {
            num++;

            if (num % 2 == 0) {
                continue;
            }
            System.out.println("Odd Number: " + num);
        }

        System.out.println("Odd number printing completed.\n");

        // ---------------- Example 5: break in Nested Loop ----------------
        System.out.println("\n==================== EXAMPLE 5: break IN NESTED LOOP ====================");
        System.out.println("""
Exit inner loop when j equals 3.
""");

        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 5; j++) {
                if (j == 3) {
                    break;
                }
                System.out.print(j + " ");
            }
            System.out.println();
        }

        System.out.println("Nested loop break executed.\n");

        // ---------------- Example 6: continue in Nested Loop ----------------
        System.out.println("\n==================== EXAMPLE 6: continue IN NESTED LOOP ====================");
        System.out.println("""
Skip printing column number 2.
""");

        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 4; j++) {
                if (j == 2) {
                    continue;
                }
                System.out.print(j + " ");
            }
            System.out.println();
        }

        System.out.println("Nested loop continue executed.\n");

        // ---------------- break vs continue ----------------
        System.out.println("\n==================== BREAK vs CONTINUE ====================");
        System.out.println("""
break:
✔ Terminates the loop
✔ Control exits loop

continue:
✔ Skips current iteration
✔ Loop continues

Use break to STOP.
Use continue to SKIP.
""");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Using break when continue is needed
✘ Forgetting loop update when using continue
✘ Overusing break causing unclear logic
✘ Confusing loop exit with iteration skip

Tip:
✔ Use control statements sparingly
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Control statements modify loop execution.
→ break exits the loop immediately.
→ continue skips the current iteration.
→ Used to control flow efficiently.
→ Essential for real-world looping logic.

Next topic: Practice programs on loops.
""");

        sc.close();
    }
}
