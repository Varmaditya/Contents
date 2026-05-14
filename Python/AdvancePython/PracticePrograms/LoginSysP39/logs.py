# logs.py

def write_log(message):
    with open("security_logs.txt", "a") as file:
        file.write(message + "\n")