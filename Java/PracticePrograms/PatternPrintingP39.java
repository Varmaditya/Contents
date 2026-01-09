// Program: Star Pyramid Pattern

public class PatternPrintingP39 {
    public static void main(String[] args) {

        int rows = 5;

        for (int i = 1; i <= rows; i++) {

            for (int space = 1; space <= rows - i; space++) {
                System.out.print(" ");
            }

            for (int star = 1; star <= i; star++) {
                System.out.print("* ");
            }

            System.out.println();
        }
    }
}
