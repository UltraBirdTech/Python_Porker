# [USAGE]: python -m unittest discover -s ./tests -p "*_test.py"
import unittest

from porker import Card
from porker import JokerCard
from porker import Deck
from porker import Player
from porker import Hand
from porker import PorkerHand
from porker import Check
from porker import StraightFlash
from porker import Flash
from porker import Straight
from porker import FiveCard
from porker import FourCard
from porker import FullHouse
from porker import ThreeCard
from porker import TwoPair
from porker import OnePair
from porker import Peke
from porker import JokerStraightFlash
from porker import JokerFlash
from porker import JokerStraight
from porker import JokerStraightFlash
from porker import JokerFiveCard
from porker import JokerFourCard
from porker import JokerThreeCard
from porker import JokerFullHouse
from porker import JokerTwoPair
from porker import JokerOnePair


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

    def test_is_joker(self):
        self.assertFalse(self.card1.is_joker())

    def test_order_number(self):
        self.assertTrue(Card('♥', '6') < Card('♥', '8'))

    def test_order_number_reverse(self):
        self.assertFalse(Card('♥', '8') < Card('♥', '6'))

    def test_order_number_one_than_king(self):
        self.assertTrue(Card('♥', 'K') < Card('♥', '1'))

    def test_order_number_one_than_king_reverse(self):
        self.assertFalse(Card('♥', '1') < Card('♥', 'K'))

    def test_order_number_two_than_king(self):
        self.assertFalse(Card('♥', 'K') < Card('♥', '2'))

    def test_order_number_two_than_king_reverse(self):
        self.assertTrue(Card('♥', '2') < Card('♥', 'K'))

    def test_order_number_one_than_two(self):
        self.assertTrue(Card('♥', '1') > Card('♥', '2'))

    def test_order_number_one_than_two_reverse(self):
        self.assertFalse(Card('♥', '2') < Card('♥', '1'))

    def test_order_number_other_number_than_one(self):
        self.assertTrue(Card('♥', '8') < Card('♥', '1'))

    def test_order_number_other_number_than_one_reverse(self):
        self.assertFalse(Card('♥', '1') < Card('♥', '8'))

    def test_order_number_one_than_two_reverse(self):
        self.assertTrue(Card('♥', '2') < Card('♥', '1'))
 
    def test_order_number_than_king(self):
        self.assertTrue(Card('♥', '8') < Card('♥', 'K'))

    def test_order_number_than_king_reverse(self):
        self.assertFalse(Card('♥', 'K') < Card('♥', '8'))

    def test_order_number_joker(self):
        self.assertFalse(JokerCard() < Card('♥', '10'))

    def test_order_number_joker_reverse(self):
        self.assertFalse(Card('♥', '10') < JokerCard())

