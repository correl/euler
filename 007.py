def primes(limit):
    primes = [2]
    i = 3
    while len(primes) < limit:
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i = i + 2
    return primes

print '6th Prime', primes(6)[-1]
print '10001st Prime', primes(10001)[-1]
