# Project: Netflix Analytics Dashboard

import csv
from collections import Counter


class NetflixTitle:

    def __init__(
        self,
        title,
        content_type,
        country,
        release_year
    ):

        self.title = title
        self.content_type = content_type
        self.country = country
        self.release_year = release_year


class NetflixAnalyzer:

    def __init__(self, filename):

        self.data = []

        self.load_data(filename)

    # Load CSV dataset
    def load_data(self, filename):

        try:

            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:

                reader = csv.DictReader(file)

                for row in reader:

                    obj = NetflixTitle(
                        row["title"],
                        row["type"],
                        row["country"],
                        row["release_year"]
                    )

                    self.data.append(obj)

            print("Dataset Loaded!")

        except FileNotFoundError:

            print("Dataset not found!")

    # Total records
    def total_titles(self):

        print(
            "\n🎬 Total Titles:",
            len(self.data)
        )

    # Movies vs TV Shows
    def content_distribution(self):

        counter = Counter()

        for item in self.data:

            counter[item.content_type] += 1

        print("\n📊 Content Distribution")

        for k, v in counter.items():

            print(k, "->", v)

    # Top release years
    def top_years(self):

        years = Counter()

        for item in self.data:

            years[item.release_year] += 1

        print("\n🔥 Top Release Years")

        for year, count in years.most_common(10):

            print(year, "->", count)

    # Search title
    def search_title(self):

        keyword = input(
            "Enter title keyword: "
        ).lower()

        found = False

        for item in self.data:

            if keyword in item.title.lower():

                print(
                    item.title,
                    "|",
                    item.release_year
                )

                found = True

        if not found:
            print("No title found")

    # Country analysis
    def country_analysis(self):

        countries = Counter()

        for item in self.data:

            if item.country:

                countries[item.country] += 1

        print("\n🌍 Top Countries")

        for country, count in countries.most_common(10):

            print(country, "->", count)


dashboard = NetflixAnalyzer(
    "netflix_titles.csv"
)

while True:

    print("\n=== NETFLIX DASHBOARD ===")
    print("1. Total Titles")
    print("2. Content Distribution")
    print("3. Top Years")
    print("4. Search Title")
    print("5. Country Analysis")
    print("6. Exit")

    choice = input("Choice: ")

    if choice == "1":
        dashboard.total_titles()

    elif choice == "2":
        dashboard.content_distribution()

    elif choice == "3":
        dashboard.top_years()

    elif choice == "4":
        dashboard.search_title()

    elif choice == "5":
        dashboard.country_analysis()

    else:
        break