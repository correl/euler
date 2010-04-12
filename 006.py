def squarediff(n):
    sumofsquares = sum([x**2 for x in range(n + 1)])
    print 'Sum of squares', sumofsquares
    squareofsum = sum(range(n + 1))**2
    print 'Square of sum', squareofsum
    print 'Difference', squareofsum - sumofsquares

squarediff(10)
squarediff(100)
