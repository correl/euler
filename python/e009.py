"""Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000.

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
    a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

TRIPLET_SUM = 1000

def main():
    for c in range(TRIPLET_SUM - 3, 3, -2):
        diff = TRIPLET_SUM - c
        for x in range(1, int(diff / 2) + 1):
            (a, b) = (x, diff - x)
            if a**2 + b**2 == c**2:
                print '{a}**2 + {b}**2 == {c}**2'.format(a=a, b=b, c=c)
                print 'Product: ', a*b*c

if __name__ == '__main__':
    main()
