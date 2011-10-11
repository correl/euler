"""Investigate the number of primes that lie on the diagonals of the spiral grid.

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13  62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

from e007 import is_prime

def spiral_corners_generator():
    n = 1
    size = 1
    while True:
        corners = []
        if size == 1:
            yield [1]
        else:
            for i in range(4):
                n = n + (size - 1)
                corners.append(n)
            yield corners
        size = size + 2

def main():
    size = 1
    diagonals = 0
    primes = 0
    for corners in spiral_corners_generator():
        diagonals = diagonals + len(corners)
        primes = primes + len([c for c in corners if is_prime(c)])
        pct = primes / float(diagonals) * 100
        if size > 7 and pct < 10.0:
            break
        size = size + 2
        
    print 'Side Length: {0}, Percentage: {1}'.format(size, pct)

if __name__ == '__main__':
    main()