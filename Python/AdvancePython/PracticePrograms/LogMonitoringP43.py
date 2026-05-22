# Program: Real-Time Log Monitoring Tool

import os
from datetime import datetime
from collections import Counter


class LogMonitor:

    def __init__(self, filename):
        self.filename = filename

    def add_log(self):

        levels = ["INFO", "WARNING", "ERROR"]

        print("\nLog Levels:", levels)

        level = input("Enter level: ").upper()
        message = input("Enter message: ")

        timestamp = datetime.now()

        with open(self.filename, "a") as file:
            file.write(f"{timestamp}|{level}|{message}\n")

        print("Log added!")

    def analyze_logs(self):

        if not os.path.exists(self.filename):
            print("No logs found!")
            return

        counter = Counter()

        with open(self.filename, "r") as file:

            for line in file:
                parts = line.strip().split("|")

                if len(parts) >= 2:
                    counter[parts[1]] += 1

        print("\n=== Log Analysis ===")

        for level, count in counter.items():
            print(level, "->", count)


monitor = LogMonitor("system_logs.txt")

while True:
    print("\n=== Log Monitor ===")
    print("1. Add Log")
    print("2. Analyze Logs")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        monitor.add_log()

    elif choice == "2":
        monitor.analyze_logs()

    else:
        break