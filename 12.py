import fileinput

def search(pattern, sizes, memo, i=0, s=0, n=0, p=0):
    key = (i, s, n, p)
    if key in memo:
        return memo[key]
    ns = len(sizes)
    if i >= len(pattern):
        if s < ns - 1:
            return 0
        if s == ns - 1 and n != sizes[-1]:
            return 0
        if s >= ns and n > 0:
            return 0
        return 1
    sn = s + 1 if p else s
    a = lambda: search(pattern, sizes, memo, i+1, s, n+1, 1)
    b = lambda: search(pattern, sizes, memo, i+1, sn, 0, 0)
    result = 0
    c = pattern[i]
    if c == '#':
        if s < ns and n < sizes[s]:
            result = a()
    elif c == '.':
        if n == 0 or (s < ns and n == sizes[s]):
            result = b()
    else:
        if n == 0:
            result = a() + b()
        elif s < ns and n < sizes[s]:
            result = a()
        elif s < ns and n == sizes[s]:
            result = b()
    memo[key] = result
    return result

total1 = total2 = 0
for line in fileinput.input():
    pattern, sizes = line.split()
    sizes = list(map(int, sizes.split(',')))
    total1 += search(pattern, sizes, {})
    total2 += search('?'.join([pattern] * 5), sizes * 5, {})

print(total1)
print(total2)
