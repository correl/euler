import poker
import unittest

class TestCards(unittest.TestCase):
    def setUp(self):
        pass
    def test_valid_number_card(self):
        card = poker.Card('9D')
        self.assertEqual(card.value, 9)
    def test_valid_face_card(self):
        card = poker.Card('QH')
        self.assertEqual(card.value, 12)
    def test_invalid_card_value(self):
        self.assertRaises(poker.InvalidCard, poker.Card, 'ZH')
    def test_invalid_card_suit(self):
        self.assertRaises(poker.InvalidCard, poker.Card, '9Z')
    def test_compare(self):
        cards = ['QH', '9D', 'JS']
        cards_sorted = sorted([poker.Card(c) for c in cards], reverse=True)
        self.assertEqual([c.value for c in cards_sorted], [12, 11, 9])

class TestFiveCardHands(unittest.TestCase):
    def setUp(self):
        self.rank_hands = {
            poker.Hand.HIGH_CARD:        poker.Hand(['5D', '8C', '9S', 'JS', 'AC']),
            poker.Hand.ONE_PAIR:         poker.Hand(['5H', '5C', '6S', '7S', 'KD']),
            poker.Hand.TWO_PAIRS:        poker.Hand(['2D', '3C', '2H', '7S', '7H']),
            poker.Hand.THREE_OF_A_KIND:  poker.Hand(['AS', '2D', 'TH', 'AH', 'AC']),
            poker.Hand.STRAIGHT:         poker.Hand(['9D', '5S', '7H', '8S', '6S']),
            poker.Hand.FLUSH:            poker.Hand(['7S', 'TS', 'KS', '3S', 'JS']),
            poker.Hand.FULL_HOUSE:       poker.Hand(['6S', '2D', '2H', '6D', '6H']),
            poker.Hand.FOUR_OF_A_KIND:   poker.Hand(['7S', '7H', '7D', '2H', '7C']),
            poker.Hand.STRAIGHT_FLUSH:   poker.Hand(['JS', '8S', 'QS', 'TS', '9S']),
            poker.Hand.ROYAL_FLUSH:      poker.Hand(['QH', 'TH', 'JH', 'KH', 'AH']),
        }
    def test_hand_rankings(self):
        for rank, hand in self.rank_hands.iteritems():
            self.assertEqual(hand.rank(), rank, 'Ranking hand: {0}, got {1}'.format(poker.Hand.RANKS[rank], poker.Hand.RANKS[hand.rank()]))
    def test_ace_high_straight(self):
        hand = poker.Hand(['AH', 'KS', 'QC', 'JS', 'TS'])
        self.assertEqual([hand.rank(), hand.values()], [poker.Hand.STRAIGHT, [14, 13, 12, 11, 10]])
    def test_ace_low_straight(self):
        hand = poker.Hand(['AH', '2S', '3C', '4S', '5S'])
        self.assertEqual([hand.rank(), hand.values()], [poker.Hand.STRAIGHT, [5, 4, 3, 2, 1]])
    def test_compare_ace_low_straight(self):
        low = poker.Hand(['AH', '2S', '3C', '4S', '5S'])
        high = poker.Hand(['2S', '3C', '4S', '5S', '6S'])
        self.assertTrue(low < high)
    def test_compare_two_pair(self):
        low = poker.Hand(['7S', '9D', 'JH', '7D', 'JS'])
        high = poker.Hand(['AS', 'AD', '5C', '2D', '2H'])
        self.assertTrue(low < high)
    def test_compare_ranks(self):
        for rank, hand in self.rank_hands.iteritems():
            for rank2, hand2 in self.rank_hands.iteritems():
                if (rank == rank2):
                    self.assertEqual(hand.rank(), hand2.rank(), '{0} == {1}'.format(poker.Hand.RANKS[rank], poker.Hand.RANKS[rank2]))
                elif (rank < rank2):
                    self.assertTrue(hand.rank() < hand2.rank(), '{0} < {1}'.format(poker.Hand.RANKS[rank], poker.Hand.RANKS[rank2]))
                else:
                    self.assertTrue(hand.rank() > hand2.rank(), '{0} > {1}'.format(poker.Hand.RANKS[rank], poker.Hand.RANKS[rank2]))

