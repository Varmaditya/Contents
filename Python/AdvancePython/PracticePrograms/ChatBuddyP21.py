# Program: Chat Buddy

class ChatBot:
    def __init__(self, name):
        self.name = name

    def reply(self, message):
        message = message.lower()

        if "hello" in message:
            return "Hi there!"
        elif "how are you" in message:
            return "I'm just code, but I'm doing great!"
        elif "bye" in message:
            return "Goodbye!"
        else:
            return "I don't understand that."


bot = ChatBot("Robo")

while True:
    msg = input("You: ")

    response = bot.reply(msg)
    print("Bot:", response)

    if "bye" in msg.lower():
        break