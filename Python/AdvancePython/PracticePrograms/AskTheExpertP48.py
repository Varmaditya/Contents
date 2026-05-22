from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('capital.txt') as file:
        for line in file:
            line = line.rstrip("\n")
            country, city = line.split("/")
            theWorld[country] = city

def write_to_file(country_name, city_name):
    with open('capital.txt', 'a') as file:
        file.write("\n" + country_name + "/" + city_name)

print("Ask the Expert - Capital Cities of the World")
root = Tk()
root.withdraw()

theWorld = {}

read_from_file()

while True:
    queryCountry = simpledialog.askstring("Country", "Type the name of a country: ")

    if queryCountry in theWorld:
        result = theWorld[queryCountry]
        messagebox.showinfo("Answer", "The capital of " + queryCountry + " is " + result + "!")
    else:
        newCity = simpledialog.askstring("Teach me", "I don\'t know! "+ "What is the capital city of " + queryCountry + "?")
        theWorld[queryCountry] = newCity
        write_to_file(queryCountry, newCity)

root.mainloop()



# Make a file named capital.txt with content give below:
# India/New Delhi
# China/Beijing
# France/Paris
# Argentina/Buenos Aires
# Egypt/Cairo
# Russia/Moscow
