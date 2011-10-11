"""How many circular primes are there below one million?

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from e007 import is_prime, prime_generator

class NotCircular(Exception):
    pass

def permutations(items, n):
    if n == 0:
        yield []
    else:
        for i in xrange(len(items)):
            for cc in permutations(items[:i] + items[i + 1:], n - 1):
                yield [items[i]] + cc

def cyclic_rotation(n):
    if n < 10:
        yield n
    else:
        s = str(n)
        for i in xrange(len(s)):
            yield int(s[i:] + s[:i])

def main():
    MAX = 1000000
    circular_primes = []
    print 'Searching for circular primes for p < {0}...'.format(MAX)
    for prime in prime_generator():
        if prime >= MAX:
            break
        try:
            # Ensure the prime *can* be circular
            if prime > 9:
                for c in [n for n in str(prime) if n not in ['1', '3', '7', '9']]:
                    raise NotCircular()
            # Check all permutations
            for rotation in cyclic_rotation(prime):
                if not is_prime(rotation):
                    raise NotCircular()
            circular_primes.append(prime)
        except NotCircular:
            pass
        # Clear all permutations from the list?
    print 'Circular Primes ({0}): {1}'.format(len(circular_primes), circular_primes)

if __name__ == '__main__':
    main()
