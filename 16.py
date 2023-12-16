from collections import *
from itertools import *
from math import *
import fileinput
import re

grid = list(line.rstrip() for line in fileinput.input())

width = len(grid[0])
height = len(grid)

E = (1, 0)
W = (-1, 0)
N = (0, -1)
S = (0, 1)

NEXT = {
    (E, '|'): [N, S],
    (E, '\\'): [S],
    (E, '/'): [N],

    (W, '|'): [N, S],
    (W, '\\'): [N],
    (W, '/'): [S],

    (N, '-'): [E, W],
    (N, '\\'): [W],
    (N, '/'): [E],

    (S, '-'): [E, W],
    (S, '\\'): [E],
    (S, '/'): [W],
}

def step(grid, positions):
    result = set()
    for x, y, d in positions:
        c = grid[y][x]
        k = (d, c)
        dirs = NEXT.get(k, [d])
        for d in dirs:
            dx, dy = d
            x += dx
            y += dy
            if x < 0 or x >= width:
                continue
            if y < 0 or y >= height:
                continue
            result.add((x, y, d))
    return result

def run(x, y, d):
    positions = {(x, y, d),}
    P = set()
    seen = set()
    while positions:
        P |= {(x, y) for x, y, d in positions}
        positions = step(grid, positions)
        positions = {x for x in positions if x not in seen}
        seen |= positions
    return len(P)

print(run(0, 0, E))

scores = []
for y in range(height):
    scores.append(run(0, y, E))
    scores.append(run(width-1, y, W))
for x in range(width):
    scores.append(run(x, 0, S))
    scores.append(run(x, height-1, N))
print(max(scores))
