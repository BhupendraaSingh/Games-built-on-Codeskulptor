# This is Card Memory game is developed by :- Bhupendra Singh Gurjar

import simplegui
import random

# define global variables
deck = range(8) + range(8)
exposed = [False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False]
state = 0
card1 = ["B", "H"]
card2 = ["B", "H"]
card_one = ""
card_two = ""
count = 0
# helper function to initialize globals
def new_game():
    global exposed, count
    random.shuffle(deck)
    exposed = [False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False]
    count = 0
    label.set_text("Turns = " +str(count))

# define event handlers
def mouseclick(pos):
    global state, card1, card2, card_one, card_two, count

    # add game state logic here
    label.set_text("Turns = " +str(count))
    card_num = pos[0]//50
    if exposed[card_num] == False:
         exposed[card_num] = True
         if state == 0:
            state = 1
            card1 = deck[card_num]
            card_one = card_num

         elif state == 1:
            state = 2
            card2 = deck[card_num]
            card_two = card_num
            count += 1

         elif state == 2:
            state = 0
            if card1 != card2:
                exposed[card_one] = False
                exposed[card_two] = False
            if state == 0:
                state = 1
                card1 = deck[card_num]
                card_one = card_num

# cards are logically 50x100 pixels in size
def draw(canvas):
    global exposed
    # creating numbers of deck which 16 in number
    Width = 20
    for enum in deck:
        canvas.draw_text(str(enum), [Width, 60], 35, "White")
        Width += 50

    # creating green rectanglur cards which 16 in number
    card_pos = -32
    for card in exposed:
        card_pos += 51
        if not(card):
            canvas.draw_line([card_pos,0], [card_pos, 100], 50, "Green")

#create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = ")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
