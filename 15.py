from collections import *
from itertools import *
from math import *
import fileinput
import re

line = list(fileinput.input())[0]

values = line.rstrip().split(',')

def f(s):
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value %= 256
    return value

total = 0
for value in values:
    total += f(value)
print(total)

boxes = [[] for _ in range(256)]
for value in values:
    if '=' in value:
        label, fl = value.split('=')
        fl = int(fl)
        h = f(label)
        for i, x in enumerate(boxes[h]):
            if x[0] == label:
                boxes[h][i] = (label, fl)
                break
        else:
            boxes[h].append((label, fl))
    else:
        label = value[:-1]
        h = f(label)
        for i, x in enumerate(boxes[h]):
            if x[0] == label:
                del boxes[h][i]
                break

score = 0
for i, box in enumerate(boxes):
    for j, (_, fl) in enumerate(box):
        score += (i+1)*(j+1)*fl
print(score)