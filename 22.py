from collections import *
from itertools import *
from math import *
import fileinput
import heapq
import re

lines = list(fileinput.input())

pieces = []
for line in lines:
    x0, y0, z0, x1, y1, z1 = map(int, re.findall(r'\d+', line))
    dx, dy, dz = x1-x0, y1-y0, z1-z0
    piece = set()
    if dx:
        for x in range(x0, x1+1):
            piece.add((x, y0, z0))
    elif dy:
        for y in range(y0, y1+1):
            piece.add((x0, y, z0))
    elif dz:
        for z in range(z0, z1+1):
            piece.add((x0, y0, z))
    else:
        piece.add((x0, y0, z0))
    pieces.append(piece)

lookup = defaultdict(list)
for i, p in enumerate(pieces):
    p = {(x, y) for x, y, z in p}
    for j, q in enumerate(pieces):
        if i == j:
            continue
        q = {(x, y) for x, y, z in q}
        if p & q:
            lookup[i].append(j)

def down(piece):
    return {(x, y, z - 1) for x, y, z in piece}

def bottom(piece):
    return any(z <= 1 for x, y, z in piece)

def move(piece, pieces):
    if bottom(piece):
        return piece
    d = down(piece)
    best = piece
    while True:
        for p in pieces:
            if p == piece:
                continue
            if d & p:
                return best
        best = d
        if bottom(d):
            return d
        d = down(d)

def step(pieces, skip=None):
    new_pieces = []
    changed = []
    for i, piece in enumerate(pieces):
        others = [pieces[j] for j in lookup[i]]
        if skip is not None:
            q = pieces[skip]
            if q in others:
                others.remove(q)
        new_piece = move(piece, others)
        # changed = changed or new_piece != piece
        if new_piece != piece:
            changed.append(i)
        new_pieces.append(new_piece)
    return new_pieces, changed

i = 0
while True:
    pieces, changed = step(pieces)
    if not changed:
        break
    print(i)
    i += 1
print(pieces)

def check(piece, pieces):
    # new_pieces = [p for p in pieces if p != piece]
    skip = pieces.index(piece)
    fell = set()
    while True:
        pieces, changed = step(pieces, skip)
        if not changed:
            break
        fell |= set(changed)
    return len(fell)

# print(sum(not check(p, pieces) for p in pieces))

total = 0
for i, p in enumerate(pieces):
    print(i)
    total += check(p, pieces)
print(total)
