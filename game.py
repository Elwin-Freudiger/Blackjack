import random
from math import *

class Deck():
    def __init__(self, deck_num = 1):
        self.deck_num = deck_num

    def deck_creation(self):
        colors = ["hearts", "diamonds", "spade", "clubs"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        all_values = values * self.deck_num
        self.cards = [(card, category) for category in colors for card in all_values]

    def shuffle(self):
        random.shuffle(self.cards)
        self.cut = random.int((52*self.deck_num*0.25), (52*self.deck_num*0.75))
    
    def reshuffle_needed(self):
        if len(self.cards) <= self.cut or len(self.cards)<1:
            self.deck_creation()
            self.shuffle()
    
    
    def dealing(self):
        card = self.cards.pop(0)
        return card
    
test = Deck(1)
test.deck_creation()
test.shuffle()
test.reshuffle_needed()




