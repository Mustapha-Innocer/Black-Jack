import random
from .card import Card
from .rank import Ranks
from .suit import Suits


class Deck:
    def __init__(self):
        self.cards = [Card(suit.name, rank) for suit in Suits for rank in Ranks.__members__.items()]

    def shuffle(self):
        return random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)
