# [USAGE]: python -m unittest tests/porker_test.py
import unittest

from porker import Card

class TestCard(unittest.TestCase):
    def setup(self):
        pass

    def test_set_card_number(self):
        card = porker.Card('♠︎', 'A')
        self.assertEqual(card.num, 'A')
