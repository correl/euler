"""
Calculate the number of possible paths from the top left corner to the bottom
right, without backtracking (no moving up or left)

i.e., for a 2x2 grid:
     _ _
    |_|_|
    |_|_|
    
Paths to each point, forming a Pascal Triangle:
    1 1 1
    1 2 3
    1 3 6

    001 001 001 001
    001 002 003 004
    001 003 006 010
    001 004 010 020
"""
def pascal(row, col):
    val = 1
    r = row + 1
    for c in range(1, col + 1):
        val = (val * ((r - c) / float(c)))
    return int(val)
def paths(size):
    return pascal(size + (size - 2), size - 1)

if __name__ == '__main__':
    # 20x20 grid
    # Points = cubes + 1
    size = 21
    print 'Paths: ', paths(size)
