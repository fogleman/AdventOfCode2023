from itertools import *
from collections import *
import fileinput
import math
import re

lines = list(fileinput.input())

times = list(map(int, re.findall(r'\d+', lines[0])))
dists = list(map(int, re.findall(r'\d+', lines[1])))

def ways(time, dist):
    count = 0
    for t in range(1, time):
        s = t
        remaining = time - t
        d = remaining * s
        if d > dist:
            count += 1
    return count

result = 1
for t, d in zip(times, dists):
    result *= ways(t, d)
print(result)

t = int(''.join(map(str, times)))
d = int(''.join(map(str, dists)))
print(ways(t, d))
