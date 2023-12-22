import fileinput

grid = list(line.rstrip() for line in fileinput.input())
w, h = len(grid[0]), len(grid)

walls = set()
start = None
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '#':
            walls.add((x, y))
        if c == 'S':
            start = (x, y)

def count(position, steps, memo, points):
    if steps == 0:
        points.add(position)
        return
    x, y = position
    key = (x, y, steps)
    if key in memo:
        return
    result = 0
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        q = ((x + dx) % w, (y + dy) % h)
        if q in walls:
            continue
        count((x + dx, y + dy), steps - 1, memo, points)
    memo[key] = True

for i in [65, 65+131, 65+262]:
    points = set()
    memo = {}
    count(start, i, memo, points)
    print(i, len(points))
