""" Works through Phase 1 """

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
IN_PLAY = False
SCORE = 0
current_deck = None
dealer_hand = None
player_hand = None
PLAYER_SUM = None
player_location = [None, 400]
dealer_location = [None, 180]
GLOBAL_MESSAGE = None

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
class Hand():
    def __init__(self):
        self.hand = list()
       
    def __str__(self):
        s = ""
        for value in self.hand:
            value = str(value)
            s = s + " " + value
        return s
        
    def add_card(self, card):
        self.hand.append(card) 

    def get_value(self):
        sum = 0
        aces_in_hand = 0
        for value in self.hand:
            card_rank = value.get_rank()
            card_val = VALUES[card_rank]
            sum += card_val
            if card_rank == 'A' and sum <= 11:
                sum += 10
                aces_in_hand += 1
            if sum > 21 and aces_in_hand > 0:
                sum -= 10
                aces_in_hand -= 1
        return sum
   
    def draw(self, canvas, pos):        
        spacing = 90
        idx = 1
        for card in self.hand:
            pos[0] = idx * spacing
            card.draw(canvas, pos)
            idx += 1    
            
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [[suit, rank] for suit in SUITS for rank in RANKS]

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        dealt_card_list = self.deck.pop(-1)
        suit, rank = dealt_card_list[0], dealt_card_list[1]
        return Card(suit, rank)
    
    def __str__(self):
        s = ""
        for suit_rank_pair in self.deck:
            current_pair = suit_rank_pair[0] + suit_rank_pair[1]
            s = s + current_pair + " "
        return s



#define event handlers for buttons
def deal():
    global IN_PLAY, current_deck, player_hand, dealer_hand, SCORE
    
    if IN_PLAY == True:
        SCORE -= 1
    
    IN_PLAY = True
    
    current_deck = Deck()
    current_deck.shuffle()
    
    player_hand = Hand()
    c1, c2, c3, c4 = current_deck.deal_card(), current_deck.deal_card(), current_deck.deal_card(), current_deck.deal_card()
    player_hand.add_card(c1)
    player_hand.add_card(c3)
    
    dealer_hand = Hand()
    dealer_hand.add_card(c2)
    dealer_hand.add_card(c4)

def hit():
    global player_hand, IN_PLAY, SCORE, GLOBAL_MESSAGE
    if IN_PLAY == True:
        new_player_card = current_deck.deal_card()
        player_hand.add_card(new_player_card)
        if player_hand.get_value() > 21:
            GLOBAL_MESSAGE = "Dealer wins! (Player busted)"
            SCORE -= 1
            IN_PLAY = False
       
def stand():
    global player_hand, dealer_hand, IN_PLAY, SCORE, GLOBAL_MESSAGE
    if player_hand.get_value() > 21:
        global_message = "Dealer wins! (Player busted)"
    else:
        while dealer_hand.get_value() < 17:
            new_dealer_card = current_deck.deal_card()
            dealer_hand.add_card(new_dealer_card)
            if dealer_hand.get_value() > 21:
                SCORE += 1
                GLOBAL_MESSAGE = "Player wins! (Dealer busted)"
                IN_PLAY = False
           
    # Determine winner in the case of player not busting:
    if IN_PLAY == True:
        if dealer_hand.get_value() >= player_hand.get_value():
            SCORE -= 1
            GLOBAL_MESSAGE = "Dealer wins! (No one busted)"
            IN_PLAY = False
        else:
            SCORE += 1
            GLOBAL_MESSAGE = "Player wins! (Neither player nor dealer busted)"
            IN_PLAY = False
        
        

# draw handler    
def draw(canvas):
    global GLOBAL_MESSAGE
    # unconditional draws:
    dealer_hand.draw(canvas, dealer_location)
    player_hand.draw(canvas, player_location)
    canvas.draw_text("BLACKJACK", (10, 50), 50, "Red")
    canvas.draw_text("PLAYER'S HAND:", (80, 370), 30, "Silver")
    canvas.draw_text("DEALER'S HAND:", (80, 150), 30, "Silver")
    canvas.draw_text(str(SCORE), (490, 580), 50, "Gold")
    canvas.draw_text("score:", (360, 580), 50, "Gold")
    
    # conditional draws:
    if IN_PLAY == True:
        canvas.draw_text("(HIT OR STAND?)", (320, 50), 30, "Blue")
        canvas.draw_polygon([(92, 178), (92, 278), (160, 278), (160, 178)], 5, 'Green', 'Red')
        canvas.draw_text("?", (106, 258), 100, "Green")
    elif IN_PLAY == False:
        canvas.draw_text("(NEW DEAL?)", (320, 50), 30, "Blue")
        canvas.draw_text(GLOBAL_MESSAGE, (10, 105), 30, "Blue")
        

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