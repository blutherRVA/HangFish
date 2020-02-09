
import turtle


def initialize_turtle():
    # Input turtle settings
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("black")
    pen.penup()

    wn=turtle.Screen()
    wn.title("HangFish 3.Bajillion")

    # game script
    letters_t = turtle.Turtle()

    return pen;


def draw_gallows(pen):
    # Here is where the gallows and noose are drawn
    pen.goto(0,-150)
    pen.backward(50)
    pen.pendown()
    pen.backward(150)
    pen.left(90)
    pen.forward(350)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(80)