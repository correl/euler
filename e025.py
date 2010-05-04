"""What is the first term in the Fibonacci sequence to contain 1000 digits?

The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

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

def main():
    (term, value) = fibonacci(10**999, 10**999)
    print 'First Fibonacci term with at least 1000 digits is #{0}: {1}'.format(term, value)

if __name__ == '__main__':
    main()
