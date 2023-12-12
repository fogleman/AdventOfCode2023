import fileinput

lines = list(fileinput.input())

def search(pattern, sizes, i, s, n, p, memo):
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
    a = lambda: search(pattern, sizes, i+1, s, n+1, 1, memo)
    b = lambda: search(pattern, sizes, i+1, sn, 0, 0, memo)
    result = 0
    c = pattern[i]
    if c == '?':
        if n == 0:
            result = a() + b()
        elif s < ns and n < sizes[s]:
            result = a()
        elif s < ns and n == sizes[s]:
            result = b()
        else:
            return 0
    elif c == '#':
        if s >= ns or n >= sizes[s]:
            return 0
        result = a()
    elif c == '.':
        if n > 0 and (s >= ns or n != sizes[s]):
            return 0
        result = b()
    memo[key] = result
    return result

for i in range(2):
    total = 0
    for index, line in enumerate(lines):
        pattern, sizes = line.split()
        sizes = list(map(int, sizes.split(',')))
        if i:
            pattern = '?'.join([pattern] * 5)
            sizes *= 5
        total += search(pattern, sizes, 0, 0, 0, 0, {})
    print(total)
