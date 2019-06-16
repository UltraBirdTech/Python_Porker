# [USAGE]: python -m unittest tests/porker_test.py
import unittest

from porker import Card
from porker import Deck
from porker import Player
from porker import Hand

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('♠︎', 'A')
        self.card2 = Card('♣︎', '2')
        self.card3 = Card('♦︎', 'K')
        self.card4 = Card('♡', '10')

    def test_set_card_number(self):
        self.assertEqual(self.card1.num, 'A')
        self.assertEqual(self.card2.num, '2')
        self.assertEqual(self.card3.num, 'K')
        self.assertEqual(self.card4.num, '10')


    def test_set_card_suite(self):
        self.assertEqual(self.card1.suite, '♠︎')
        self.assertEqual(self.card2.suite, '♣︎')
        self.assertEqual(self.card3.suite, '♦︎')
        self.assertEqual(self.card4.suite, '♡')

    def test_set_card_value(self):
        self.assertEqual(self.card1.value, '♠︎A')
        self.assertEqual(self.card2.value, '♣︎2')
        self.assertEqual(self.card3.value, '♦︎K')
        self.assertEqual(self.card4.value, '♡10')

    def test_card_number(self):
        self.assertEqual(self.card1.card_number(), 1)
        self.assertEqual(self.card2.card_number(), 2)
        self.assertEqual(self.card3.card_number(), 13)
        self.assertEqual(self.card4.card_number(), 10)

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_check_deck_num(self):
        len(self.deck.deck_list) == 4 * 12 # ['♠︎', '♣︎', '♦︎', '♡''] * [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]

    def test_draw(self):
        self.assertEqual(type(self.deck.draw()), type(Card('♠︎', 'A')))
        len(self.deck.deck_list) == ((4 * 12) - 1)

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.player = Player(self.deck)

    def test_player_initialize(self):
        self.assertEqual(type(self.player.hand), type(Hand()))

    def test_draw(self):
        deck_list_num = len(self.deck.deck_list)
        self.assertEqual(len(self.player.hand.all()), 5)
        self.player.draw(self.deck)
        self.assertEqual(len(self.deck.deck_list), deck_list_num - 1)
        self.assertEqual(len(self.player.hand.all()), 6)
