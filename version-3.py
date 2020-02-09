#This is Version 3 of Hangfish, where fish names are selected randomly, and all graphics and logic have been debugged



print("Welcome to HangFish")
print("Rules: Guess letters for the word, (which will inevitably be a fish), Once you piece the letters together, guess the word!")




import random

# Initiate turtle module, window
import turtle




# Input game variables
letter_1 = "_ "
letter_2 = "_ "
letter_3 = "_ "
letter_4 = "_ "


letters_t.hideturtle()
letters_t.speed(0)
letters_t.color("black")
letters_t.penup()
letters_t.goto(0, 260)
letters_t.write("Word:" + letter_1 + letter_2 + letter_3 + letter_4 , align="center",font=("Courier", 20, "normal"))









print("The fish is a " + str(len(word)) + " letter word. You will have 10 tries to get the word right")
print("Let's Begin...")

i = 0
is_done = False
has_won = False

if fish_index == 0:

    while is_done is False:

        guess_a_letter = input("Guess a letter:  ")

        if i < 10 and has_won is False:

            if guess_a_letter == letters[0]:
                print("Nice!")
                letter_1 = "t "
                letters_t.write("Word:" + letter_1 + letter_2 + letter_3 + letter_4, align="center",font=("Courier", 20, "normal"))
            elif guess_a_letter == letters[1]:
                print("Nice!")
                letter_2 = "u "
                letters_t.write("Word:" + letter_1 + letter_2 + letter_3 + letter_4, align="center",font=("Courier", 20, "normal"))
            elif guess_a_letter == letters[2]:
                print("Nice!")
                letter_3 = "n "
                letters_t.write("Word:" + letter_1 + letter_2 + letter_3 + letter_4, align="center",font=("Courier", 20, "normal"))
            elif guess_a_letter == letters[3]:
                print("Nice!")
                letter_4 = "a "
                letters_t.write("Word:" + letter_1 + letter_2 + letter_3 + letter_4, align="center",font=("Courier", 20, "normal"))
            elif guess_a_letter == word:
                print("Great work!")
                letters_t.goto(0, -260)
                letters_t.write("Congratulations You Win!!!", align="center", font=("Courier", 20, "normal"))
                print("Enter any input to exit the game and start over")
                pen.penup()
                pen.hideturtle()
                pen.goto(0, -290)
                pen.write("Enter any input to exit the game and start over", align="center",font=("Courier", 15, "normal"))
                has_won = True
            else:
                if i == 0:
                    # Here is where the fishes face is drawn, miss 1
                    pen.right(30)
                    pen.forward(75)
                    pen.backward(75)
                    pen.left(60)
                    i += 1
                    print("Nope, guess again!")
                elif i == 1:
                    # miss 2
                    pen.forward(75)
                    pen.backward(75)
                    pen.right(60)
                    i += 1
                    print("Nope, guess again!")
                elif i == 2:
                    # Here is where the eyes are drawn, miss 3
                    eye = turtle.Turtle()
                    eye.penup()
                    eye.goto(-10, 70)
                    eye.pendown()
                    eye.color("black", "black")
                    eye.begin_fill()
                    eye.shape("circle")
                    eye.shapesize(stretch_wid=.4, stretch_len=.4)
                    eye.end_fill()
                    eye.penup()
                    i += 1
                    print("Nope, guess again!")
                elif i == 3:
                    # Here is where the gills were drawn, miss 4
                    gills = turtle.Turtle()
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
                    i += 1
                    print("Nope, guess again!")
                elif i == 4:
                    # Back to where the fish outline is drawn, miss 5
                    pen.forward(75)
                    pen.left(30)
                    pen.left(20)
                    pen.forward(90)
                    pen.right(50)

                    i += 1
                    print("Nope, guess again!")
                elif i == 5:
                    # miss 6
                    pen.forward(40)
                    pen.left(120)
                    i += 1
                    print("Nope, guess again!")
                elif i == 6:
                    # End tail + pen Goes to other side of fish to reset, miss 7
                    pen.forward(54)
                    pen.penup()
                    pen.goto(0, 120)
                    pen.right(60)
                    pen.pendown()
                    pen.forward(75)
                    pen.right(30)
                    i += 1
                    print("Nope, guess again!")
                elif i == 7:
                    # Pen Continue to draw, miss 8
                    pen.right(20)
                    pen.forward(90)
                    pen.left(50)
                    i += 1
                    print("Nope, guess again!")
                elif i == 8:
                    # miss 9
                    pen.forward(40)
                    pen.hideturtle()
                    i += 1
                    print("Nope, guess again!")
                else:
                    # Here is where the pectoral fin is drawn, miss 10
                    p_fin = turtle.Turtle()
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
                    print("Out of guesses")
                    pen.penup()
                    pen.goto(0, -260)
                    pen.write("You have exceeded your ten guesses. YOU LOSE!", align="center", font=("Courier", 20, "normal"))
                    i += 1
                    print("Enter any input to exit the game and start over")
                    pen.penup()
                    pen.goto(0, -290)
                    pen.write("Enter any input to exit the game and start over", align="center", font=("Courier", 15, "normal"))
        else:
            is_done = True


