from collections import *
import fileinput
import re

total = 0
counts = defaultdict(int)
for line in fileinput.input():
    nums = re.findall(r'\d+', line)
    nums = list(map(int, nums))
    card, nums = nums[0], nums[1:]
    winning, have = nums[:10], nums[10:]
    count = len(set(winning) & set(have))
    counts[card] += 1
    if count:
        total += 2 ** (count - 1)
        for i in range(card + 1, card + 1 + count):
            counts[i] += counts[card]

print(total)
print(sum(counts.values()))
