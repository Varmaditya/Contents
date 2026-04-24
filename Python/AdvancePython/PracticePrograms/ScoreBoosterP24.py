# Program: Game Score Booster

def double_score(func):
    # Decorator to boost score
    def wrapper(score):
        print("Score boosted!")
        return func(score * 2)
    return wrapper


class Game:
    @double_score
    def add_score(self, score):
        print("Final Score:", score)


game = Game()

score = int(input("Enter your score: "))
game.add_score(score)