"""Using an efficient algorithm find the maximal sum in the triangle?

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (p067/triangle.txt), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (10**12) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

from e018 import Triangle

def main():
    vertex_data = []
    with open('p067/triangle.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            vertex_data = vertex_data + [int(v) for v in line.split(' ')]
    t = Triangle(vertex_data)
    t.find_path()
    path = t.get_path()
    print 'Path', [v.value for v in path]
    print 'Sum', sum([v.value for v in path])

if __name__ == '__main__':
    main()
