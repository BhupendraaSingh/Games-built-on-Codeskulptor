# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# Globals
num_range =  100

# helper function to start and restart the game
def new_game():
    global secret_number
    global chances

    # for range from 0 to 100
    if (num_range == 100):
        secret_number = random.randrange(0, 100)
        chances = 7
        print ("New game. Range is from 0 to 100")
        print ("Reamining guess is ",chances)

    # for range from 0 to 1000
    elif (num_range == 1000):
        secret_number = random.randrange(0, 1000)
        chances = 10
        print ("New game. Range is from 0 to 1000")
        print ("Reamining guess is ", chances)



    print ("")

# define event handlers for control panel
def range100():
    # updates num_range for range [0, 100]
    global num_range
    num_range = 100

    # calls new_game function with updated num_range
    new_game()


def range1000():
    # updates num_range for range [0, 1000]
    global num_range
    num_range = 1000

    # calls new_game function with updated num_range
    new_game()



def input_guess(guess):
    guess_num = int(guess)
    global secret_number
    global chances
    # reduce the value by entering guess
    chances = chances - 1

    print  ("Guess was",guess_num)
    print ("Reamining guess is ",chances)


    if (guess_num < secret_number) and (chances >= 0):
        print ("Higher!")
        print ("")

    elif (guess_num > secret_number) and (chances >= 0):
        print ("Lower!")
        print ("")

    elif (guess_num == secret_number) and (chances >= 0):
        print ("Correct!!!")
        print ("")
        new_game()


    # if chances become 0 calls new_game with last game_mode
    if chances == 0:
        print ("==========================================================")
        new_game()




# create frame
frame = simplegui.create_frame("Guess the Number", 250, 250)


# register event handlers for control elements and start frame

frame.add_button("Range is [0,100)", range100, 150)
frame.add_button("Range is [0,1000)", range1000, 150)
frame.add_label("")
frame.add_input("Enter a Guess", input_guess, 100)


# call new_game
frame.start()
new_game()


# always remember to check your completed program against the grading rubric
