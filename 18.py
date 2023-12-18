import fileinput

DIRS = {
    'R': (1, 0), 'L': (-1, 0),
    'U': (0, -1), 'D': (0, 1),
}

points1 = [(0, 0)]
points2 = [(0, 0)]
for line in fileinput.input():
    d, n, c = line.split()
    n = int(n)
    dx, dy = DIRS[d]
    x, y = points1[-1]
    points1.append((x + dx * n, y + dy * n))

    n = int(c[2:-2], 16)
    dx, dy = DIRS['RDLU'[int(c[-2])]]
    x, y = points2[-1]
    points2.append((x + dx * n, y + dy * n))

def area(points):
    area = 0
    perimeter = 0
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        area += x0 * y1 - y0 * x1
        perimeter += abs(x0 - x1) + abs(y0 - y1)
    return area // 2 + perimeter // 2 + 1

print(area(points1))
print(area(points2))
