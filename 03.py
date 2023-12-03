from collections import defaultdict
import fileinput
import re

numbers = []
symbols = set()
gears = set()
for y, row in enumerate(fileinput.input()):
    for m in re.finditer(r'\d+', row):
        x0, x1 = m.span()
        numbers.append((x0, x1, y, int(m.group())))
    for m in re.finditer(r'[^\d\.\n]', row):
        x = m.span()[0]
        symbols.add((x, y))
        if m.group() == '*':
            gears.add((x, y))

def adjacent(x0, x1, y, symbols):
    return {(sx, sy) for x in range(x0, x1) for sx, sy in symbols
        if abs(sx - x) <= 1 and abs(sy - y) <= 1}

# part 1
print(sum(number for x0, x1, y, number in numbers
    if adjacent(x0, x1, y, symbols)))

# part 2
gear_numbers = defaultdict(list)
for x0, x1, y, number in numbers:
    for k in adjacent(x0, x1, y, gears):
        gear_numbers[k].append(number)
print(sum(g[0] * g[1] for g in gear_numbers.values() if len(g) == 2))
