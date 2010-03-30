from e054 import *
import unittest

class TestCards(unittest.TestCase):
    def setUp(self):
        pass
    def test_valid_number_card(self):
        card = PokerCard('9D')
        self.assertEqual(card.value, 9)
    def test_valid_face_card(self):
        card = PokerCard('QH')
        self.assertEqual(card.value, 12)
    def test_invalid_card_value(self):
        self.assertRaises(InvalidCard, PokerCard, 'ZH')
    def test_invalid_card_suit(self):
        self.assertRaises(InvalidCard, PokerCard, '9Z')
    def test_compare(self):
        cards = ['QH', '9D', 'JS']
        cards_sorted = sorted([PokerCard(c) for c in cards], cmp=PokerCard.compare, reverse=True)
        self.assertEqual([c.value for c in cards_sorted], [12, 11, 9])

class TestHands(unittest.TestCase):
    def setUp(self):
        pass
    

if __name__ == '__main__':
    unittest.main()