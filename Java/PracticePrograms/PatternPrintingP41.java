// Program: Hollow Square Pattern

public class PatternPrintingP41 {
    public static void main(String[] args) {

        int size = 5;

        for (int i = 1; i <= size; i++) {
            for (int j = 1; j <= size + 1; j++) {

                if (i == 1 || i == size || j == 1 || j == size + 1) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
}
