"""What is the smallest number divisible by each of the numbers 1 to 20?

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
"""

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
def main():
    print 'Smallest number: ', divisible(20)

if __name__ == '__main__':
    main()
