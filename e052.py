"""Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits in some order.

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

MAX = 6

def main():
    i = 1
    while True:
        digits = sorted([int(c) for c in str(i)])
        d = [int(c) for c in str(i * MAX)]
        if len(d) > len(digits):
            # No chance of matching, jump ahead to the new digit count
            i = 10**(len(d) - 1)
            print 'Jumping to', i
            continue
        try:
            for multiplier in range(2, MAX + 1):
                if sorted([int(c) for c in str(i * multiplier)]) != digits:
                    raise Exception()
            print 'Smallest number with same digits in multiples up to {0}x: {1}'.format(MAX, i)
            break
        except:
            pass
        i = i + 1
            
if __name__ == '__main__':
    main()
