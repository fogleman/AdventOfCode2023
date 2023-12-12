import fileinput

lines = list(fileinput.input())

def search(pattern, sizes, i, si, n, prev, memo):
    key = (i, si, n, prev)
    if key in memo:
        return memo[key]
    result = 0
    if i >= len(pattern):
        if si < len(sizes) - 1:
            return 0
        if si == len(sizes) - 1 and n != sizes[-1]:
            return 0
        if si == len(sizes) and n > 0:
            return 0
        return 1
    c = pattern[i]
    nsi = si+1 if prev else si
    if c == '?':
        if n == 0:
            result += search(pattern, sizes, i+1, si, n+1, 1, memo)
            result += search(pattern, sizes, i+1, nsi, 0, 0, memo)
        elif si < len(sizes) and n < sizes[si]: # '#'
            result += search(pattern, sizes, i+1, si, n+1, 1, memo)
        elif si < len(sizes) and n == sizes[si]: # '.'
            result += search(pattern, sizes, i+1, nsi, 0, 0, memo)
        else:
            return 0
    elif c == '#':
        if si >= len(sizes) or n >= sizes[si]:
            return 0
        result += search(pattern, sizes, i+1, si, n+1, 1, memo)
    elif c == '.':
        if n > 0 and (si >= len(sizes) or n != sizes[si]):
            return 0
        result += search(pattern, sizes, i+1, nsi, 0, 0, memo)
    else:
        raise
    memo[key] = result
    return result

total = 0
for index, line in enumerate(lines):
    pattern, sizes = line.split()
    sizes = list(map(int, sizes.split(',')))

    pattern = '?'.join([pattern] * 5)
    pattern = pattern.rstrip('.')
    sizes = sizes * 5

    n = pattern.count('?')

    # print(index, pattern, sizes, n)

    count = search(pattern, sizes, 0, 0, 0, 0, {})
    # count = 0
    # for i in range(2 ** n):
    #     p = []
    #     for j in range(n):
    #         mask = 1 << j
    #         p.append('#' if mask & i else '.')
    #     q = []
    #     for i, c in enumerate(pattern):
    #         if c == '?':
    #             c = p.pop()
    #         q.append(c)
    #     q = ''.join(q)
    #     if [len(x) for x in q.split('.') if x] == sizes:
    #         count += 1
    total += count
    # print(count)
print(total)
