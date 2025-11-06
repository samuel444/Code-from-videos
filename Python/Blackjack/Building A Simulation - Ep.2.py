import random
import numpy as np
from matplotlib import pyplot as plt


deck = ['AH','AS','AD','AC','2H','2S','2D','2C','3H','3S','3D','3C','4H','4S','4D','4C','5H','5S','5D','5C','6H','6S','6D','6C','7H','7S','7D','7C','8H','8S','8D','8C','9H','9S','9D','9C','10H','10S','10D','10C','JH','JS','JD','JC','QH','QS','QD','QC','KH','KS','KD','KC']

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

    return cardsLeft, money


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
