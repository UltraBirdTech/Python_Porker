import random

def main():
    deck = Deck()
    player = Player(deck)
    player.print_my_hand()
    player.exchange(deck)
    player.print_my_hand()
    player.check_poker_hand()

class Card():
    def __init__(self, suite, num):
        self.suite = suite
        self.num = num
        self.value = suite + num

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


class Deck():
    def __init__(self):
        suites = ['♠','♣','♥','♦']
        numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck_list = []
        for s in suites:
            for n in numbers:
                deck_list.append(Card(s, n))
        
        self.deck_list = deck_list

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
        input_value = input()
        if input_value == 'p':
            print('exchange is pass')
            return

        input_list = input_value.split(',')
        input_list.reverse()
        for i in input_list:
            self.cut(i)
            self.draw(deck)

    def print_my_hand(self):
        self.hand.print_my_hand()

    def check_poker_hand(self):
        self.hand.check_porker_hand()

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
        Check().check()

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
 
    def get_all_suites(self):
        suites = []
        for h in self.hand:
            suites.append(h.suite)
        return suites


class Check():
    def __init__(self):
        pass

    def check(self):
        # write something...
        pass

if __name__ == '__main__':
    main()
