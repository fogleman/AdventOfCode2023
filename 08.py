from itertools import *
from collections import *
from math import *
import fileinput
import re

lines = list(fileinput.input())
nodes = {}
for line in lines[2:]:
    key, l, r = re.findall(r'\w+', line)
    nodes[key] = (l, r)

def run(keys):
    steps = 0
    times = defaultdict(list)
    RL = cycle(lines[0].strip())
    while True:
        for i, k in enumerate(keys):
            if k.endswith('Z'):
                times[i].append(steps)
        if all(len(times[i]) > 1 for i in range(len(keys))):
            return lcm(*[times[i][-1] - times[i][-2]
                for i in range(len(keys))])
        i = int(next(RL) == 'R')
        keys = [nodes[key][i] for key in keys]
        steps += 1
    return steps

print(run(['AAA']))
print(run([x for x in nodes if x.endswith('A')]))
