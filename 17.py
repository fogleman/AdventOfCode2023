import fileinput
import heapq

grid = [list(map(int, line.rstrip())) for line in fileinput.input()]
w, h = len(grid[0]), len(grid)

def shortest_path(grid, source, target, part):
    seen = set()
    queue = [(0, *source, (0, 0), 10)]
    while queue:
        s, x, y, v, n = heapq.heappop(queue)
        vx, vy = v
        if (x, y) == target:
            return s
        if (x, y, v, n) in seen:
            continue
        seen.add((x, y, v, n))
        for d in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            dx, dy = d
            nx, ny = x + dx, y + dy
            if dx == -vx and dy == -vy:
                continue
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            m = n + 1 if d == v else 1
            if part == 1:
                if m > 3:
                    continue
            else:
                if m > 10:
                    continue
                if n < 4 and m == 1:
                    continue
            heapq.heappush(queue, (s + grid[ny][nx], nx, ny, d, m))

for part in [1, 2]:
    print(shortest_path(grid, (0, 0), (w - 1, h - 1), part))
