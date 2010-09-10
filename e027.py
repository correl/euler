"""Find the value of d < 1000 for which 1/d contains the longest recurring cycle.A unit fraction contains 1 in the numerator.

The decimal representation of the unit fractions with denominators 2 to 10 are given:
    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from decimal import Decimal
from e003 import pfactor

def coprime(a, b):
    """Are integers a and b coprime?"""

    primes_a = pfactor(a)
    primes_b = pfactor(b)
    primes = [p for p in primes_a if p in primes_b]
    return bool(primes)

def period_length(numerator, denominator):
    """Determine the period length of a non-terminating decimal"""
    
    length = None
    numerator = Decimal(numerator)
    denominator = Decimal(denominator)
    if numerator == 1:
        if denominator == 1:
            return 1
        primes = pfactor(int(denominator))
        
        """
        From Wikipedia:
            Terminating decimals represent rational numbers of the form
            k/2^n5^m

            However, a terminating decimal also has a representation as a
            repeating decimal, obtained by decreasing the final (nonzero)
            digit by one and appending an infinitely repeating sequence of
            nines. 1 = 0.999999... and 1.585 = 1.584999999... are two
            examples of this.
        """
        if len([p for p in primes if p not in [2, 5]]) == 0:
            return 1

        if coprime(denominator, 10):
            pass
    else:
        raise Exception('Non-reciprocal period detection not yet implemented')
    return length

def main():
    MAX = 10
    longest_cycle = 0
    for i in xrange((MAX), 1, -1):
        # The period of 1/k for integer k is always ² k ? 1.
        if longest_cycle >= i:
            break
        
        cycle = period_length(1, i)
        fraction = Decimal(1) / Decimal(i)
        print '1/{0} = {1} ({2})'.format(i, fraction, cycle), fraction.is_subnormal()
if __name__ == '__main__':
    main()