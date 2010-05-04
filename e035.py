from e007 import primes

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

if __name__ == '__main__':
    MAX = 1000000
    circular_primes = []
    print 'Generating primes for p < {0}...'.format(MAX)
    prime_list = primes(0, MAX)
    print 'Searching for circular primes...'
    for prime in prime_list:
        try:
            # Ensure the prime *can* be circular
            if prime > 9:
                for c in [n for n in str(prime) if n not in ['1', '3', '7', '9']]:
                    raise NotCircular()
            # Check all permutations
            for rotation in cyclic_rotation(prime):
                if rotation not in prime_list:
                    raise NotCircular()
            circular_primes.append(prime)
        except NotCircular:
            pass
        # Clear all permutations from the list?
    print 'Circular Primes ({0}): {1}'.format(len(circular_primes), circular_primes)
