from itertools import *
from collections import *
import fileinput
import math
import re

lines = list(fileinput.input())

rls = lines[0].strip()

nodes = {}
for line in lines[2:]:
    items = re.findall(r'\w+', line)
    key, l, r = items
    nodes[key] = (l, r)

rls = cycle(rls)
i = 0
# key = 'AAA'
keys = [x for x in nodes if x.endswith('A')]
times = defaultdict(list)
while not all(x.endswith('Z') for x in keys):
    for j, k in enumerate(keys):
        if k.endswith('Z'):
            times[j].append(i)
    for j in range(len(keys)):
        if len(times[j]) > 2:
            print(j, times[j][-1]-times[j][-2], times[j][-2]-times[j][-3])
    print()
    rl = next(rls)
    if rl == 'L':
        keys = [nodes[key][0] for key in keys]
    else:
        keys = [nodes[key][1] for key in keys]
    i += 1
print(i)

# 20569,18727,14429,13201,18113,22411
# 29783523552667816112727361
# 10921547990923
