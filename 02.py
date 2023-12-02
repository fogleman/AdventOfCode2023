from collections import *
from itertools import *
import fileinput
import math
import re

lines = list(fileinput.input())

total = 0
powers = 0
for line in lines:
    line = line.rstrip()
    a, b = line.split(':')
    game = int(a.split()[-1])
    rounds = b.split(';')
    ok = True
    fewest = defaultdict(int)
    for r in rounds:
        m = re.findall(r'(\d+) (red|green|blue)', r)
        for n, c in m:
            n = int(n)
            fewest[c] = max(fewest[c], n)
            if c == 'red' and n > 12:
                ok = False
            if c == 'green' and n > 13:
                ok = False
            if c == 'blue' and n > 14:
                ok = False
    power = fewest['red']*fewest['green']*fewest['blue']
    powers += power
    if ok:
        total += game
print(total)
print(powers)
