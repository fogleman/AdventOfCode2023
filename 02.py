from collections import defaultdict
import fileinput
import re

part1 = part2 = 0
limit = dict(red=12, green=13, blue=14)
for line in fileinput.input():
    a, b = line.split(':')
    fewest = defaultdict(int)
    ok = True
    for r in b.split(';'):
        for n, c in re.findall(r'(\d+) (red|green|blue)', r):
            fewest[c] = max(fewest[c], int(n))
            ok = ok and int(n) <= limit[c]
    part1 += int(a.split()[-1]) if ok else 0
    part2 += fewest['red'] * fewest['green'] * fewest['blue']

print(part1)
print(part2)
