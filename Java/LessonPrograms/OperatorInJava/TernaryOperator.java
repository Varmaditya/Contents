// Program: Ternary Operator in Java (Detailed)

import java.util.Scanner;

public class TernaryOperator {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== TERNARY OPERATOR ====================");
        System.out.println("""
The ternary operator is a compact form of if-else.
It evaluates a condition and selects a value based on whether the condition is true or false.

Syntax:
    condition ? value_if_true : value_if_false;

Characteristics:
✔ Works with boolean conditions
✔ Returns a value (not a statement)
✔ Mostly used in place of simple if-else statements
""");


        // ---------------- Basic Example ----------------
        System.out.println("\n==================== 1. BASIC EXAMPLE ====================");
        System.out.println("""
Example:
    int a = 10, b = 20;
    String result = (a > b) ? "a is greater" : "b is greater";

Result depends on whether a > b.
""");

        int a = 10, b = 20;
        String result = (a > b) ? "a is greater" : "b is greater";

        System.out.println("Example Output:");
        System.out.println("a = " + a + ", b = " + b);
        System.out.println("Result: " + result);


        // ---------------- Using Ternary with Input ----------------
        System.out.println("\n==================== 2. TERNARY WITH USER INPUT ====================");
        System.out.println("""
Let us take a number from the user and check whether it is EVEN or ODD
using the ternary operator.

Example:
    (num % 2 == 0) ? "Even" : "Odd";
""");

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        String type = (num % 2 == 0) ? "Even" : "Odd";

        System.out.println("You entered: " + num);
        System.out.println("It is: " + type);


        // ---------------- Nested Ternary Operator ----------------
        System.out.println("\n==================== 3. NESTED TERNARY OPERATOR ====================");
        System.out.println("""
A ternary operator can be nested inside another ternary.
Used to check multiple conditions in short form.

Example:
    int marks = 85;
    String grade = (marks >= 90 ? "A+" :
                    marks >= 75 ? "A" :
                    marks >= 60 ? "B" : "C");

Note: Use nested ternary carefully to maintain readability.
""");

        int marks = 85;
        String grade = (marks >= 90 ? "A+" :
                marks >= 75 ? "A" :
                        marks >= 60 ? "B" : "C");

        System.out.println("Example Output:");
        System.out.println("Marks = " + marks);
        System.out.println("Grade = " + grade);


        // ---------------- Ternary vs if-else (Use Case) ----------------
        System.out.println("\n==================== 4. USE CASE: TERNARY vs IF-ELSE ====================");
        System.out.println("""
Ternary is best used when we need a compact single-line conditional result.

if-else version:
    if(age >= 18) {
        msg = "Eligible";
    } else {
        msg = "Not Eligible";
    }

Ternary version:
    msg = (age >= 18) ? "Eligible" : "Not Eligible";

Use ternary for simple choice-based decisions where only one value needs to be selected.
Avoid ternary for long or complex decision-making.
""");

        int age = 16;
        String eligibility = (age >= 18) ? "Eligible" : "Not Eligible";

        System.out.println("Example Output:");
        System.out.println("Age = " + age);
        System.out.println("Eligibility: " + eligibility);


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Ternary operator is a shorter version of if-else.
→ Syntax: condition ? value_if_true : value_if_false;
→ Returns a VALUE, not a statement.
→ Useful for small decisions like:
     - Pass/Fail
     - Even/Odd
     - Eligible/Not Eligible
→ Nested ternary works but should be used carefully to maintain readability.

Mastering the ternary operator helps write cleaner and shorter decision logic.
""");

        sc.close();
    }
}
