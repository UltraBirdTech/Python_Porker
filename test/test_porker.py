# [USAGE]: python -m unittest test/porker_test.py
import unittest

import porker

class TestCard(unittest.TestCase):
    def setup(self):
        pass

    def test_set_card_number(self):
        card = porker.Card('♠︎', 'A')
        self.assertEqual(card.num, 'A')
