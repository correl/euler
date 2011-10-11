"""Calculate the sum of all the primes below two million.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from e007 import prime_generator

def main():
    print 'Fetching all primes for n < 2,000,000'
    total = 0
    generator = prime_generator()
    while True:
        prime = generator.next()
        if prime >= 2000000:
            break
        total += prime
    print 'Sum:', total

if __name__ == '__main__':
    main()
