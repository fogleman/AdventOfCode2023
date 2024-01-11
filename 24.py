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
n = 0
for i, p0 in enumerate(particles):
    for j, p1 in enumerate(particles[i+1:]):
        p = check(p0, p1)
        if p is None:
            continue
        x, y = p
        if x >= i0 and x <= i1 and y >= i0 and y <= i1:
            n += 1
print(n)

# x0 + vx0 * t0 = x1 + vx1 * t0
# x0 + vx0 * t1 = x2 + vx2 * t1
# a + b * t = c + d * t
# Ax = b

# 19-2*a=x+v*a
# 18-1*b=x+v*b
# 20-2*c=x+v*c

N = 1000
vxs = set(range(-N, N))
vys = set(range(-N, N))
vzs = set(range(-N, N))

def update(a, b):
    x0, y0, z0, vx0, vy0, vz0 = a
    x1, y1, z1, vx1, vy1, vz1 = b
    if vx0 == vx1:
        dx = abs(x0 - x1)
        for x in range(-N, N):
            if x != vx0 and dx % (x - vx0) != 0:
                vxs.discard(x)
    if vy0 == vy1:
        dy = abs(y0 - y1)
        for y in range(-N, N):
            if y != vy0 and dy % (y - vy0) != 0:
                vys.discard(y)
    if vz0 == vz1:
        dz = abs(z0 - z1)
        for z in range(-N, N):
            if z != vz0 and dz % (z - vz0) != 0:
                vzs.discard(z)

for i, p0 in enumerate(particles):
    for j, p1 in enumerate(particles[i+1:]):
        update(p0, p1)

vx = list(vxs)[0]
vy = list(vys)[0]
vz = list(vzs)[0]

apx, apy, apz, avx, avy, avz = particles[0]
bpx, bpy, bpz, bvx, bvy, bvz = particles[1]
ma = (avy - vy) / (avx - vx)
mb = (bvy - vy) / (bvx - vx)
ca = apy - (ma * apx)
cb = bpy - (mb * bpx)
x = int((cb - ca) / (ma - mb))
y = int(ma * x + ca)
t = (x - apx) // (avx - vx)
z = apz + (avz - vz) * t
print(x + y + z)
