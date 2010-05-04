"""What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import math

def lexicographic_permutation(list, position):
    items = len(list)
    list = sorted(list)
    p = []
    position = position - 1
    while len(p) < items:
        index = 0 
        # Find the next index to pop
        l = len(list) - 1
        f = math.factorial(l) if l else 0
        while position and position >= f:
            position = position - f
            index = index + 1

        p.append(list.pop(index))
    return p

def main():
    print 'Testing permutations of 0..2:'
    list = [str(i) for i in [0, 1, 2]]
    for i in range(1, math.factorial(len(list)) + 1):
        p = lexicographic_permutation(list, i)
        print '\tPermutation', i, ''.join(p)

    list = [str(i) for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    p = lexicographic_permutation(list, 1000000)
    print '1 millionth lexicographic permutation of 0..9:', ''.join(p)

if __name__ == '__main__':
    main()
