from collections import *
from itertools import *
from math import *
import fileinput
import re

groups = ''.join(fileinput.input()).split('\n\n')

def fx(grid):
    h = len(grid)
    w = len(grid[0])
    cols = [[grid[y][x] for y in range(h)] for x in range(w)]
    for x in range(0, w-1):
        ok = True
        error = 0
        for i in range(w):
            i0 = x - i
            i1 = x + i + 1
            if i0 < 0 or i1 >= w:
                break
            if cols[i0] != cols[i1]:
                error += sum([a != b for a, b in zip(cols[i0], cols[i1])])
                ok = False
                # break
        # print(x, error)
        if not ok and error == 1:
            return x + 1
    return -1

def fy(grid):
    h = len(grid)
    w = len(grid[0])
    rows = [[grid[y][x] for x in range(w)] for y in range(h)]
    for y in range(0, h-1):
        ok = True
        error = 0
        for i in range(h):
            i0 = y - i
            i1 = y + i + 1
            if i0 < 0 or i1 >= h:
                break
            if rows[i0] != rows[i1]:
                error += sum([a != b for a, b in zip(rows[i0], rows[i1])])
                ok = False
                # break
        # print(y, error)
        if not ok and error == 1:
            return y + 1
    return -1

total = 0
for group in groups:
    grid = [line.rstrip() for line in group.split('\n')]
    x = fx(grid)
    y = fy(grid)
    print()
    print('\n'.join(grid))
    print(x, y)
    if x >= 0:
        total += x
    if y >= 0:
        total += y*100
print(total)
# 32236