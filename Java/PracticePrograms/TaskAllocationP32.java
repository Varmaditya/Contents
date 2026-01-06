// Program: Task Allocation System

import java.util.Scanner;

public class TaskAllocationP32 {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        System.out.print("Enter your job role (Feeding, Cleaner, Security, Tour Guide): ");
        String jobRole = scan.nextLine();

        int time = 0;
        time = switch (jobRole) {
            case "Feeding", "Cleaner", "Tour Guide":
                System.out.print("What is the time now? ");
                yield scan.nextInt();
            default:
                yield 0;
        };

        switch (jobRole) {
            case "Feeding":
                if ( time < 20 && time > 7 ){
                    System.out.println("Your task is to feed the Dinosaurs.");
                }else{
                    System.out.println("Prepare food for feeding the Dinosaurs.");
                }
                break;
            case "Cleaner":
                if ( time < 13 || time > 15 ) {
                    System.out.println("Your task is to clean the enclosure alloted to you.");
                }else {
                    System.out.println("Its your break time.");
                }
                break;
            case "Security":
                System.out.print("Mention parks safety rating: ");
                float safetyRating = scan.nextFloat();

                if ( safetyRating > 9 ){
                    System.out.println("Your job is to look after park's safety.");
                }else {
                    System.out.println("Park's safety rating is low, increase surveillance.");
                }
                break;
            case "Tour Guide":
                if ( time < 10 || time > 19 ){
                    System.out.println("Park is closed, no tour guiding help other employees.");
                }else{
                    System.out.println("Guide the visitors through the park.");
                }
                break;
            default:
                System.out.println("Unknown job role.");
                break;

        }

        scan.close();
    }
}