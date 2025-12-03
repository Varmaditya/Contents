// Program: Java Naming Conventions

public class NamingConvention {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== JAVA NAMING CONVENTIONS ====================");
        System.out.println("""
Naming conventions are a set of rules that define how to name:
- classes
- methods
- variables
- constants
- packages

They make Java programs:
✔ Easy to read  
✔ Easy to understand  
✔ Consistent for all developers  
✔ Professional and well-structured  

Java is case-sensitive, so naming conventions are VERY important.
Let us understand each convention in detail.
""");


        // ---------------- 1. Class Naming Convention ----------------
        System.out.println("\n==================== 1. CLASS NAMES ====================");
        System.out.println("""
RULES:
✔ Class names should be nouns.
✔ Follow PascalCase (also called UpperCamelCase).
✔ First letter of every word is capital.
✔ Name should be meaningful.

Examples of GOOD class names:
    StudentRecord
    EmployeeDetails
    PaymentGateway

BAD examples:
    studentrecord
    employeedetails
    paymentgateway
""");

        // Demonstration of class-like names
        System.out.println("Correct Class Name Example: StudentData");
        System.out.println("Incorrect Class Name Example: studentdata\n");


        // ---------------- 2. Method Naming Convention ----------------
        System.out.println("\n==================== 2. METHOD NAMES ====================");
        System.out.println("""
RULES:
✔ Methods should be verbs because they perform an action.
✔ Use camelCase.
✔ First word starts lowercase, next words start capital.

Examples of GOOD method names:
    getName()
    calculateSalary()
    printReport()

BAD examples:
    GetName()
    Calculate_salary()
    print_report()
""");

        // Demonstration of method-like names
        System.out.println("Correct Method Name Example: displayResult()");
        System.out.println("Incorrect Method Name Example: Displayresult()\n");


        // ---------------- 3. Variable Naming Convention ----------------
        System.out.println("\n==================== 3. VARIABLE NAMES ====================");
        System.out.println("""
RULES:
✔ Use camelCase
✔ Should be meaningful
✔ Start with a letter, not a digit
✔ Use lowercase for the first word
✔ Avoid very short names unless in loops (i, j)

Examples of GOOD variable names:
    totalMarks
    studentName
    numberOfItems

BAD examples:
    Totalmarks
    Student_name
    NUMBEROFITEMS
""");

        // Demonstration of variable-like examples
        System.out.println("Correct Variable Name Example: studentAge");
        System.out.println("Incorrect Variable Name Example: Studentage\n");


        // ---------------- 4. Constant Naming Convention ----------------
        System.out.println("\n==================== 4. CONSTANTS ====================");
        System.out.println("""
RULES:
✔ Constants must be written in UPPERCASE.
✔ Words are separated using underscores.
✔ Use final keyword when declaring actual constants.

Examples of GOOD constant names:
    MAX_SPEED
    PI_VALUE
    LOGIN_ATTEMPTS_LIMIT

BAD examples:
    maxspeed
    PiValue
    loginattemptslimit
""");

        // Demonstration of constant-like examples
        System.out.println("Correct Constant Name Example: MAX_VALUE");
        System.out.println("Incorrect Constant Name Example: MaxValue\n");


        // ---------------- 5. Package Naming Convention ----------------
        System.out.println("\n==================== 5. PACKAGE NAMES ====================");
        System.out.println("""
RULES:
✔ Use all lowercase letters.
✔ Should represent directory structure.
✔ Reverse domain naming is common in companies.

Examples:
    com.companyname.project
    org.example.app

GOOD package names:
    student.management
    data.processing

BAD examples:
    Student.Management
    Data.Processing
""");

        // Demonstration of package-like names
        System.out.println("Correct Package Name Example: utilities.helper");
        System.out.println("Incorrect Package Name Example: Utilities.Helper\n");


        // ---------------- 6. Interface Naming Convention ----------------
        System.out.println("\n==================== 6. INTERFACE NAMES ====================");
        System.out.println("""
RULES:
✔ Interfaces should be adjectives (mostly).
✔ Use PascalCase like class names.

Examples:
    Runnable
    Readable
    Printable
    Connectable
""");

        System.out.println("Correct Interface Name Example: Drivable");
        System.out.println("Incorrect Interface Name Example: drivable\n");


        // ---------------- 7. File Naming Convention ----------------
        System.out.println("\n==================== 7. FILE NAMES ====================");
        System.out.println("""
RULES:
✔ A Java file should have the same name as the public class inside it.
✔ It must end with .java

Example:
If class name is StudentData → file name must be StudentData.java
""");

        System.out.println("Correct File Name Example: OrderDetails.java");
        System.out.println("Incorrect File Name Example: orderdetails.java\n");


        // ---------------- 8. Full Demo Program ----------------
        System.out.println("\n==================== COMPLETE DEMO USING ALL NAMING RULES ====================");
        System.out.println("""
Below is a small example (printed as text)
showing correct naming conventions applied:

-----------------------------
package student.management;

public class StudentProfile {

    public static final int MAX_AGE = 120;
    
    private String studentName;
    private int studentAge;

    public void displayInfo() {
        System.out.println("Name: " + studentName);
        System.out.println("Age: " + studentAge);
    }
}
-----------------------------
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Naming conventions improve readability and consistency.

Java Naming Rules:
✔ Class → PascalCase (StudentInfo)  
✔ Method → camelCase (printData())  
✔ Variable → camelCase (totalMarks)  
✔ Constant → UPPER_CASE (MAX_SPEED)  
✔ Package → lowercase (student.data)  
✔ Interface → PascalCase (Runnable)  
✔ File Name → Same as public class  

Following naming conventions makes your code clean and professional.
""");
    }
}
