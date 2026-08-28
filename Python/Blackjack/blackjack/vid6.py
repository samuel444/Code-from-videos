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

split_strategy = {
    (2, '2'): 'no', (2, '3'): 'no', (2, '4'): 'yes', (2, '5'): 'yes', (2, '6'): 'yes',
    (2, '7'): 'yes', (2, '8'): 'no', (2, '9'): 'no', (2, '10'): 'no', (2, 'J'): 'no', (2, 'Q'): 'no', (2, 'K'): 'no', (2, 'A'): 'no',

    (3, '2'): 'no', (3, '3'): 'no', (3, '4'): 'yes', (3, '5'): 'yes', (3, '6'): 'yes',
    (3, '7'): 'yes', (3, '8'): 'no', (3, '9'): 'no', (3, '10'): 'no', (3, 'J'): 'no', (3, 'Q'): 'no', (3, 'K'): 'no', (3, 'A'): 'no',

    (4, '2'): 'no', (4, '3'): 'no', (4, '4'): 'no', (4, '5'): 'no', (4, '6'): 'yes',
    (4, '7'): 'no', (4, '8'): 'no', (4, '9'): 'no', (4, '10'): 'no', (4, 'J'): 'no', (4, 'Q'): 'no', (4, 'K'): 'no', (4, 'A'): 'no',

    (5, '2'): 'no', (5, '3'): 'no', (5, '4'): 'no', (5, '5'): 'no', (5, '6'): 'yes',
    (5, '7'): 'no', (5, '8'): 'no', (5, '9'): 'no', (5, '10'): 'no', (5, 'J'): 'no', (5, 'Q'): 'no', (5, 'K'): 'no', (5, 'A'): 'no',

    (6, '2'): 'yes', (6, '3'): 'yes', (6, '4'): 'yes', (6, '5'): 'yes', (6, '6'): 'yes',
    (6, '7'): 'no', (6, '8'): 'no', (6, '9'): 'no', (6, '10'): 'no', (6, 'J'): 'no', (6, 'Q'): 'no', (6, 'K'): 'no', (6, 'A'): 'no',

    (7, '2'): 'yes', (7, '3'): 'yes', (7, '4'): 'yes', (7, '5'): 'yes', (7, '6'): 'yes',
    (7, '7'): 'yes', (7, '8'): 'no', (7, '9'): 'no', (7, '10'): 'no', (7, 'J'): 'no', (7, 'Q'): 'no', (7, 'K'): 'no', (7, 'A'): 'no',

    (8, '2'): 'yes', (8, '3'): 'yes', (8, '4'): 'yes', (8, '5'): 'yes', (8, '6'): 'yes',
    (8, '7'): 'yes', (8, '8'): 'yes', (8, '9'): 'yes', (8, '10'): 'yes', (8, 'J'): 'yes', (8, 'Q'): 'yes', (8, 'K'): 'yes', (8, 'A'): 'yes',

    (9, '2'): 'yes', (9, '3'): 'yes', (9, '4'): 'yes', (9, '5'): 'yes', (9, '6'): 'yes',
    (9, '7'): 'no', (9, '8'): 'yes', (9, '9'): 'yes', (9, '10'): 'no', (9, 'J'): 'no', (9, 'Q'): 'no', (9, 'K'): 'no', (9, 'A'): 'no',

    (10, '2'): 'no', (10, '3'): 'no', (10, '4'): 'no', (10, '5'): 'no', (10, '6'): 'no',
    (10, '7'): 'no', (10, '8'): 'no', (10, '9'): 'no', (10, '10'): 'no', (10, 'J'): 'no', (10, 'Q'): 'no', (10, 'K'): 'no', (10, 'A'): 'no',

   (11, '2'): 'yes', (11, '3'): 'yes', (11, '4'): 'yes', (11, '5'): 'yes', (11, '6'): 'yes',
    (11, '7'): 'yes', (11, '8'): 'yes', (11, '9'): 'yes', (11, '10'): 'yes', (11, 'J'): 'yes', (11, 'Q'): 'yes', (11, 'K'): 'yes', (11, 'A'): 'yes'
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
    global money_graph, wins, loss, betSize
    blackjack = False
    dealer_blackjack = False
    p = 3  # Number of NPC players

    cards = []
    players = [[]]
    dealer = []

    for i in range(p):
        cards.append([])

     # Determine bet size based on true 
    bet = betSize

    # Deal initial cards
    for i in range(2):
        cardsLeft, players[0] = takeCard(cardsLeft, players[0])
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
    initialVal, soft = value(players[0])
    if initialVal == 21 and len(players[0]) == 2:
        blackjack = True
        if not dealer_blackjack:
            money += (bet * 1.5)
            wins += 1
        doubled_down = False
    if not blackjack and dealer_blackjack:
        money -= bet
        loss += 1
    if not dealer_blackjack and not blackjack:
        # Handle splitting
        splitting = True
        while splitting:
            check = 0
            for i in range(len(players)):
                if value([players[i][0]]) == value([players[i][1]]):
                    values, soft = value([players[i][0]])
                    key = (values, dealer[0][:-1])
                    try:
                        split = split_strategy[key]
                    except KeyError:
                        pass
                    if split == 'yes':
                        players.append([players[i][1]])
                        players[i] = [players[i][0]]
                        cardsLeft, players[i],  = takeCard(cardsLeft, players[i], )
                        cardsLeft, players[-1],  = takeCard(cardsLeft, players[-1], )
                    else:
                        check += 1
                else:
                    check += 1
                if check == len(players):
                    splitting = False

        # Process each hand
        hands = len(players)
        bets = [bet for _ in range(hands)]
        amount = [0 for _ in range(hands)]
        doubled_down = [False for _ in range(hands)]

        for i in range(len(players)):
            amount[i], cardsLeft, doubled_down[i] = player(cardsLeft, players[i], dealer[0])
            if doubled_down[i]:
                bets[i] *= 2

    if not dealer_blackjack:
        # Play NPC hands
        for i in range(p):
            cardsLeft, fill = npc(cardsLeft, cards[i], dealer[0])

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
                if (amount[i] > valuation or valuation > 21) and amount[i] <= 21:
                    money += bets[i]
                    wins += 1
                elif amount[i] == valuation and amount[i] <= 21:
                    pass  # push
                else:
                    money -= bets[i]
                    loss += 1
    if takeInsurance:
        if dealer[1][:-1] in ['10', 'J', 'K', 'Q']:
            money += bet
        else:
            money -= bet/2
    money_graph.append(money)
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
            return cardsLeft, hand

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
            return cardsLeft, hand
        elif action == 'double':
            cardsLeft, hand  = takeCard(cardsLeft, hand)
            return cardsLeft, hand



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

money_graph = [money]
wins,loss = 0,0
repetitions = 1000000
betSize = 10

rep = 0
while rep <= repetitions and money > 0:
    rep += 1
    if len(cardsLeft) <= (decks * 52 * 0.2):
        cardsLeft = reshuffle(decks)
    cardsLeft, money = newhand(cardsLeft,money)

x_values = [i for i in range(len(money_graph))]
plt.plot(x_values, money_graph)
plt.ylabel('Money ($)')
plt.xlabel('Hands Played')
plt.show() 

winsPercent = int(10000*wins/(wins+loss)) / 100
plt.bar((('Wins\n' + str(winsPercent)+'%'),('Loss\n'+str(100-winsPercent)+'%')),(wins,loss))
plt.ylabel('Frequency')
plt.show()

expected = 100*(money-100000) / (betSize*rep)
if expected < 0:
    print ("From this run you will lose " + str(-1*expected) + "% your bet every hand!")
else:
    print ("From this run you will win " + str(expected) + "% your bet size every hand!")

print ("After", rep, "runs the resulting money is $" + str(money) + " from $100,000")