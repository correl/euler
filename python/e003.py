"""Find the largest prime factor of a composite number.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def pfactor(n):
    i = 2
    while (n % i != 0 and i < n):
        i = i + 1
    if i == n:
        return [n]
    p = pfactor(n // i)
    p.append(i)
    return sorted(p, reverse=True)

def main():
    print 'Prime factors of 600851475143:'
    print pfactor(600851475143)

if __name__ == '__main__':
    main()
