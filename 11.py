import fileinput

grid = []
for line in fileinput.input():
    grid.append(line.rstrip())

def empty_y(grid):
    h = len(grid)
    w = len(grid[0])
    result = set()
    for y in range(h):
        row = [grid[y][x] for x in range(w)]
        if all(c == '.' for c in row):
            result.add(y)
    return result

def empty_x(grid):
    h = len(grid)
    w = len(grid[0])
    result = set()
    for x in range(w):
        col = [grid[y][x] for y in range(h)]
        if all(c == '.' for c in col):
            result.add(x)
    return result

def find_galaxies(grid):
    h = len(grid)
    w = len(grid[0])
    result = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '#':
                result.append((x, y))
    return result

positions = find_galaxies(grid)
X = empty_x(grid)
Y = empty_y(grid)
total = 0
for i, (x0, y0) in enumerate(positions):
    for x1, y1 in positions[i+1:]:
        X0, X1 = min(x0, x1), max(x0, x1)
        Y0, Y1 = min(y0, y1), max(y0, y1)
        d = abs(x1-x0) + abs(y1-y0)
        for x in range(X0, X1+1):
            if x in X:
                d += 1000000-1
        for y in range(Y0, Y1+1):
            if y in Y:
                d += 1000000-1
        total += d
print(total)
