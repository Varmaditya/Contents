# Program: Smart Email Sender

def check_message(func):
    # Decorator to validate message
    def wrapper(self, message):
        if len(message) == 0:
            print("Cannot send empty message!")
        else:
            func(self, message)
    return wrapper


class EmailService:
    @check_message
    def send(self, message):
        print("Sending email:", message)


email = EmailService()

msg = input("Enter message: ")
email.send(msg)