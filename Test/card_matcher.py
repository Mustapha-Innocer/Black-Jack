from Deck.card import Card


class CardMatcher:
    expected: Card

    def __init__(self, expected):
        self.expected = expected

    def __eq__(self, other):
        return self.expected.suit == other.suit and \
               self.expected.rank == other.rank and \
               self.expected.value == other.value