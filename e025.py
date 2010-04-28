def fibonacci(n, limit=None):
    fibonacci = [0, 1]
    i = 2
    while i <= n:
        f = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(f)
        if limit and f >= limit:
            return (i, fibonacci[-1])
        i = i + 1
    return (n, fibonacci[n])

if __name__ == '__main__':
    (term, value) = fibonacci(10**999, 10**999)
    print 'First Fibonacci term with at least 1000 digits is #{0}: {1}'.format(term, value)
