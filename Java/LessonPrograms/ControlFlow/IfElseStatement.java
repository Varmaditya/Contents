// Program: if-else Statement in Java

import java.util.Scanner;

public class IfElseStatement {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== IF-ELSE STATEMENT IN JAVA ====================");
        System.out.println("""
The 'if-else' statement is an extension of the 'if' statement.

It allows a program to choose between TWO paths:
✔ One block executes when the condition is true
✔ Another block executes when the condition is false

This is called TWO-WAY decision making.
""");

        // ---------------- Syntax ----------------
        System.out.println("\n==================== SYNTAX OF IF-ELSE ====================");
        System.out.println("""
Syntax:

    if (condition) {
        // executes when condition is true
    } else {
        // executes when condition is false
    }

Important points:
✔ Exactly one block executes
✔ Condition must be boolean
✔ else cannot exist without if
""");

        // ---------------- Flow Explanation ----------------
        System.out.println("\n==================== FLOW OF IF-ELSE ====================");
        System.out.println("""
Execution Flow:

START
 ↓
Check condition
 ↓
true  → Execute if block
false → Execute else block
 ↓
Continue program execution
""");

        // ---------------- Example 1: Even or Odd ----------------
        System.out.println("\n==================== EXAMPLE 1: EVEN OR ODD ====================");
        System.out.println("""
Check whether a number is EVEN or ODD.

Condition:
    number % 2 == 0
""");

        int number = 15;

        if (number % 2 == 0) {
            System.out.println("The number is EVEN.");
        } else {
            System.out.println("The number is ODD.");
        }

        System.out.println("Even/Odd check completed.\n");

        // ---------------- Example 2: Pass or Fail ----------------
        System.out.println("\n==================== EXAMPLE 2: PASS OR FAIL ====================");
        System.out.println("""
Check if a student has passed an exam.

Condition:
    marks >= 35
""");

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter marks: ");
        int marks = sc.nextInt();

        if (marks >= 35) {
            System.out.println("Result: PASS");
        } else {
            System.out.println("Result: FAIL");
        }

        System.out.println("Result evaluation completed.\n");

        // ---------------- Example 3: Login Validation ----------------
        System.out.println("\n==================== EXAMPLE 3: LOGIN VALIDATION ====================");
        System.out.println("""
Check whether login is successful.

Condition:
    enteredPin == correctPin
""");

        int correctPin = 1234;

        System.out.print("Enter PIN: ");
        int enteredPin = sc.nextInt();

        if (enteredPin == correctPin) {
            System.out.println("Login successful.");
        } else {
            System.out.println("Invalid PIN.");
        }

        System.out.println("Login attempt finished.\n");

        // ---------------- Example 4: Bank Balance Check ----------------
        System.out.println("\n==================== EXAMPLE 4: BANK BALANCE CHECK ====================");
        System.out.println("""
Check whether withdrawal is allowed.

Condition:
    balance >= withdrawAmount
""");

        int balance = 5000;
        int withdrawAmount = 7000;

        if (balance >= withdrawAmount) {
            balance = balance - withdrawAmount;
            System.out.println("Withdrawal successful.");
            System.out.println("Remaining balance: " + balance);
        } else {
            System.out.println("Insufficient balance.");
        }

        System.out.println("Transaction completed.\n");

        // ---------------- Example 5: Boolean Condition ----------------
        System.out.println("\n==================== EXAMPLE 5: BOOLEAN CONDITION ====================");
        System.out.println("""
Boolean variables can directly control if-else logic.
""");

        boolean isInternetConnected = false;

        if (isInternetConnected) {
            System.out.println("Internet is connected.");
        } else {
            System.out.println("No internet connection.");
        }

        System.out.println("Connection check finished.\n");

        // ---------------- Example 6: Discount Eligibility ----------------
        System.out.println("\n==================== EXAMPLE 6: DISCOUNT ELIGIBILITY ====================");
        System.out.println("""
Check whether customer gets a discount.

Condition:
    purchaseAmount >= 2000
""");

        System.out.print("Enter purchase amount: ");
        double amount = sc.nextDouble();

        if (amount >= 2000) {
            System.out.println("Discount applied.");
        } else {
            System.out.println("No discount available.");
        }

        System.out.println("Billing check completed.\n");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Forgetting else block logic
✘ Using assignment (=) instead of comparison (==)
✘ Writing conditions that are not boolean
✘ Assuming both blocks will execute (only one executes)

Remember:
✔ Either if OR else executes, never both
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ if-else provides TWO-WAY decision making.
→ One block executes when condition is true.
→ The other block executes when condition is false.
→ Condition must always be boolean.
→ Used in validation, checking, comparisons, decisions.

Next topic: if-else-if ladder.
""");

        sc.close();
    }
}
