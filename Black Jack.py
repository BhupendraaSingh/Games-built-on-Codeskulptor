# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
hand_value = 0
dealer = []
my_hand = []
my_dec = []
wins, lose = 0, 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self): # Create a list of all cards in the Hand
        self.list_of_cards = []


    def __str__(self): # output the cards in hand
        s = 'Hand contains '
        for e in self.list_of_cards:
            s += str(e)
            s += ' '

        return s

    def add_card(self, card):
        self.list_of_cards.append(card) # add a card in the hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        ace = False
        for card in self.list_of_cards:
            hand_value += VALUES[card.get_rank()]

            if card.get_rank() == 'A':
                ace = True

        if ace and hand_value + 10 <= 21:
            hand_value += 10

        return hand_value

    def draw(self, canvas, pos):
        i = 0
        for ecard in self.list_of_cards:
            ecard.draw(canvas,[i+ pos[0], pos[1]])
            i += 100

# define deck class
class Deck:
    def __init__(self): # Create a deck with all 52 cards
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        s = random.choice(self.deck) # takes a card randomly
        self.deck.remove(s) # remove that card from deck
        return s

    def __str__(self):  # output cards in the deck
        deck = 'Deck contains '
        for c in self.deck:
            deck += str(c)
            deck += ' '

        return deck


#define event handlers for buttons
def deal():
    global outcome, in_play, my_hand, dealer, my_dec
    outcome = ''
    wins, lose = 0, 0
    my_dec, my_hand, dealer = Deck(), Hand(), Hand()
    my_dec.shuffle()

    my_hand.add_card(my_dec.deal_card())
    my_hand.add_card(my_dec.deal_card())
    dealer.add_card(my_dec.deal_card())
    dealer.add_card(my_dec.deal_card())
    in_play = True
    outcome = "Hit or Stand ?"


def hit():
    global in_play, outcome, lose
    if hand_value <= 21:
        my_hand.add_card(my_dec.deal_card())

    elif hand_value > 21:
        outcome =  "You have busted"
        lose += 1
        in_play = False

    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score

def stand():
    global in_play, outcome, dealer, lose, wins
    if my_hand.get_value() > 21:
        outcome = "You have busted, Dealer wins"
        lose += 1
        in_play = False

    elif in_play:
        while dealer.get_value() <= 17:
            dealer.add_card(my_dec.deal_card())

    if dealer.get_value() > 21 and in_play:
        outcome = "Dealer busted, You wins"
        in_play = False
        wins += 1

    elif my_hand.get_value() <= dealer.get_value() and in_play:
        outcome = "Dealer wins"
        lose += 1
        in_play = False

    elif my_hand.get_value() > dealer.get_value() and in_play:
        outcome = "Player wins"
        in_play = False
        wins += 1


    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler
def draw(canvas):
    canvas.draw_text("BLACK JACK", [170, 40], 40, "Blue")
    canvas.draw_text("===========", [170,60], 40, "Red")
    canvas.draw_text("Dealer", [50, 100], 30, "Black")
    canvas.draw_text("Player", [50, 340], 30, "Black")
    canvas.draw_text("Wins:"+str(wins), [350, 100], 30, "Black")
    canvas.draw_text("Lose:"+str(lose), [470, 100], 30, "Black")
    canvas.draw_text(outcome, [230, 550], 30, "Black")
    canvas.draw_text("Total: " + str(my_hand.get_value()), [200, 340], 30, "Black")

    #draw cards
    dealer.draw(canvas,[50,150])
    my_hand.draw(canvas,[50, 390])

    if in_play == False:
        canvas.draw_text(" Deal Again ?", [350, 340], 30, "Black")

    # Draw back of card
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [85,196], CARD_BACK_SIZE,)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
