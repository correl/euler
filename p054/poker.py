import operator
import random

class InvalidCard(Exception):
    """Invalid Card Exception
    
    Thrown if an invalid face value or suit is supplied for a card
    """
    pass
class InvalidHand(Exception):
    """Invalid Hand Exception
    
    Thrown if the hand being created includes zero or more than 5 cards
    """
    pass

def unique_combinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in unique_combinations(items[i+1:],n-1):
                yield [items[i]]+cc



class Card:
    """Represents a single poker playing card"""
    
    VALUES = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    SUITS = {'Hearts': 'H', 'Diamonds': 'D', 'Clubs': 'C', 'Spades': 'S'}
    def __init__(self, string):
        self.value = string[0]
        if self.value in '23456789':
            self.value = int(self.value)
        else:
            try:
                self.value = Card.VALUES[self.value]
            except KeyError as e:
                raise InvalidCard('Invalid value: {0}'.format(string))
        self.suit = string[1]
        if not self.suit in Card.SUITS.values():
            raise InvalidCard('Invalid suit: {0}'.format(string))
    def __cmp__(self, other):
        """Compare hand values
        
        Compares this card's value with another. Used for sorting.
        """
        
        result = cmp(self.value, other.value)
        if result == 0:
            """Values are identical, suits differ. Doesn't affect ranking in
            any way."""
            result = cmp(self.suit, other.suit)
        return result
    def __repr__(self):
        """Builds a string representation of the hand"""
        val = self.value
        for k, v in Card.VALUES.iteritems():
            if self.value == v:
                val = k
        return str.format('{0}{1}', val, self.suit)

class Deck():
    def __init__(self):
        self.__cards = []
        for suit in Card.SUITS.values():
            for i in range(2,15):
                if i >= 10:
                    for k, v in Card.VALUES.iteritems():
                        if i == v: value = k
                else:
                    value = i
                self.__cards.append(Card('{0}{1}'.format(value, suit)))
    def shuffle(self):
        random.shuffle(self.__cards)
    def cards(self):
        return self.__cards
    def deal(self, n=1, players=[]):
        if players:
            for i in range(n):
                for player in players:
                    player.add_card(self.__cards.pop())
        else:
            cards = []
            for i in range(n):
                cards.append(self.__cards.pop())
            return cards

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
        if len(cards) < 1 or len(cards) > 5:
            raise InvalidHand(cards)
        self.__rank = None
        self.__cards = sorted([Card(c) for c in cards], reverse=True)
        self.__values = []
        self.rank()
    def __repr__(self):
        """Builds a string representation of the hand"""
        return str.format("Cards: {0} Rank: '{1}' Values: {2}",
            self.__cards,
            Hand.RANKS[self.rank()],
            self.values())
    def rank(self):
        """Get the hand rank
        
        Determines the rank of the poker hand if it has not already been
        computed, and returns it.
        """
        
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
            elif multiples:
                if multiples[0][1] > 3:
                    self.__rank = Hand.FOUR_OF_A_KIND
                elif multiples[0][1] == 3:
                    self.__rank = Hand.THREE_OF_A_KIND
                else:
                    self.__rank = Hand.ONE_PAIR
            mvalues = sorted([m[0] for m in multiples], reverse=True)
            self.__values = mvalues + [c.value for c in self.__cards if c.value not in mvalues]
            if not self.__rank:
                self.__rank = Hand.HIGH_CARD

        return self.__rank
    def values(self):
        """Returns a list of card values for the hand
        
        Values for sets are provided first in order of importance and descending
        strength, followed by all additional card values in order of descending
        strength. Used for comparison and sorting.
        
        Examples:
            Full House  ['5S', '5D', '5H', '8S', '8C']
            Values = [5, 8]
            
            Two Pair    ['9D', '9S', '5H', '5C', 'KH']
            Values = [9, 5, 13]
            
            Straight    ['AS', '2H', '3C', '4C', '5H']
            Values = [5, 4, 3, 2, 1]
        """
        if not self.__values:
            self.rank()
        return self.__values
    def cards(self):
        return self.__cards
    @staticmethod
    def create_best_hand(cards):
        """Create the strongest possible poker hand
        
        Using the supplied cards, this will build the strongest possible five-
        card poker hand.
        
        Uses smart hand creation if more than five cards are specified.
        """
        
        if len(cards) <= 5:
            return Hand(cards)
        else:
            for hand in Hand.create_best_hand_smart(cards):
                return hand
        return false
    @staticmethod
    def create_best_hand_bruteforce(cards):
        """Create the strongest possible poker hand
        
        Builds every possible poker hand from the supplied set of cards, and
        returns the strongest result.
        """
        
        combos = unique_combinations(cards, 5)
        hands = [Hand(combo) for combo in combos]
        hands = sorted(hands, reverse=True)
        return hands[0]
    @staticmethod
    def create_best_hand_smart(cards):
        """Create the strongest possible poker hand
        
        Intelligently seeks out the strongest possible poker hand from the
        supplied set of cards using the following steps:
        
        * Find all flushes
        * Find all straights
        ** Return best hand present in both flushes and straights, if applicable
        * Find all sets
        ** Return best quads with top remaining card
        ** Find and return best full house
        ** Find and return best three of a kind with top remaining cards
        ** Find and return best two pair with top remaining cards
        ** Find and return best single pair with top remaining cards
        ** Return top 5 cards
        """
        cards = sorted([Card(c) for c in cards], reverse=True)
        
        # Get all flushes
        flushes = []
        for suit in Card.SUITS.values():
            suited = [str(c) for c in cards if c.suit == suit]
            if len(suited) >= 5:
                combos = unique_combinations(suited, 5)
                for combo in combos: flushes.append(Hand(combo))
        flushes = sorted(flushes, reverse=True)
        if (flushes and flushes[0].rank() >= Hand.STRAIGHT_FLUSH):
            # Straight flush! No need to check anything else
            yield flushes[0]
        
        #Get all sets
        merged = {}
        for c in cards:
            if c.value in merged:
                merged[c.value] = merged[c.value] + 1
            else:
                merged[c.value] = 1
        multiples = [m for m in sorted(merged.items(), key = operator.itemgetter(1), reverse = True) if m[1] > 1]
        quads = [c[0] for c in multiples if c[1] == 4]
        quads = [c for c in cards if c.value in quads]
        trips = [c[0] for c in multiples if c[1] == 3]
        trips = [c for c in cards if c.value in trips]
        pairs = [c[0] for c in multiples if c[1] == 2]
        pairs = [c for c in cards if c.value in pairs]
        remaining = [c for c in cards if c.value not in [m[0] for m in multiples]]
        
        if quads:
            h = quads[:4]
            remaining = [c for c in cards if c.value not in [cc.value for cc in h]][:1]
            for r in remaining: h.append(r)
            yield Hand([str(c) for c in h])
        if trips and pairs:
            # Get a full house together
            h = trips[:3]
            remaining = pairs[:2]
            for r in remaining: h.append(r)
            yield Hand([str(c) for c in h])
        if flushes:
            # We've already got a flush, return it!
            yield flushes[0]
        # Look for a straight!
        mvals = sorted(merged.keys(), reverse=True)
        for i in range(0, len(mvals) -4, 1):
            if (mvals[i] - mvals[i + 4]) == 4:
                # Regular straight
                h = [[c for c in cards if c.value == v][0] for v in mvals[i:i + 5]]
                yield Hand([str(c) for c in h])
            elif 14 in [c.value for c in cards] and mvals[i + 1] == 5 and mvals[i + 4] == 2:
                # Ace low straight
                h = [[c for c in cards if c.value == v][0] for v in mvals[i + 1:i + 5]]
                h.append([c for c in cards if c.value == 14][0])
                yield Hand([str(c) for c in h])
        
        if trips:
            h = trips[:3]
            remaining = [c for c in cards if c.value not in [cc.value for cc in h]][:2]
            for r in remaining: h.append(r)
            yield Hand([str(c) for c in h])
        if pairs:
            if len(pairs) > 2:
                h = pairs[:4]
                remaining = [c for c in cards if c.value not in [cc.value for cc in h]][:1]
                for r in remaining: h.append(r)
                yield Hand([str(c) for c in h])
            else:
                h = pairs
                remaining = [c for c in cards if c.value not in [cc.value for cc in h]][:3]
                for r in remaining: h.append(r)
                yield Hand([str(c) for c in h])
        
        # High card, send the top 5 reverse-sorted cards
        yield Hand([str(c) for c in cards[:5]])
    def __cmp__(self, other):
        """Compare hand rankings
        
        Compares this hand with another by first checking rank, and if they are
        equal in that regard, by their card values. Used for sorting.
        """
        
        result = cmp(self.rank(), other.rank())
        if (result == 0):
            # Compare hand values
            for i in range(len(self.values())):
                result = cmp(self.values()[i], other.values()[i])
                if (result != 0):
                    return result
        return result

