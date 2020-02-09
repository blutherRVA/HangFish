#! /usr/bin/env python3

import random

from constants import FISH

def initializeGame():
    # Game input prompts anf variables
    # input_num = random.randint(1, 3)
    # fish_index = (int(input_num) - 1)
    # word = FISH[fish_index]

    # SUGGESTION: utilize the standard library, which provides a standard method
    # for doing what you did above.
    word = random.choice(FISH)
    return word

if __name__ == '__main__':
    selected_word = initializeGame()
    print(selected_word)