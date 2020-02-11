import random
from constants import MESSAGE, LETTER_DEFAULT
from collections import defaultdict


class Game():

    def __init__(self, max_turns, fish_options, game_gui):
        self.secret_word = random.choice(fish_options)
        self.is_over = False
        self.game_gui = game_gui
        self.used_guesses = 0
        self.max_turns = max_turns

        self.letters = list(self.secret_word)
        self.guessed_letters = [[letter, LETTER_DEFAULT]
                                for letter in self.letters]

    def printInstructions(self):
        print(MESSAGE.format(str(len(self.secret_word))).strip())

    def runGameLoop(self):
        self.game_gui.contine(True, [ letter[1] for letter in self.guessed_letters ])

        while not self.isOver():
            guess = input("Next Guess?")
            result = self.checkGuess(guess)
            self.game_gui.contine(result, [ letter[1] for letter in self.guessed_letters ])
        else:
            if self.didWin():
                self.celebrate()
                self.game_gui.win()
            else:
                self.shameLoser()
                self.game_gui.lose()

    def isOver(self):
        didWin = self.didWin()
        overLimit = self.used_guesses >= self.max_turns
        return didWin or overLimit

    def checkGuess(self, guess):
        self.used_guesses = self.used_guesses + 1
        print("Print Guess", guess)
        if guess in self.letters:
            letter_instances = [
                letter for letter in self.guessed_letters if letter[0] == guess]
            unused_letter_instances = [
                letter for letter in letter_instances if self.letterIsStillDefault(letter)
            ]
            if not len(unused_letter_instances):
                print('Correct Guess, but no more ', guess, "'s are found")
                return True
            else:
                unused_letter_instances[0][1] = guess
                print('Correct Guess')
                return True
        else:
            print('Missed guess')
            return False

    def didWin(self):
        unguessed_letters = [letter for letter in self.guessed_letters if self.letterIsStillDefault(letter)]
        return not bool(len(unguessed_letters))

    def letterIsStillDefault(self, guessable_letter):
        return guessable_letter[1] == LETTER_DEFAULT

    def celebrate(self):
        self.game_gui.win()
        print("You Win")

    def shameLoser(self):
        self.game_gui.lose()
        print("You Lose")
