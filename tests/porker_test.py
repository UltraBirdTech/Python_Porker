# [USAGE]: python -m unittest tests/porker_test.py
import unittest

from porker import Card
from porker import Deck
from porker import Player
from porker import Hand
from porker import PorkerHand
from porker import Check
from porker import StraightFlash
from porker import Flash
from porker import Straight
from porker import FourCard
from porker import FullHouse
from porker import ThreeCard
from porker import TwoPair
from porker import OnePair
from porker import Peke


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('♠︎', 'A')
        self.card2 = Card('♣︎', '2')
        self.card3 = Card('♦︎', 'K')
        self.card4 = Card('♥', '10')

    def test_set_card_number(self):
        self.assertEqual(self.card1.num, 'A')
        self.assertEqual(self.card2.num, '2')
        self.assertEqual(self.card3.num, 'K')
        self.assertEqual(self.card4.num, '10')

    def test_set_card_suit(self):
        self.assertEqual(self.card1.suit, '♠︎')
        self.assertEqual(self.card2.suit, '♣︎')
        self.assertEqual(self.card3.suit, '♦︎')
        self.assertEqual(self.card4.suit, '♥')

    def test_set_card_value(self):
        self.assertEqual(self.card1.value, '♠︎A')
        self.assertEqual(self.card2.value, '♣︎2')
        self.assertEqual(self.card3.value, '♦︎K')
        self.assertEqual(self.card4.value, '♥10')

    def test_card_number(self):
        self.assertEqual(self.card1.card_number(), 1)
        self.assertEqual(self.card2.card_number(), 2)
        self.assertEqual(self.card3.card_number(), 13)
        self.assertEqual(self.card4.card_number(), 10)


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_check_deck_num(self):
        # ['♠︎', '♣︎', '♦︎', '♥''] * [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
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
        hand = self.player.hand
        self.assertEqual(len(hand.all()), hand.max_hand)  # max_hand is 5

        self.player.draw(self.deck)
        self.assertEqual(len(self.deck.deck_list), deck_list_num - 1)
        hand = self.player.hand
        self.assertEqual(len(hand.all()), hand.max_hand + 1)

    def test_cut(self):
        hand = self.player.hand
        self.assertEqual(len(hand.all()), hand.max_hand)  # max_hand is 5
        self.player.cut(0)
        self.assertEqual(len(hand.all()), hand.max_hand - 1)

    # mock method
    def input(self):
        print('input function is mocked')
        return '0'

    def test_exchange(self):
        hand = self.player.hand
        self.assertEqual(len(hand.all()), hand.max_hand)
        # self.player.exchange(self.deck)
        self.assertEqual(len(hand.all()), hand.max_hand)

    def test_print_usage(self):
        pass

    def test_check_input_value(self):
        pass

    def test_print_my_hand(self):
        pass

    def test_print_result(self):
        pass

    def test_check_porker_hand(self):
        pass


class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand()

    def initialize_hand(self):
        self.hand.hand += ([
            Card('♠', 'A'),
            Card('♣︎', '2'),
            Card('♦︎', 'K'),
            Card('♥', '10'),
            Card('♠', 'J')
        ])

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

    def test_check_porker_hand(self):
        self.initialize_hand()
        self.hand.check_porker_hand()
        self.assertEqual(type(self.hand.porker_hand), type(Peke()))

    def test_get_numbers(self):
        self.initialize_hand()
        numbers = self.hand.get_numbers()
        for num in numbers:
            self.assertEqual(type(num), str)
        self.assertEqual(numbers, ['A', '2', 'K', '10', 'J'])

    def test_get_numbers_as_int(self):
        self.initialize_hand()
        numbers = self.hand.get_numbers_as_int()
        for num in numbers:
            self.assertEqual(type(num), int)
        self.assertEqual(numbers, [1, 2, 13, 10, 11])

    def test_get_suits(self):
        self.initialize_hand()
        suits = self.hand.get_all_suits()
        for suit in suits:
            self.assertEqual(type(suit), str)
        self.assertEqual(suits, ['♠', '♣︎', '♦︎', '♥', '♠'])

class TestCheck(unittest.TestCase):
    def setUp(self):
        self.check = Check()

        deck = Deck()
        player = Player(deck)
        self.hand = player.hand

    def initialize_hand(self):
        self.hand.hand = ([
            Card('♠', 'A'),
            Card('♣︎', '2'),
            Card('♦︎', 'K'),
            Card('♥', '10'),
            Card('♠', 'J')
        ])

    def test_initialize_porker_hands(self):
        self.check.initialize_porker_hands()
        self.assertEqual(type(self.check.straight_flash), type(StraightFlash()))
        self.assertEqual(type(self.check.flash), type(Flash()))
        self.assertEqual(type(self.check.straight), type(Straight()))
        self.assertEqual(type(self.check.four_card), type(FourCard()))
        self.assertEqual(type(self.check.full_house), type(FullHouse()))
        self.assertEqual(type(self.check.three_card), type(ThreeCard()))
        self.assertEqual(type(self.check.two_pair), type(TwoPair()))
        self.assertEqual(type(self.check.one_pair), type(OnePair()))
        self.assertEqual(type(self.check.peke), type(Peke()))

    def test_check(self):
        self.initialize_hand()
        self.hand.print_my_hand()
        self.assertEqual(type(self.check.check(self.hand)), type(Peke()))
        