class TestJokerCard(unittest.TestCase):
    def setUp(self):
        self.card = JokerCard()

    def test_initialize(self):
        self.assertEqual(self.card.num, 'Joker')
        self.assertEqual(self.card.suit, 'Joker')
        self.assertEqual(self.card.value, 'Joker')
        self.assertEqual(self.card.card_number(), 'Joker')

    def test_is_joker(self):
        self.assertTrue(self.card.is_joker())


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_check_deck_num(self):
        # ['♠︎', '♣︎', '♦︎', '♥''] * [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K] + [Joker]
        self.assertEqual(len(self.deck.deck_list), 4 * 13 + 1)

    def test_draw(self):
        self.assertEqual(type(self.deck.draw()), type(Card('♠︎', 'A')))
        self.assertEqual(len(self.deck.deck_list), ((4 * 13 + 1) - 1))


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

    def test_is_joker(self):
        self.initialize_hand()
        self.hand.cut(0)
        self.hand.add(JokerCard())
        self.assertEqual(self.hand.is_joker(), True)

    def test_is_not_joker(self):
        self.initialize_hand()
        self.assertEqual(self.hand.is_joker(), False)

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
        check_sf = self.check.straight_flash
        self.assertEqual(type(check_sf), type(StraightFlash()))
        self.assertEqual(type(self.check.flash), type(Flash()))
        self.assertEqual(type(self.check.straight), type(Straight()))
        self.assertEqual(type(self.check.five_card), type(FiveCard()))
        self.assertEqual(type(self.check.four_card), type(FourCard()))
        self.assertEqual(type(self.check.full_house), type(FullHouse()))
        self.assertEqual(type(self.check.three_card), type(ThreeCard()))
        self.assertEqual(type(self.check.two_pair), type(TwoPair()))
        self.assertEqual(type(self.check.one_pair), type(OnePair()))
        self.assertEqual(type(self.check.peke), type(Peke()))

    def test_initialize_joker_porker_hands(self):
        self.check.initialize_joker_porker_hands()
        check_sf = self.check.straight_flash
        self.assertEqual(type(check_sf), type(JokerStraightFlash()))
        self.assertEqual(type(self.check.flash), type(JokerFlash()))
        self.assertEqual(type(self.check.straight), type(JokerStraight()))
        self.assertEqual(type(self.check.five_card), type(JokerFiveCard()))
        self.assertEqual(type(self.check.four_card), type(JokerFourCard()))
        self.assertEqual(type(self.check.full_house), type(JokerFullHouse()))
        self.assertEqual(type(self.check.three_card), type(JokerThreeCard()))
        self.assertEqual(type(self.check.two_pair), type(JokerTwoPair()))
        self.assertEqual(type(self.check.one_pair), type(OnePair()))
        self.assertEqual(type(self.check.peke), type(Peke()))

    def test_check(self):
        self.initialize_hand()
        self.assertEqual(type(self.check.check(self.hand)), type(Peke()))

    def test_check_three_card(self):
        self.hand.hand = ([
            Card('♠', 'A'),
            Card('♦︎', 'A'),
            Card('♥', 'A'),
            Card('♥', '10'),
            Card('♠', 'J')
        ])
        self.assertEqual(type(self.check.check(self.hand)), type(ThreeCard()))

    def test_check_four_card(self):
        self.hand.hand = ([
            Card('♠', 'A'),
            Card('♦︎', 'A'),
            Card('♥', 'A'),
            Card('♠', 'A'),
            Card('♥', '10')
        ])
        self.assertEqual(type(self.check.check(self.hand)), type(FourCard()))

    def test_check_five_card(self):
        self.check.initialize_joker_porker_hands()
        self.hand.hand = ([
            Card('♠', 'A'),
            Card('♦︎', 'A'),
            Card('♥', 'A'),
            Card('♠', 'A'),
            JokerCard()
        ])
        self.assertEqual(type(self.check.check(self.hand)), type(JokerFiveCard()))


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
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♠︎', '2'),
                          Card('♠︎', '3'),
                          Card('♠︎', '4'),
                          Card('♠︎', '5')]

        self.flash.check(self.hand)
        self.straight.check(self.hand)
        flash_result = self.flash.result
        straight_result = self.straight.result
        self.straight_flash.check(self.hand, flash_result, straight_result)
        self.assertEqual(self.straight_flash.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          Card('♠︎', '9')]
        self.flash.check(self.hand)
        self.straight.check(self.hand)
        flash_result = self.flash.result
        straight_result = self.straight.result
        self.straight_flash.check(self.hand, flash_result, straight_result)
        self.assertEqual(self.straight_flash.result, False)

    def test_check_royal_straight_flash(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♠︎', '10'),
                          Card('♠︎', 'J'),
                          Card('♠︎', 'Q'),
                          Card('♠︎', 'K')]

        self.flash.check(self.hand)
        self.straight.check(self.hand)
        self.straight_flash.check(self.hand,
                                  self.flash.result,
                                  self.straight.result)
        self.assertEqual(self.straight_flash.result, True)
        self.assertEqual(self.straight_flash.porker_hand, 'RoyalStraightFlash')
        self.assertEqual(self.straight_flash.is_royal(self.hand), True)

    def test_is_royal_true(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♠︎', '10'),
                          Card('♠︎', 'J'),
                          Card('♠︎', 'Q'),
                          Card('♠︎', 'K')]
        self.assertEqual(self.straight_flash.is_royal(self.hand), True)

    def test_is_royal_false(self):
        self.hand.hand = [Card('♠︎', '9'),
                          Card('♠︎', '10'),
                          Card('♠︎', 'J'),
                          Card('♠︎', 'Q'),
                          Card('♠︎', 'K')]
        self.assertEqual(self.straight_flash.is_royal(self.hand), False)

