// Program: Advanced / Next Topics in Arrays

public class AdvanceTopicsInArrays {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== ADVANCED / NEXT TOPICS IN ARRAYS ====================");
        System.out.println("""
So far, we have covered the CORE fundamentals of arrays in Java.

Now that you understand how arrays work,
it is important to know what MORE exists
beyond the basics.

In this program:
✔ We introduce advanced array concepts
✔ We explain WHY they matter
✔ We show SMALL examples for understanding

These topics will be studied in detail later.
""");


        // ---------------- Why Advanced Array Topics ----------------
        System.out.println("\n==================== WHY ADVANCED ARRAY TOPICS ====================");
        System.out.println("""
Basic arrays help you store and access data.

Advanced array concepts help you:
✔ Write efficient programs
✔ Handle larger data sets
✔ Avoid common bugs
✔ Prepare for interviews and DSA
✔ Transition to Collections framework
""");


        // ---------------- Array Algorithms ----------------
        System.out.println("\n==================== ARRAY ALGORITHMS ====================");
        System.out.println("""
Array algorithms are step-by-step logical procedures
used to solve common problems using arrays.

Examples:
✔ Finding maximum or minimum
✔ Searching elements
✔ Reversing data
✔ Counting occurrences

These problems improve logical thinking.
""");

        int[] numbers = {5, 10, 15, 20};

        int max = numbers[0];
        for (int n : numbers) {
            if (n > max) {
                max = n;
            }
        }

        System.out.print("Array values: ");
        for (int n : numbers) {
            System.out.print(n + " ");
        }
        System.out.println("\nMaximum value (algorithm example): " + max);


        // ---------------- Time & Space Complexity ----------------
        System.out.println("\n==================== TIME & SPACE COMPLEXITY ====================");
        System.out.println("""
This topic focuses on PERFORMANCE.

It answers questions like:
✔ How fast does an operation run?
✔ How does performance change as data grows?

Idea:
Accessing one element is quick,
but checking every element takes more time.
""");

        System.out.println("Accessing first element: " + numbers[0]);
        System.out.println("Total elements checked: " + numbers.length);


        // ---------------- Fixed Size Limitation ----------------
        System.out.println("\n==================== FIXED SIZE LIMITATION ====================");
        System.out.println("""
Arrays have a FIXED size once created.

This means:
✔ You cannot add elements later
✔ You cannot remove elements
✔ Size must be known in advance
""");

        System.out.println("Array size is fixed at: " + numbers.length);


        // ---------------- Dynamic Arrays (Concept) ----------------
        System.out.println("\n==================== DYNAMIC ARRAYS (CONCEPT) ====================");
        System.out.println("""
Dynamic arrays overcome fixed-size limitation.

They can:
✔ Grow automatically
✔ Shrink when needed

In Java, this concept leads to:
✔ ArrayList
✔ Java Collections Framework

You will learn this after arrays.
""");

        System.out.println("(Dynamic resizing example will be shown later)");


        // ---------------- Arrays vs Collections ----------------
        System.out.println("\n==================== ARRAYS VS COLLECTIONS ====================");
        System.out.println("""
Arrays:
✔ Fixed size
✔ Faster access
✔ Simple structure

Collections:
✔ Dynamic size
✔ Rich features
✔ Easier data handling

Understanding arrays makes collections easier.
""");

        System.out.println("Array element example: " + numbers[2]);


        // ---------------- Arrays and Methods ----------------
        System.out.println("\n==================== ARRAYS AND METHODS ====================");
        System.out.println("""
Arrays can be passed to methods.

When passed:
✔ Methods can access all elements
✔ Changes affect the original array

This introduces reference behavior.
""");

        printFirstElement(numbers);


        // ---------------- Reference Behavior (Heap Concept) ----------------
        System.out.println("\n==================== REFERENCE BEHAVIOR ====================");
        System.out.println("""
Array variables store REFERENCES, not actual data.

This means:
✔ Multiple variables can refer to same array
✔ Changes from one reference affect original array
""");

        int[] ref = numbers;
        ref[0] = 99;

        System.out.println("Modified using another reference:");
        System.out.println("numbers[0] = " + numbers[0]);


        // ---------------- Array Copying ----------------
        System.out.println("\n==================== ARRAY COPYING ====================");
        System.out.println("""
Array copying is used to:
✔ Avoid unwanted data modification
✔ Create independent copies
✔ Protect original data
""");

        int[] copy = numbers.clone();
        copy[1] = 77;

        System.out.println("Original numbers[1]: " + numbers[1]);
        System.out.println("Copied   copy[1]: " + copy[1]);


        // ---------------- Mutability & Safety ----------------
        System.out.println("\n==================== ARRAY MUTABILITY & SAFETY ====================");
        System.out.println("""
Arrays are MUTABLE by default.

This means:
✔ Values can be changed after creation
✔ Care is needed when sharing arrays
""");

        System.out.println("Mutable example: numbers[2] = " + numbers[2]);


        // ---------------- Why These Topics Matter ----------------
        System.out.println("\n==================== WHY THESE TOPICS MATTER ====================");
        System.out.println("""
Understanding these concepts helps you:
✔ Write safer programs
✔ Reduce logical errors
✔ Learn collections easily
✔ Prepare for real-world Java
✔ Build DSA foundation
""");


        // ---------------- Learning Path ----------------
        System.out.println("\n==================== LEARNING PATH ====================");
        System.out.println("""
Recommended next steps:

1. Practice array problems
2. Learn Strings in Java
3. Learn Methods deeply
4. Move to Collections
5. Start Data Structures
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Arrays are more powerful than they appear.
→ Advanced topics improve efficiency and safety.
→ These ideas prepare you for next Java chapters.
→ Each topic will be covered step by step later.

Arrays are the foundation of Data Structures.
""");
    }

    // ---------------- Helper Method ----------------
    static void printFirstElement(int[] arr) {
        System.out.println("First element via method: " + arr[0]);
    }
}
