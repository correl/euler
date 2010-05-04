"""Find the longest sequence using a starting number under one million.

The following iterative sequence is defined for the set of positive integers:
    n  n/2 (n is even)
    n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
    13  40  20  10  5  16  8  4  2  1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz(n):
    steps = 0
    while n > 1:
        steps = steps + 1
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
    return steps

def main():
    i = 1000000
    max = 0
    maxnum = i
    while i > 1:
        i = i - 1
        c = collatz(i)
        if c > max:
            max = c
            maxnum = i
    print 'Max was {0} steps for {1}'.format(max, maxnum)

if __name__ == '__main__':
    main()
