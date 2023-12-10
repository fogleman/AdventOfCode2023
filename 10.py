from collections import defaultdict
import fileinput

NEIGHBORS = {
    '|': [(0, -1), (0, 1)],
    '-': [(-1, 0), (1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(-1, 0), (0, -1)],
    '7': [(-1, 0), (0, 1)],
    'F': [(0, 1), (1, 0)],
}

CW = {
    (0, -1): (1, 0), (1, 0): (0, 1),
    (0, 1): (-1, 0), (-1, 0): (0, -1),
}

CCW = dict((v, k) for k, v in CW.items())

grid = defaultdict(lambda: '.')
start = None
for y, line in enumerate(fileinput.input()):
    for x, c in enumerate(line.rstrip()):
        grid[(x, y)] = c
        if c == 'S':
            start = (x, y)

def starting_tile(grid, start):
    x, y = start
    for tile in NEIGHBORS:
        for dx, dy in NEIGHBORS[tile]:
            other = grid[(x + dx, y + dy)]
            if not any((x + dx + nx, y + dy + ny) == start
                for nx, ny in NEIGHBORS.get(other, [])):
                    break
        else:
            return tile

grid[start] = starting_tile(grid, start)

def find_path(grid, start):
    path = []
    seen = set()
    x, y = start
    while True:
        path.append((x, y))
        seen.add((x, y))
        for dx, dy in NEIGHBORS[grid[(x, y)]]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in seen:
                x, y = nx, ny
                break
        else:
            break
    return path

path = find_path(grid, start)
print(len(path) // 2)

def flood_fill(grid, seen, start):
    result = set()
    queue = [start]
    while queue:
        x, y = queue.pop()
        if (x, y) in seen or (x, y) in result:
            continue
        result.add((x, y))
        for nx, ny in ((x, y-1), (x-1, y), (x, y+1), (x+1, y)):
            if (nx, ny) in grid and (nx, ny) not in seen:
                queue.append((nx, ny))
    return result

def inside(grid, path, d):
    result = set()
    seen = set(path)
    for a, b in zip(path, path[1:]):
        x0, y0 = a
        x1, y1 = b
        dx, dy = d[(x1 - x0, y1 - y0)]
        for p in [(x0 + dx, y0 + dy), (x1 + dx, y1 + dy)]:
            if p not in result:
                result |= flood_fill(grid, seen, p)
    return result

a = len(inside(grid, path, CW))
b = len(inside(grid, path, CCW))
print(min(a, b))
