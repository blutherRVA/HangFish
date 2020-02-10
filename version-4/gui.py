
import turtle


def draw_initial():
    # Input game variables
    letter_1 = "_ "
    letter_2 = "_ "
    letter_3 = "_ "
    letter_4 = "_ "


from letters_printer import LettersPrinter
from fish_drawer import FishDrawer

class GameGUI():

    word_template = "Word: {0}"
    font_settings = ("Courier", 20, "normal")

    def __init__(self):
        self.window = turtle.Screen()
        self.letters = []
        self.letters_printer = LettersPrinter()
        self.fish_drawer = FishDrawer()
