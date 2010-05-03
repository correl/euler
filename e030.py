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

p = power_sums(4)
print 'power_sums(4)', p, sum(p)
p = power_sums(5)
print 'power_sums(5)', p, sum(p)
