// Program: Types of Methods in Java

public class TypesOfMethods {

    // 1. No parameters, no return value
    static void greet() {
        System.out.println("Welcome to Java!");
    }

    // 2. Parameters, no return value
    static void add(int a, int b) {
        System.out.println("Sum = " + (a + b));
    }

    // 3. No parameters, return value
    static int getNumber() {
        return 10;
    }

    // 4. Parameters and return value
    static int square(int n) {
        return n * n;
    }

    // 5. Boolean return type
    static boolean isEven(int n) {
        return n % 2 == 0;
    }

    public static void main(String[] args) {

        greet();                      // Type 1

        add(5, 7);                    // Type 2

        int num = getNumber();        // Type 3
        System.out.println("Number = " + num);

        int result = square(4);       // Type 4
        System.out.println("Square = " + result);

        System.out.println("Is 6 even? " + isEven(6)); // Type 5
    }
}
