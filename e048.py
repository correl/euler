"""Find the last ten digits of 1**1 + 2**2 + ... + 1000**1000.

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

def powerseries(n):
    i = 1
    total = 0
    while i <= n:
        total = total + i**i
        i = i + 1
    return total

def main():
    val = str(powerseries(1000))
    print 'Last 10:', val[-10:]

if __name__ == '__main__':
    main()
