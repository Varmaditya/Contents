// Program: Diamond Star Pattern

public class PatternPrintingP43 {
    public static void main(String[] args) {

        int rows = 5;

        for (int i = 1; i <= rows; i++) {
            for (int s = rows - i; s > 0; s--) {
                System.out.print(" ");
            }
            for (int st = 1; st <= i; st++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        for (int i = rows - 1; i >= 1; i--) {
            for (int s = rows - i; s > 0; s--) {
                System.out.print(" ");
            }
            for (int st = 1; st <= i; st++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
