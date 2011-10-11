"""What is the sum of the digits of the number 21000?

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
"""

n = 2**1000

def main():
    s = str(n)
    total = 0
    for c in s:
        total = total + int(c)
    print 'Sum of digits for {0}: {1}'.format(n, total)

if __name__ == '__main__':
    main()
