// Program: Horizontal Histogram

public class HistogramGraphP54 {
    public static void main(String[] args) {

        int[] data = {9, 3, 5, 7};

        System.out.println("[ ]  [n] Histogram");

        for (int i = 0; i < data.length; i++) {

            // Print index and value
            System.out.print(i + "   " + data[i] + "   ");

            // Print stars equal to value
            for (int j = 1; j <= data[i]; j++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }
}
