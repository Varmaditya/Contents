// Program: Introduction to Methods in Java

public class MethodsInJava {

    // ---------------- Method with No Parameters ----------------
    static void greet() {
        System.out.println("Hello! Welcome to Java Methods.");
    }

    // ---------------- Method with Parameters ----------------
    static void add(int a, int b) {
        int sum = a + b;
        System.out.println("Sum = " + sum);
    }

    // ---------------- Method with Return Value ----------------
    static int square(int num) {
        return num * num;
    }

    // ---------------- Method Returning Boolean ----------------
    static boolean isEven(int n) {
        return n % 2 == 0;
    }

    // ---------------- Method Using String ----------------
    static void printMessage(String name) {
        System.out.println("Hello, " + name);
    }

    // ---------------- Method with Multiple Operations ----------------
    static int max(int a, int b) {
        if (a > b) {
            return a;
        }
        return b;
    }

    public static void main(String[] args) {

        // Calling method with no parameters
        greet();

        // Calling method with parameters
        add(10, 20);
        add(5, 7);

        // Calling method with return value
        int sq = square(4);
        System.out.println("Square = " + sq);

        // Using boolean return value
        boolean result = isEven(10);
        System.out.println("Is 10 even? " + result);

        // Passing String as argument
        printMessage("Aditya");

        // Method returning max value
        int bigger = max(15, 9);
        System.out.println("Maximum value = " + bigger);
    }
          }
