#! /usr/bin/env python3

# SUGGESTION: use a "hash bang" to make your script executable
# https://stackoverflow.com/questions/2429511/why-do-people-write-the-usr-bin-env-python-shebang-on-the-first-line-of-a-pyt

import random
import sys
import turtle

from constants import FISH, MESSAGE
from gui import GameGUI
from game import Game

if __name__ == '__main__':

    game = Game(max_turns = 10, fish_options = FISH, game_gui=GameGUI())
    game.printInstructions()

    while not game.isOver():
        guess = input("Next Guess?")
        game.checkGuess(guess)

    if game.didWin():
        game.celebrate()
    else:
        game.shameLoser()

    sys.exit()