import operator

class InvalidCard(Exception):
    pass
class InvalidHand(Exception):
    pass

def unique_combinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in unique_combinations(items[i+1:],n-1):
                yield [items[i]]+cc



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
    def __cmp__(self, other):
        return cmp(self.value, other.value)

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
        self.__rank = None
        self.__cards = sorted([Card(c) for c in cards], reverse=True)
        self.__values = []
        self.rank()
    def __str__(self):
        return str.format("Cards: {0} Rank: '{1}' Values: {2}",
            [str(c.value) + c.suit for c in self.__cards],
            Hand.RANKS[self.rank()],
            self.values())
    def rank(self):
        if self.__rank:
            return self.__rank
        flush = True
        straight = False
        last = None
        merged = {}
        for c in self.__cards:
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
            if self.__cards[0].value - self.__cards[4].value == 4:
                straight = True
            if self.__cards[4].value == 2 and self.__cards[1].value == 5 and self.__cards[0].value == 14:
                straight = True
                # Set the value of the ace to 1 and resort so hand comparisons work correctly
                self.__cards[0].value = 1
                self.__cards = sorted(self.__cards, reverse=True)
            if straight and flush:
                if self.__cards[0].value == 14:
                    self.__rank = Hand.ROYAL_FLUSH
                else:
                    self.__rank = Hand.STRAIGHT_FLUSH
            elif flush:
                self.__rank = Hand.FLUSH
            elif straight:
                self.__rank = Hand.STRAIGHT
            else:
                self.__rank = Hand.HIGH_CARD
            self.__values = [c.value for c in self.__cards]
        else:
            multiples = [m for m in sorted(merged.items(), key = operator.itemgetter(1), reverse = True) if m[1] > 1]
            if len(multiples) > 1:
                if multiples[0][1] == multiples[1][1]:
                    self.__rank = Hand.TWO_PAIRS
                else:
                    self.__rank = Hand.FULL_HOUSE 
            else:
                if multiples[0][1] > 3:
                    self.__rank = Hand.FOUR_OF_A_KIND
                elif multiples[0][1] == 3:
                    self.__rank = Hand.THREE_OF_A_KIND
                else:
                    self.__rank = Hand.ONE_PAIR
            mvalues = [m[0] for m in multiples]
            self.__values = mvalues + [c.value for c in self.__cards if c.value not in mvalues]

        return self.__rank
    def values(self):
        if not self.__values:
            self.rank()
        return self.__values
    @staticmethod
    def create_best_hand(cards):
        if len(cards) == 5:
            return Hand(cards)
        elif len(cards) < 5:
            raise InvalidHand
        else:
            return Hand.create_best_hand_bruteforce(cards)
        return false
    @staticmethod
    def create_best_hand_bruteforce(cards):
        combos = unique_combinations(cards, 5)
        hands = [Hand(combo) for combo in combos]
        hands = sorted(hands, reverse=True)
        return hands[0]
    @staticmethod
    def create_best_hand_smart(cards):
        #TODO: Figure out a smarter algorithm for getting the best hand!
        pass
    def __cmp__(self, other):
        # Compare hand rankings
        result = cmp(self.rank(), other.rank())
        if (result == 0):
            # Compare hand values
            for i in range(len(self.values())):
                result = cmp(self.values()[i], other.values()[i])
                if (result != 0):
                    return result
        return result