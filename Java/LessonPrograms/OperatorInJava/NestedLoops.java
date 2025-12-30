// Program: Nested Loops in Java

import java.util.Scanner;

public class NestedLoops {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== NESTED LOOPS IN JAVA ====================");
        System.out.println("""
Nested loops mean a loop placed INSIDE another loop.

In simple words:
✔ One loop runs completely
✔ For EACH iteration of the outer loop, the inner loop runs fully

Nested loops are commonly used for:
✔ Tables
✔ Matrices
✔ Pattern printing
✔ Multi-dimensional data
""");

        // ---------------- Why Nested Loops ----------------
        System.out.println("\n==================== WHY NESTED LOOPS ====================");
        System.out.println("""
Some problems require repetition inside repetition.

Examples:
✔ A class has multiple students, each student has multiple subjects
✔ A calendar has months and days
✔ A grid has rows and columns

Such problems require nested looping.
""");

        // ---------------- Flow Explanation ----------------
        System.out.println("\n==================== FLOW OF NESTED LOOPS ====================");
        System.out.println("""
Execution Flow:

Outer Loop → Iteration 1
    Inner Loop → runs completely
Outer Loop → Iteration 2
    Inner Loop → runs completely
...

Inner loop finishes ALL iterations
for each single iteration of outer loop.
""");

        // ---------------- Example 1: Nested for Loop ----------------
        System.out.println("\n==================== EXAMPLE 1: NESTED FOR LOOP ====================");
        System.out.println("""
Print a 3x3 grid of stars using nested for loops.
""");

        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        System.out.println("Nested for loop completed.\n");

        // ---------------- Example 2: Multiplication Table ----------------
        System.out.println("\n==================== EXAMPLE 2: MULTIPLICATION TABLE ====================");
        System.out.println("""
Print multiplication tables from 1 to 3.
""");

        for (int i = 1; i <= 3; i++) {
            System.out.println("Table of " + i);
            for (int j = 1; j <= 10; j++) {
                System.out.println(i + " x " + j + " = " + (i * j));
            }
            System.out.println();
        }

        System.out.println("Tables printed.\n");

        // ---------------- Example 3: Nested while Loop ----------------
        System.out.println("\n==================== EXAMPLE 3: NESTED WHILE LOOP ====================");
        System.out.println("""
Print numbers in a row-column format.
""");

        int row = 1;

        while (row <= 3) {
            int col = 1;
            while (col <= 4) {
                System.out.print(col + " ");
                col++;
            }
            System.out.println();
            row++;
        }

        System.out.println("Nested while loop completed.\n");

        // ---------------- Example 4: Pattern Printing ----------------
        System.out.println("\n==================== EXAMPLE 4: PATTERN PRINTING ====================");
        System.out.println("""
Print right-angled triangle pattern.
""");

        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        System.out.println("Pattern printed.\n");

        // ---------------- Example 5: Nested do-while Loop ----------------
        System.out.println("\n==================== EXAMPLE 5: NESTED DO-WHILE LOOP ====================");
        System.out.println("""
Demonstrate nested do-while loops.
""");

        int a = 1;

        do {
            int b = 1;
            do {
                System.out.print(a + "," + b + "  ");
                b++;
            } while (b <= 3);

            System.out.println();
            a++;
        } while (a <= 3);

        System.out.println("Nested do-while loop completed.\n");

        // ---------------- Example 6: Matrix-like Output ----------------
        System.out.println("\n==================== EXAMPLE 6: MATRIX OUTPUT ====================");
        System.out.println("""
Display matrix-style numbering.
""");

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of rows: ");
        int rows = sc.nextInt();

        System.out.print("Enter number of columns: ");
        int cols = sc.nextInt();

        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                System.out.print(i + "," + j + "  ");
            }
            System.out.println();
        }

        System.out.println("Matrix displayed.\n");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Forgetting to reset inner loop variable
✘ Confusing outer and inner loop counters
✘ Creating infinite loops
✘ Too much nesting making code hard to read

Tip:
✔ Keep nesting levels minimal
✔ Use proper indentation
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Nested loops are loops inside loops.
→ Inner loop runs completely for each outer loop iteration.
→ Used for grids, tables, matrices, and patterns.
→ Can be for, while, or do-while combinations.
→ Powerful but must be used carefully.

Next topic: Loop control statements (break & continue).
""");

        sc.close();
    }
}
