// Program: More Array Topics in Java (Array of Objects & 2D Arrays)

import java.util.Scanner;

public class TypesOfArrays {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== MORE ARRAY TOPICS IN JAVA ====================");
        System.out.println("""
So far, we have learned arrays of primitive data types.

Java also supports:
✔ Arrays of OBJECTS
✔ MULTI-DIMENSIONAL arrays (2D arrays)

These are commonly used in real-world applications
like student records, tables, grids, and matrices.
""");

        // ---------------- Array of Objects ----------------
        System.out.println("\n==================== ARRAY OF OBJECTS ====================");
        System.out.println("""
An array of objects stores REFERENCES to objects.

Instead of storing primitive values,
it stores objects created from a class.

Example:
    Student[] students = new Student[3];
""");

        // ---------------- Defining a Simple Class ----------------
        System.out.println("\n==================== STUDENT CLASS ====================");
        System.out.println("""
We will create a simple Student class
to demonstrate array of objects.
""");

        // Creating array of Student objects
        Student[] students = new Student[3];

        students[0] = new Student("Amit", 85);
        students[1] = new Student("Neha", 90);
        students[2] = new Student("Rahul", 78);

        // ---------------- Accessing Object Array ----------------
        System.out.println("\n==================== ACCESSING ARRAY OF OBJECTS ====================");
        System.out.println("""
Each array element refers to an object.
We access object data using dot (.) operator.
""");

        for (int i = 0; i < students.length; i++) {
            System.out.println("Student " + (i + 1) + ":");
            System.out.println("Name: " + students[i].name);
            System.out.println("Marks: " + students[i].marks);
            System.out.println();
        }

        // ---------------- Real-World Use Case ----------------
        System.out.println("\n==================== REAL-WORLD USE CASE ====================");
        System.out.println("""
Array of objects is used to store:
✔ Student records
✔ Employee details
✔ Product information
✔ Bank accounts

Each object holds multiple properties.
""");

        // ---------------- 2D Arrays Introduction ----------------
        System.out.println("\n==================== 2D ARRAYS IN JAVA ====================");
        System.out.println("""
A 2D array is an array of arrays.

It is used to store data in:
✔ Rows and columns
✔ Table format
✔ Matrix structure

Example:
    int[][] matrix = new int[3][3];
""");

        // ---------------- 2D Array Declaration ----------------
        System.out.println("\n==================== 2D ARRAY DECLARATION ====================");
        System.out.println("""
Syntax:
    dataType[][] arrayName;

Example:
    int[][] numbers;
""");

        int[][] numbers;

        // ---------------- 2D Array Creation ----------------
        System.out.println("\n==================== 2D ARRAY CREATION ====================");
        System.out.println("""
Memory allocation for 2D array.

Syntax:
    arrayName = new dataType[rows][columns];
""");

        numbers = new int[2][3];

        // ---------------- 2D Array Initialization ----------------
        System.out.println("\n==================== 2D ARRAY INITIALIZATION ====================");
        System.out.println("""
Values are assigned using row and column index.
""");

        numbers[0][0] = 10;
        numbers[0][1] = 20;
        numbers[0][2] = 30;
        numbers[1][0] = 40;
        numbers[1][1] = 50;
        numbers[1][2] = 60;

        // ---------------- Accessing 2D Array ----------------
        System.out.println("\n==================== ACCESSING 2D ARRAY ====================");
        System.out.println("""
2D array elements are accessed using:
    array[row][column]
""");

        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < numbers[i].length; j++) {
                System.out.print(numbers[i][j] + " ");
            }
            System.out.println();
        }

        // ---------------- 2D Array with Initialization Block ----------------
        System.out.println("\n==================== 2D ARRAY INITIALIZATION (INLINE) ====================");
        System.out.println("""
2D arrays can also be initialized directly.
""");

        int[][] table = {
                {1, 2, 3},
                {4, 5, 6}
        };

        for (int i = 0; i < table.length; i++) {
            for (int j = 0; j < table[i].length; j++) {
                System.out.print(table[i][j] + " ");
            }
            System.out.println();
        }

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Forgetting to initialize objects in object array
✘ Confusing rows and columns
✘ Accessing invalid index
✘ Assuming all rows have same length

Remember:
✔ 2D arrays are arrays of arrays
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Array of objects stores references to objects.
→ Objects are accessed using dot operator.
→ 2D arrays store data in rows and columns.
→ Accessed using two indexes.
→ Used in tables, matrices, and structured data.
""");
    }
}


// ---------------- Student Class ----------------
class Student {
    String name;
    int marks;

    Student(String name, int marks) {
        this.name = name;
        this.marks = marks;
    }
}
