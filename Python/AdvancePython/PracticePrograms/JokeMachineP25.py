# Program: Endless Joke Machine

class JokeMachine:
    def __init__(self):
        self.jokes = [
            "Why do programmers hate nature? Too many bugs.",
            "Why did Python go to school? To improve its class.",
            "Why do Java developers wear glasses? Because they don’t C#."
        ]

    def jokes_generator(self):
        # Generator cycles forever
        while True:
            for joke in self.jokes:
                yield joke


machine = JokeMachine()
gen = machine.jokes_generator()

while True:
    user = input("\nPress Enter for joke or type exit: ")
    if user == "exit":
        break
    print(next(gen))