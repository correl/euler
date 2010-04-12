def divisible(n):
    i = 0
    while True:
        i = i + 1
        x = n * i
        for ii in range(n, 0, -1):
            if x % ii != 0:
                break
        if ii == 1:
            return x
if __name__ == '__main__':
    print 'Smallest number: ', divisible(20)
