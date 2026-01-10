// Program: Array Operations in Java (Traversal & Common Operations)

import java.util.Scanner;

public class ArrayOperations {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== ARRAY OPERATIONS IN JAVA ====================");
        System.out.println("""
Once an array is created and initialized,
we need to PERFORM OPERATIONS on it.

Common array operations include:
✔ Traversing (accessing all elements)
✔ Reading values
✔ Updating values
✔ Calculating sum and average
✔ Finding maximum and minimum
✔ Searching for an element

These operations are usually performed using LOOPS.
""");

        // ---------------- Sample Array ----------------
        System.out.println("\n==================== SAMPLE ARRAY ====================");
        System.out.println("""
We will use the following integer array
for demonstrating operations.
""");

        int[] marks = {78, 85, 92, 66, 88};

        System.out.println("Array created: {78, 85, 92, 66, 88}");

        // ---------------- Traversing using for Loop ----------------
        System.out.println("\n==================== TRAVERSING USING for LOOP ====================");
        System.out.println("""
Traversing means accessing each element of the array
one by one.

The for loop is most commonly used
when index is required.
""");

        for (int i = 0; i < marks.length; i++) {
            System.out.println("marks[" + i + "] = " + marks[i]);
        }

        System.out.println("Traversal using for loop completed.\n");

        // ---------------- Traversing using while Loop ----------------
        System.out.println("\n==================== TRAVERSING USING while LOOP ====================");
        System.out.println("""
The while loop is useful when
iteration count is not fixed beforehand.
""");

        int i = 0;
        while (i < marks.length) {
            System.out.println("marks[" + i + "] = " + marks[i]);
            i++;
        }

        System.out.println("Traversal using while loop completed.\n");

        // ---------------- Traversing using Enhanced for Loop ----------------
        System.out.println("\n==================== TRAVERSING USING for-each LOOP ====================");
        System.out.println("""
The enhanced for loop (for-each):
✔ Is simple and readable
✔ Does NOT provide index
✔ Used only for reading elements

Syntax:
    for (dataType var : array) {
        // use var
    }
""");

        for (int value : marks) {
            System.out.println("Value: " + value);
        }

        System.out.println("Traversal using for-each completed.\n");

        // ---------------- Reading Array Values from User ----------------
        System.out.println("\n==================== READING VALUES INTO ARRAY ====================");
        System.out.println("""
Arrays are often filled using user input.
""");

        Scanner sc = new Scanner(System.in);
        int[] numbers = new int[5];

        System.out.println("Enter 5 numbers:");

        for (int j = 0; j < numbers.length; j++) {
            numbers[j] = sc.nextInt();
        }

        System.out.println("User input stored in array.\n");

        // ---------------- Updating Array Element ----------------
        System.out.println("\n==================== UPDATING ARRAY ELEMENT ====================");
        System.out.println("""
Array elements can be updated using index.
""");

        System.out.println("Before update: numbers[2] = " + numbers[2]);
        numbers[2] = 999;
        System.out.println("After update: numbers[2] = " + numbers[2]);

        // ---------------- Sum of Array Elements ----------------
        System.out.println("\n==================== SUM OF ARRAY ELEMENTS ====================");
        System.out.println("""
Calculate total of all elements in array.
""");

        int sum = 0;

        for (int val : numbers) {
            sum = sum + val;
        }

        System.out.println("Sum of elements: " + sum);

        // ---------------- Average of Array Elements ----------------
        System.out.println("\n==================== AVERAGE OF ARRAY ELEMENTS ====================");
        System.out.println("""
Average = Sum / Number of elements
""");

        double average = (double) sum / numbers.length;
        System.out.println("Average value: " + average);

        // ---------------- Finding Maximum Element ----------------
        System.out.println("\n==================== FINDING MAXIMUM VALUE ====================");
        System.out.println("""
Find the largest element in the array.
""");

        int max = numbers[0];

        for (int k = 1; k < numbers.length; k++) {
            if (numbers[k] > max) {
                max = numbers[k];
            }
        }

        System.out.println("Maximum value: " + max);

        // ---------------- Finding Minimum Element ----------------
        System.out.println("\n==================== FINDING MINIMUM VALUE ====================");
        System.out.println("""
Find the smallest element in the array.
""");

        int min = numbers[0];

        for (int k = 1; k < numbers.length; k++) {
            if (numbers[k] < min) {
                min = numbers[k];
            }
        }

        System.out.println("Minimum value: " + min);

        // ---------------- Searching an Element ----------------
        System.out.println("\n==================== SEARCHING AN ELEMENT ====================");
        System.out.println("""
Check whether a given value exists in array.
""");

        System.out.print("Enter value to search: ");
        int search = sc.nextInt();

        boolean found = false;

        for (int val : numbers) {
            if (val == search) {
                found = true;
                break;
            }
        }

        if (found) {
            System.out.println("Value found in array.");
        } else {
            System.out.println("Value not found.");
        }

        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD USE CASES ====================");
        System.out.println("""
Array operations are used in:
✔ Student marks analysis
✔ Salary processing
✔ Sensor data monitoring
✔ Sales report calculations
✔ Game score tracking
""");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Using wrong loop condition
✘ Accessing index out of bounds
✘ Forgetting array length
✘ Using for-each when index is needed

Tip:
✔ Use array.length instead of hardcoding size
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Traversing means accessing all elements.
→ Arrays can be traversed using for, while, and for-each.
→ Common operations include sum, average, search, max, min.
→ Loops are essential for array operations.
→ Arrays simplify bulk data processing.
""");

        sc.close();
    }
}
