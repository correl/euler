def pfactor(n):
    i = 2
    while (n % i != 0 and i < n):
        i = i + 1
    if i == n:
        return [n]
    p = pfactor(n // i)
    p.append(i)
    return sorted(p, reverse=True)

if __name__ == '__main__':
    print 'Prime factors of 600851475143:'
    print pfactor(600851475143)
