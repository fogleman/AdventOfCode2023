import fileinput

grid = [line.rstrip() for line in fileinput.input()]

w, h = len(grid[0]), len(grid)
xs = set(x for x in range(w) if all(grid[y][x] == '.' for y in range(h)))
ys = set(y for y in range(h) if all(grid[y][x] == '.' for x in range(w)))
positions = [(x, y) for y in range(h) for x in range(w) if grid[y][x] == '#']

for e in [2, 1000000]:
    total = 0
    for i, (x0, y0) in enumerate(positions):
        for x1, y1 in positions[i+1:]:
            X0, X1 = min(x0, x1), max(x0, x1)
            Y0, Y1 = min(y0, y1), max(y0, y1)
            total += X1 - X0 + Y1 - Y0
            total += sum(x in xs for x in range(X0, X1)) * (e - 1)
            total += sum(y in ys for y in range(Y0, Y1)) * (e - 1)
    print(total)