class ChinesePokerHand:
    def __init__(self, cards):
        if len(cards) != 13:
            raise InvalidHand();
        self.__cards = cards
        self.build_hands()
    def build_hands(self):
        self.build_hands_dumb()
    def build_hands_dumb(self):
        self.__bottom = Hand.create_best_hand([str(c) for c in self.__cards])
        self.__middle = Hand.create_best_hand([str(c) for c in self.__cards if c not in self.__bottom.cards()])
        self.__top = Hand.create_best_hand([str(c) for c in self.__cards if c not in (self.__bottom.cards() + self.__middle.cards())])
    def __repr__(self):
        return 'Chinese Poker Hand:\n\tTop: {0}\n\tMiddle: {1}\n\tBottom: {2}'.format(self.__top, self.__middle, self.__bottom)
    

class Player:
    def __init__(self, name):
        self.__name = name
        self.__hand = None
        self.__cards = []
        self.__community_cards = []
    def add_card(self, card, community=False):
        if community:
            self.__community_cards.append(card)
        else:
            self.__cards.append(card)
        
        # Rebuild and re-evaluate hand
        self.__hand = Hand.create_best_hand([str(c) for c in self.__community_cards + self.__cards])
    def discard(self, index):
        self.__cards.pop(index)
        self.__hand = Hand.create_best_hand([str(c) for c in self.__community_cards + self.__cards])
    def hand(self):
        return self.__hand
    def __repr__(self):
        return '"{0}"\n\tCards: {1}\n\tHand: {2}'.format(self.__name, self.__cards, self.__hand)
    def __cmp__(self, other):
        return cmp(self.hand(), other.hand())
    
if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    players = []
    for i in range(1,10):
        players.append(Player('Player {0}'.format(i)))
    community_cards = []
    deck.deal(2, players)
    deck.deal()
    community_cards.extend(deck.deal(3))
    deck.deal()
    community_cards.extend(deck.deal())
    deck.deal()
    community_cards.extend(deck.deal())
    for player in players:
        for card in community_cards:
            player.add_card(card, True)
    players = sorted(players, reverse=True)
    print 'Community', community_cards
    for player in players:
        print player
    
    print '\nChinese Poker Example'
    deck = Deck()
    deck.shuffle()
    for i in range(4):
        cards = deck.deal(13)
        chinese = ChinesePokerHand(cards)
        print chinese