import unittest
from Deck.deck import Deck
from Deck.card import Card
from Deck.suit import Suits
from Deck.rank import Ranks
from card_matcher import CardMatcher
from Player.player import Player


class DeckTest(unittest.TestCase):
    def test_deck_size(self):
        deck = Deck()
        expected_value = 52
        actual_value = len(deck.cards)
        self.assertEqual(actual_value, expected_value)

    def test_card(self):
        deck = Deck()
        expected_card = Card(Suits.Spade.name, Ranks.Two)
        print(expected_card.value)
        actual_card = deck.cards[0]
        print(actual_card.value)
        self.assertEqual(CardMatcher(actual_card), expected_card)


class PlayerTest(unittest.TestCase):
    def test_player(self):
        deck = Deck()
        player = Player(1, deck.deal_card(), deck.deal_card())
        expected_value = 2
        actual_value = len(player.cards)
        self.assertEqual(actual_value, expected_value)

    def test_collect(self):
        deck = Deck()
        player = Player(1, deck.deal_card(), deck.deal_card())
        player.collect(deck.deal_card())
        expected_value = 3
        actual_value = len(player.cards)
        self.assertEqual(actual_value, expected_value)

    def test_total(self):
        card1 = Card(Suits.Spade.name, Ranks.Two)
        card2 = Card(Suits.Spade.name, Ranks.Two)
        player = Player(1, card1, card2)
        expected_value = 4
        actual_value = player.total()
        self.assertEqual(actual_value, expected_value)
