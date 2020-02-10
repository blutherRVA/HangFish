# SUGGESTION: read up about itertools, it's very useful
from itertools import chain

# SUGGESTION: use tuples over lists when the contents are immutable (meaning they can't/won't change)
FISH = ("tuna", "bass", "hake",)
LETTERS = tuple(set(chain.from_iterable(FISH)))

# SUGGESTION: learn about multiline strings
MESSAGE = \
"""
Welcome to HangFish
Rules: Guess letters for the word, (which will inevitably be a fish), Once you piece the letters together, guess the word!
The fish is a {} letter word. You will have 10 tries to get the word right
Let's Begin...
"""