class TestJokerStraightFlash(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand

        self.straight_flash = JokerStraightFlash()
        self.flash = JokerFlash()
        self.straight = JokerStraight()

    def test_initialize(self):
        self.assertEqual(self.straight_flash.result, False)
        self.assertEqual(self.straight_flash.porker_hand, 'StraightFlash')

    def test_check_is_True(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♠︎', '2'),
                          Card('♠︎', '3'),
                          Card('♠︎', '4'),
                          JokerCard()]

        self.flash.check(self.hand)
        self.straight.check(self.hand)
        flash_result = self.flash.result
        straight_result = self.straight.result
        self.straight_flash.check(self.hand, flash_result, straight_result)
        self.assertEqual(self.straight_flash.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          JokerCard()]
        self.flash.check(self.hand)
        self.straight.check(self.hand)
        flash_result = self.flash.result
        straight_result = self.straight.result
        self.straight_flash.check(self.hand, flash_result, straight_result)
        self.assertEqual(self.straight_flash.result, False)

    def test_check_royal_straight_flash(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♠︎', '10'),
                          Card('♠︎', 'J'),
                          Card('♠︎', 'Q'),
                          JokerCard()]

        self.flash.check(self.hand)
        self.straight.check(self.hand)
        self.straight_flash.check(self.hand,
                                  self.flash.result,
                                  self.straight.result)
        self.assertEqual(self.straight_flash.result, True)
        self.assertEqual(self.straight_flash.porker_hand, 'RoyalStraightFlash')
        self.assertEqual(self.straight_flash.is_royal(self.hand), True)

    def test_is_royal_true(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♠︎', '10'),
                          Card('♠︎', 'J'),
                          Card('♠︎', 'Q'),
                          JokerCard()]
        self.assertEqual(self.straight_flash.is_royal(self.hand), True)

    def test_is_royal_false(self):
        self.hand.hand = [Card('♠︎', '9'),
                          Card('♠︎', '10'),
                          Card('♠︎', 'J'),
                          Card('♠︎', 'Q'),
                          JokerCard()]
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
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♠︎', '3'),
                          Card('♠︎', '5'),
                          Card('♠︎', '7'),
                          Card('♠︎', '9')]
        self.flash.check(self.hand)
        self.assertEqual(self.flash.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          Card('♠︎', '9')]
        self.flash.check(self.hand)
        self.assertEqual(self.flash.result, False)

class TestJokerFlash(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.flash = JokerFlash()

    def test_initialize(self):
        self.assertEqual(self.flash.result, False)
        self.assertEqual(self.flash.porker_hand, 'Flash')

    def test_check_is_True(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♠︎', '3'),
                          Card('♠︎', '5'),
                          Card('♠︎', '7'),
                          JokerCard()]
        self.flash.check(self.hand)
        self.assertEqual(self.flash.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          JokerCard()]
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
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '2'),
                          Card('♠︎', '3'),
                          Card('♠︎', '4'),
                          Card('♠︎', '5')]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, True)

    def test_check_is_True_first_10(self):
        self.hand.hand = [Card('♠︎', '10'),
                          Card('♦', 'J'),
                          Card('♠︎', 'Q'),
                          Card('♠︎', 'K'),
                          Card('♠︎', 'A')]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          Card('♠︎', '9')]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, False)

class TestJokerStraight(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.straight = JokerStraight()

    def test_initialize(self):
        self.assertEqual(self.straight.result, False)
        self.assertEqual(self.straight.porker_hand, 'Straight')

    def test_check_is_True_end_joker(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '2'),
                          Card('♠︎', '3'),
                          Card('♠︎', '4'),
                          JokerCard()]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, True)

    def test_check_is_True_start_joker(self):
        self.hand.hand = [JokerCard(),
                          Card('♦', '2'),
                          Card('♠︎', '3'),
                          Card('♠︎', '4'),
                          Card('♠︎', '5'),]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, True)

    def test_check_is_True_between_joker(self):
        self.hand.hand = [Card('♦', '1'),
                          Card('♦', '2'),
                          JokerCard(),
                          Card('♠︎', '4'),
                          Card('♠︎', '5'),]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, True)

    def test_check_is_True_first_10_end_joker(self):
        self.hand.hand = [Card('♠︎', '10'),
                          Card('♦', 'J'),
                          Card('♠︎', 'Q'),
                          Card('♠︎', 'K'),
                          JokerCard()]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, True)

    def test_check_is_True_first_10_but_joker(self):
        self.hand.hand = [JokerCard(),
                          Card('♦', 'J'),
                          Card('♠︎', 'Q'),
                          Card('♠︎', 'K'),
                          Card('♠︎', 'A')]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, True)

    def test_check_is_True_first_10_end_joker(self):
        self.hand.hand = [Card('♠︎', '10'),
                          Card('♦', 'J'),
                          JokerCard(),
                          Card('♠︎', 'K'),
                          Card('♠︎', 'A')]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          JokerCard()]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, False)

    def test_check_is_True_nothing_king(self):
        self.hand.hand = [Card('♠︎', '10'),
                          Card('♦', 'J'),
                          Card('♦', 'Q'),
                          JokerCard(),
                          Card('♠︎', 'A')]
        self.straight.check(self.hand)
        self.assertEqual(self.straight.result, True)

 
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
        self.hand.hand = [Card('♠︎', '3'),
                          Card('♣︎', '3'),
                          Card('♦︎', '3'),
                          Card('♥', '3'),
                          Card('♠︎', '9')]
        self.four_card.check(self.hand)
        self.assertEqual(self.four_card.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          Card('♠︎', '9')]
        self.four_card.check(self.hand)
        self.assertEqual(self.four_card.result, False)

