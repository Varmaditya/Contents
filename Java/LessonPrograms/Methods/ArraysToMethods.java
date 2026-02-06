// Program: Passing & Returning Arrays to/from Methods in Java

public class ArraysToMethods {

    // ---------------- Method to Print Array ----------------
    static void printArray(int[] arr) {

        System.out.println("Printing array elements:");
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    // ---------------- Method to Calculate Sum ----------------
    static int calculateSum(int[] arr) {

        int sum = 0;
        for (int value : arr) {
            sum += value;   // accumulating array values
        }
        return sum;
    }

    // ---------------- Method to Modify Array ----------------
    static void modifyArray(int[] arr) {

        for (int i = 0; i < arr.length; i++) {
            arr[i] = arr[i] * 2;   // modifying original array
        }
    }

    // ---------------- Method that RETURNS an Array ----------------
    static int[] createSquaredArray(int[] arr) {

        int[] result = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            result[i] = arr[i] * arr[i];   // creating new array
        }

        return result;   // returning array reference
    }

    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== ARRAYS & METHODS ====================");
        System.out.println("""
Arrays can be:
✔ Passed TO methods
✔ Modified INSIDE methods
✔ Returned FROM methods

Understanding all three is VERY IMPORTANT
for writing clean and reusable Java programs.
""");


        // ---------------- Why Arrays with Methods ----------------
        System.out.println("\n==================== WHY USE ARRAYS WITH METHODS ====================");
        System.out.println("""
Using arrays with methods helps you:
✔ Divide logic into smaller units
✔ Reuse array-processing code
✔ Keep main() clean
✔ Write modular programs
""");


        // ---------------- Creating an Array ----------------
        System.out.println("\n==================== ARRAY CREATION ====================");
        System.out.println("""
We create an array in main()
and pass it to different methods.
""");

        int[] numbers = {10, 20, 30, 40, 50};


        // ---------------- Passing Array to Method ----------------
        System.out.println("\n==================== PASSING ARRAY TO METHOD ====================");
        System.out.println("""
When an array is passed to a method:
✔ Reference of array is passed
✔ No copy is created
✔ Method can access all elements
""");

        printArray(numbers);


        // ---------------- Array Used for Calculation ----------------
        System.out.println("\n==================== ARRAY USED FOR CALCULATION ====================");
        System.out.println("""
A method can process array data
and return a SINGLE value.
""");

        int total = calculateSum(numbers);
        System.out.println("Sum of array elements: " + total);


        // ---------------- Modifying Array Inside Method ----------------
        System.out.println("\n==================== MODIFYING ARRAY INSIDE METHOD ====================");
        System.out.println("""
Arrays are mutable.

If a method modifies the array,
the changes affect the original array.
""");

        modifyArray(numbers);

        System.out.println("Array after modification:");
        printArray(numbers);


        // ---------------- Returning Array from Method ----------------
        System.out.println("\n==================== RETURNING ARRAY FROM METHOD ====================");
        System.out.println("""
A method can also RETURN an array.

✔ Method return type must be array type
✔ Returned value is a reference to array
✔ Can return SAME or NEW array
""");

        int[] squaredNumbers = createSquaredArray(numbers);

        System.out.println("Returned array (squared values):");
        printArray(squaredNumbers);


        // ---------------- Reference Behavior Explanation ----------------
        System.out.println("\n==================== REFERENCE BEHAVIOR ====================");
        System.out.println("""
Arrays are OBJECTS in Java.

✔ Passed by reference (actually reference value)
✔ Shared between methods
✔ Changes reflect if same array is modified
""");


        // ---------------- Difference: Modify vs Return ----------------
        System.out.println("\n==================== MODIFY vs RETURN ====================");
        System.out.println("""
MODIFY ARRAY:
✔ Same array changes
✔ Affects original data

RETURN ARRAY:
✔ New array can be created
✔ Original array remains safe
""");


        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD MAPPING ====================");
        System.out.println("""
Marks System:
✔ Pass marks array to calculate total
✔ Pass marks array to apply grace
✔ Return new array with grades

This avoids data corruption.
""");


        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Assuming array is copied automatically
✘ Modifying array unintentionally
✘ Forgetting array length
✘ Returning wrong array type
""");


        // ---------------- What Comes Next ----------------
        System.out.println("\n==================== WHAT COMES NEXT ====================");
        System.out.println("""
Next topics:

✔ Passing 2D arrays to methods
✔ Arrays with method overloading
✔ Arrays and scope
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Arrays can be passed to methods.
→ Methods can modify arrays.
→ Methods can return arrays.
→ Reference behavior is important.
→ This concept is used everywhere in Java.

Arrays + Methods = Powerful Programming.
""");
    }
}
