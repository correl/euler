TRIPLET_SUM = 1000

for c in range(TRIPLET_SUM - 3, 3, -2):
    diff = TRIPLET_SUM - c
    for x in range(1, int(diff / 2) + 1):
        (a, b) = (x, diff - x)
        if a**2 + b**2 == c**2:
            print '{a}**2 + {b}**2 == {c}**2'.format(a=a, b=b, c=c)
            print 'Product: ', a*b*c
