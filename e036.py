"""Find the sum of all numbers less than one million, which are palindromic in base 10 and base 2.

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

MAX = 1000000

def binary(n):
    return '{0:b}'.format(n)

def main():
    total = 0
    i = 0 
    while i < MAX:
        i = i + 1
        n = str(i)
        if n != n[::-1]:
            continue
        b = binary(i)
        if b != b[::-1]:
            continue
        print n, b
        total = total + i
    print 'Total:', total

if __name__ == '__main__':
    main()