class TestSevenCardHands(unittest.TestCase):
    def setUp(self):
        self.rank_hands = {
            poker.Hand.HIGH_CARD:        poker.Hand.create_best_hand(['5D', '8C', '9S', 'JS', '4C', '3D', 'AC']),
            poker.Hand.ONE_PAIR:         poker.Hand.create_best_hand(['5H', 'JC', '6S', '7S', 'KD', '4C', '5C']),
            poker.Hand.TWO_PAIRS:        poker.Hand.create_best_hand(['2D', '3C', '2H', '7S', 'JC', '8H', '7H']),
            poker.Hand.THREE_OF_A_KIND:  poker.Hand.create_best_hand(['AS', '2D', 'TH', 'AH', 'JC', '8S', 'AC']),
            poker.Hand.STRAIGHT:         poker.Hand.create_best_hand(['9D', '5S', '7H', '8S', '2H', 'AC', '6S']),
            poker.Hand.FLUSH:            poker.Hand.create_best_hand(['7S', 'TS', 'KS', '3S', 'AC', '3H', 'JS']),
            poker.Hand.FULL_HOUSE:       poker.Hand.create_best_hand(['6S', '2D', '2H', '6D', '8C', '4S', '6H']),
            poker.Hand.FOUR_OF_A_KIND:   poker.Hand.create_best_hand(['7S', '7H', '7D', '2H', '8D', '9D', '7C']),
            poker.Hand.STRAIGHT_FLUSH:   poker.Hand.create_best_hand(['JS', '8S', 'QS', 'TS', '4D', '2S', '9S']),
            poker.Hand.ROYAL_FLUSH:      poker.Hand.create_best_hand(['QH', 'TH', 'JH', 'KH', '9H', '6S', 'AH']),
        }
    def test_hand_rankings(self):
        for rank, hand in self.rank_hands.iteritems():
            self.assertEqual(hand.rank(), rank, 'Ranking hand: {0}, got {1}'.format(poker.Hand.RANKS[rank], poker.Hand.RANKS[hand.rank()]))
    def test_ace_high_straight(self):
        hand = poker.Hand.create_best_hand(['AH', 'KS', 'QC', 'JS', '9S', '7D', 'TS'])
        self.assertEqual([hand.rank(), hand.values()], [poker.Hand.STRAIGHT, [14, 13, 12, 11, 10]])
    def test_ace_low_straight(self):
        hand = poker.Hand.create_best_hand(['AH', '2S', '3C', '4S', '9D', 'JC', '5S'])
        self.assertEqual([hand.rank(), hand.values()], [poker.Hand.STRAIGHT, [5, 4, 3, 2, 1]])
    def test_compare_ace_low_straight(self):
        low = poker.Hand.create_best_hand(['AH', '2S', '3C', '4S', '9D', '4C', '5S'])
        high = poker.Hand.create_best_hand(['2S', '3C', '4S', '5S', '8D', 'TC', '6S'])
        self.assertTrue(low < high)
    def test_compare_two_pair(self):
        low = poker.Hand.create_best_hand(['3D', 'KC', '7S', '9D', 'JH', '7D', 'JS'])
        high = poker.Hand.create_best_hand(['4D', '9H', 'AS', 'AD', '5C', '2D', '2H'])
        self.assertTrue(low < high)
    def test_compare_ranks(self):
        for rank, hand in self.rank_hands.iteritems():
            for rank2, hand2 in self.rank_hands.iteritems():
                if (rank == rank2):
                    self.assertEqual(hand.rank(), hand2.rank(), '{0} == {1}'.format(poker.Hand.RANKS[rank], poker.Hand.RANKS[rank2]))
                elif (rank < rank2):
                    self.assertTrue(hand.rank() < hand2.rank(), '{0} < {1}'.format(poker.Hand.RANKS[rank], poker.Hand.RANKS[rank2]))
                else:
                    self.assertTrue(hand.rank() > hand2.rank(), '{0} > {1}'.format(poker.Hand.RANKS[rank], poker.Hand.RANKS[rank2]))

if __name__ == '__main__':
    unittest.main()
