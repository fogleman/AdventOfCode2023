from itertools import product
from collections import Counter
import fileinput

def rank(hand):
    c = Counter(Counter(hand).values())
    if c[5]: return 0
    if c[4]: return 1
    if c[3] and c[2]: return 2
    if c[3]: return 3
    if c[2] > 1: return 4
    if c[2]: return 5
    return 6

def best_rank(hand, part2):
    jokers = 0
    if part2:
        jokers = hand.count('J')
        hand = ''.join(c for c in hand if c != 'J')
    return min(rank(hand + ''.join(cs))
        for cs in product('23456789TQKA', repeat=jokers))

def run(lines, part2):
    cards = 'AKQT98765432J' if part2 else 'AKQJT98765432'
    items = []
    for line in lines:
        hand, bid = line.strip().split()
        items.append((
            best_rank(hand, part2),
            tuple(cards.index(c) for c in hand),
            int(bid)))
    items.sort(reverse=True)
    return sum((i + 1) * bid for i, (_, _, bid) in enumerate(items))

lines = list(fileinput.input())
for i in range(2):
    print(run(lines, i))
