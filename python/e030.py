"""Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 14 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def power_sums(n):
    numbers = []
    i = 9
    while i <= 10**(n+1):
        i = i + 1
        if int(max(str(i)))**n > i:
            continue
        s = sum([int(c)**n for c in str(i)])
        if i == s:
            numbers.append(i)
    return numbers

def main():
    p = power_sums(4)
    print 'power_sums(4)', p, sum(p)
    p = power_sums(5)
    print 'power_sums(5)', p, sum(p)

if __name__ == '__main__':
    main()
