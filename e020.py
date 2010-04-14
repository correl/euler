# Could use math.factorial, but that takes the fun out of it, doesn it
def factorial(n):
    f = n
    i = n - 1
    while i > 1:
        f = f * i
        i = i - 1
    return f

f = str(factorial(100))
sum = 0
for c in f:
    sum = sum + int(c)

print 'Sum of digits in 100!:', sum