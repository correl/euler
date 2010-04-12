from e018 import Triangle
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