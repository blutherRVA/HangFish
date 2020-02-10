

class LettersPrinter():
    self.word_template = "Words: {}"

    def __init__(self):
        self.letters_printer = turtle.Turtle()
        self.letters_printer.hideturtle()
        self.letters_printer.speed(0)
        self.letters_printer.color("black")

        self.letters = []

    def setLetters(self, letters):
        self.letters = letters

    def printLetters(self):
        self.letters_printer.penup()
        self.letters_printer.goto(0, 260)
        self.letters_printer.write(
            self.word_template.format(self.letters.join(" ")),
            align="center",
            font=("Courier", 20, "normal"))