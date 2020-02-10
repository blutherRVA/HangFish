
class FishDrawer():

    __init__():

        pen = turtle.Turtle()
        eye = turtle.Turtle()
        gills = turtle.Turtle()
        p_fin = turtle.Turtle()

        pen.speed(0)
        pen.color("black")
        pen.penup()

        wn.title("HangFish 3.Bajillion")

        # game script

    def printLetters():
        self.letters_t.write(
            self.word_template.format(self.letter_1, self.letter_2,
                                      self.letter_3, self.letter_4),
            align="center",
            font=self.font_settings)

    def draw_gallows():
        # Here is where the gallows and noose are drawn
        pen.goto(0, -150)
        pen.backward(50)
        pen.pendown()
        pen.backward(150)
        pen.left(90)
        pen.forward(350)
        pen.right(90)
        pen.forward(200)
        pen.right(90)
        pen.forward(80)

    def loser():
        pen.penup()
        pen.goto(0, -260)
        pen.write("You have exceeded your ten guesses. YOU LOSE!",
                  align="center", font=("Courier", 20, "normal"))
        pen.penup()
        pen.goto(0, -290)
        pen.write("Enter any input to exit the game and start over",
                  align="center", font=("Courier", 15, "normal"))

    def drawEyes():
        eye.penup()
        eye.goto(-10, 70)
        eye.pendown()
        eye.color("black", "black")
        eye.begin_fill()
        eye.shape("circle")
        eye.shapesize(stretch_wid=.4, stretch_len=.4)
        eye.end_fill()
        eye.penup()

    def drawFace():
        # Here is where the fishes face is drawn, miss 1
        pen.right(30)
        pen.forward(75)
        pen.backward(75)
        pen.left(60)

    def drawGills():
        gills.hideturtle()
        gills.penup()
        gills.goto(0, 50)
        gills.pendown()
        gills.left(20)
        gills.forward(20)
        gills.backward(20)
        gills.left(140)
        gills.forward(20)
        gills.penup()

    def drawFishOutline():
        pen.forward(75)
        pen.left(30)
        pen.left(20)
        pen.forward(90)
        pen.right(50)

    def drawPectoralFin():
        p_fin.penup()
        p_fin.goto(0, 30)
        p_fin.left(90)
        p_fin.pendown()
        p_fin.color("black", "white")
        p_fin.begin_fill()
        p_fin.shape("triangle")
        p_fin.shapesize(stretch_wid=.5, stretch_len=1)
        p_fin.end_fill()
        p_fin.penup()

    def drawEndTail():
        # End tail + pen goes to other side of fish to reset, miss 7
        pen.forward(54)
        pen.penup()
        pen.goto(0, 120)
        pen.right(60)
        pen.pendown()
        pen.forward(75)
        pen.right(30)
