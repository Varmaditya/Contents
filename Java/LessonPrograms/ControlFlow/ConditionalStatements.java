// Program: Conditional Statements in Java

public class ConditionalStatements {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== CONDITIONAL STATEMENTS IN JAVA ====================");
        System.out.println("""
In real life, decisions are made based on CONDITIONS.

Examples:
✔ If traffic light is RED, stop.
✔ If marks are greater than or equal to 35, pass.
✔ If balance is sufficient, allow withdrawal.

Similarly, Java programs need to make decisions
based on conditions. This is done using CONDITIONAL STATEMENTS.
""");

        // ---------------- What are Conditions ----------------
        System.out.println("\n==================== WHAT IS A CONDITION ====================");
        System.out.println("""
A condition is an expression that evaluates to:
✔ true
✔ false

Conditions are created using:
✔ relational operators (>, <, >=, <=, ==, !=)
✔ logical operators (&&, ||, !)

Example conditions:
    age >= 18
    marks < 35
    balance > amount
""");

        // ---------------- Why Conditional Statements ----------------
        System.out.println("\n==================== WHY CONDITIONAL STATEMENTS ====================");
        System.out.println("""
Without conditional statements:
✘ Programs would always execute line by line
✘ No decision-making would be possible
✘ Programs would not respond to different inputs

Conditional statements allow:
✔ selecting different execution paths
✔ controlling logic flow
✔ making programs dynamic and intelligent
""");

        // ---------------- Types of Conditional Statements ----------------
        System.out.println("\n==================== TYPES OF CONDITIONAL STATEMENTS ====================");
        System.out.println("""
Java provides the following conditional statements:

1. if statement
2. if-else statement
3. if-else-if ladder
4. nested if statement
5. switch statement

Each of these allows decision-making in different scenarios.
""");

        // ---------------- Simple Flow Example ----------------
        System.out.println("\n==================== SIMPLE DECISION FLOW ====================");
        System.out.println("""
Decision-making flow:

START
 ↓
Check Condition
 ↓
true  → Execute one block
false → Execute another block (or skip)

This basic flow is the foundation of all conditional statements.
""");

        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD MAPPING ====================");
        System.out.println("""
Real-world decisions mapped to Java:

✔ ATM System:
   If PIN is correct → Allow transaction
   Else → Block access

✔ Exam Result:
   If marks >= passing marks → Pass
   Else → Fail

✔ Online Shopping:
   If stock available → Place order
   Else → Show out of stock

Conditional statements make such logic possible in code.
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Conditional statements control decision-making in Java.
→ They execute code based on true or false conditions.
→ Conditions are formed using relational and logical operators.
→ Java provides multiple conditional statements for different scenarios.

Conditional statements are the backbone of program logic.
""");
    }
}
