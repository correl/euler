# -*- coding: utf-8 -*-
"""
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:
    1£1 + 150p + 220p + 15p + 12p + 31p

How many different ways can £2 be made using any number of coins?
"""

def combinations(amount, denominations):
    total = 0
    if not denominations:
        return total
    denominations = sorted(denominations, reverse=True)
    for i in range(len(denominations)):
        d = denominations[i]
        n = 1
        while d * n <= amount:
            if d * n == amount:
                total += 1
            total += combinations(amount - (d * n), denominations[i+1:])
            n += 1
    return total

def main():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    print combinations(200, coins)

if __name__ == '__main__':
    main()