# Check Porker Hand class
class TestPorkerHand(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand

    def test_initialize(self):
        porker_hand = PorkerHand('Test')
        self.assertEqual(porker_hand.result, False)
        self.assertEqual(porker_hand.porker_hand, 'Test')

    def test_check_conditions(self):
        pass

    def test_check(self):
        pass

    def display(self):
        pass

class TestStraightFlash(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand

        self.straight_flash = StraightFlash()
        self.flash = Flash()
        self.straight = Straight()

    def test_initialize(self):
        self.assertEqual(self.straight_flash.result, False)
        self.assertEqual(self.straight_flash.porker_hand, 'StraightFlash')

    def test_check_is_True(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♠︎', '2'),
                             Card('♠︎', '3'),
                             Card('♠︎', '4'),
                             Card('♠︎', '5')]
        
        self.flash.check(self.hand)
        self.straight.check(self.hand)
        self.straight_flash.check(self.hand, self.flash.result, self.straight.result)
        self.assertEqual(self.straight_flash.result, True)
    
    def test_check_is_False(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♦', '3'),
                             Card('♠︎', '5'),
                             Card('♦', '7'),
                             Card('♠︎', '9')]
        self.flash.check(self.hand)
        self.straight.check(self.hand)
        self.straight_flash.check(self.hand, self.flash.result, self.straight.result)
        self.assertEqual(self.straight_flash.result, False)

    def test_check_royal_straight_flash(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♠︎', '10'),
                             Card('♠︎', 'J'),
                             Card('♠︎', 'Q'),
                             Card('♠︎', 'K')]
        
        self.flash.check(self.hand)
        self.straight.check(self.hand)
        self.straight_flash.check(self.hand, self.flash.result, self.straight.result)
        self.assertEqual(self.straight_flash.result, True)
        self.assertEqual(self.straight_flash.porker_hand, 'RoyalStraightFlash')
        self.assertEqual(self.straight_flash.is_royal(self.hand), True)

    def test_is_royal_true(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♠︎', '10'),
                             Card('♠︎', 'J'),
                             Card('♠︎', 'Q'),
                             Card('♠︎', 'K')]
        self.assertEqual(self.straight_flash.is_royal(self.hand), True)

    def test_is_royal_false(self):
        self.hand.hand =    [Card('♠︎', '9'),
                             Card('♠︎', '10'),
                             Card('♠︎', 'J'),
                             Card('♠︎', 'Q'),
                             Card('♠︎', 'K')]
        self.assertEqual(self.straight_flash.is_royal(self.hand), False)


class TestFlash(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.flash = Flash()

    def test_initialize(self):
        self.assertEqual(self.flash.result, False)
        self.assertEqual(self.flash.porker_hand, 'Flash')

    def test_check_is_True(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♠︎', '3'),
                             Card('♠︎', '5'),
                             Card('♠︎', '7'),
                             Card('♠︎', '9')]
        self.flash.check(self.hand)
        self.assertEqual(self.flash.result, True)
    
    def test_check_is_False(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♦', '3'),
                             Card('♠︎', '5'),
                             Card('♦', '7'),
                             Card('♠︎', '9')]
        self.flash.check(self.hand)
        self.assertEqual(self.flash.result, False)

class TestStraight(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.straight = Straight()

    def test_initialize(self):
        self.assertEqual(self.straight.result, False)
        self.assertEqual(self.straight.porker_hand, 'Straight')

    def test_check_is_True(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♦', '2'),
                             Card('♠︎', '3'),
                             Card('♠︎', '4'),
                             Card('♠︎', '5')]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, True)

    def test_check_is_True_first_10(self):
        self.hand.hand =    [Card('♠︎', '10'),
                             Card('♦', 'J'),
                             Card('♠︎', 'Q'),
                             Card('♠︎', 'K'),
                             Card('♠︎', 'A')]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, True)
    
    def test_check_is_False(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♦', '3'),
                             Card('♠︎', '5'),
                             Card('♦', '7'),
                             Card('♠︎', '9')]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, False)

class TestFourCard(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.four_card = FourCard()

    def test_initialize(self):
        self.assertEqual(self.four_card.result, False)
        self.assertEqual(self.four_card.porker_hand, 'FourCard')

    def test_check_is_True(self):
        self.hand.hand =    [Card('♠︎', '3'),
                             Card('♣︎', '3'),
                             Card('♦︎', '3'),
                             Card('♥', '3'),
                             Card('♠︎', '9')]
        self.four_card.check(self.hand)
        self.assertEqual(self.four_card.result, True)
    
    def test_check_is_False(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♦', '3'),
                             Card('♠︎', '5'),
                             Card('♦', '7'),
                             Card('♠︎', '9')]
        self.four_card.check(self.hand)
        self.assertEqual(self.four_card.result, False)

class TestThreeCard(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.three_card = ThreeCard()

    def test_initialize(self):
        self.assertEqual(self.three_card.result, False)
        self.assertEqual(self.three_card.porker_hand, 'ThreeCard')

    def test_check_is_True(self):
        self.hand.hand =    [Card('♠︎', '3'),
                             Card('♣︎', '3'),
                             Card('♦︎', '3'),
                             Card('♥', '4'),
                             Card('♠︎', '9')]
        self.three_card.check(self.hand)
        self.assertEqual(self.three_card.result, True)
    
    def test_check_is_False(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♦', '3'),
                             Card('♠︎', '5'),
                             Card('♦', '7'),
                             Card('♠︎', '9')]
        self.three_card.check(self.hand)
        self.assertEqual(self.three_card.result, False)

class TestFulleHouse(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.full_house = FullHouse()
        
        self.three_card = ThreeCard()
        self.one_pair = OnePair()

    def test_initialize(self):
        self.assertEqual(self.full_house.result, False)
        self.assertEqual(self.full_house.porker_hand, 'FullHouse')  

    def test_check_is_True(self):
        self.hand.hand =   [Card('♠︎', '3'),
                            Card('♣︎', '3'),
                            Card('♦︎', '5'),
                            Card('♥', '5'),
                            Card('♠︎', '5')]
        self.three_card.check(self.hand)
        self.one_pair.check(self.hand)       
        self.full_house.check(self.hand, self.one_pair.result , self.three_card.result) 
        self.assertEqual(self.full_house.result, True)
    
    def test_check_is_False(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♦', '3'),
                             Card('♠︎', '5'),
                             Card('♦', '7'),
                             Card('♠︎', '9')]
        self.three_card.check(self.hand)
        self.one_pair.check(self.hand)       
        self.full_house.check(self.hand, self.one_pair.result , self.three_card.result) 
        self.assertEqual(self.full_house.result, False)

class TestTwoPair(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.two_pair = TwoPair()

    def test_initialize(self):
        self.assertEqual(self.two_pair.result, False)
        self.assertEqual(self.two_pair.porker_hand, 'TwoPair')

    def test_check_is_True(self):
        self.hand.hand =    [Card('♠︎', '3'),
                             Card('♣︎', '3'),
                             Card('♦︎', '5'),
                             Card('♥', '5'),
                             Card('♠︎', '9')]
        self.two_pair.check(self.hand)
        self.assertEqual(self.two_pair.result, True)
    
    def test_check_is_False(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♦', '3'),
                             Card('♠︎', '5'),
                             Card('♦', '7'),
                             Card('♠︎', '9')]
        self.two_pair.check(self.hand)
        self.assertEqual(self.two_pair.result, False)

    def test_check_is_False_when_one_pair(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♦', 'A'),
                             Card('♠︎', '3'),
                             Card('♦', '5'),
                             Card('♠︎', '9')]
        self.two_pair.check(self.hand)
        self.assertEqual(self.two_pair.result, False)

class TestOnePair(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.one_pair = OnePair()

    def test_initialize(self):
        self.assertEqual(self.one_pair.result, False)
        self.assertEqual(self.one_pair.porker_hand, 'OnePair')

    def test_check_is_True(self):
        self.hand.hand =    [Card('♠︎', '3'),
                             Card('♣︎', '3'),
                             Card('♦︎', '5'),
                             Card('♥', '4'),
                             Card('♠︎', '9')]
        self.one_pair.check(self.hand)
        self.assertEqual(self.one_pair.result, True)
    
    def test_check_is_False(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♦', '3'),
                             Card('♠︎', '5'),
                             Card('♦', '7'),
                             Card('♠︎', '9')]
        self.one_pair.check(self.hand)
        self.assertEqual(self.one_pair.result, False)

    def test_check_is_False_when_two_pair(self):
        self.hand.hand =    [Card('♠︎', 'A'),
                             Card('♦', 'A'),
                             Card('♠︎', '5'),
                             Card('♦', '5'),
                             Card('♠︎', '9')]
        self.one_pair.check(self.hand)
        self.assertEqual(self.one_pair.result, False)

class TestPeke(unittest.TestCase):
    def setUp(self):
        self.peke = Peke()

    def test_initialize(self):
        self.assertEqual(self.peke.porker_hand, 'PEKE')
