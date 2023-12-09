from itertools import cycle
from collections import defaultdict
from math import lcm
import fileinput
import re

lines = list(fileinput.input())
RL = cycle(lines[0].strip())
nodes = {}
for line in lines[2:]:
    key, l, r = re.findall(r'\w+', line)
    nodes[key] = (l, r)

def run(part2):
    steps = 0
    keys = [x for x in nodes if x.endswith('A')] if part2 else ['AAA']
    times = defaultdict(list)
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

for i in range(2):
    print(run(i))
