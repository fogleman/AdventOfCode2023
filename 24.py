from collections import *
from itertools import *
from math import *
import fileinput
import heapq
import re

lines = list(fileinput.input())
# grid = list(line.rstrip() for line in fileinput.input())

particles = []
for line in lines:
    x, y, z, vx, vy, vz = map(int, re.findall(r'[-\d]+', line))
    particles.append((x, y, z, vx, vy, vz))

# 7, 27
# 200000000000000, 400000000000000

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def check(a, b):
    n = 1000000000000000
    x0, y0, z0, vx0, vy0, vz0 = a
    x1, y1, z1, vx1, vy1, vz1 = b
    x01 = x0 + vx0 * n
    y01 = y0 + vy0 * n
    x11 = x1 + vx1 * n
    y11 = y1 + vy1 * n
    if not intersect((x0, y0), (x01, y01), (x1, y1), (x11, y11)):
        return None
    return line_intersection(((x0, y0), (x01, y01)), ((x1, y1), (x11, y11)))

i0 = 200000000000000
i1 = 400000000000000
count = 0
for i, p0 in enumerate(particles):
    for j, p1 in enumerate(particles[i+1:]):
        p = check(p0, p1)
        if p is None:
            continue
        x, y = p
        if x >= i0 and x <= i1 and y >= i0 and y <= i1:
            count += 1
print(count)

# x0 + vx0 * t0 = x1 + vx1 * t0
# x0 + vx0 * t1 = x2 + vx2 * t1
# a + b * t = c + d * t
# Ax = b

# 19-2*a=x+v*a
# 18-1*b=x+v*b
# 20-2*c=x+v*c
