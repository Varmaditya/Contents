// Program: Nested Conditional Statements in Java

import java.util.Scanner;

public class NestedConditionals {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== NESTED CONDITIONAL STATEMENTS ====================");
        System.out.println("""
Nested conditional statements are conditional statements
written INSIDE another conditional statement.

In simple words:
✔ An if (or if-else) inside another if or else block
✔ Used when a decision depends on another decision

Nested conditionals allow multi-level decision making.
""");

        // ---------------- Why Nested Conditionals ----------------
        System.out.println("\n==================== WHY NESTED CONDITIONALS ====================");
        System.out.println("""
Some situations cannot be solved using a single condition.

Example:
✔ If user is logged in
      then check user role
✔ If student passed
      then check grade
✔ If balance is sufficient
      then check daily limit

Such problems require nested condition checks.
""");

        // ---------------- Syntax ----------------
        System.out.println("\n==================== SYNTAX OF NESTED CONDITIONALS ====================");
        System.out.println("""
Basic syntax:

    if (condition1) {
        if (condition2) {
            // executes if both conditions are true
        }
    }

With else:

    if (condition1) {
        if (condition2) {
            // inner if true
        } else {
            // inner else
        }
    } else {
        // outer else
    }

Execution depends on OUTER condition first.
""");

        // ---------------- Flow Explanation ----------------
        System.out.println("\n==================== FLOW OF NESTED CONDITIONALS ====================");
        System.out.println("""
Execution Flow:

START
 ↓
Check outer condition
 ↓
If false → outer else executes
If true  → check inner condition
              ↓
         inner true  → execute block
         inner false → execute inner else
""");

        // ---------------- Example 1: Login and Role Check ----------------
        System.out.println("\n==================== EXAMPLE 1: LOGIN & ROLE CHECK ====================");
        System.out.println("""
Check user access based on:
1. Login status
2. User role
""");

        boolean isLoggedIn = true;
        String role = "admin";

        if (isLoggedIn) {
            if (role.equalsIgnoreCase("admin")) {
                System.out.println("Access granted: Admin Dashboard");
            } else {
                System.out.println("Access granted: User Dashboard");
            }
        } else {
            System.out.println("Access denied: Please login first");
        }

        System.out.println("Login check completed.\n");

        // ---------------- Example 2: Exam Result with Distinction ----------------
        System.out.println("\n==================== EXAMPLE 2: EXAM RESULT CHECK ====================");
        System.out.println("""
Check result:
✔ First check pass/fail
✔ If passed, check distinction
""");

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter marks: ");
        int marks = sc.nextInt();

        if (marks >= 35) {
            System.out.println("Result: PASS");

            if (marks >= 75) {
                System.out.println("Distinction awarded");
            }
        } else {
            System.out.println("Result: FAIL");
        }

        System.out.println("Result evaluation completed.\n");

        // ---------------- Example 3: ATM Withdrawal ----------------
        System.out.println("\n==================== EXAMPLE 3: ATM WITHDRAWAL ====================");
        System.out.println("""
Check withdrawal:
✔ Sufficient balance
✔ Amount within daily limit
""");

        int balance = 10000;
        int dailyLimit = 5000;

        System.out.print("Enter withdrawal amount: ");
        int withdraw = sc.nextInt();

        if (withdraw <= balance) {
            if (withdraw <= dailyLimit) {
                balance = balance - withdraw;
                System.out.println("Withdrawal successful");
                System.out.println("Remaining balance: " + balance);
            } else {
                System.out.println("Amount exceeds daily limit");
            }
        } else {
            System.out.println("Insufficient balance");
        }

        System.out.println("ATM transaction completed.\n");

        // ---------------- Example 4: Driving License Eligibility ----------------
        System.out.println("\n==================== EXAMPLE 4: DRIVING LICENSE ELIGIBILITY ====================");
        System.out.println("""
Eligibility rules:
✔ Age >= 18
✔ Must have learner license
""");

        System.out.print("Enter age: ");
        int age = sc.nextInt();

        boolean hasLearner = true;

        if (age >= 18) {
            if (hasLearner) {
                System.out.println("Eligible for permanent license");
            } else {
                System.out.println("Apply for learner license first");
            }
        } else {
            System.out.println("Not eligible due to age");
        }

        System.out.println("Eligibility check completed.\n");

        // ---------------- Example 5: Online Order Placement ----------------
        System.out.println("\n==================== EXAMPLE 5: ONLINE ORDER PLACEMENT ====================");
        System.out.println("""
Order rules:
✔ User logged in
✔ Product in stock
""");

        boolean loggedIn = true;
        boolean inStock = false;

        if (loggedIn) {
            if (inStock) {
                System.out.println("Order placed successfully");
            } else {
                System.out.println("Product out of stock");
            }
        } else {
            System.out.println("Please login to place order");
        }

        System.out.println("Order check completed.\n");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Deep nesting making code hard to read
✘ Forgetting braces { }
✘ Confusing which else belongs to which if
✘ Using nested if when if-else-if ladder is better

Tip:
✔ Indentation is very important in nested conditionals
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Nested conditionals mean one conditional inside another.
→ Outer condition is checked first.
→ Inner condition runs only if outer condition is true.
→ Used for multi-level decision making.
→ Common in login systems, exams, banking, and validations.

Next topic: Looping statements (Introduction).
""");

        sc.close();
    }
}
