import fileinput
import re

lines = list(fileinput.input())

def extrapolate(values, index, sign):
    diff = [b - a for a, b in zip(values, values[1:])]
    result = values[index]
    if any(diff):
        result += extrapolate(diff, index, sign) * sign
    return result

def run(index, sign):
    total = 0
    for line in lines:
        values = list(map(int, line.split()))
        total += extrapolate(values, index, sign)
    return total

print(run(-1, 1))
print(run(0, -1))
