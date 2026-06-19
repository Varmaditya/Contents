# storage/JSONStorage.py

import json
import os


class JSONStorage:

    # LOAD DATA FROM JSON FILE
    @staticmethod
    def load_data(file_name):

        try:
            # Create file if it doesn't exist
            if not os.path.exists(file_name):
                with open(file_name, "w") as file:
                    json.dump([], file)

            with open(file_name, "r") as file:
                data = json.load(file)
                return data

        except json.JSONDecodeError:
            print( f"Error reading {file_name}" )
            return []

        except Exception as error:
            print("Unexpected Error:", error)
            return []

    # SAVE DATA TO JSON FILE
    @staticmethod
    def save_data(file_name, data):

        try:
            with open(file_name, "w") as file:
                json.dump(
                    data,
                    file,
                    indent=4
                )

        except Exception as error:
            print("Save Error:", error)

    # APPEND SINGLE RECORD
    @staticmethod
    def append_data(file_name, record):

        data = JSONStorage.load_data(
            file_name
        )

        data.append(record)

        JSONStorage.save_data(
            file_name,
            data
        )

    # CLEAR FILE DATA
    @staticmethod
    def clear_data(file_name):

        JSONStorage.save_data(
            file_name,
            []
        )

        print(
            f"{file_name} cleared successfully."
        )

    # COUNT RECORDS
    @staticmethod
    def count_records(file_name):

        data = JSONStorage.load_data(
            file_name
        )

        return len(data)

    # FILE EXISTS CHECK
    @staticmethod
    def file_exists(file_name):

        return os.path.exists(file_name)

    # DISPLAY FILE CONTENT
    @staticmethod
    def display_data(file_name):

        data = JSONStorage.load_data(
            file_name
        )

        if not data:
            print("No Data Found.")
            return

        print("\n===== FILE DATA =====")

        for record in data:
            print(record)