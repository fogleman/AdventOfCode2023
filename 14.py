from collections import *
from itertools import *
from math import *
import fileinput
import re

lines = list(fileinput.input())
grid = [list(line.rstrip()) for line in lines]

N = 0
W = 1
S = 2
E = 3

def shift(grid, d):
    done = True
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if d == N and y < len(grid) - 1 and c == '.' and grid[y+1][x] == 'O':
                grid[y][x] = 'O'
                grid[y+1][x] = '.'
                done = False
            if d == S and y > 0 and c == '.' and grid[y-1][x] == 'O':
                grid[y][x] = 'O'
                grid[y-1][x] = '.'
                done = False
            if d == E and x > 0 and c == '.' and grid[y][x-1] == 'O':
                grid[y][x] = 'O'
                grid[y][x-1] = '.'
                done = False
            if d == W and x < len(grid[0])-1 and c == '.' and grid[y][x+1] == 'O':
                grid[y][x] = 'O'
                grid[y][x+1] = '.'
                done = False
    return done

def shifts(grid, d):
    while True:
        done = shift(grid, d)
        if done:
            break

def round(grid):
    for d in range(4):
        shifts(grid, d)

def score(grid):
    result = 0
    h = len(grid)
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'O':
                result += h-y
    return result

# shifts(grid)
# print(score(grid))

seen = {}
for i in range(1000000000):
    round(grid)
    k = '\n'.join(''.join(r) for r in grid)
    s = score(grid)
    p = seen.get(k, -1)
    seen[k] = i
    p+=1
    j = i+1
    if (1000000000-j)%(j-p) == 0:
        print(j, s, j-p)
    # print('\n'.join(''.join(r) for r in grid))
    # break