from collections import *
from itertools import *
from math import *
import fileinput
import heapq
import re
import sys

sys.setrecursionlimit(10000)

# lines = list(fileinput.input())
grid = list(line.rstrip() for line in fileinput.input())
w, h = len(grid[0]), len(grid)

start = (1, 0)
target = (w - 2, h - 1)

DIRS = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, -1),
    'v': (0, 1),
}

blank = 0
for row in grid:
    for c in row:
        if c == '.':
            blank += 1

nodes = [start, target]
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '#':
            continue
        ways = 0
        for dx, dy in DIRS.values():
            nx, ny = new_position = (x + dx, y + dy)
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            if grid[ny][nx] == '#':
                continue
            ways += 1
        if ways > 2:
            nodes.append((x, y))
print(len(nodes))

def shortest_path(source, target):
    seen, queue = set(), [(0, source, [])]
    while queue:
        d, p, path = heapq.heappop(queue)
        if p == target:
            return path
        if p in seen:
            continue
        if p in nodes and p != source:
            continue
        seen.add(p)
        x, y = p
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            q = nx, ny = (x + dx, y + dy)
            if q in seen:
                continue
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            if grid[ny][nx] == '#':
                continue
            heapq.heappush(queue, (d + 1, q, path + [q]))

def longest_path(position, target, path, seen):
    if position == target:
        yield path
        return
    x, y = position
    c = grid[y][x]
    for dx, dy in DIRS.values():
        nx, ny = new_position = (x + dx, y + dy)
        if new_position in seen:
            continue
        if nx < 0 or ny < 0 or nx >= w or ny >= h:
            continue
        if grid[ny][nx] == '#':
            continue
        path.append(new_position)
        seen.add(new_position)
        yield from longest_path(new_position, target, path, seen)
        path.pop()
        seen.discard(new_position)

G = defaultdict(list)
for i, n0 in enumerate(nodes):
    for n1 in nodes[i+1:]:
        path = shortest_path(n0, n1)
        if not path:
            continue
        # if len(set(path[:-1]) & set(nodes)) > 0:
        #     continue
        def label(n):
            return '%d_%d' % n
        # x = def longest_path(position, target, path, seen):
        # x = max(len(p) for p in longest_path(n0, n1, [n0], {n0}) if len(set(p[1:-1]) & set(nodes)) <= 0)-1
        x = len(path)
        print(n0, n1, len(path), x)
        # print('%s -- %s;' % (label(n0), label(n1)))
        G[n0].append((n1, x))
        G[n1].append((n0, x))

def search_shortest(position):
    q = [(position, 0)]
    min_dist = {}
    while q:
        p, d = q.pop()
        if p in min_dist and d >= min_dist[p]:
            continue
        min_dist[p] = d
        x, y = p
        for dx, dy in DIRS.values():
            nx, ny = new_position = (x + dx, y + dy)
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            if grid[ny][nx] == '#':
                continue
            q.append(((nx, ny), d + 1))
    return min_dist

def search(position, target, path, seen, score):
    # print(path)
    if position == target:
        # print(score, path)
        yield score
        return
    # x, y = position
    # c = grid[y][x]
    # if c in DIRS:
    #     dx, dy = DIRS[c]
    #     new_position = (x + dx, y + dy)
    #     if new_position in seen:
    #         return
    #     path.append(new_position)
    #     seen.add(new_position)
    #     yield from search(new_position, target, path, seen)
    #     path.pop()
    #     seen.discard(new_position)
    #     return
    for q, d in G[position]:
        if q in seen:
            continue
        # if grid[ny][nx] == '#':
        #     continue
        # if new_position in best:
        #     if len(path) <= best[new_position]:
        #         print(len(path), best[new_position])
        #         continue
        # best[new_position] = len(path)
        path.append(q)
        seen.add(q)
        yield from search(q, target, path, seen, score + d)
        path.pop()
        seen.discard(q)

min_dist = search_shortest(target)
# print(min_dist)

hi = 0
for score in search(start, target, [start], set([start]), 0):
    # print(score)
    # hi = max(hi, score)
    if score > hi:
        hi = score
        print(hi)
print(hi)
