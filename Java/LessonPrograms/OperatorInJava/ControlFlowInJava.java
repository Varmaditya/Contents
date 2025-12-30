// Program: Control Flow Statements in Java

public class ControlFlowInJava {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== CONTROL FLOW STATEMENTS ====================");
        System.out.println("""
In a Java program, statements normally execute from TOP to BOTTOM
in a sequential manner.

However, real-world programs need to:
✔ make decisions
✔ repeat tasks
✔ choose between multiple paths
✔ stop or skip execution based on conditions

Control Flow Statements allow us to CONTROL
the flow of execution of a program.
""");

        // ---------------- Why Control Flow is Needed ----------------
        System.out.println("\n==================== WHY CONTROL FLOW IS NEEDED ====================");
        System.out.println("""
Without control flow:
- Every line would execute in order
- No decision-making would be possible
- Programs would not be interactive or intelligent

Examples of real-life decisions:
✔ If it rains, take an umbrella
✔ If marks >= 35, pass else fail
✔ Repeat task until work is complete

All these require control flow.
""");

        // ---------------- Types of Control Flow Statements ----------------
        System.out.println("\n==================== TYPES OF CONTROL FLOW STATEMENTS ====================");
        System.out.println("""
Java control flow statements are broadly divided into FOUR categories:

1. Decision-Making Statements
2. Looping Statements
3. Jump Statements
4. Exception Control (introduced later)

Let us briefly understand each category.
""");

        // ---------------- Decision-Making Statements ----------------
        System.out.println("\n==================== 1. DECISION-MAKING STATEMENTS ====================");
        System.out.println("""
Decision-making statements execute code based on CONDITIONS.

They allow the program to choose ONE path from multiple options.

Common decision-making statements:
✔ if
✔ if-else
✔ if-else-if ladder
✔ switch

Example idea:
    If age >= 18 → allow voting
    Else → deny voting
""");

        // ---------------- Looping Statements ----------------
        System.out.println("\n==================== 2. LOOPING STATEMENTS ====================");
        System.out.println("""
Looping statements are used to REPEAT a block of code
until a condition is satisfied.

Instead of writing the same code again and again,
loops help reduce repetition.

Common looping statements:
✔ for loop
✔ while loop
✔ do-while loop

Example idea:
    Print numbers from 1 to 10
    Repeat until user enters correct password
""");

        // ---------------- Jump Statements ----------------
        System.out.println("\n==================== 3. JUMP STATEMENTS ====================");
        System.out.println("""
Jump statements transfer control from one part of the program
to another part immediately.

They are used to:
✔ exit loops
✔ skip iterations
✔ return values from methods

Common jump statements:
✔ break
✔ continue
✔ return

Example idea:
    Stop loop when condition is met
    Skip current iteration
""");

        // ---------------- Flow Control Visualization ----------------
        System.out.println("\n==================== HOW CONTROL FLOW WORKS ====================");
        System.out.println("""
Control flow changes the normal execution order:

SEQUENTIAL FLOW:
    Statement 1
    Statement 2
    Statement 3

CONTROLLED FLOW:
    Decision → choose path
    Loop → repeat block
    Jump → move execution instantly

This makes programs dynamic and logical.
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Control flow statements control the execution order of a program.
→ They allow decision-making, repetition, and jumping.
→ Main categories:
   ✔ Decision-making
   ✔ Looping
   ✔ Jump statements
→ Control flow is essential for real-world logic in programs.

This forms the foundation for writing intelligent Java programs.
""");
    }
}
