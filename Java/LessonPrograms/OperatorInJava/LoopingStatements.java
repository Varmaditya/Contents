// Program: Looping Statements in Java

public class LoopingStatements {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== LOOPING STATEMENTS IN JAVA ====================");
        System.out.println("""
In many situations, a task needs to be performed REPEATEDLY.

Examples:
✔ Print numbers from 1 to 10
✔ Display all students in a class
✔ Retry login until correct password is entered
✔ Process multiple transactions

Writing the same code again and again is inefficient.
Looping statements allow us to REPEAT a block of code automatically.
""");

        // ---------------- What is a Loop ----------------
        System.out.println("\n==================== WHAT IS A LOOP ====================");
        System.out.println("""
A loop is a control flow structure that:
✔ Executes a block of code repeatedly
✔ Continues execution based on a condition

Every loop has three key parts:
1. Initialization   → starting point
2. Condition        → decides whether loop continues
3. Update           → changes loop control variable
""");

        // ---------------- Why Looping Statements ----------------
        System.out.println("\n==================== WHY LOOPING STATEMENTS ====================");
        System.out.println("""
Without loops:
✘ Code repetition increases
✘ Programs become lengthy and hard to maintain
✘ Logic becomes difficult to modify

With loops:
✔ Less code
✔ Better readability
✔ Easy repetition
✔ Efficient execution
""");

        // ---------------- Types of Looping Statements ----------------
        System.out.println("\n==================== TYPES OF LOOPING STATEMENTS ====================");
        System.out.println("""
Java provides THREE main looping statements:

1. for loop
2. while loop
3. do-while loop

Each loop is used in different scenarios based on:
✔ Known number of iterations
✔ Unknown number of iterations
✔ At least one execution requirement
""");

        // ---------------- Loop Execution Flow ----------------
        System.out.println("\n==================== LOOP EXECUTION FLOW ====================");
        System.out.println("""
General loop execution flow:

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
        Repeat condition check
false → Exit loop
""");

        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD MAPPING ====================");
        System.out.println("""
Real-life examples of loops:

✔ Attendance register:
   Repeat for each student

✔ ATM PIN attempt:
   Repeat until correct PIN

✔ Washing machine:
   Repeat wash cycle steps

✔ Mobile app refresh:
   Repeat data fetch until stopped

Loops model repetition found in daily activities.
""");

        // ---------------- Loop Control Statements ----------------
        System.out.println("\n==================== LOOP CONTROL STATEMENTS ====================");
        System.out.println("""
Loop execution can be controlled using special statements:

✔ break     → exits the loop immediately
✔ continue  → skips current iteration
✔ return    → exits method (covered later)

These statements modify normal loop flow.
""");

        // ---------------- Common Loop Problems ----------------
        System.out.println("\n==================== COMMON LOOP PROBLEMS ====================");
        System.out.println("""
✘ Infinite loops (condition never becomes false)
✘ Off-by-one errors
✘ Incorrect update logic
✘ Wrong condition placement

Understanding loop structure helps avoid these problems.
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Looping statements allow repetition of code.
→ They reduce redundancy and improve efficiency.
→ Java provides for, while, and do-while loops.
→ Each loop has initialization, condition, and update.
→ Loops are essential for processing repetitive tasks.

This forms the foundation of iterative programming in Java.
""");
    }
}
