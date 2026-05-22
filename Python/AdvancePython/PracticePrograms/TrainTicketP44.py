# Program: Smart Railway Reservation System

import json
import os
from datetime import datetime


class Train:

    def __init__(self, train_no, name, seats):

        self.train_no = train_no
        self.name = name
        self.seats = seats


class ReservationSystem:

    def __init__(self, filename):

        self.filename = filename

        self.trains = [
            Train(101, "Express Line", 5),
            Train(202, "Night Rider", 3),
            Train(303, "Mountain Express", 2)
        ]

        if not os.path.exists(filename):

            with open(filename, "w") as file:
                json.dump([], file)

    def show_trains(self):

        print("\n=== Available Trains ===")

        for train in self.trains:

            print(
                train.train_no,
                "|",
                train.name,
                "| Seats:",
                train.seats
            )

    def book_ticket(self):

        try:

            train_no = int(input("Enter Train Number: "))
            passenger = input("Passenger Name: ")

            selected = None

            for train in self.trains:

                if train.train_no == train_no:
                    selected = train

            if not selected:
                raise Exception("Train not found!")

            if selected.seats <= 0:
                raise Exception("No seats available!")

            selected.seats -= 1

            ticket = {
                "passenger": passenger,
                "train": selected.name,
                "time": str(datetime.now())
            }

            with open(self.filename, "r") as file:
                data = json.load(file)

            data.append(ticket)

            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)

            print("\n✅ Ticket Booked Successfully!")

        except ValueError:
            print("Invalid train number!")

        except Exception as e:
            print("Booking Failed:", e)

    def show_bookings(self):

        with open(self.filename, "r") as file:
            data = json.load(file)

        print("\n=== Booking Records ===")

        for ticket in data:

            print(
                ticket["passenger"],
                "|",
                ticket["train"],
                "|",
                ticket["time"]
            )


system = ReservationSystem("tickets.json")

while True:

    print("\n=== Railway Reservation System ===")
    print("1. Show Trains")
    print("2. Book Ticket")
    print("3. View Bookings")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        system.show_trains()

    elif choice == "2":
        system.book_ticket()

    elif choice == "3":
        system.show_bookings()

    else:
        break