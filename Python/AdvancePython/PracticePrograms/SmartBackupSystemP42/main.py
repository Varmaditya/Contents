# main.py for Smart Backup System

from backup import BackupSystem

system = BackupSystem()

while True:
    print("\n=== Smart Backup System ===")
    print("1. Backup File")
    print("2. Exit")

    if input("Choice: ") == "1":
        system.backup_file()
    else:
        break
