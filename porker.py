import random


def main():
    try:
        deck = Deck()
        player = Player(deck)
        player.exchange(deck)
        player.print_my_hand()
        player.check_poker_hand()
        player.print_result()
    except InputValueError as err:
        print('[ERROR]' + err.message)
    except Exception as err:
        print(err)


class Card():
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num
        self.value = suit + num

    def card_number(self):
        if self.num not in ['A', 'J', 'Q', 'K']:
            return int(self.num)

        card_mapping = {
            'K': 13,
            'Q': 12,
            'J': 11,
            'A': 1
        }
        return card_mapping[self.num]

    def __lt__(self, other):
        if not isinstance(other, Card):
            return

        if other.is_joker():
            return False

        if self.card_number() == 1:
            return False
 
        if other.card_number() == 1:
            return True
 
        return self.card_number() < other.card_number()

    def __eq__(self, other):
        if not isinstance(other, Card):
            return
        return self.card_number() == other.card_number()

    def is_joker(self):
        return False

class JokerCard(Card):
     def __init__(self):
        self.joker = 'Joker'
        self.suit = self.joker
        self.num = self.joker
        self.value = self.joker

     def card_number(self):
        return self.joker

     def __lt__(self, other):
        if self.is_joker():
            return False

        if other.is_joker():
            return True
 
     def __eq__(self, other):
        return False

     def is_joker(self):
        return True

class Deck():
    def __init__(self):
        suits = ['♠', '♣', '♥', '♦']
        numbers = ['A', '2', '3', '4', '5', '6', '7',
                   '8', '9', '10', 'J', 'Q', 'K']
        self.deck_list = []
        for s in suits:
            for n in numbers:
                self.deck_list.append(Card(s, n))
        self.deck_list.append(JokerCard())

    def draw(self):
        card = random.choice(self.deck_list)
        self.deck_list.remove(card)
        return card


class Player():
    def __init__(self, deck):
        self.hand = Hand()
        for i in range(0, self.hand.max_hand):
            self.draw(deck)

    def draw(self, deck):
        self.hand.add(deck.draw())

    def cut(self, num):
        self.hand.cut(int(num))

    def exchange(self, deck):
        self.print_usage()
        input_value = input()
        input_list = input_value.split(',')
        self.check_input_value(input_list)
        if 'p' in input_list:
            print('exchange is pass')
            return

        input_list_single = list(set(input_list))
        input_list_single.sort()
        input_list_single.reverse()
        for i in input_list_single:
            self.cut(i)
            self.draw(deck)

    def print_usage(self):
        print('交換する手札を番号で入力してください')
        print('複数ある場合は","区切りで入力してください')
        for i, c in enumerate(self.hand.all()):
            print(str(i) + ': [' + c.value + ']')
        print('p: (pass)手札交換をスキップします')

    def check_input_value(self, input_list):
        correct_values = ['0', '1', '2', '3', '4', 'p']
        for value in input_list:
            if value in correct_values:
                continue
            else:
                message = '入力値は数値(0~4)で入力してください。'
                raise InputValueError(message)

    def print_my_hand(self):
        self.hand.print_my_hand()

    def print_result(self):
        self.hand.porker_hand.display()

    def check_poker_hand(self):
        self.hand.check_porker_hand()


class InputValueError(Exception):
    def __init__(self, message):
        self.message = message


class Hand():
    def __init__(self):
        self.max_hand = 5
        self.hand = []

    def add(self, card):
        self.hand.append(card)

    def cut(self, num):
        del self.hand[num]

    def all(self):
        return self.hand

    def print_my_hand(self):
        for c in self.hand:
            print('[' + c.value + ']', end='')
        print()

    def check_porker_hand(self):
        self.porker_hand = Check(self.is_joker()).check(self)

    def get_numbers(self):
        numbers = []
        for c in self.hand:
            numbers.append(c.num)
        return numbers

    def get_numbers_as_int(self):
        numbers = []
        for c in self.hand:
            numbers.append(c.card_number())
        return numbers

    def get_all_suits(self):
        suits = []
        for h in self.hand:
            suits.append(h.suit)
        return suits

    def is_joker(self):
        for card in self.hand:
            if card.is_joker():
                return True
        return False


