"""What is the difference between the sum of the squares and the square of the sums?

The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def squarediff(n):
    print 'Checking for n =', n
    sumofsquares = sum([x**2 for x in range(n + 1)])
    print 'Sum of squares', sumofsquares
    squareofsum = sum(range(n + 1))**2
    print 'Square of sum', squareofsum
    print 'Difference', squareofsum - sumofsquares

def main():
    squarediff(10)
    squarediff(100)

if __name__ == '__main__':
    main()
