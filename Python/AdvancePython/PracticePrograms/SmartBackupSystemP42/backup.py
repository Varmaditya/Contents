# backup.py

import shutil
import os
from datetime import datetime


class BackupSystem:

    def backup_file(self):

        try:
            filename = input("Enter filename: ")

            if not os.path.exists(filename):
                raise FileNotFoundError

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            backup_name = f"backup_{timestamp}_{filename}"

            shutil.copy(filename, backup_name)

            print("Backup created:", backup_name)

        except FileNotFoundError:
            print("File not found!")

        except Exception as e:
            print("Error:", e)
