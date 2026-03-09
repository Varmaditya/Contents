// Program: Movie Ticket Booking System

import java.util.Scanner;

class Movie {

    String name;
    int seats;

    Movie(String name, int seats) {
        this.name = name;
        this.seats = seats;
    }

    boolean book(int n) {

        if (n <= seats) {
            seats -= n;
            return true;
        }
        return false;
    }
}

public class MovieTicketBookingP84 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Movie[] movies = {
                new Movie("Avengers", 10),
                new Movie("Batman", 8),
                new Movie("Spiderman", 6)
        };

        System.out.println("Available Movies:");

        for (int i = 0; i < movies.length; i++)
            System.out.println(i + " - " + movies[i].name + " Seats:" + movies[i].seats);

        System.out.print("Select movie: ");
        int m = sc.nextInt();

        System.out.print("Enter seats: ");
        int seats = sc.nextInt();

        if (movies[m].book(seats))
            System.out.println("Booking Confirmed");
        else
            System.out.println("Not enough seats");

        sc.close();
    }
}