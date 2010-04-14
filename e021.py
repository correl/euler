from e007 import is_prime
from e012 import factor

def proper_divisors(n):
    """Returns the proper divisors of n
    
    Proper divisors are defined as numbers less than n which divide evenly into n
    """
    divisors = factor(n)
    # Knock off the last factor, since it is equal to n
    return divisors[:-1]

if __name__ == '__main__':
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