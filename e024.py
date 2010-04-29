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

if __name__ == '__main__':
    print 'Testing permutations of 0..2:'
    list = [str(i) for i in [0, 1, 2]]
    for i in range(1, math.factorial(len(list)) + 1):
        p = lexicographic_permutation(list, i)
        print '\tPermutation', i, ''.join(p)

    list = [str(i) for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    p = lexicographic_permutation(list, 1000000)
    print '1 millionth lexicographic permutation of 0..9:', ''.join(p)
