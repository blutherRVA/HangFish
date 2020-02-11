import turtle


class LettersPrinter():
    word_template = "Letters: {}"
    LARGE_SIZE = {"align": "center", "font": ("Courier", 20, "normal")}
    SMALL_SIZE = {"align": "center", "font": ("Courier", 15, "normal")}

    def __init__(self):
        self.letters_printer = turtle.Turtle()
        self.letters_printer.hideturtle()
        self.letters_printer.speed(0)
        self.letters_printer.color("black")

        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("black")
        self.pen.penup()

        self.pen.hideturtle()
        self.letters_printer.hideturtle()

        self.letters = []

    def setLetters(self, letters):
        self.letters = letters

    def printLetters(self):
        self.letters_printer.clear()
        self.letters_printer.penup()
        self.letters_printer.goto(0, 260)
        self.letters_printer.write(
            self.word_template.format(" ".join(self.letters)),
            **self.LARGE_SIZE)

    def loser(self):
        self.pen.penup()
        self.pen.goto(0, -260)
        self.pen.write("You have exceeded your ten guesses. YOU LOSE!",
                       **self.LARGE_SIZE)
        self.pen.penup()
        self.pen.goto(0, -290)
        self.pen.write("Enter any input to exit the game and start over",
                       **self.SMALL_SIZE)

    def winner(self):
        self.letters_printer.goto(0, -260)
        self.letters_printer.write(
            "Congratulations You Win!!!", **self.LARGE_SIZE)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, -290)
        self.pen.write("Enter any input to exit the game and start over",
                       **self.SMALL_SIZE)
