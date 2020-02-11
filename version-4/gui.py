import turtle

from letters_printer import LettersPrinter
from fish_drawer import FishDrawer


class GameGUI():

    def __init__(self):
        self.window = turtle.Screen()
        self.letters = []
        self.letters_printer = LettersPrinter()
        self.fish_drawer = FishDrawer()

    def contine(self, got_it_right, letters_to_print):
        if got_it_right:
            self.letters_printer.setLetters(letters_to_print)
            self.letters_printer.printLetters()
        else:
            next(self.fish_drawer)()

    def win(self):
        self.letters_printer.winner()

    def lose(self):
        self.letters_printer.loser()
