"""Calculate the sum of all the primes below two million.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from e007 import primes;

def main():
    print 'Fetching all primes for n < 2,000,000'
    p = primes(0, 2000000)
    print 'Sum:', sum(p)

if __name__ == '__main__':
    main()
