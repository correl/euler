from e003 import pfactor
from p054.poker import unique_combinations

def triangle(n):
    x = 0
    for i in range(n + 1):
        x = x + i
    return x

def badfactor(n):
    f = []
    for i in range(n, 0, -1):
        if n % i == 0:
            f.append(i)
    return f

def product(l):
    p = 1
    for n in l:
        p = p * n
    return p

def factor(n):
    primes = pfactor(n)
    factors = []
    pow = {}
    for p in primes:
        if p not in pow.keys():
            pow[p] = 0
        pow[p] = pow[p] + 1
        factors.append(p**pow[p])
    for p in [f for f in factors if f < n / 2]:
        factors.append(n / p)
    
    if n not in factors:
        factors.append(n)
    
    return sorted(set(factors))
if __name__ == '__main__':
    i = 1
    while True:
        i = i + 1
        t = triangle(i)
        f = factor(t)
        print 'Checking triangle', i, t
        if len(f) > 500:
            break
    
    print 'Triangle number {0} has {1} factors ({2})'.format(t, len(f), f)