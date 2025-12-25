// Program: if Statement in Java

import java.util.Scanner;

public class IfStatement {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== IF STATEMENT IN JAVA ====================");
        System.out.println("""
The 'if' statement is the MOST BASIC conditional statement in Java.
It allows a program to execute a block of code ONLY when a condition is true.

If the condition is false:
✔ the code inside the if block is skipped
✔ program execution continues normally

The if statement performs ONE-WAY decision making.
""");

        // ---------------- Syntax ----------------
        System.out.println("\n==================== SYNTAX OF IF STATEMENT ====================");
        System.out.println("""
Syntax:

    if (condition) {
        // code to execute if condition is true
    }

Important points:
✔ Condition must return true or false
✔ Condition is written inside parentheses ( )
✔ Code block is written inside braces { }
""");

        // ---------------- Flow Explanation ----------------
        System.out.println("\n==================== FLOW OF IF STATEMENT ====================");
        System.out.println("""
Execution Flow:

START
 ↓
Check condition
 ↓
If true  → Execute if block
If false → Skip if block
 ↓
Continue program execution
""");

        // ---------------- Example 1: Simple Condition ----------------
        System.out.println("\n==================== EXAMPLE 1: SIMPLE CONDITION ====================");
        System.out.println("""
Check whether a number is positive.

Condition:
    number > 0
""");

        int number = 10;

        if (number > 0) {
            System.out.println("The number is positive.");
        }

        System.out.println("Program continues after if.\n");

        // ---------------- Example 2: User Input Check ----------------
        System.out.println("\n==================== EXAMPLE 2: USER INPUT CHECK ====================");
        System.out.println("""
Check if a person is eligible to vote.
Condition:
    age >= 18
""");

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = sc.nextInt();

        if (age >= 18) {
            System.out.println("You are eligible to vote.");
        }

        System.out.println("Voting eligibility check completed.\n");

        // ---------------- Example 3: Password Length Validation ----------------
        System.out.println("\n==================== EXAMPLE 3: PASSWORD VALIDATION ====================");
        System.out.println("""
Check if a password length is at least 8 characters.
""");

        sc.nextLine(); // clear buffer
        System.out.print("Enter a password: ");
        String password = sc.nextLine();

        if (password.length() >= 8) {
            System.out.println("Password length is valid.");
        }

        System.out.println("Password check done.\n");

        // ---------------- Example 4: Multiple Conditions (Logical AND) ----------------
        System.out.println("\n==================== EXAMPLE 4: MULTIPLE CONDITIONS ====================");
        System.out.println("""
Check if a student has passed:
Condition:
✔ Marks >= 35
✔ Attendance >= 75%
""");

        System.out.print("Enter marks: ");
        int marks = sc.nextInt();

        System.out.print("Enter attendance percentage: ");
        int attendance = sc.nextInt();

        if (marks >= 35 && attendance >= 75) {
            System.out.println("Student has passed.");
        }

        System.out.println("Result evaluation completed.\n");

        // ---------------- Example 5: Using Boolean Variable ----------------
        System.out.println("\n==================== EXAMPLE 5: BOOLEAN CONDITION ====================");
        System.out.println("""
Boolean variables can be used directly in if conditions.
""");

        boolean isLoggedIn = true;

        if (isLoggedIn) {
            System.out.println("Welcome! You are logged in.");
        }

        System.out.println("Login check finished.\n");

        // ---------------- Example 6: Nested Logic Inside if ----------------
        System.out.println("\n==================== EXAMPLE 6: LOGIC INSIDE IF BLOCK ====================");
        System.out.println("""
The if block can contain multiple statements.
""");

        int balance = 5000;
        int withdraw = 2000;

        if (balance >= withdraw) {
            balance = balance - withdraw;
            System.out.println("Withdrawal successful.");
            System.out.println("Remaining balance: " + balance);
        }

        System.out.println("ATM operation completed.\n");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Using '=' instead of '==' in condition
✘ Missing braces { } for multiple statements
✘ Using non-boolean condition (not allowed in Java)

Correct:
    if (x == 10)

Incorrect:
    if (x = 10)
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ The if statement executes code ONLY when condition is true.
→ It performs one-way decision making.
→ Condition must be boolean (true/false).
→ Multiple statements require braces { }.
→ if is the foundation of all conditional logic in Java.

Next step: if-else statement.
""");

        sc.close();
    }
}
