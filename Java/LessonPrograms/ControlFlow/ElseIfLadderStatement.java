// Program: if-else-if Ladder in Java

import java.util.Scanner;

public class ElseIfLadderStatement {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== IF-ELSE-IF LADDER IN JAVA ====================");
        System.out.println("""
The 'if-else-if' ladder is used when we need to check
MULTIPLE conditions one after another.

Only ONE block executes:
✔ The FIRST condition that evaluates to true
✔ Remaining conditions are skipped

This provides MULTI-WAY decision making.
""");

        // ---------------- Syntax ----------------
        System.out.println("\n==================== SYNTAX OF IF-ELSE-IF LADDER ====================");
        System.out.println("""
Syntax:

    if (condition1) {
        // executes if condition1 is true
    } else if (condition2) {
        // executes if condition2 is true
    } else if (condition3) {
        // executes if condition3 is true
    } else {
        // executes if all conditions are false
    }

Important points:
✔ Conditions are checked from TOP to BOTTOM
✔ First true condition executes
✔ else block is optional but recommended
""");

        // ---------------- Flow Explanation ----------------
        System.out.println("\n==================== FLOW OF IF-ELSE-IF LADDER ====================");
        System.out.println("""
Execution Flow:

START
 ↓
Check condition1
 ↓
true  → Execute block1 → STOP
false → Check condition2
 ↓
true  → Execute block2 → STOP
false → Check next condition
 ↓
All false → Execute else block
""");

        // ---------------- Example 1: Grade Calculator ----------------
        System.out.println("\n==================== EXAMPLE 1: GRADE CALCULATOR ====================");
        System.out.println("""
Assign grade based on marks.

Conditions:
✔ marks >= 90 → A+
✔ marks >= 75 → A
✔ marks >= 60 → B
✔ marks >= 50 → C
✔ else → Fail
""");

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter marks: ");
        int marks = sc.nextInt();

        if (marks >= 90) {
            System.out.println("Grade: A+");
        } else if (marks >= 75) {
            System.out.println("Grade: A");
        } else if (marks >= 60) {
            System.out.println("Grade: B");
        } else if (marks >= 50) {
            System.out.println("Grade: C");
        } else {
            System.out.println("Result: Fail");
        }

        System.out.println("Grade evaluation completed.\n");

        // ---------------- Example 2: Traffic Signal System ----------------
        System.out.println("\n==================== EXAMPLE 2: TRAFFIC SIGNAL ====================");
        System.out.println("""
Decide action based on traffic signal color.
""");

        sc.nextLine(); // clear buffer
        System.out.print("Enter traffic light color: ");
        String signal = sc.nextLine();

        if (signal.equalsIgnoreCase("RED")) {
            System.out.println("STOP");
        } else if (signal.equalsIgnoreCase("YELLOW")) {
            System.out.println("GET READY");
        } else if (signal.equalsIgnoreCase("GREEN")) {
            System.out.println("GO");
        } else {
            System.out.println("Invalid signal color");
        }

        System.out.println("Traffic signal check completed.\n");

        // ---------------- Example 3: Electricity Bill Slab ----------------
        System.out.println("\n==================== EXAMPLE 3: ELECTRICITY BILL SLAB ====================");
        System.out.println("""
Calculate electricity slab category (not amount).

Conditions:
✔ units <= 100 → Low Usage
✔ units <= 300 → Medium Usage
✔ units <= 600 → High Usage
✔ else → Very High Usage
""");

        System.out.print("Enter units consumed: ");
        int units = sc.nextInt();

        if (units <= 100) {
            System.out.println("Usage Category: Low");
        } else if (units <= 300) {
            System.out.println("Usage Category: Medium");
        } else if (units <= 600) {
            System.out.println("Usage Category: High");
        } else {
            System.out.println("Usage Category: Very High");
        }

        System.out.println("Usage classification completed.\n");

        // ---------------- Example 4: Age Group Classification ----------------
        System.out.println("\n==================== EXAMPLE 4: AGE GROUP ====================");
        System.out.println("""
Classify person based on age.
""");

        System.out.print("Enter age: ");
        int age = sc.nextInt();

        if (age < 13) {
            System.out.println("Category: Child");
        } else if (age < 20) {
            System.out.println("Category: Teenager");
        } else if (age < 60) {
            System.out.println("Category: Adult");
        } else {
            System.out.println("Category: Senior Citizen");
        }

        System.out.println("Age group identification completed.\n");

        // ---------------- Example 5: Bank Account Type ----------------
        System.out.println("\n==================== EXAMPLE 5: BANK ACCOUNT TYPE ====================");
        System.out.println("""
Decide minimum balance requirement based on account type.
""");

        sc.nextLine(); // clear buffer
        System.out.print("Enter account type (Savings/Current/Salary): ");
        String accType = sc.nextLine();

        if (accType.equalsIgnoreCase("Savings")) {
            System.out.println("Minimum balance: ₹1000");
        } else if (accType.equalsIgnoreCase("Current")) {
            System.out.println("Minimum balance: ₹5000");
        } else if (accType.equalsIgnoreCase("Salary")) {
            System.out.println("Minimum balance: ₹0");
        } else {
            System.out.println("Invalid account type");
        }

        System.out.println("Account check completed.\n");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Incorrect condition order (more general before specific)
✘ Forgetting else block
✘ Expecting multiple blocks to run (only one executes)
✘ Using == instead of equals() for String comparison

Always arrange conditions from MOST specific to MOST general.
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ if-else-if ladder allows MULTI-WAY decision making.
→ Conditions are checked top to bottom.
→ First true condition executes and rest are skipped.
→ else block handles all remaining cases.
→ Used when choices depend on ranges or multiple values.

Next topic: nested if statement.
""");

        sc.close();
    }
}