class Check():
    def __init__(self, is_joker=False):
        if is_joker:
            #self.initialize_joker_porker_hands()
            self.initialize_porker_hands()
            return
        self.initialize_porker_hands()

    def check(self, hand):
        self.flash.check(hand)
        self.straight.check(hand)

        flash_result = self.flash.result
        straight_result = self.straight.result
        self.straight_flash.check(hand, flash_result, straight_result)
        if self.straight_flash.result:
            return self.straight_flash

        if self.flash.result:
            return self.flash

        if self.straight.result:
            return self.straight

        self.five_card.check(hand)
        if self.five_card.result:
            return self.five_card

        self.four_card.check(hand)
        if self.four_card.result:
            return self.four_card

        self.three_card.check(hand)
        self.one_pair.check(hand)

        one_pair_result = self.one_pair.result
        three_card_result = self.three_card.result
        self.full_house.check(hand, one_pair_result, three_card_result)
        if self.full_house.result:
            return self.full_house

        if self.three_card.result:
            return self.three_card

        self.two_pair.check(hand)
        if self.two_pair.result:
            return self.two_pair

        if self.one_pair.result:
            return self.one_pair

        return self.peke

    def initialize_porker_hands(self):
        self.straight_flash = StraightFlash()
        self.flash = Flash()
        self.straight = Straight()
        self.five_card = FiveCard()
        self.four_card = FourCard()
        self.full_house = FullHouse()
        self.three_card = ThreeCard()
        self.two_pair = TwoPair()
        self.one_pair = OnePair()
        self.peke = Peke()

    def initialize_joker_porker_hands(self):
        self.straight_flash = JokerStraightFlash()
        self.flash = JokerFlash()
        self.straight = JokerStraight()
        self.five_card = JokerFiveCard()
        self.four_card = JokerFourCard()
        self.full_house = JokerFullHouse()
        self.three_card = ThreeCard()
        self.two_pair = TwoPair()
        self.one_pair = OnePair()
        self.peke = Peke()

class PorkerHand():
    def __init__(self, porker_hand):
        self.porker_hand = porker_hand
        self.result = False

    def check_conditions(self, hand):
        print('You should write about conditions for each class.')

    def check(self, hand):
        self.check_conditions(hand)

    def display(self):
        print('My hand is ' + self.porker_hand)


class StraightFlash(PorkerHand):
    def __init__(self):
        super().__init__('StraightFlash')

    def check_conditions(self, hand, straight_result, flash_result):
        if not (straight_result and flash_result):
            return

        if self.is_royal(hand):
            self.porker_hand = 'RoyalStraightFlash'

        self.result = True

    def check(self, hand, straight_result, flash_result):
        self.check_conditions(hand, straight_result, flash_result)

    def is_royal(self, hand):
        hand_list = hand.get_numbers()
        check_list = ['10', 'J', 'Q', 'K', 'A']
        hand_list.sort()
        check_list.sort()
        return check_list == hand_list

# TODO: Add rogic
class JokerStraightFlash(StraightFlash):
    pass
    
class Flash(PorkerHand):
    def __init__(self, hand_name='Flash'):
        super().__init__(hand_name)
        self.duplicate_suite_count = 1  # 重複をはじいた結果が1であればフラッシュ

    def check_conditions(self, hand):
        suits = hand.get_all_suits()
        self.result = (len(set(suits)) == self.duplicate_suite_count)

class JokerFlash(Flash):
    def __init__(self):
        super().__init__('JokerFlash')
        self.duplicate_suite_count = 2 # Jokerを含めて重複をはじいた結果が2であればフラッシュ

