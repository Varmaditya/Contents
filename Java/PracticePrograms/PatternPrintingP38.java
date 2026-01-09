// Program: Number Palindrome Pyramid

public class PatternPrintingP38 {
    public static void main(String[] args) {

        int rows = 5;

        for (int i = 1; i <= rows; i++) {

            for (int s = rows - i; s > 0; s--) {
                System.out.print(" ");
            }

            for (int n = 1; n <= i; n++) {
                System.out.print(n);
            }

            for (int n = i - 1; n >= 1; n--) {
                System.out.print(n);
            }

            System.out.println();
        }
    }
}
