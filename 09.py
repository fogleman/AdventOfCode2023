from itertools import *
from collections import *
from math import *
import fileinput
import re

lines = list(fileinput.input())

def extrapolate(values, depth):
    d = [b - a for a, b in zip(values, values[1:])]
    if not any(d):
        result = values[-1]
    else:
        result = values[-1] + extrapolate(d, depth+1)
    return result

def extrapolate(values, depth):
    d = [b - a for a, b in zip(values, values[1:])]
    if not any(d):
        result = values[0]
    else:
        result = values[0] - extrapolate(d, depth+1)
    return result

total = 0
for line in lines:
    values = list(map(int, line.strip().split()))
    print(values, extrapolate(values, 0))
    total += extrapolate(values, 0)
print(total)
