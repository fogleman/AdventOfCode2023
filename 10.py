from itertools import *
from collections import *
from math import *
import fileinput
import heapq
import re

grid = {}
start = None
for y, line in enumerate(fileinput.input()):
    for x, c in enumerate(line.rstrip()):
        grid[(x, y)] = c
        if c == 'S':
            start = (x, y)

x0 = min(x for x, y in grid)
y0 = min(y for x, y in grid)
x1 = max(x for x, y in grid)+1
y1 = max(y for x, y in grid)+1

NEIGHBORS = {
    '|': [(0, 1), (0, -1)],
    '-': [(1, 0), (-1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)],
    'S': [(1, 0), (0, 1)],
    '.': [],
}

def shortest_path(cells, source, target):
    dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
    seen, queue = set(), [(0, source)]
    while queue:
        d, p = heapq.heappop(queue)
        if p == target:
            return d
        seen.add(p)
        for dx, dy in zip(dxs, dys):
            q = (p[0] + dx, p[1] + dy)
            if q in cells and q not in seen:
                heapq.heappush(queue, (d + 1, q))

def heuristic(p, t):
    return abs(p[0] - t[0]) + abs(p[1] - t[1])

def shortest_path(cells, source, target):
    seen, queue = set(), [(heuristic(source, target), 0, source)]
    while queue:
        _, d, p = heapq.heappop(queue)
        if p == target:
            return d
        seen.add(p)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            q = (p[0] + dx, p[1] + dy)
            if q in cells and q not in seen:
                heapq.heappush(queue,
                    (heuristic(q, target), d + 1, q))

def search(grid, x, y):
    dist = {}
    q = [(x, y, 0)]
    M = 0
    while q:
        nx, ny, d = q.pop(0)
        if (nx, ny) not in grid:
            continue
        if dist.get((nx, ny), 1e9) <= d:
            continue
        dist[(nx, ny)] = d
        if d > M:
            M = d
            print(M, nx, ny)
        c = grid[(nx, ny)]
        for dx, dy in NEIGHBORS[c]:
            nnx, nny = nx + dx, ny + dy
            q.append((nnx, nny, d + 1))

    keys = set(dist)
    for y in range(y0, y1):
        for x in range(x0, x1):
            print('X ' if (x, y) in keys else '. ', end='')
        print()
        print()

    cells = set()
    for y in range(y0, y1):
        for x in range(x0, x1):
            if (x, y) in keys:
                continue
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    cells.add((3 * x + dx, 3 * y + dy))
    for x, y in keys:
        # for dx in range(-1, 2):
        #     for dy in range(-1, 2):
        #         cells.remove((3 * x + dx, 3 * y + dy))
        cells.add((3 * x + 0, 3 * y + 0))
        for dx, dy in NEIGHBORS[grid[(x, y)]]:
            cells.add((3 * x + dx, 3 * y + dy))
    count = 0
    for p in cells:
        x, y = p
        if x%3==0 and y%3==0:
            if shortest_path(cells, p, (0, 0)) is None:
                count += 1
    print(count)

    for y in range(y0*3, y1*3):
        for x in range(x0*3, x1*3):
            print('. ' if (x, y) in cells else 'X ', end='')
        print()
        print()

search(grid, *start)
