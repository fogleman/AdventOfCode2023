from collections import *
from itertools import *
from math import *
import fileinput
import heapq
import re

inp = ''.join(fileinput.input())
A, B = inp.split('\n\n')

rules = {}
for line in A.split('\n'):
    line = line.replace('{', ' ')
    line = line.replace('}', '')
    name, r = line.split()
    r = r.split(',')
    rules[name] = r

parts = []
for line in B.split('\n'):
    x, m, a, s = map(int, re.findall(r'\d+', line))
    parts.append(dict(x=x, m=m, a=a, s=s))
# print(parts)

def run_rule(rules, name, part):
    if name == 'A':
        return True
    if name == 'R':
        return False
    for r in rules[name]:
        if ':' in r:
            a, b = r.split(':')
            v = a[0]
            c = a[1]
            d = int(a[2:])
            if c == '<':
                if part[v] < d:
                    return run_rule(rules, b, part)
            else:
                if part[v] > d:
                    return run_rule(rules, b, part)
        else:
            return run_rule(rules, r, part)

def run(rules, part):
    return run_rule(rules, 'in', part)

total = 0
for part in parts:
    if run(rules, part):
        total += sum(part.values())
print(total)

# [1, 4000]

def count(path):
    things = dict(
        x=set(range(1, 4001)),
        m=set(range(1, 4001)),
        a=set(range(1, 4001)),
        s=set(range(1, 4001)),
    )
    for v, c, d in path:
        if c == '<':
            things[v] &= set(range(1, d))
        else:
            things[v] &= set(range(d+1, 4001))
    return len(things['x'])*len(things['m'])*len(things['a'])*len(things['s'])

def search(rules, name, index, path):
    if name == 'A':
        print(path)
        total = count(path)
        return total
    if name == 'R':
        return 0
    total = 0
    r = rules[name][index]
    if ':' in r:
        a, b = r.split(':')
        v = a[0]
        c = a[1]
        d = int(a[2:])
        path.append((v, c, d))
        total += search(rules, b, 0, path)
        path.pop()
        if c == '<':
            c = '>'
            d = d - 1
        else:
            c = '<'
            d = d + 1
        path.append((v, c, d))
        total += search(rules, name, index+1, path)
        path.pop()
    else:
        total += search(rules, r, 0, path)
    return total

print(search(rules, 'in', 0, []))

#167409079868000
#496817446000000

# lines = list(fileinput.input())
# grid = list(line.rstrip() for line in fileinput.input())

# for line in lines:
#     print(line)
