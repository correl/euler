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

class TestFiveCardHands(unittest.TestCase):
    def setUp(self):
        self.rank_hands = {
            PokerHand.HIGH_CARD:        PokerHand(['5D', '8C', '9S', 'JS', 'AC']),
            PokerHand.ONE_PAIR:         PokerHand(['5H', '5C', '6S', '7S', 'KD']),
            PokerHand.TWO_PAIRS:        PokerHand(['2D', '3C', '2H', '7S', '7H']),
            PokerHand.THREE_OF_A_KIND:  PokerHand(['AS', '2D', 'TH', 'AH', 'AC']),
            PokerHand.STRAIGHT:         PokerHand(['9D', '5S', '7H', '8S', '6S']),
            PokerHand.FLUSH:            PokerHand(['7S', 'TS', 'KS', '3S', 'JS']),
            PokerHand.FULL_HOUSE:       PokerHand(['6S', '2D', '2H', '6D', '6H']),
            PokerHand.FOUR_OF_A_KIND:   PokerHand(['7S', '7H', '7D', '2H', '7C']),
            PokerHand.STRAIGHT_FLUSH:   PokerHand(['JS', '8S', 'QS', 'TS', '9S']),
            PokerHand.ROYAL_FLUSH:      PokerHand(['QH', 'TH', 'JH', 'KH', 'AH']),
        }
    def test_hand_rankings(self):
        for rank, hand in self.rank_hands.iteritems():
            self.assertEqual(hand.rank(), rank, 'Ranking hand: {0}'.format(PokerHand.RANKS[rank]))
    def test_ace_high_straight(self):
        hand = PokerHand(['AH', 'KS', 'QC', 'JS', 'TS'])
        self.assertEqual([hand.rank(), hand.values()], [PokerHand.STRAIGHT, [14, 13, 12, 11, 10]])
    def test_ace_low_straight(self):
        hand = PokerHand(['AH', '2S', '3C', '4S', '5S'])
        self.assertEqual([hand.rank(), hand.values()], [PokerHand.STRAIGHT, [14, 5, 4, 3, 2]])
    def test_compare_ace_low_straight(self):
        low = PokerHand(['AH', '2S', '3C', '4S', '5S'])
        high = PokerHand(['2S', '3C', '4S', '5S', '6S'])
        self.assertTrue(low < high)
    def test_compare_ranks(self):
        for rank, hand in self.rank_hands.iteritems():
            for rank2, hand2 in self.rank_hands.iteritems():
                if (rank == rank2):
                    self.assertEqual(hand.rank(), hand2.rank(), '{0} == {1}'.format(PokerHand.RANKS[rank], PokerHand.RANKS[rank2]))
                elif (rank < rank2):
                    self.assertTrue(hand.rank() < hand2.rank(), '{0} < {1}'.format(PokerHand.RANKS[rank], PokerHand.RANKS[rank2]))
                else:
                    self.assertTrue(hand.rank() > hand2.rank(), '{0} > {1}'.format(PokerHand.RANKS[rank], PokerHand.RANKS[rank2]))

if __name__ == '__main__':
    unittest.main()