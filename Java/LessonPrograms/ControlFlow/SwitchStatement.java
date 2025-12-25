// Program: switch Statement in Java

import java.util.Scanner;

public class SwitchStatement {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== SWITCH STATEMENT IN JAVA ====================");
        System.out.println("""
The 'switch' statement is a multi-way decision-making statement.
It is used when a variable is compared against MULTIPLE fixed values.

Instead of writing long if-else-if ladders,
switch provides a cleaner and more readable structure.

The switch statement works with:
✔ int
✔ char
✔ String
✔ enum (later)

Let us understand how switch works.
""");

        // ---------------- Syntax ----------------
        System.out.println("\n==================== SYNTAX OF SWITCH STATEMENT ====================");
        System.out.println("""
Syntax:

    switch (expression) {
        case value1:
            // statements
            break;

        case value2:
            // statements
            break;

        default:
            // executes if no case matches
    }

Important points:
✔ Expression is evaluated once
✔ case values must be constant
✔ break prevents fall-through
✔ default is optional but recommended
""");

        // ---------------- Flow Explanation ----------------
        System.out.println("\n==================== FLOW OF SWITCH STATEMENT ====================");
        System.out.println("""
Execution Flow:

START
 ↓
Evaluate expression
 ↓
Match with case value
 ↓
Execute matching case
 ↓
break → exit switch
 ↓
If no match → default executes
""");

        // ---------------- Example 1: Day of Week ----------------
        System.out.println("\n==================== EXAMPLE 1: DAY OF WEEK ====================");
        System.out.println("""
Display day name based on day number.
""");

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter day number (1–7): ");
        int day = sc.nextInt();

        switch (day) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println("Invalid day number");
        }

        System.out.println("Day check completed.\n");

        // ---------------- Example 2: Calculator Menu ----------------
        System.out.println("\n==================== EXAMPLE 2: SIMPLE CALCULATOR ====================");
        System.out.println("""
Perform arithmetic operation based on user choice.
""");

        System.out.print("Enter first number: ");
        int a = sc.nextInt();

        System.out.print("Enter second number: ");
        int b = sc.nextInt();

        System.out.print("""
Choose operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter choice: """);
        int choice = sc.nextInt();

        switch (choice) {
            case 1:
                System.out.println("Result: " + (a + b));
                break;
            case 2:
                System.out.println("Result: " + (a - b));
                break;
            case 3:
                System.out.println("Result: " + (a * b));
                break;
            case 4:
                System.out.println("Result: " + (a / b));
                break;
            default:
                System.out.println("Invalid operation choice");
        }

        System.out.println("Calculation completed.\n");

        // ---------------- Example 3: Traffic Signal ----------------
        System.out.println("\n==================== EXAMPLE 3: TRAFFIC SIGNAL ====================");
        System.out.println("""
Decide action based on traffic light color.
""");

        sc.nextLine(); // clear buffer
        System.out.print("Enter signal color: ");
        String signal = sc.nextLine();

        switch (signal.toUpperCase()) {
            case "RED":
                System.out.println("STOP");
                break;
            case "YELLOW":
                System.out.println("GET READY");
                break;
            case "GREEN":
                System.out.println("GO");
                break;
            default:
                System.out.println("Invalid signal color");
        }

        System.out.println("Traffic signal check completed.\n");

        // ---------------- Example 4: Vowel or Consonant ----------------
        System.out.println("\n==================== EXAMPLE 4: VOWEL CHECK ====================");
        System.out.println("""
Check whether a character is a vowel.
""");

        System.out.print("Enter a character: ");
        char ch = sc.next().toLowerCase().charAt(0);

        switch (ch) {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
                System.out.println("It is a Vowel");
                break;
            default:
                System.out.println("It is a Consonant");
        }

        System.out.println("Character check completed.\n");

        // ---------------- Example 5: Month Days ----------------
        System.out.println("\n==================== EXAMPLE 5: DAYS IN MONTH ====================");
        System.out.println("""
Display number of days in a month (non-leap year).
""");

        System.out.print("Enter month number (1–12): ");
        int month = sc.nextInt();

        switch (month) {
            case 1: case 3: case 5: case 7:
            case 8: case 10: case 12:
                System.out.println("31 days");
                break;

            case 4: case 6: case 9: case 11:
                System.out.println("30 days");
                break;

            case 2:
                System.out.println("28 days");
                break;

            default:
                System.out.println("Invalid month");
        }

        System.out.println("Month check completed.\n");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Forgetting break (causes fall-through)
✘ Using variables in case labels
✘ Duplicate case values
✘ Using unsupported data types (like double)

Remember:
✔ break stops execution
✔ default handles unmatched cases
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ switch is used for multi-way decision making.
→ Expression is matched against constant case values.
→ break prevents fall-through.
→ default executes when no case matches.
→ switch improves readability over long if-else-if ladders.

Next topic: Looping statements.
""");

        sc.close();
    }
}
