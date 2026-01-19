// Program: Linear Search in Array

import java.util.Scanner;

public class ArraySearchP49 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] data = new int[10];
        boolean found = false;

        for (int i = 0; i < data.length; i++) {
            System.out.print("Enter value: ");
            data[i] = sc.nextInt();
        }

        System.out.print("Enter value to search: ");
        int key = sc.nextInt();

        for (int i = 0; i < data.length; i++) {
            if (data[i] == key) {
                System.out.println("Found at index " + i);
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("Value not found");
        }

        sc.close();
    }
}
