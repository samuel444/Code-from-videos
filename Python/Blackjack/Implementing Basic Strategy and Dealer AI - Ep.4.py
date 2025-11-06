import random
import numpy as np
from matplotlib import pyplot as plt


deck = ['AH','AS','AD','AC','2H','2S','2D','2C','3H','3S','3D','3C','4H','4S','4D','4C','5H','5S','5D','5C','6H','6S','6D','6C','7H','7S','7D','7C','8H','8S','8D','8C','9H','9S','9D','9C','10H','10S','10D','10C','JH','JS','JD','JC','QH','QS','QD','QC','KH','KS','KD','KC']
hard_strategy = {
    # Hard Totals
    (9, '2'): 'hit', (9, '3'): 'double', (9, '4'): 'double', (9, '5'): 'double', (9, '6'): 'double',
    (9, '7'): 'hit', (9, '8'): 'hit', (9, '9'): 'hit', (9, '10'): 'hit', (9, 'J'): 'hit', (9, 'Q'): 'hit', (9, 'K'): 'hit', (9, 'A'): 'hit',

    (10, '2'): 'double', (10, '3'): 'double', (10, '4'): 'double', (10, '5'): 'double', (10, '6'): 'double',
    (10, '7'): 'double', (10, '8'): 'double', (10, '9'): 'double', (10, '10'): 'hit', (10, 'J'): 'hit', (10, 'Q'): 'hit', (10, 'K'): 'hit', (10, 'A'): 'hit',

    (11, '2'): 'double', (11, '3'): 'double', (11, '4'): 'double', (11, '5'): 'double', (11, '6'): 'double',
    (11, '7'): 'double', (11, '8'): 'double', (11, '9'): 'double', (11, '10'): 'double', (11, 'J'): 'double', (11, 'Q'): 'double', (11, 'K'): 'double', (11, 'A'): 'double',

    (12, '2'): 'hit', (12, '3'): 'hit', (12, '4'): 'stand', (12, '5'): 'stand', (12, '6'): 'stand',
    (12, '7'): 'hit', (12, '8'): 'hit', (12, '9'): 'hit', (12, '10'): 'hit', (12, 'J'): 'hit', (12, 'Q'): 'hit', (12, 'K'): 'hit', (12, 'A'): 'hit',

    (13, '2'): 'stand', (13, '3'): 'stand', (13, '4'): 'stand', (13, '5'): 'stand', (13, '6'): 'stand',
    (13, '7'): 'hit', (13, '8'): 'hit', (13, '9'): 'hit', (13, '10'): 'hit', (13, 'J'): 'hit', (13, 'Q'): 'hit', (13, 'K'): 'hit', (13, 'A'): 'hit',

    (14, '2'): 'stand', (14, '3'): 'stand', (14, '4'): 'stand', (14, '5'): 'stand', (14, '6'): 'stand',
    (14, '7'): 'hit', (14, '8'): 'hit', (14, '9'): 'hit', (14, '10'): 'hit', (14, 'J'): 'hit', (14, 'Q'): 'hit', (14, 'K'): 'hit', (14, 'A'): 'hit',

    (15, '2'): 'stand', (15, '3'): 'stand', (15, '4'): 'stand', (15, '5'): 'stand', (15, '6'): 'stand',
    (15, '7'): 'hit', (15, '8'): 'hit', (15, '9'): 'hit', (15, '10'): 'hit', (15, 'J'): 'hit', (15, 'Q'): 'hit', (15, 'K'): 'hit', (15, 'A'): 'hit',

    (16, '2'): 'stand', (16, '3'): 'stand', (16, '4'): 'stand', (16, '5'): 'stand', (16, '6'): 'stand',
    (16, '7'): 'hit', (16, '8'): 'hit', (16, '9'): 'hit', (16, '10'): 'hit', (16, 'J'): 'hit', (16, 'Q'): 'hit', (16, 'K'): 'hit', (16, 'A'): 'hit',

    (17, '2'): 'stand', (17, '3'): 'stand', (17, '4'): 'stand', (17, '5'): 'stand', (17, '6'): 'stand',
    (17, '7'): 'stand', (17, '8'): 'stand', (17, '9'): 'stand', (17, '10'): 'stand', (17, 'J'): 'stand', (17, 'Q'): 'stand', (17, 'K'): 'stand', (17, 'A'): 'stand',

    (18, '2'): 'stand', (18, '3'): 'stand', (18, '4'): 'stand', (18, '5'): 'stand', (18, '6'): 'stand',
    (18, '7'): 'stand', (18, '8'): 'stand', (18, '9'): 'stand', (18, '10'): 'stand', (18, 'J'): 'stand', (18, 'Q'): 'stand', (18, 'K'): 'stand', (18, 'A'): 'stand',

    (19, '2'): 'stand', (19, '3'): 'stand', (19, '4'): 'stand', (19, '5'): 'stand', (19, '6'): 'stand',
    (19, '7'): 'stand', (19, '8'): 'stand', (19, '9'): 'stand', (19, '10'): 'stand', (19, 'J'): 'stand', (19, 'Q'): 'stand', (19, 'K'): 'stand', (19, 'A'): 'stand',

    (20, '2'): 'stand', (20, '3'): 'stand', (20, '4'): 'stand', (20, '5'): 'stand', (20, '6'): 'stand',
    (20, '7'): 'stand', (20, '8'): 'stand', (20, '9'): 'stand', (20, '10'): 'stand', (20, 'J'): 'stand', (20, 'Q'): 'stand', (20, 'K'): 'stand', (20, 'A'): 'stand',

    (21, '2'): 'stand', (21, '3'): 'stand', (21, '4'): 'stand', (21, '5'): 'stand', (21, '6'): 'stand',
    (21, '7'): 'stand', (21, '8'): 'stand', (21, '9'): 'stand', (21, '10'): 'stand', (21, 'J'): 'stand', (21, 'Q'): 'stand', (21, 'K'): 'stand', (21, 'A'): 'stand',

}

