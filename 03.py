from collections import *
from itertools import *
import fileinput
import math
import re

lines = list(fileinput.input())

grid = []
for line in lines:
    grid.append(line.rstrip())

symbols = set()
gears = set()
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c not in '.0123456789':
            symbols.add((x, y))
        if c == '*':
            gears.add((x, y))

total = 0
for y, row in enumerate(grid):
    for m in re.finditer(r'\d+', row):
        x0, x1 = m.span()
        ok = False
        for x in range(x0, x1):
            for sx, sy in symbols:
                dx = abs(sx-x)
                dy = abs(sy-y)
                if dx <= 1 and dy <= 1:
                    ok = True
        if ok:
            total += int(m.group())
print(total)

total = 0
gear_ratios = defaultdict(list)
for y, row in enumerate(grid):
    for m in re.finditer(r'\d+', row):
        x0, x1 = m.span()
        ok = False
        for x in range(x0, x1):
            for sx, sy in gears:
                dx = abs(sx-x)
                dy = abs(sy-y)
                if dx <= 1 and dy <= 1:
                    ok = (sx, sy)
        if ok:
            gear_ratios[ok].append(int(m.group()))
total = 0
for gears in gear_ratios.values():
    if len(gears) == 2:
        total += gears[0] * gears[1]
print(total)
