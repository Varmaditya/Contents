// Program: Enhanced for Loop in Java

public class EnhancedForLoop {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== ENHANCED FOR LOOP IN JAVA ====================");
        System.out.println("""
The Enhanced for loop, also called the for-each loop,
is a looping statement used to traverse elements
one by one in a sequence.

It provides a simpler syntax compared to the traditional for loop
when we only need to ACCESS values sequentially.
""");


        // ---------------- Syntax ----------------
        System.out.println("\n==================== SYNTAX OF ENHANCED FOR LOOP ====================");
        System.out.println("""
Syntax:

    for (dataType variable : source) {
        // loop body
    }

Explanation:
✔ variable holds one value at a time
✔ source represents a group of values
✔ Loop automatically moves to next value
""");


        // ---------------- Flow Explanation ----------------
        System.out.println("\n==================== FLOW OF ENHANCED FOR LOOP ====================");
        System.out.println("""
Execution Flow:

START
 ↓
Pick first value
 ↓
Assign to loop variable
 ↓
Execute loop body
 ↓
Pick next value
 ↓
Repeat until values are exhausted
""");


        // ---------------- Example 1: Printing Values ----------------
        System.out.println("\n==================== EXAMPLE 1: PRINTING VALUES ====================");
        System.out.println("""
Print values using enhanced for loop.
""");

        int[] values = {1, 2, 3, 4, 5};

        for (int v : values) {
            System.out.println("Value: " + v);
        }

        System.out.println("Value printing completed.\n");


        // ---------------- Example 2: Summation ----------------
        System.out.println("\n==================== EXAMPLE 2: SUMMATION ====================");
        System.out.println("""
Calculate sum of values.
""");

        int sum = 0;

        for (int v : values) {
            sum = sum + v;
        }

        System.out.println("Sum = " + sum);
        System.out.println("Summation completed.\n");


        // ---------------- Example 3: Conditional Check ----------------
        System.out.println("\n==================== EXAMPLE 3: CONDITIONAL CHECK ====================");
        System.out.println("""
Check and print values greater than 3.
""");

        for (int v : values) {
            if (v > 3) {
                System.out.println(v + " is greater than 3");
            }
        }

        System.out.println("Conditional check completed.\n");


        // ---------------- Comparison with for Loop ----------------
        System.out.println("\n==================== FOR vs ENHANCED FOR ====================");
        System.out.println("""
Traditional for loop:
✔ Uses index
✔ More control
✔ Suitable when position matters

Enhanced for loop:
✔ No index handling
✔ Cleaner syntax
✔ Suitable when only values are needed
""");


        // ---------------- Limitations ----------------
        System.out.println("\n==================== LIMITATIONS ====================");
        System.out.println("""
Enhanced for loop:
✘ Cannot access index
✘ Cannot modify loop sequence
✘ Cannot iterate in reverse

Use traditional for loop when such control is required.
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Enhanced for loop simplifies looping.
→ Automatically iterates over values.
→ Best for read-only traversal.
→ Improves readability and reduces errors.

This completes Enhanced for Loop.
""");
    }
}
