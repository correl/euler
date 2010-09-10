"""Find the sum of all eleven primes that are both truncatable from left to right and right to left.

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from e007 import is_prime, prime_generator

def is_truncatable(prime):
    if prime < 10:
        return False
    rtl = [int(str(prime)[:i]) for i in xrange(len(str(prime))) if i > 0 and i < len(str(prime))]
    ltr = [int(str(prime)[i:]) for i in xrange(len(str(prime))) if i > 0 and i < len(str(prime))]
    truncated = sorted(rtl + ltr, reverse=True)
    for n in truncated:
        if not is_prime(n):
            return False
    print 'OK', prime, rtl, ltr
    return True

def main():
    truncatable = []
    generator = prime_generator()
    print 'Searching for truncatable primes...'
    while len(truncatable) < 11:
        prime = generator.next()
        if is_truncatable(prime):
            truncatable.append(prime)
    print 'Found {0} truncatable primes'.format(len(truncatable))
    print 'Sum:', sum(truncatable)

if __name__ == '__main__':
    main()