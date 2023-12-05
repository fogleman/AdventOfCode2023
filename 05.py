import fileinput
import re

groups = ''.join(fileinput.input()).split('\n\n')

seeds = list(map(int, re.findall(r'\d+', groups[0])))

mappings = []
for group in groups[1:]:
    mapping = []
    for line in group.split('\n')[1:]:
        dst, src, length = map(int, re.findall(r'\d+', line))
        mapping.append((dst, src, length))
    mapping.sort(key=lambda x: x[1])
    mappings.append(mapping)

def lookup(mapping, value):
    for dst, src, length in mapping:
        d = value - src
        if d >= 0 and d < length:
            return dst + d
    return value

def lookup_all(mappings, value):
    for mapping in mappings:
        value = lookup(mapping, value)
    return value

print(min(lookup_all(mappings, seed) for seed in seeds))

def lookup_ranges(mapping, ranges):
    result = []
    for i1, n1 in ranges:
        j1 = i1 + n1
        positions = [i1]
        for dst, i2, n2 in mapping:
            j2 = i2 + n2
            if i2 > i1 and i2 < j1:
                positions.append(i2)
            if j2 > i1 and j2 < j1:
                positions.append(j2)
        positions.append(j1)
        for i, j in zip(positions, positions[1::]):
            d = 0
            for dst, i2, n2 in mapping:
                if i >= i2 and i < i2 + n2:
                    d = dst - i2
                    break
            result.append((i + d, j - i))
    return result

def lookup_ranges_all(mappings, ranges):
    for mapping in mappings:
        ranges = lookup_ranges(mapping, ranges)
    return ranges

ranges = list(zip(seeds[::2], seeds[1::2]))
ranges = lookup_ranges_all(mappings, ranges)
print(min(x for x, y in ranges))
