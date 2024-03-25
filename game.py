import random as rand
from math import *

values = {"Ace": 11, "2": 2, "3": 3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}
BJ_payout = 1.5
spread = 10


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
    
    def get_card(self, card):
        self.hand.append(card)

    def get_value(self):
        self.value = 0
        aces = 0
        for card in self.hand:
            self.value += values[card]
            if card == 'Ace':
                aces += 1
        if self.value > 21 & aces > 0:
            self.value -= 10
            aces -= 1
        return self.value
    
    def reset_hand(self):
        self.hand = []

class Player(object):
    def __init__(self, balance):
        self.balance = balance
        self.bet = 0
        self.choice = None
    
    def get_balance(self):
        print('Your balance is:',self.balance)
    
    def win(self):
        self.balance += self.bet

    def bj_win(self):
        self.balance += (BJ_payout*self.bet)
    
    def loss(self):
        self.balance -= self.bet
    
    def place_bet(self, bet):
        while True:
            try:
                if bet > self.balance:
                    print('Not enough money')
                else:
                    self.bet = bet
                    break
            except ValueError:
                print('This is not a number')


class Blackjack_input(object):
    def __init__(self, decks, money):
        self.deck = decks
        self.money = money
        

    def play_game(self):
        deck = Deck(self.deck)
        deck.deck_creation()
        deck.shuffle()
        print('Welcome to the blackjack game')
        while True:
            b = input('Please enter the amount of money you will would like to bet: ')

            choice = input('Would you like to keep playing? (y/n)')
            if choice.lower() == 'n':
                break
