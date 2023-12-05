from collections import *
import fileinput
import re

total = 0
counts = defaultdict(int)
for line in fileinput.input():
    nums = re.findall(r'\d+|\|', line)
    card = int(nums.pop(0))
    i = nums.index('|')
    count = len(set(nums[:i]) & set(nums[i:]))
    counts[card] += 1
    if count:
        total += 2 ** (count - 1)
        for i in range(card + 1, card + 1 + count):
            counts[i] += counts[card]

print(total)
print(sum(counts.values()))
