


class Game():

    def __init__(self, max_turns, fish_options, game_gui):
        self.secret_word = random.choice(fish_options)
        self.is_over = False
        self.game_gui = game_gui
        self.used_guesses = 0

    def printInstructions(self):
        print(MESSAGE.format(str(len(self.secret_word))).strip())

    def isOver(self):
        is_over = self.is_over
        self.is_over = True
        return is_over

    def checkGuess(self, guess):
        self.used_guesses = self.used_guesses + 1
        print("Print Guess", guess)

    def didWin(self):
        return True

    def celebrate(self):
        print("You Win")

    def shameLoser(self):
        print("Failed")
