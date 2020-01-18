#This is the 1st Version of HangFish for Python 

print("Welcome to HangFish")
print("Rules: 1) Guess a number between one and three 2) Guess letters for the word, (which will inevitably be a fish) 3) Once you piece the letters together, guess the word!")
print("Let's Begin...")

fish = ["tuna","bass","hake"]
letters = ["t","u","n","a","b","a","s","s","h","a","k","e"]



input_num = input("What is uour number?:  ")
fish_index = (int(input_num) - 1)
word = fish[fish_index]



print("The fish is a " + str(len(word)) + " letter word. You will have 10 tries to get the word right")

is_done = False


if fish_index == 0:
    i= 0
    while i <= 10 and not is_done:
        guess_a_letter = input("Guess a letter:  ")

        if guess_a_letter == letters[0]:
            print("Nice!")
            print("t _ _ _")
            i += 1
        elif guess_a_letter == letters[1]:
            print("Nice")
            print("_ u _ _")
            i += 1
        elif guess_a_letter == letters[2]:
            print("Nice!")
            print("_ _ n _")
            i += 1
        elif guess_a_letter == letters[3]:
            print("Nice")
            print("_ _ _a")
            i += 1
        elif guess_a_letter == word:
            is_done = True
        else:
            print("Guess again!")
            i += 1
    if i > 10:
        print("You have exceeded your ten guesses. YOU LOSE!")

    else:
        print("Congratulations, you win!")

elif fish_index == 1:
    i= 0
    while i <= 10 and not is_done:
        guess_a_letter = input("Guess a letter:  ")

        if guess_a_letter == letters[4]:
            print("Nice!")
            print("b _ _ _")
            i += 1
        elif guess_a_letter == letters[5]:
            print("Nice")
            print("_ a _ _")
            i += 1
        elif guess_a_letter == letters[6]:
            print("Nice!")
            print("_ _ s s")
            i += 1
        elif guess_a_letter == word:
            print("You win!")
            is_done = True
        else:
            print("Guess again!")
            i += 1
    if i > 10:
        print("You have exceeded your ten guesses. YOU LOSE!")

    else:
        print("Congratulations, you win!")




else:
    i= 0
    while i <= 10 and not is_done:
        guess_a_letter = input("Guess a letter:  ")

        if guess_a_letter == letters[8]:
            print("Nice!")
            print("h _ _ _")
            i += 1
        elif guess_a_letter == letters[9]:
            print("Nice")
            print("_ a _ _")
            i += 1
        elif guess_a_letter == letters[10]:
            print("Nice!")
            print("_ _ k _")
            i += 1
        elif guess_a_letter == letters[11]:
            print("Nice")
            print("_ _ _ e")
            i += 1
        elif guess_a_letter == word:
            print("You win!")
            is_done = True
        else:
            print("Guess again!")
            i += 1
    if i > 10:
        print("You have exceeded your ten guesses. YOU LOSE!")

    else:
        print("Congratulations, you win!")
