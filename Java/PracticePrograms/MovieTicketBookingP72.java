// Program: Cinema Seat Booking Map

import java.util.Scanner;

public class MovieTicketBookingP72 {

    static void showSeats(char[] seats) {
        System.out.println("\nSeat Layout:");
        for (int i = 0; i < seats.length; i++)
            System.out.print("[" + seats[i] + "] ");
        System.out.println();
    }

    static boolean bookSeat(char[] seats, int seatNo) {

        if (seatNo < 1 || seatNo > seats.length)
            return false;

        if (seats[seatNo - 1] == 'X')
            return false;

        seats[seatNo - 1] = 'X';
        return true;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        char[] seats = {'O','O','O','O','O','O','O','O'};

        while (true) {

            showSeats(seats);

            System.out.print("Enter seat number (0 to exit): ");
            int seat = sc.nextInt();

            if (seat == 0)
                break;

            if (bookSeat(seats, seat))
                System.out.println("Seat booked!");
            else
                System.out.println("Invalid or already booked seat!");
        }

        sc.close();
    }
}