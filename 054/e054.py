import poker

if __name__ == '__main__':
    wins = 0
    counter = 0
    with open('poker.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            counter = counter + 1
            cards = line.strip().split()
            one = poker.Hand(cards[:5])
            two = poker.Hand(cards[-5:])
            result = poker.Hand.compare(one, two)
            if result > 0:
                wins = wins + 1
                outcome = 'Player One wins'
            elif result == 0:
                outcome = 'Tie'
            else:
                outcome = 'Player Two wins'
            print "Hand #{0}: {1}\n {2}\n {3}".format(
                counter,
                outcome,
                one,
                two)
    print "Player one won {0} hands".format(wins)
