from e021 import proper_divisors

abundant = []
total = 1

i = 2
while i < 28123:
    s = sum(proper_divisors(i))
    if s > i:
        abundant.append(i)
    summed = False
    for a in abundant:
        if i - a in abundant:
            summed = True
            break
    if not summed:
        total = total + i
    i = i + 1

print 'Total:', total
