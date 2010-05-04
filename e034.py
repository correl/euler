import math

def sum_factorial(n):
    s = str(n)
    total = 0
    for c in s:
        total = total + math.factorial(int(c))
    return total

MAX = 100000

if __name__ == '__main__':
    total = 0
    i = 2
    while i <= MAX:
        i = i + 1
        if i == sum_factorial(i):
            print i
            total = total + i
    print 'Total:', total
