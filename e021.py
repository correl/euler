"""Evaluate the sum of all amicable pairs under 10000.

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from e007 import is_prime
from e012 import factor

def proper_divisors(n):
    """Returns the proper divisors of n
    
    Proper divisors are defined as numbers less than n which divide evenly into n
    """
    divisors = factor(n)
    # Knock off the last factor, since it is equal to n
    return divisors[:-1]

def main():
    MIN = 2
    MAX = 10000
    
    sums = {}
    amicable = []
    i = MIN
    while i < MAX:
        if not is_prime(i):
            s = sum(proper_divisors(i))
            sums[i] = s
            if s in sums and i == sums[s] and i != s:
                print i, s, sums[s]
                amicable.append(i)
                amicable.append(s)
        i = i + 1
    print 'Sum of amicable numbers less than {0}: {1}'.format(MAX, sum(amicable))
if __name__ == '__main__':
    main()
