def powerseries(n):
    i = 1
    total = 0
    while i <= n:
        total = total + i**i
        i = i + 1
    return total

if __name__ == '__main__':
    val = str(powerseries(1000))
    print 'Last 10:', val[-10:]