soft_strategy = {
    (13, '2'): 'hit', (13, '3'): 'hit', (13, '4'): 'hit', (13, '5'): 'double', (13, '6'): 'double',
    (13, '7'): 'hit', (13, '8'): 'hit', (13, '9'): 'hit', (13, '10'): 'hit', (13, 'J'): 'hit', (13, 'Q'): 'hit', (13, 'K'): 'hit', (13, 'A'): 'hit',
    
    (14, '2'): 'hit', (14, '3'): 'hit', (14, '4'): 'hit', (14, '5'): 'double', (14, '6'): 'double',
    (14, '7'): 'hit', (14, '8'): 'hit', (14, '9'): 'hit', (14, '10'): 'hit', (14, 'J'): 'hit', (14, 'Q'): 'hit', (14, 'K'): 'hit', (14, 'A'): 'hit',

    (15, '2'): 'hit', (15, '3'): 'hit', (15, '4'): 'double', (15, '5'): 'double', (15, '6'): 'double',
    (15, '7'): 'hit', (15, '8'): 'hit', (15, '9'): 'hit', (15, '10'): 'hit', (15, 'J'): 'hit', (15, 'Q'): 'hit', (15, 'K'): 'hit', (15, 'A'): 'hit',

    (16, '2'): 'hit', (16, '3'): 'hit', (16, '4'): 'double', (16, '5'): 'double', (16, '6'): 'double',
    (16, '7'): 'hit', (16, '8'): 'hit', (16, '9'): 'hit', (16, '10'): 'hit', (16, 'J'): 'hit', (16, 'Q'): 'hit', (16, 'K'): 'hit', (16, 'A'): 'hit',

    (17, '2'): 'hit', (17, '3'): 'double', (17, '4'): 'double', (17, '5'): 'double', (17, '6'): 'double',
    (17, '7'): 'hit', (17, '8'): 'hit', (17, '9'): 'hit', (17, '10'): 'hit', (17, 'J'): 'hit', (17, 'Q'): 'hit', (17, 'K'): 'hit', (17, 'A'): 'hit',

    (18, '2'): 'stand', (18, '3'): 'stand', (18, '4'): 'stand', (18, '5'): 'stand', (18, '6'): 'stand',
    (18, '7'): 'stand', (18, '8'): 'stand', (18, '9'): 'hit', (18, '10'): 'hit', (18, 'J'): 'hit', (18, 'Q'): 'hit', (18, 'K'): 'hit', (18, 'A'): 'hit',

    (19, '2'): 'stand', (19, '3'): 'stand', (19, '4'): 'stand', (19, '5'): 'stand', (19, '6'): 'stand',
    (19, '7'): 'stand', (19, '8'): 'stand', (19, '9'): 'stand', (19, '10'): 'stand', (19, 'J'): 'stand', (19, 'Q'): 'stand', (19, 'K'): 'stand', (19, 'A'): 'stand',

    (20, '2'): 'stand', (20, '3'): 'stand', (20, '4'): 'stand', (20, '5'): 'stand', (20, '6'): 'stand',
    (20, '7'): 'stand', (20, '8'): 'stand', (20, '9'): 'stand', (20, '10'): 'stand', (20, 'J'): 'stand', (20, 'Q'): 'stand', (20, 'K'): 'stand', (20, 'A'): 'stand',

    (21, '2'): 'stand', (21, '3'): 'stand', (21, '4'): 'stand', (21, '5'): 'stand', (21, '6'): 'stand',
    (21, '7'): 'stand', (21, '8'): 'stand', (21, '9'): 'stand', (21, '10'): 'stand', (21, 'J'): 'stand', (21, 'Q'): 'stand', (21, 'K'): 'stand', (21, 'A'): 'stand',

}

# Draws a card from the deck and updates Hi-Lo 
def takeCard(cardsLeft, hand):
    hand.append(cardsLeft[0])
    del cardsLeft[0]
    return cardsLeft, hand


