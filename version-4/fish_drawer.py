import turtle


class FishDrawer():

    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("black")
        self.pen.penup()

        self.eye = turtle.Turtle()
        self.gills = turtle.Turtle()
        self.p_fin = turtle.Turtle()

        self.n = 0
        self.iteration_steps = [
            self.drawFace,
            self.missTwo,
            self.drawEyes,
            self.drawGills,
            self.drawFishOutline,
            self.missSix,
            self.drawEndTail,
            self.missEight,
            self.missNine,
            self.drawPectoralFin,
        ]

        self.pen.hideturtle()
        self.eye.hideturtle()
        self.gills.hideturtle()
        self.p_fin.hideturtle()

        self.drawGallows()


    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= len(self.iteration_steps):
            index = self.n
            self.n += 1
            return self.iteration_steps[index]
        else:
            raise StopIteration

    def missTwo(self):
        self.pen.forward(75)
        self.pen.backward(75)
        self.pen.right(60)

    def missSix(self):
        self.pen.forward(40)
        self.pen.left(120)

    def missEight(self):
        self.pen.right(20)
        self.pen.forward(90)
        self.pen.left(50)

    def missNine(self):
        self.pen.forward(40)
        self.pen.hideturtle()

    def drawGallows(self):
        # Here is where the gallows and noose are drawn
        self.pen.goto(0, -150)
        self.pen.backward(50)
        self.pen.pendown()
        self.pen.backward(150)
        self.pen.left(90)
        self.pen.forward(350)
        self.pen.right(90)
        self.pen.forward(200)
        self.pen.right(90)
        self.pen.forward(80)

    def drawEyes(self):
        self.eye.penup()
        self.eye.goto(-10, 70)
        self.eye.pendown()
        self.eye.color("black", "black")
        self.eye.begin_fill()
        self.eye.shape("circle")
        self.eye.shapesize(stretch_wid=.4, stretch_len=.4)
        self.eye.end_fill()
        self.eye.penup()
        self.eye.showturtle()

    def drawFace(self):
        # Here is where the fishes face is drawn, miss 1
        self.pen.right(30)
        self.pen.forward(75)
        self.pen.backward(75)
        self.pen.left(60)

    def drawGills(self):
        self.gills.hideturtle()
        self.gills.penup()
        self.gills.goto(0, 50)
        self.gills.pendown()
        self.gills.left(20)
        self.gills.forward(20)
        self.gills.backward(20)
        self.gills.left(140)
        self.gills.forward(20)
        self.gills.penup()

    def drawFishOutline(self):
        self.pen.forward(75)
        self.pen.left(30)
        self.pen.left(20)
        self.pen.forward(90)
        self.pen.right(50)

    def drawPectoralFin(self):
        self.p_fin.penup()
        self.p_fin.goto(0, 30)
        self.p_fin.left(90)
        self.p_fin.pendown()
        self.p_fin.color("black", "white")
        self.p_fin.begin_fill()
        self.p_fin.shape("triangle")
        self.p_fin.shapesize(stretch_wid=.5, stretch_len=1)
        self.p_fin.end_fill()
        self.p_fin.penup()

    def drawEndTail(self):
        # End tail + pen goes to other side of fish to reset, miss 7
        self.pen.forward(54)
        self.pen.penup()
        self.pen.goto(0, 120)
        self.pen.right(60)
        self.pen.pendown()
        self.pen.forward(75)
        self.pen.right(30)
