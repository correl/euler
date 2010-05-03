n = 1
total = 1
size = 1

MAX_SIZE = 1001

while size <= MAX_SIZE:
    for i in range(4):
        n = n + (size - 1)
        if n > 1:
            total = total + n
    size = size + 2

print 'Total:', total