# Reshuffles a new shoe of n decks
def reshuffle(n):
    cardsLeft = []
    for i in range(n):
        cardsLeft.extend(deck)
    random.shuffle(cardsLeft)
    return cardsLeft


# Initializes a new hand for players and dealer
def newhand(cardsLeft, money):
    global betSize
    blackjack = False
    dealer_blackjack = False
    p = 3  # Number of NPC players

    cards = []
    players = []
    dealer = []

    for i in range(p):
        cards.append([])

     # Determine bet size based on true 
    bet = betSize

    # Deal initial cards
    for i in range(2):
        cardsLeft, players = takeCard(cardsLeft, players)
        for j in range(p):
            cardsLeft, cards[j] = takeCard(cardsLeft, cards[j])
        cardsLeft, dealer = takeCard(cardsLeft, dealer)

    
    

    # Offer insurance if dealer shows Ace
    takeInsurance = False
    if dealer[0][0] == 'A':    
        takeInsurance = False

    dealerInitialVal, soft = value(dealer)
    if dealerInitialVal == 21:
        dealer_blackjack = True

    # Check for player's blackjack
    initialVal, soft = value(players)
    if initialVal == 21 and len(players) == 2:
        blackjack = True
        if not dealer_blackjack:
            money += (bet * 1.5)
        doubled_down = False
    if not blackjack and dealer_blackjack:
        money -= bet
    if not dealer_blackjack and not blackjack:
        bets = bet
        amount = 0
        doubled_down = False

        amount, cardsLeft, doubled_down = player(cardsLeft, players, dealer[0])
        if doubled_down:
            bets *= 2

    if not dealer_blackjack:
        # Play NPC hands
        for i in range(p):
            cardsLeft  = npc(cardsLeft, cards[i], dealer[0])

        # Dealer's turn
        done = False
        while not done:
            valuation, soft = value(dealer)
            if valuation < 17 or (soft and valuation < 18):
                cardsLeft, dealer = takeCard(cardsLeft, dealer)
            else:
                done = True

        # Resolve outcomes
        if not blackjack:
            for i in range(len(players)):
                if (amount > valuation or valuation > 21) and amount <= 21:
                    money += bets
                elif amount == valuation and amount <= 21:
                    pass  # push
                else:
                    money -= bets
    if takeInsurance:
        if dealer[1][:-1] in ['10', 'J', 'K', 'Q']:
            money += bet
        else:
            money -= bet/2
    return cardsLeft, money


# Handles player's turn based on strategy
def player(cardsLeft, hand, dealer):
    while True:
        valuation, soft = value(hand)

        if valuation > 21:
            return valuation, cardsLeft, False


        action = ''
        key = (valuation, dealer[:-1])
        if not soft:
            try:
                action = hard_strategy[key]
            except KeyError:
                pass
        else:
            try:
                action = soft_strategy[key]
            except KeyError:
                pass
        
            

        if (action == 'double' and len(hand) > 2) or action == '':
            action = 'hit'

        

        if action == 'hit':
            cardsLeft, hand  = takeCard(cardsLeft, hand)
        elif action == 'stand':
            return valuation, cardsLeft, False
        elif action == 'double':
            cardsLeft, hand  = takeCard(cardsLeft, hand)
            valuation, soft = value(hand)
            return valuation, cardsLeft, True


# Simulates NPC strategy
def npc(cardsLeft, hand, dealer):
    while True:
        valuation, soft = value(hand)

        if valuation > 21:
            return cardsLeft

        key = (valuation, dealer[:-1])
        if not soft:
            try:
                action = hard_strategy[key]
            except KeyError:
                action = 'hit'
        else:
            try:
                action = soft_strategy[key]
            except KeyError:
                action = 'hit'

        if action == 'hit':
            cardsLeft, hand  = takeCard(cardsLeft, hand)
        elif action == 'stand':
            return cardsLeft
        elif action == 'double':
            cardsLeft, hand  = takeCard(cardsLeft, hand)
            return cardsLeft



# Returns the total value and whether it's a soft hand
def value(hand):
    totals = 0
    aces = 0

    for card in hand:
        rank = card[:-1]
        if rank == 'A':
            totals += 11
            aces += 1
        elif rank in ['K', 'Q', 'J']:
            totals += 10
        else:
            totals += int(rank)

    while totals > 21 and aces > 0:
        totals -= 10
        aces -= 1

    soft = len(hand) == 2 and (aces == 1)
    return totals, soft


# Starts a new simulation
def start():
    m = 100000  # Starting money
    n = 6      # Number of decks
    return n, m


decks, money = start()
cardsLeft = reshuffle(decks)

repetitions = 1000000
betSize = 10

rep = 0
while rep <= repetitions and money > 0:
    rep += 1
    if len(cardsLeft) <= (decks * 52 * 0.2):
        cardsLeft = reshuffle(decks)
    cardsLeft, money = newhand(cardsLeft,money)

print ("After", rep, "runs the resulting money is $" + str(money) + " from $100,000")
