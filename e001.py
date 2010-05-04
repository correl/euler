"""Add all the natural numbers below one thousand that are multiples of 3 or 5.

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def main():
    total = 0
    for x in range(1000):
        if (0 == x % 3) or (0 == x % 5):
            total = total + x
    print 'Answer', total

if __name__ == '__main__':
    main()
