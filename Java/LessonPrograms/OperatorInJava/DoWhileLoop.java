// Program: do-while Loop in Java

import java.util.Scanner;

public class DoWhileLoop {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== DO-WHILE LOOP IN JAVA ====================");
        System.out.println("""
The 'do-while' loop is a looping statement that
executes a block of code AT LEAST ONCE.

Unlike the while loop:
✔ The condition is checked AFTER execution
✔ Loop body runs first, condition later

The do-while loop is called an EXIT-CONTROLLED loop.
""");

        // ---------------- Syntax ----------------
        System.out.println("\n==================== SYNTAX OF DO-WHILE LOOP ====================");
        System.out.println("""
Syntax:

    do {
        // loop body
    } while (condition);

Important points:
✔ Loop body executes at least once
✔ Condition must be boolean
✔ Semicolon (;) after while is mandatory
""");

        // ---------------- Flow Explanation ----------------
        System.out.println("\n==================== FLOW OF DO-WHILE LOOP ====================");
        System.out.println("""
Execution Flow:

START
 ↓
Execute loop body
 ↓
Update
 ↓
Check condition
 ↓
true  → Repeat loop
false → Exit loop
""");

        // ---------------- Example 1: Print Numbers ----------------
        System.out.println("\n==================== EXAMPLE 1: PRINT NUMBERS ====================");
        System.out.println("""
Print numbers from 1 to 5.
""");

        int i = 1;

        do {
            System.out.println("Number: " + i);
            i++;
        } while (i <= 5);

        System.out.println("Number printing completed.\n");

        // ---------------- Example 2: Menu-Driven Program ----------------
        System.out.println("\n==================== EXAMPLE 2: MENU-DRIVEN PROGRAM ====================");
        System.out.println("""
Display menu until user chooses to exit.
""");

        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n1. Check Balance");
            System.out.println("2. Deposit Money");
            System.out.println("3. Exit");
            System.out.print("Enter choice: ");

            choice = sc.nextInt();

            if (choice == 1) {
                System.out.println("Balance: ₹5000");
            } else if (choice == 2) {
                System.out.println("Deposit successful");
            } else if (choice == 3) {
                System.out.println("Exiting...");
            } else {
                System.out.println("Invalid choice");
            }

        } while (choice != 3);

        System.out.println("Menu loop completed.\n");

        // ---------------- Example 3: Password Retry ----------------
        System.out.println("\n==================== EXAMPLE 3: PASSWORD RETRY ====================");
        System.out.println("""
Prompt user until correct password is entered.
""");

        sc.nextLine(); // clear buffer
        String correctPassword = "java123";
        String input;

        do {
            System.out.print("Enter password: ");
            input = sc.nextLine();
        } while (!input.equals(correctPassword));

        System.out.println("Access granted.\n");

        // ---------------- Example 4: Sum of Digits ----------------
        System.out.println("\n==================== EXAMPLE 4: SUM OF DIGITS ====================");
        System.out.println("""
Calculate sum of digits of a number.
""");

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        int sum = 0;

        do {
            sum = sum + (num % 10);
            num = num / 10;
        } while (num != 0);

        System.out.println("Sum of digits: " + sum);
        System.out.println("Digit sum calculation completed.\n");

        // ---------------- while vs do-while ----------------
        System.out.println("\n==================== WHILE vs DO-WHILE ====================");
        System.out.println("""
while loop:
✔ Condition checked before execution
✔ Loop may not execute even once

do-while loop:
✔ Condition checked after execution
✔ Loop executes at least once

Choose do-while when one execution is mandatory.
""");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Forgetting semicolon after while
✘ Assuming condition checked first
✘ Infinite loop due to wrong condition
✘ Not updating loop variable

Remember:
✔ do-while always runs once
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ do-while loop executes code at least once.
→ Condition is checked after loop body.
→ It is an exit-controlled loop.
→ Useful for menus, retries, confirmations.

Next topic: Nested loops.
""");

        sc.close();
    }
}
