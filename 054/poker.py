import operator

class InvalidCard(Exception):
    pass
class InvalidHand(Exception):
    pass

class Card:
    values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    def __init__(self, string):
        self.value = string[0]
        if self.value in '23456789':
            self.value = int(self.value)
        else:
            try:
                self.value = Card.values[self.value]
            except KeyError as e:
                raise InvalidCard
        self.suit = string[1]
        if not self.suit in ['H', 'C', 'S', 'D']:
            raise InvalidCard
    @staticmethod
    def compare(a, b):
        if a.value > b.value:
            return 1
        elif a.value == b.value:
            return 0
        else:
            return -1

class Hand:
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9
    RANKS = [
        'High Card',
        'One Pair',
        'Two Pairs',
        'Three of a Kind',
        'Straight',
        'Flush',
        'Full House',
        'Four of a Kind',
        'Straight Flush',
        'Royal Flush'
    ]
    def __init__(self, cards):
        self._rank = None
        self._cards = sorted([Card(c) for c in cards], cmp=Card.compare, reverse=True)
        self._values = []
        self.rank()
    def __str__(self):
        return str.format("Cards: {0} Rank: '{1}' Values: {2}",
            [str(c.value) + c.suit for c in self._cards],
            Hand.RANKS[self.rank()],
            self.values())
    def rank(self):
        if self._rank:
            return self._rank
        flush = True
        straight = False
        last = None
        merged = {}
        for c in self._cards:
            if last:
                if flush and c.suit != last.suit:
                    flush = False
            last = c
            if c.value in merged:
                merged[c.value] = merged[c.value] + 1
            else:
                merged[c.value] = 1
        if (len(merged)) == 5:
            # All unique cards, check for a straight
            if self._cards[0].value - self._cards[4].value == 4 or \
               (self._cards[4].value == 2 and self._cards[1].value == 5 and self._cards[0].value == 14):
                straight = True
            if straight and flush:
                if self._cards[0].value == 14:
                    self._rank = Hand.ROYAL_FLUSH
                else:
                    self._rank = Hand.STRAIGHT_FLUSH
            elif flush:
                self._rank = Hand.FLUSH
            elif straight:
                self._rank = Hand.STRAIGHT
            else:
                self._rank = Hand.HIGH_CARD
            self._values = [c.value for c in self._cards]
        else:
            multiples = [m for m in sorted(merged.items(), key = operator.itemgetter(1), reverse = True) if m[1] > 1]
            if len(multiples) > 1:
                if multiples[0][1] == multiples[1][1]:
                    self._rank = Hand.TWO_PAIRS
                else:
                    self._rank = Hand.FULL_HOUSE 
            else:
                if multiples[0][1] > 3:
                    self._rank = Hand.FOUR_OF_A_KIND
                elif multiples[0][1] == 3:
                    self._rank = Hand.THREE_OF_A_KIND
                else:
                    self._rank = Hand.ONE_PAIR
            mvalues = [m[0] for m in multiples]
            self._values = mvalues + [c.value for c in self._cards if c.value not in mvalues]

        return self._rank
    def values(self):
        if not self._values:
            self.rank()
        return self._values
    @staticmethod
    def compare(a, b):
        # Compare hand rankings
        result = cmp(a.rank(), b.rank())
        if (result == 0):
            # Compare hand values
            for i in range(len(a.values())):
                result = cmp(a.values()[i], b.values()[i])
                if (result != 0):
                    return result
        return result