elif fish_index == 1:
    while is_done is False:

        guess_a_letter = input("Guess a letter:  ")

        if i < 10 and has_won is False:

            if guess_a_letter == letters[4]:
                print("Nice!")
                letter_1 = "b "
                letters_t.write("Word:" + letter_1 + letter_2 + letter_3 + letter_4, align="center",
                                font=("Courier", 20, "normal"))
            elif guess_a_letter == letters[5]:
                print("Nice!")
                letter_2 = "a "
                letters_t.write("Word:" + letter_1 + letter_2 + letter_3 + letter_4, align="center",
                                font=("Courier", 20, "normal"))
            elif guess_a_letter == letters[6]:
                print("Nice!")
                letter_3 = "s "
                letter_4 = "s "
                letters_t.write("Word:" + letter_1 + letter_2 + letter_3 + letter_4, align="center",
                                font=("Courier", 20, "normal"))
            elif guess_a_letter == word:
                print("Great work!")
                letters_t.goto(0, -260)
                letters_t.write("Congratulations You Win!!!", align="center", font=("Courier", 20, "normal"))
                print("Enter any input to exit the game and start over")
                pen.penup()
                pen.hideturtle()
                pen.goto(0, -290)
                pen.write("Enter any input to exit the game and start over", align="center",font=("Courier", 15, "normal"))
                has_won = True
            else:
                if i == 0:
                    # Here is where the fishes face is drawn, miss 1
                    pen.right(30)
                    pen.forward(75)
                    pen.backward(75)
                    pen.left(60)
                    i += 1
                    print("Nope, guess again!")
                elif i == 1:
                    # miss 2
                    pen.forward(75)
                    pen.backward(75)
                    pen.right(60)
                    i += 1
                    print("Nope, guess again!")
                elif i == 2:
                    # Here is where the eyes are drawn, miss 3
                    eye = turtle.Turtle()
                    eye.penup()
                    eye.goto(-10, 70)
                    eye.pendown()
                    eye.color("black", "black")
                    eye.begin_fill()
                    eye.shape("circle")
                    eye.shapesize(stretch_wid=.4, stretch_len=.4)
                    eye.end_fill()
                    eye.penup()
                    i += 1
                    print("Nope, guess again!")
                elif i == 3:
                    # Here is where the gills were drawn, miss 4
                    gills = turtle.Turtle()
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
                    i += 1
                    print("Nope, guess again!")
                elif i == 4:
                    # Back to where the fish outline is drawn, miss 5
                    pen.forward(75)
                    pen.left(30)
                    pen.left(20)
                    pen.forward(90)
                    pen.right(50)

                    i += 1
                    print("Nope, guess again!")
                elif i == 5:
                    # miss 6
                    pen.forward(40)
                    pen.left(120)

                    i += 1
                    print("Nope, guess again!")
                elif i == 6:
                    # End tail + pen goes to other side of fish to reset, miss 7
                    pen.forward(54)
                    pen.penup()
                    pen.goto(0, 120)
                    pen.right(60)
                    pen.pendown()
                    pen.forward(75)
                    pen.right(30)
                    i += 1
                    print("Nope, guess again!")
                elif i == 7:
                    # Pen Continue to draw, miss 8
                    pen.right(20)
                    pen.forward(90)
                    pen.left(50)
                    i += 1
                    print("Nope, guess again!")
                elif i == 8:
                    # miss 9
                    pen.forward(40)
                    pen.hideturtle()
                    i += 1
                    print("Nope, guess again!")
                else:
                    # Here is where the pectoral fin is drawn, miss 10
                    p_fin = turtle.Turtle()
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
                    print("Out of guesses")
                    pen.penup()
                    pen.goto(0, -260)
                    pen.write("You have exceeded your ten guesses. YOU LOSE!", align="center", font=("Courier", 20, "normal"))
                    i += 1
                    print("Enter any input to exit the game and start over")
                    pen.penup()
                    pen.goto(0, -290)
                    pen.write("Enter any input to exit the game and start over", align="center", font=("Courier", 15, "normal"))
        else:
            is_done = True


