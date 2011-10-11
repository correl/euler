"""Finding the nth digit of the fractional part of the irrational number.

An irrational decimal fraction is created by concatenating the positive integers:
    0.12345678910[1]112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.
    d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
"""

from e011 import product

def irrational_generator():
    i = 0
    pos = 0
    data = []
    while True:
        i = i + 1
        s = str(i)
        for c in s:
            yield int(c)

def main():
    values = []
    counter = 0
    stops = [10**n for n in range(7)]
    for i in irrational_generator():
        counter = counter + 1
        if counter in stops:
            values.append(i)
        if counter == max(stops):
            break
    print 'Values: ', values
    print 'Product: ', product(values)

if __name__ == '__main__':
    main()
