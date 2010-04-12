def collatz(n):
    steps = 0
    while n > 1:
        steps = steps + 1
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
    return steps

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