elif fish_index == 2:

    while is_done is False:

        guess_a_letter = input("Guess a letter:  ")

        if i < 10 and has_won is False:

            if guess_a_letter == letters[8]:
                print("Nice!")
                letter_1 = "h "
                letters_t.write("Word:" + letter_1 + letter_2 + letter_3 + letter_4, align="center",
                                font=("Courier", 20, "normal"))
            elif guess_a_letter == letters[9]:
                print("Nice")
                letter_2 = "a "
                letters_t.write("Word:" + letter_1 + letter_2 + letter_3 + letter_4, align="center",
                                font=("Courier", 20, "normal"))
            elif guess_a_letter == letters[10]:
                print("Nice!")
                letter_3 = "k "
                letters_t.write("Word:" + letter_1 + letter_2 + letter_3 + letter_4, align="center",
                                font=("Courier", 20, "normal"))
            elif guess_a_letter == letters[11]:
                print("Nice")
                letter_4 = "e "
                letters_t.write("Word:" + letter_1 + letter_2 + letter_3 + letter_4, align="center",
                                font=("Courier", 20, "normal"))
            elif guess_a_letter == word:
                print("Great work!")
                letters_t.goto(0, -260)
                letters_t.write("Congratulations You Win!!!", align="center", font=("Courier", 20, "normal"))
                print("Enter any input to exit the game and start over")
                pen.penup()
                pen.hideturtle()
                pen.goto(0, -290)
                pen.write("Enter any input to exit the game and start over", align="center",font=("Courier", 15, "normal"))
                has_won = True
            else:
                if i == 0:
                    # Here is where the fishes face is drawn, miss 1
                    pen.right(30)
                    pen.forward(75)
                    pen.backward(75)
                    pen.left(60)
                    i += 1
                    print("Nope, guess again!")
                elif i == 1:
                    # miss 2
                    pen.forward(75)
                    pen.backward(75)
                    pen.right(60)
                    i += 1
                    print("Nope, guess again!")
                elif i == 2:
                    # Here is where the eyes are drawn, miss 3
                    eye = turtle.Turtle()
                    eye.penup()
                    eye.goto(-10, 70)
                    eye.pendown()
                    eye.color("black", "black")
                    eye.begin_fill()
                    eye.shape("circle")
                    eye.shapesize(stretch_wid=.4, stretch_len=.4)
                    eye.end_fill()
                    eye.penup()
                    i += 1
                    print("Nope, guess again!")
                elif i == 3:
                    # Here is where the gills were drawn, miss 4
                    gills = turtle.Turtle()
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
                    i += 1
                    print("Nope, guess again!")
                elif i == 4:
                    # Back to where the fish outline is drawn, miss 5
                    pen.forward(75)
                    pen.left(30)
                    pen.left(20)
                    pen.forward(90)
                    pen.right(50)

                    i += 1
                    print("Nope, guess again!")
                elif i == 5:
                    # miss 6
                    pen.forward(40)
                    pen.left(120)
                    i += 1
                    print("Nope, guess again!")
                elif i == 6:
                    # End tail + pen goes to other side of fish to reset, miss 7
                    pen.forward(54)
                    pen.penup()
                    pen.goto(0, 120)
                    pen.right(60)
                    pen.pendown()
                    pen.forward(75)
                    pen.right(30)
                    i += 1
                    print("Nope, guess again!")
                elif i == 7:
                    # Pen Continue to draw, miss 8
                    pen.right(20)
                    pen.forward(90)
                    pen.left(50)
                    i += 1
                    print("Nope, guess again!")
                elif i == 8:
                    # miss 9
                    pen.forward(40)
                    pen.hideturtle()
                    i += 1
                    print("Nope, guess again!")
                else:
                    # Here is where the pectoral fin is drawn, miss 10
                    p_fin = turtle.Turtle()
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
                    print("Out of guesses")
                    pen.penup()
                    pen.goto(0, -260)
                    pen.write("You have exceeded your ten guesses. YOU LOSE!", align="center", font=("Courier", 20, "normal"))
                    i += 1
                    print("Enter any input to exit the game and start over")
                    pen.penup()
                    pen.goto(0, -290)
                    pen.write("Enter any input to exit the game and start over", align="center", font=("Courier", 15, "normal"))
        else:
            is_done = True
