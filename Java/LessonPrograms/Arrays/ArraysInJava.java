// Program: Arrays in Java

public class ArraysInJava {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== ARRAYS IN JAVA ====================");
        System.out.println("""
An array is a DATA STRUCTURE used to store
MULTIPLE values of the SAME data type
under a SINGLE variable name.

Arrays help us manage large amounts of data efficiently
without creating multiple variables.
""");

        // ---------------- Why Arrays ----------------
        System.out.println("\n==================== WHY ARRAYS ARE NEEDED ====================");
        System.out.println("""
Without arrays:
    int m1, m2, m3, m4, m5;

Problems:
✘ Too many variables
✘ Difficult to manage
✘ Hard to process collectively

With arrays:
✔ Single variable
✔ Easy access
✔ Organized data
✔ Efficient processing
""");

        // ---------------- What is an Array ----------------
        System.out.println("\n==================== WHAT IS AN ARRAY ====================");
        System.out.println("""
An array is:
✔ A collection of elements
✔ Stored in CONTIGUOUS memory locations
✔ All elements are of SAME data type
✔ Indexed (index starts from 0)

Example:
    int[] marks = {80, 85, 90};

Indexes:
    marks[0] → 80
    marks[1] → 85
    marks[2] → 90
""");

        // ---------------- Array Declaration ----------------
        System.out.println("\n==================== ARRAY DECLARATION ====================");
        System.out.println("""
Array declaration tells Java:
✔ What type of data the array will store
✔ The name of the array

Syntax:
    dataType[] arrayName;
OR
    dataType arrayName[];

Example:
    int[] numbers;
    String names[];
""");

        int[] numbers;
        String[] names;

        // ---------------- Array Creation ----------------
        System.out.println("\n==================== ARRAY CREATION ====================");
        System.out.println("""
Array creation allocates MEMORY to the array.

Syntax:
    arrayName = new dataType[size];

Example:
    numbers = new int[5];

This creates an array of size 5
(index range: 0 to 4)
""");

        numbers = new int[5];

        // ---------------- Array Initialization ----------------
        System.out.println("\n==================== ARRAY INITIALIZATION ====================");
        System.out.println("""
Initialization means assigning values to array elements.

There are THREE common ways to initialize arrays.
""");

        // ---------------- Method 1: Initialization at Declaration ----------------
        System.out.println("\n==================== METHOD 1: DECLARATION + INITIALIZATION ====================");
        System.out.println("""
Values are provided directly at the time of declaration.

Syntax:
    int[] arr = {10, 20, 30};

Size is automatically decided.
""");

        int[] arr1 = {10, 20, 30};

        System.out.println("arr1[0] = " + arr1[0]);
        System.out.println("arr1[1] = " + arr1[1]);
        System.out.println("arr1[2] = " + arr1[2]);

        // ---------------- Method 2: Using new keyword ----------------
        System.out.println("\n==================== METHOD 2: USING new KEYWORD ====================");
        System.out.println("""
Array is created first, then values are assigned manually.

Syntax:
    int[] arr = new int[3];
    arr[0] = 5;
    arr[1] = 10;
    arr[2] = 15;
""");

        int[] arr2 = new int[3];
        arr2[0] = 5;
        arr2[1] = 10;
        arr2[2] = 15;

        System.out.println("arr2[0] = " + arr2[0]);
        System.out.println("arr2[1] = " + arr2[1]);
        System.out.println("arr2[2] = " + arr2[2]);

        // ---------------- Method 3: Anonymous Array ----------------
        System.out.println("\n==================== METHOD 3: ANONYMOUS ARRAY ====================");
        System.out.println("""
Anonymous arrays are used when
array is needed only once.

Syntax:
    new int[]{1, 2, 3}
""");

        System.out.println("Anonymous array element: " + new int[]{100, 200, 300}[1]);

        // ---------------- Default Values ----------------
        System.out.println("\n==================== DEFAULT VALUES IN ARRAYS ====================");
        System.out.println("""
When an array is created using 'new',
Java assigns default values automatically.

int[]      → 0
double[]   → 0.0
char[]     → '\\u0000'
boolean[]  → false
String[]   → null
""");

        int[] defaultArray = new int[3];
        System.out.println("Default int value: " + defaultArray[0]);

        // ---------------- Array of Strings ----------------
        System.out.println("\n==================== ARRAY OF STRINGS ====================");
        System.out.println("""
Arrays can store String objects.

Example:
    String[] cities = {"Mumbai", "Delhi", "Pune"};
""");

        String[] cities = {"Mumbai", "Delhi", "Pune"};

        System.out.println("City 1: " + cities[0]);
        System.out.println("City 2: " + cities[1]);
        System.out.println("City 3: " + cities[2]);

        // --------------- Accessing Array Elements ----------------
        System.out.println("\n==================== ACCESSING ARRAY ELEMENTS ====================");
        System.out.println("""
Array elements are accessed using INDEX.

Syntax:
    arrayName[index]

Important:
✔ Index starts from 0
✔ Last index = size - 1
✔ Accessing invalid index causes error
""");

        int[] scores = {70, 80, 90};

        System.out.println("First score: " + scores[0]);
        System.out.println("Second score: " + scores[1]);
        System.out.println("Third score: " + scores[2]);

        // ---------------- Real-World Use Case ----------------
        System.out.println("\n==================== REAL-WORLD USE CASE ====================");
        System.out.println("""
Arrays are commonly used to store:
✔ Student marks
✔ Employee salaries
✔ Product prices
✔ Sensor readings
✔ Daily temperatures

Arrays make bulk data handling simple.
""");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Accessing index outside array size
✘ Forgetting index starts from 0
✘ Mixing data types
✘ Assuming array size can change (fixed size)

Remember:
✔ Array size is FIXED once created
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Arrays store multiple values of same data type.
→ Stored in contiguous memory.
→ Index starts from 0.
→ Declaration, creation, and initialization are separate steps.
→ Multiple initialization methods exist.
→ Arrays are fundamental for data handling.
""");
    }
}
