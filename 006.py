def squarediff(n):
    print 'Checking for n =', n
    sumofsquares = sum([x**2 for x in range(n + 1)])
    print 'Sum of squares', sumofsquares
    squareofsum = sum(range(n + 1))**2
    print 'Square of sum', squareofsum
    print 'Difference', squareofsum - sumofsquares

if __name__ == '__main__':
    squarediff(10)
    squarediff(100)