class Straight(PorkerHand):
    def __init__(self, hand_name='Straight'):
        super().__init__(hand_name)

    def check_conditions(self, hand):
        numbers = hand.get_numbers_as_int()
        numbers.sort()
        number_list = []
        if (1 in numbers) and (13 in numbers):
            number_list = list(range(10, 10 + 4))
            number_list.insert(0, 1)
        else:
            number_list = list(range(numbers[0], numbers[0] + 5))
        self.result = (numbers == number_list)

class JokerStraight(Straight):
    def __init__(self):
        super().__init__('JokerStraight')

    def check_conditions(self, hand):
        numbers = hand.get_numbers_as_int()
        numbers.remove('Joker') # joker は邪魔なのでremove()して取り除く
        numbers.sort()
        number_list = []
        if (1 in numbers) and (13 in numbers):
            number_list = list(range(10, 10 + 4))
            number_list.insert(0, 1)
        else:
            number_list = list(range(numbers[0], numbers[0] + 5))
        numbers_diff = (set(number_list) - set(numbers))
        self.result = len(numbers_diff) == 1 # 差分が1であればストレートと判定

class Kind(PorkerHand):
    def __init__(self, porker_hand):
        super().__init__(porker_hand)

    def check_conditions(self, hand):
        numbers = hand.get_numbers_as_int()
        for num in numbers:
            if numbers.count(num) == self.card_num:
                self.result = True
                break

class FiveCard(Kind):
    def __init__(self):
        super().__init__('FiveCard')
        self.card_num = 5

    def check_conditions(self, hand):
        self.result = False # Joker が存在しない場合は必ずFalse

class JokerFiveCard(Kind):
    def __init__(self):
        super().__init__('FiveCard')
        self.card_num = 4 # Joker含めて4枚あればファイブカード

    def check_conditions(self, hand):
        super().check_conditions(hand)

class FourCard(Kind):
    def __init__(self):
        super().__init__('FourCard')
        self.card_num = 4

    def check_conditions(self, hand):
        super().check_conditions(hand)

class JokerFourCard(Kind):
    def __init__(self):
        super().__init__('FourCard')
        self.card_num = 3 # Joker含めて3枚あれば4カード

    def check_conditions(self, hand):
        super().check_conditions(hand)

class ThreeCard(Kind):
    def __init__(self):
        super().__init__('ThreeCard')
        self.card_num = 3

    def check_conditions(self, hand):
        super().check_conditions(hand)


class FullHouse(PorkerHand):
    def __init__(self):
        super().__init__('FullHouse')

    def check_conditions(self, hand, onepair_result, three_card_result):
        self.result = (onepair_result and three_card_result)

    def check(self, hand, onepair_result, three_card_result):
        self.check_conditions(hand, onepair_result, three_card_result)

class JokerFullHouse(FullHouse):
    def __init__(self):
        super().__init__()

    def check_conditions(self, hand, onepair_result, three_card_result):
        self.result = (onepair_result and three_card_result)

    def check(self, hand, onepair_result, three_card_result):
        self.check_conditions(hand, onepair_result, three_card_result)


class Pair(PorkerHand):
    def __init__(self, porker_hand):
        super().__init__(porker_hand)

    def check_conditions(self, hand):
        check_dict = {}
        for n in hand.get_numbers():
            if n in check_dict:
                check_dict[n] += 1
            else:
                check_dict[n] = 1
        self.result = list(check_dict.values()).count(2) == self.pair_num


class TwoPair(Pair):
    def __init__(self):
        super().__init__('TwoPair')
        self.pair_num = 2

    def check_conditions(self, hand):
        super().check_conditions(hand)


class OnePair(Pair):
    def __init__(self):
        super().__init__('OnePair')
        self.pair_num = 1

    def check_conditions(self, hand):
        super().check_conditions(hand)


class Peke(PorkerHand):
    def __init__(self):
        super().__init__('PEKE')

    def display(self):
        print('PE☆KE')

if __name__ == '__main__':
    main()
