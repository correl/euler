MAX = 1000000

def binary(n):
    return '{0:b}'.format(n)

if __name__ == '__main__':
    total = 0
    i = 0 
    while i < MAX:
        i = i + 1
        n = str(i)
        if n != n[::-1]:
            continue
        b = binary(i)
        if b != b[::-1]:
            continue
        print n, b
        total = total + i
    print 'Total:', total
