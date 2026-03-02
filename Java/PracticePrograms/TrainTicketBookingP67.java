// Practice Program: Train Ticket Booking System

import java.util.Scanner;

public class TrainTicketBookingP67 {

    static boolean validateSeats(int available, int requested) {
        return requested > 0 && requested <= available;
    }

    static int bookSeats(int available, int requested) {
        return available - requested;
    }

    static void printTicket(String name, int seats) {
        System.out.println("\n===== TICKET CONFIRMATION =====");
        System.out.println("Passenger: " + name);
        System.out.println("Seats Booked: " + seats);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int availableSeats = 10;
        int choice;

        do {
            System.out.println("\n1.Book Ticket  2.Exit");
            System.out.print("Choose option: ");
            choice = sc.nextInt();
            sc.nextLine();

            if (choice == 1) {
                System.out.print("Enter name: ");
                String name = sc.nextLine();

                System.out.print("Enter seats required: ");
                int seats = sc.nextInt();

                if (validateSeats(availableSeats, seats)) {
                    availableSeats = bookSeats(availableSeats, seats);
                    printTicket(name, seats);
                } else {
                    System.out.println("Booking Failed");
                }

                if (availableSeats == 0) {
                    System.out.println("All seats booked!");
                    break;
                }
            }

        } while (choice != 2);

        sc.close();
    }
}