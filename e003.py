def factor(n):
    i = 2
    while (n % i != 0 and i < n):
        i = i + 1
    if i == n:
        return [n]
    p = factor(n // i)
    p.append(i)
    return sorted(p, reverse=True)

print 'Prime factors of 600851475143:'
print factor(600851475143)
