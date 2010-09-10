"""Find the 10001st prime.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""

import math

def is_prime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    
    r = math.floor(math.sqrt(n))
    f = 5
    while f <= r:
        if (n % f == 0) or (n % (f + 2) == 0):
            return False
        f = f + 6
    return True

def prime_generator():
    i = 1
    yield 2
    while True:
        i += 2
        if is_prime(i):
            yield i

def primes(max_count = 0, max_value = 0):
    if not max_count and not max_value:
        raise Exception('There must be a constraint on how many primes to return!')
    primes = [2]
    i = 1
    while (not max_count or len(primes) < max_count) \
    and (not max_value or i < max_value):
        i = i + 2
        if is_prime(i):
            primes.append(i)
    return primes

def main():
    i = 0
    prime = 0
    generator = prime_generator()
    while i < 10000:
        i += 1
        prime = generator.next()
        if i == 6:
            print '6th Prime', prime
    print '10001st Prime', prime

if __name__ == '__main__':
    main()
