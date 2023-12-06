import fileinput
import re

lines = list(fileinput.input())
times = list(map(int, re.findall(r'\d+', lines[0])))
dists = list(map(int, re.findall(r'\d+', lines[1])))

def ways(time, dist):
    return sum((time - t) * t > dist for t in range(1, time))

result = 1
for t, d in zip(times, dists):
    result *= ways(t, d)
print(result)

t = int(''.join(map(str, times)))
d = int(''.join(map(str, dists)))
print(ways(t, d))