class TestFiveCard(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.five_card = FiveCard()

    def test_initialize(self):
        self.assertEqual(self.five_card.result, False)
        self.assertEqual(self.five_card.porker_hand, 'FiveCard')

    def test_check_is_False(self):
        # Jokerがないと5カードになることはない
        self.hand.hand = [Card('♠︎', '3'),
                          Card('♣︎', '3'),
                          Card('♦︎', '3'),
                          Card('♥', '3'),
                          Card('♥', '4')]
        self.five_card.check(self.hand)
        self.assertFalse(self.five_card.result)


class TestJokerFiveCard(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.five_card = JokerFiveCard()

    def test_initialize(self):
        self.assertEqual(self.five_card.result, False)
        self.assertEqual(self.five_card.porker_hand, 'FiveCard')

    def test_check_is_True(self):
        self.hand.hand = [Card('♠︎', '3'),
                          Card('♣︎', '3'),
                          Card('♦︎', '3'),
                          Card('♥', '3'),
                          JokerCard()]
        self.five_card.check(self.hand)
        self.assertEqual(self.five_card.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '7'),
                          Card('♦', '7'),
                          JokerCard()]
        self.five_card.check(self.hand)
        self.assertEqual(self.five_card.result, False)

class TestJokerFourCard(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.four_card = JokerFourCard()

    def test_initialize(self):
        self.assertEqual(self.four_card.result, False)
        self.assertEqual(self.four_card.porker_hand, 'FourCard')

    def test_check_is_True(self):
        self.hand.hand = [Card('♠︎', '4'),
                          Card('♣︎', '3'),
                          Card('♦︎', '3'),
                          Card('♥', '3'),
                          JokerCard()]
        self.four_card.check(self.hand)
        self.assertEqual(self.four_card.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '7'),
                          Card('♦', '7'),
                          JokerCard()]
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
        self.hand.hand = [Card('♠︎', '3'),
                          Card('♣︎', '3'),
                          Card('♦︎', '3'),
                          Card('♥', '4'),
                          Card('♠︎', '9')]
        self.three_card.check(self.hand)
        self.assertEqual(self.three_card.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          Card('♠︎', '9')]
        self.three_card.check(self.hand)
        self.assertEqual(self.three_card.result, False)

    def test_check_is_false_because_four_card(self):
        self.hand.hand = [Card('♠︎', '3'),
                          Card('♣︎', '3'),
                          Card('♦︎', '3'),
                          Card('♥', '3'),
                          Card('♠︎', '9')]
        self.three_card.check(self.hand)
        self.assertFalse(self.three_card.result)

class TestJokerThreeCard(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.three_card = JokerThreeCard()

    def test_initialize(self):
        self.assertEqual(self.three_card.result, False)
        self.assertEqual(self.three_card.porker_hand, 'ThreeCard')

    def test_check_is_True(self):
        self.hand.hand = [Card('♠︎', '3'),
                          Card('♣︎', '3'),
                          JokerCard(),
                          Card('♥', '4'),
                          Card('♠︎', '9')]
        self.three_card.check(self.hand)
        self.assertTrue(self.three_card.result)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          JokerCard(),
                          Card('♦', '7'),
                          Card('♠︎', '9')]
        self.three_card.check(self.hand)
        self.assertFalse(self.three_card.result)

    def test_check_is_false_because_four_card(self):
        self.hand.hand = [Card('♠︎', '3'),
                          Card('♣︎', '3'),
                          Card('♦︎', '3'),
                          JokerCard(),
                          Card('♠︎', '9')]
        self.three_card.check(self.hand)
        self.assertFalse(self.three_card.result)

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
        self.hand.hand = [Card('♠︎', '3'),
                          Card('♣︎', '3'),
                          Card('♦︎', '5'),
                          Card('♥', '5'),
                          Card('♠︎', '5')]
        self.three_card.check(self.hand)
        self.one_pair.check(self.hand)
        self.full_house.check(self.hand,
                              self.one_pair.result,
                              self.three_card.result)
        self.assertEqual(self.full_house.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          Card('♠︎', '9')]
        self.three_card.check(self.hand)
        self.one_pair.check(self.hand)
        self.full_house.check(self.hand,
                              self.one_pair.result,
                              self.three_card.result)
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
        self.hand.hand = [Card('♠︎', '3'),
                          Card('♣︎', '3'),
                          Card('♦︎', '5'),
                          Card('♥', '5'),
                          Card('♠︎', '9')]
        self.two_pair.check(self.hand)
        self.assertEqual(self.two_pair.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          Card('♠︎', '9')]
        self.two_pair.check(self.hand)
        self.assertEqual(self.two_pair.result, False)

    def test_check_is_False_when_one_pair(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', 'A'),
                          Card('♠︎', '3'),
                          Card('♦', '5'),
                          Card('♠︎', '9')]
        self.two_pair.check(self.hand)
        self.assertEqual(self.two_pair.result, False)

class TestJokerTwoPair(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.two_pair = JokerTwoPair()

    def test_initialize(self):
        self.assertEqual(self.two_pair.result, False)
        self.assertEqual(self.two_pair.porker_hand, 'TwoPair')

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', '3'),
                          Card('♣︎', '3'),
                          Card('♦︎', '5'),
                          Card('♥', '5'),
                          Card('♠︎', '9')]
        self.two_pair.check(self.hand)
        self.assertFalse(self.two_pair.result)

    def test_check_is_False_with_joker(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', 'A'),
                          Card('♠︎', '5'),
                          JokerCard(),
                          Card('♠︎', '9')]
        self.two_pair.check(self.hand)
        self.assertFalse(self.two_pair.result)


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
        self.hand.hand = [Card('♠︎', '3'),
                          Card('♣︎', '3'),
                          Card('♦︎', '5'),
                          Card('♥', '4'),
                          Card('♠︎', '9')]
        self.one_pair.check(self.hand)
        self.assertEqual(self.one_pair.result, True)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          Card('♠︎', '9')]
        self.one_pair.check(self.hand)
        self.assertEqual(self.one_pair.result, False)

    def test_check_is_False_when_two_pair(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', 'A'),
                          Card('♠︎', '5'),
                          Card('♦', '5'),
                          Card('♠︎', '9')]
        self.one_pair.check(self.hand)
        self.assertEqual(self.one_pair.result, False)

