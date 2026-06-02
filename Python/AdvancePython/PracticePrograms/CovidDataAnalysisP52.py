# Project: Global COVID-19 Data Analyzer

import csv

# ---------------- COUNTRY CLASS ----------------
class Country:
    def __init__(self, name, total_cases, total_deaths, total_recovered):
        self.name = name
        self.total_cases = int(total_cases)
        self.total_deaths = int(total_deaths)
        self.total_recovered = int(total_recovered)

    # Calculate death rate percentage
    def death_rate(self):
        return (self.total_deaths / self.total_cases) * 100

    # Calculate recovery rate percentage
    def recovery_rate(self):
        return (self.total_recovered / self.total_cases) * 100


# ---------------- ANALYZER CLASS ----------------
class CovidAnalyzer:

    def __init__(self, filename):
        self.countries = []
        self.load_data(filename)

    # Read CSV dataset
    def load_data(self, filename):
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    country = Country(row["country"], row["total_cases"], row["total_deaths"], row["total_recovered"])
                    self.countries.append(country)
            print("✅ Dataset Loaded Successfully")

        except FileNotFoundError:
            print("❌ Dataset File Not Found")

    # Total cases worldwide
    def total_cases(self):
        total = 0

        for country in self.countries:
            total += country.total_cases

        print("\n🌍 Total Cases:", total)

    # Country with highest cases
    def highest_cases(self):
        country = max(self.countries, key=lambda c: c.total_cases)
        print("\n🏆 Highest Cases")
        print(country.name)
        print("Cases:", country.total_cases)

    # Country with highest deaths
    def highest_deaths(self):
        country = max(self.countries, key=lambda c: c.total_deaths)
        print("\n💀 Highest Deaths")
        print(country.name)
        print("Deaths:", country.total_deaths)

    # Show death rate report
    def death_rate_report(self):
        print("\n📊 Death Rate Report")

        for country in self.countries:
            print(country.name, "->", round(country.death_rate(), 2), "%")

    # Search country
    def search_country(self):
        name = input("Enter Country Name: ").lower()
        found = False

        for country in self.countries:
            if name in country.name.lower():
                print("\nCountry:", country.name)
                print("Cases:", country.total_cases)
                print("Deaths:", country.total_deaths)
                print("Recovered:", country.total_recovered)
                print("Recovery Rate:", round(country.recovery_rate(), 2), "%")
                found = True

        if not found:
            print("Country Not Found")


# ---------------- MAIN PROGRAM ----------------
analyzer = CovidAnalyzer("covid_data.csv")

while True:

    print("\n=== COVID DATA ANALYZER ===")
    print("1. Total Cases")
    print("2. Highest Cases")
    print("3. Highest Deaths")
    print("4. Death Rate Report")
    print("5. Search Country")
    print("6. Exit")

    choice = input("Choice: ")

    if choice == "1":
        analyzer.total_cases()
    elif choice == "2":
        analyzer.highest_cases()
    elif choice == "3":
        analyzer.highest_deaths()
    elif choice == "4":
        analyzer.death_rate_report()
    elif choice == "5":
        analyzer.search_country()
    elif choice == "6":
        break
    else:
        print("Invalid Choice")