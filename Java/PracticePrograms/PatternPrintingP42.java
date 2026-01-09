// Program: Hollow Pyramid Pattern

public class PatternPrintingP42 {
    public static void main(String[] args) {

        int rows = 5;

        for (int i = 1; i <= rows; i++) {

            for (int s = rows - i; s > 0; s--) {
                System.out.print(" ");
            }

            for (int j = 1; j <= (2 * i - 1); j++) {

                if (j == 1 || j == (2 * i - 1) || i == rows) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }

            System.out.println();
        }
    }
}
