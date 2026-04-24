# Program: Movie Ticket Booking

class Movie:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket booked!")
        else:
            print("Housefull!")

    def show_details(self):
        print(self.name, "| Seats left:", self.seats)


movie = Movie("Avengers", 5)

while True:
    print("\n=== Movie Booking ===")
    print("1. Show Details")
    print("2. Book Ticket")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        movie.show_details()
    elif choice == "2":
        movie.book_ticket()
    elif choice == "3":
        break