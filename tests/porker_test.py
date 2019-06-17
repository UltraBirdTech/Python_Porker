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


    def test_set_card_suit(self):
        self.assertEqual(self.card1.suit, '♠︎')
        self.assertEqual(self.card2.suit, '♣︎')
        self.assertEqual(self.card3.suit, '♦︎')
        self.assertEqual(self.card4.suit, '♡')

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
        # ['♠︎', '♣︎', '♦︎', '♡''] * [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
        self.assertEqual(len(self.deck.deck_list), 4 * 13)

    def test_draw(self):
        self.assertEqual(type(self.deck.draw()), type(Card('♠︎', 'A')))
        self.assertEqual(len(self.deck.deck_list), ((4 * 13) - 1))

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.player = Player(self.deck)

    def test_player_initialize(self):
        self.assertEqual(type(self.player.hand), type(Hand()))

    def test_draw(self):
        deck_list_num = len(self.deck.deck_list)
        self.assertEqual(len(self.player.hand.all()), self.player.hand.max_hand) # max_hand is 5

        self.player.draw(self.deck)
        self.assertEqual(len(self.deck.deck_list), deck_list_num - 1)
        self.assertEqual(len(self.player.hand.all()), self.player.hand.max_hand + 1)

    def test_cut(self):
        self.assertEqual(len(self.player.hand.all()), self.player.hand.max_hand) # max_hand is 5
        self.player.cut(0)
        self.assertEqual(len(self.player.hand.all()), self.player.hand.max_hand - 1)

    # mock method
    def input(self):
        print('input function is mocked')
        return '0'

    def test_exchange(self):
        self.assertEqual(len(self.player.hand.all()), self.player.hand.max_hand)
        #self.player.exchange(self.deck)
        self.assertEqual(len(self.player.hand.all()), self.player.hand.max_hand)

    def test_print_my_hand(self):
        pass

    def test_print_result(self):
        pass

    def test_check_porker_hand(self):
        pass

class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand()

    def test_hand_initialize(self):
        self.assertEqual(self.hand.max_hand, 5)
        self.assertEqual(type(self.hand.hand), type([]))

    def test_add(self):
        self.assertEqual(len(self.hand.hand), 0)
        self.hand.add(Card('♠︎', '1'))
        self.assertEqual(len(self.hand.hand), 1)
    
    def test_cut(self):
        self.hand.add(Card('♠︎', '1'))
        self.assertEqual(len(self.hand.hand), 1)
        self.hand.cut(0)
        self.assertEqual(len(self.hand.hand), 0)
    
    def test_all(self):
        self.assertEqual(type(self.hand.hand), type([]))

    def test_print_hand(self):
        pass

    def test_get_number(self):
        pass
