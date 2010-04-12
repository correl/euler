n = 2**1000

s = str(n)
total = 0
for c in s:
    total = total + int(c)
print 'Sum of digits for {0}: {1}'.format(n, total)
