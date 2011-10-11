"""Find the sum of all numbers which are equal to the sum of the factorial of their digits.

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math

def sum_factorial(n):
    s = str(n)
    total = 0
    for c in s:
        total = total + math.factorial(int(c))
    return total

MAX = 100000

def main():
    total = 0
    i = 2
    while i <= MAX:
        i = i + 1
        if i == sum_factorial(i):
            print i
            total = total + i
    print 'Total:', total

if __name__ == '__main__':
    main()
