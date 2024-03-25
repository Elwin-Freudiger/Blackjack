import random as rand
from math import *

value = {"Ace": 11, "2": 2, "3": 3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}

class Deck():
    def __init__(self, deck_num = 1):
        self.deck_num = deck_num

    def deck_creation(self):
        colors = ["hearts", "diamonds", "spade", "clubs"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        all_values = values * self.deck_num
        self.cards = [(card, category) for category in colors for card in all_values]

    def shuffle(self):
        rand.shuffle(self.cards)
        self.cut = rand.randint((52*self.deck_num*0.25), (52*self.deck_num*0.75))
    
    def reshuffle_needed(self):
        if len(self.cards) <= self.cut or len(self.cards)<1:
            self.deck_creation()
            self.shuffle()
    
    
    def dealing(self):
        card = self.cards.pop(0)
        return card
    
class Cards():
    def __init__(self, name, value=0):
        self.name = name
        self.value = value
    
    def __str__(self):
        return "%s of %s" % (self.name[0], self.name[1])

class Hand:
    def __init__(self):
        self.hand = []
    
    def value(self, hand):
        value = 0
    
    def reset_hand(self):
        self.hand = []