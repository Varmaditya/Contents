// Program: Enhanced switch Statement in Java

import java.util.Scanner;

public class EnhancedSwitchStatement {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== ENHANCED SWITCH STATEMENT ====================");
        System.out.println("""
The Enhanced switch statement is a modern version of the traditional switch.
It was introduced to make switch statements:
✔ cleaner
✔ shorter
✔ less error-prone

Enhanced switch removes common problems like:
✘ missing break statements
✘ fall-through bugs
✘ lengthy repetitive code

It is available in newer versions of Java (Java 12+).
""");

        // ---------------- Traditional vs Enhanced Switch ----------------
        System.out.println("\n==================== TRADITIONAL vs ENHANCED SWITCH ====================");
        System.out.println("""
Traditional switch:
✔ Uses colon (:)
✔ Requires break
✔ Prone to fall-through errors

Enhanced switch:
✔ Uses arrow (->)
✔ No break required
✔ More readable and safer
""");

        // ---------------- Syntax of Enhanced Switch ----------------
        System.out.println("\n==================== SYNTAX OF ENHANCED SWITCH ====================");
        System.out.println("""
Basic syntax:

    switch (expression) {
        case value1 -> statement;
        case value2 -> statement;
        default     -> statement;
    }

Multiple values can be combined:
    case 1, 2, 3 -> statement;
""");

        // ---------------- Example 1: Day of Week ----------------
        System.out.println("\n==================== EXAMPLE 1: DAY OF WEEK ====================");
        System.out.println("""
Display day name using enhanced switch.
""");

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter day number (1–7): ");
        int day = sc.nextInt();

        switch (day) {
            case 1 -> System.out.println("Monday");
            case 2 -> System.out.println("Tuesday");
            case 3 -> System.out.println("Wednesday");
            case 4 -> System.out.println("Thursday");
            case 5 -> System.out.println("Friday");
            case 6 -> System.out.println("Saturday");
            case 7 -> System.out.println("Sunday");
            default -> System.out.println("Invalid day");
        }

        System.out.println("Day check completed.\n");

        // ---------------- Example 2: Multiple Case Labels ----------------
        System.out.println("\n==================== EXAMPLE 2: MULTIPLE CASE LABELS ====================");
        System.out.println("""
Multiple values can share the same logic.
""");

        System.out.print("Enter month number (1–12): ");
        int month = sc.nextInt();

        switch (month) {
            case 1, 3, 5, 7, 8, 10, 12 -> System.out.println("31 days");
            case 4, 6, 9, 11          -> System.out.println("30 days");
            case 2                    -> System.out.println("28 days");
            default                   -> System.out.println("Invalid month");
        }

        System.out.println("Month check completed.\n");

        // ---------------- Example 3: switch as Expression ----------------
        System.out.println("\n==================== EXAMPLE 3: SWITCH AS AN EXPRESSION ====================");
        System.out.println("""
Enhanced switch can RETURN a value.
This makes it useful as an expression.
""");

        System.out.print("Enter marks: ");
        int marks = sc.nextInt();

        String grade = switch (marks / 10) {
            case 10, 9 -> "A+";
            case 8     -> "A";
            case 7     -> "B";
            case 6     -> "C";
            default    -> "Fail";
        };

        System.out.println("Grade: " + grade);
        System.out.println("Grade evaluation completed.\n");

        // ---------------- Example 4: Using yield ----------------
        System.out.println("\n==================== EXAMPLE 4: USING yield ====================");
        System.out.println("""
When a case contains a block of code,
the 'yield' keyword is used to return a value.
""");

        System.out.print("Enter operation (+, -, *, /): ");
        char op = sc.next().charAt(0);

        System.out.print("Enter first number: ");
        int a = sc.nextInt();

        System.out.print("Enter second number: ");
        int b = sc.nextInt();

        int result = switch (op) {
            case '+' -> a + b;
            case '-' -> a - b;
            case '*' -> a * b;
            case '/' -> {
                if (b == 0) {
                    yield 0;
                }
                yield a / b;
            }
            default -> 0;
        };

        System.out.println("Result: " + result);
        System.out.println("Calculation completed.\n");

        // ---------------- Example 5: String-based Enhanced Switch ----------------
        System.out.println("\n==================== EXAMPLE 5: STRING SWITCH ====================");
        System.out.println("""
Enhanced switch works well with Strings.
""");

        sc.nextLine(); // clear buffer
        System.out.print("Enter role (admin/user/guest): ");
        String role = sc.nextLine();

        String access = switch (role.toLowerCase()) {
            case "admin" -> "Full Access";
            case "user"  -> "Limited Access";
            case "guest" -> "Read Only Access";
            default      -> "No Access";
        };

        System.out.println("Access Level: " + access);
        System.out.println("Role check completed.\n");

        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Using break in enhanced switch (not required)
✘ Mixing colon syntax with arrow syntax
✘ Forgetting default case
✘ Using enhanced switch in old Java versions

Remember:
✔ Use -> instead of :
✔ Use yield only inside block cases
""");

        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Enhanced switch is a modern, cleaner version of switch.
→ Uses arrow (->) syntax instead of colon.
→ No break statements required.
→ Can return values directly (expression-style).
→ Supports multiple case labels and yield.

Enhanced switch improves readability and reduces errors.
""");

        sc.close();
    }
}