class TestJokerOnePair(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        player = Player(deck)
        self.hand = player.hand
        self.one_pair = JokerOnePair()

    def test_initialize(self):
        self.assertEqual(self.one_pair.result, False)
        self.assertEqual(self.one_pair.porker_hand, 'OnePair')

    def test_check_is_True_include_joker(self):
        self.hand.hand = [Card('♠︎', '2'),
                          Card('♣︎', '3'),
                          JokerCard(),
                          Card('♥', '4'),
                          Card('♠︎', '9')]
        self.one_pair.check(self.hand, True)
        self.assertEqual(self.one_pair.result, True)

    def test_check_is_False_include_joker(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', '3'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          Card('♠︎', '9')]
        self.one_pair.check(self.hand, True)
        self.assertEqual(self.one_pair.result, False)

    def test_check_is_False_when_three_card_include_joker(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', 'A'),
                          JokerCard(),
                          Card('♦', '5'),
                          Card('♠︎', '9')]
        self.one_pair.check(self.hand, True)
        self.assertEqual(self.one_pair.result, False)

    def test_check_is_True(self):
        self.hand.hand = [Card('♠︎', '2'),
                          Card('♣︎', '3'),
                          JokerCard(),
                          Card('♥', '4'),
                          Card('♠︎', '9')]
        self.one_pair.check(self.hand, False)
        self.assertEqual(self.one_pair.result, False)

    def test_check_is_False(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', 'A'),
                          Card('♠︎', '5'),
                          Card('♦', '7'),
                          Card('♠︎', '9')]
        self.one_pair.check(self.hand, False)
        self.assertEqual(self.one_pair.result, True)

    def test_check_is_False_when_three_card(self):
        self.hand.hand = [Card('♠︎', 'A'),
                          Card('♦', 'A'),
                          JokerCard(),
                          Card('♦', '5'),
                          Card('♠︎', '9')]
        self.one_pair.check(self.hand, False)
        self.assertEqual(self.one_pair.result, True)

class TestPeke(unittest.TestCase):
    def setUp(self):
        self.peke = Peke()

    def test_initialize(self):
        self.assertEqual(self.peke.porker_hand, 'PEKE')
