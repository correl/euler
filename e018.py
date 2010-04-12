from e012 import triangle

class Vertex:
    """Holds information on each vertex in the triangle
    
    The weight represents the weight of any edge between an adjacent vertex and
    this one
    """
    def __init__(self, value):
        self.value = value
        self.weight = 100 - self.value
        self.min_distance = float('+inf')
        self.previous_vertex = None
        self.adjacent = []
    def add_adjacent(self, vertex):
        self.adjacent.append(vertex)
    def __cmp__(self, other):
        return cmp(self.min_distance, other.min_distance)
    def __repr__(self):
        return '{0} ({1})'.format(self.value, [a.value for a in self.adjacent])

class Triangle:
    def __init__(self, vertex_data):
        self.vertices = []
        i = 0
        row = 1
        for v in vertex_data:
            if (i >= triangle(row)):
                row = row + 1
            vertex = Vertex(v)
            if row > 1:
                # Find upwards adjacent vertices
                above_row = self.vertices[triangle(row - 2):triangle(row - 1)]
                total_this_row = triangle(row) - triangle(row - 1)
                pos = i - triangle(row - 1)  + 1
                start = int((pos / float(total_this_row)) * len(above_row)) - 1
                end = int(((pos + 1) / float(total_this_row)) * len(above_row))
                adjacent = above_row[start if start >= 0 else 0:end]
                for a in adjacent:
                    vertex.add_adjacent(a)
            self.vertices.append(vertex)
            i = i + 1
        self.rows = row
        if len(self.vertices) != triangle(self.rows):
            raise Exception('Invalid vertex set')
    def find_path(self):
        """Implementation of Dijkstra's algorithm"""
        
        # Reset vertice info
        for v in self.vertices:
            v.min_distance = float('+inf')
            v.previous_vertex = None
        orig = Vertex(100)
        orig.min_distance = 0
        adjacent = self.vertices[triangle(self.rows - 1):]
        for a in adjacent:
            orig.add_adjacent(a)
        Q = [orig] + [v for v in self.vertices]
        while len(Q) > 0:
            u = min(Q)
            if u.min_distance == float('+inf'):
                return False
            Q.remove(u)
            for v in u.adjacent:
                distance = u.min_distance + v.weight
                if distance < v.min_distance:
                    v.min_distance = distance
                    v.previous_vertex = u
        return True
    def get_path(self):
        """Returns the found path as a list of vertices, from the top of the
        triangle to the bottom
        """
        
        v = self.vertices[0]
        path = [v]
        for i in range(self.rows - 1):
            v = v.previous_vertex
            if not v:
                raise Exception('Missing or incomplete path!')
            path.append(v)
        return path

if __name__ == '__main__':
    vertex_data = []
    with open('p018/triangle.txt', 'r') as f:
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
