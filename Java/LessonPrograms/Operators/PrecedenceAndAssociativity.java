// Program: Operator Precedence and Associativity in Java

public class PrecedenceAndAssociativity {
    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== OPERATOR PRECEDENCE ====================");
        System.out.println("""
Operator precedence defines the order in which operators are evaluated in an expression.
Just like mathematics, Java follows a specific priority to solve expressions.

Example:
    int result = 10 + 5 * 2;
Here, multiplication (*) is done first, then addition.

If we want to change the order, we must use parentheses ( ).
""");


        // ---------------- 1. Basic Precedence Example ----------------
        System.out.println("\n==================== 1. BASIC PRECEDENCE EXAMPLE ====================");
        System.out.println("""
In mathematics: 10 + (5 * 2) = 20

Similarly in Java:
    10 + 5 * 2  → 20 (not 30)
""");

        int result1 = 10 + 5 * 2;
        System.out.println("Example Output: 10 + 5 * 2 = " + result1);


        // ---------------- 2. Using Parentheses ----------------
        System.out.println("\n==================== 2. USING PARENTHESES ====================");
        System.out.println("""
Parentheses have the highest precedence.
They can change the normal priority of operators.

Example:
    (10 + 5) * 2  → 30
""");

        int result2 = (10 + 5) * 2;
        System.out.println("Example Output: (10 + 5) * 2 = " + result2);


        // ---------------- 3. Operator Precedence Table ----------------
        System.out.println("\n==================== 3. OPERATOR PRECEDENCE TABLE ====================");
        System.out.println("""
Priority Order:
1. ()  ++  --  !
2. *  /  %
3. +  -
4. <  >  <=  >=
5. ==  !=
6. &&
7. ||
8. =  +=  -=  *=  /=  %=   (Lowest)

Let us see a mixed example:
    int x = 5 + 10 * 2 > 20 ? 1 : 0;
""");

        int x = 5 + 10 * 2 > 20 ? 1 : 0;
        System.out.println("Example Output: 5 + 10 * 2 > 20 ? 1 : 0  → " + x);


        // ---------------- 4. Associativity Concept ----------------
        System.out.println("\n==================== 4. ASSOCIATIVITY IN OPERATORS ====================");
        System.out.println("""
When operators have the same precedence, Java uses ASSOCIATIVITY to decide which one executes first.

Two Types of Associativity:
1. Left to Right → + , - , * , / , %, relational, logical AND/OR
2. Right to Left → = , += , -= , *= , /= , %= , ++ , --

Example (Left to Right):
    int m = 50 / 5 * 2;
Steps:
    50 / 5 = 10
    10 * 2 = 20

Example (Right to Left):
    int a = b = 10;
Means:
    b = 10  → then a = 10
""");

        int m = 50 / 5 * 2;
        int b = 10, a2 = 0;
        a2 = b = 10;

        System.out.println("Example Output:");
        System.out.println("50 / 5 * 2 = " + m);
        System.out.println("a = b = 10 → a = " + a2 + ", b = " + b);


        // ---------------- 5. Unary + Arithmetic + Relational ----------------
        System.out.println("\n==================== 5. UNARY + ARITHMETIC + RELATIONAL ====================");
        System.out.println("""
Unary (++ , -- , !) have higher precedence than arithmetic and relational.

Example:
    int a = 5, b = 3;
    boolean result = ++a * b > 15;

Step-by-step:
    ++a → a becomes 6
    6 * b → 18
    18 > 15 → true
""");

        int a3 = 5, b3 = 3;
        boolean boolResult = ++a3 * b3 > 15;
        System.out.println("Example Output: ++a * b > 15 → " + boolResult);


        // ---------------- 6. Logical Precedence ----------------
        System.out.println("\n==================== 6. LOGICAL OPERATOR PRECEDENCE ====================");
        System.out.println("""
AND (&&) has higher precedence than OR (||).
Associativity is left to right.

Example:
    boolean x = true || false && false;

Step:
    false && false → false
    true || false → true
""");

        boolean logicResult = true || false && false;
        System.out.println("Example Output: true || false && false → " + logicResult);


        // ---------------- 7. Assignment and Precedence ----------------
        System.out.println("\n==================== 7. ASSIGNMENT & PRECEDENCE ====================");
        System.out.println("""
Assignment (=) has the lowest precedence.
Expression at the right is fully evaluated first due to RIGHT TO LEFT associativity.

Example:
    int p;
    p = 10 + 2 * 3 - 4;
""");

        int p = 10 + 2 * 3 - 4;
        System.out.println("Example Output: p = 10 + 2 * 3 - 4 → " + p);


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Operator Precedence decides the ORDER of evaluation.
→ Parentheses () have the HIGHEST precedence.
→ Associativity resolves conflicts when operators have the SAME precedence:
   ✔ Left to Right → +, -, *, /, %, <, >, <=, >=, &&, ||
   ✔ Right to Left → =, +=, -=, *=, /=, %=, ++, --
→ Always use parentheses to avoid confusion and programming mistakes.

Understanding precedence + associativity is key to writing correct expressions.
""");
    }
}
