from itertools import *
from collections import *
import fileinput
import math
import re

lines = list(fileinput.input())

def value(card):
    # return 'AKQJT98765432'.index(card)
    return 'AKQT98765432J'.index(card)

def hand_value(hand):
    return tuple(value(c) for c in hand)

def rank(hand):
    c = Counter(hand)
    counts = Counter(c.values())
    # print(counts)
    if counts[5]:
        return 0
    if counts[4]:
        return 1
    if counts[3] and counts[2]:
        return 2
    if counts[3]:
        return 3
    if counts[2] > 1:
        return 4
    if counts[2]:
        return 5
    return 6

def best_rank(hand):
    jokers = hand.count('J')
    if not jokers:
        return rank(hand)
    hand = ''.join(c for c in hand if c != 'J')
    best = 99
    for cs in product('AKQT98765432', repeat=jokers):
        h = hand + ''.join(cs)
        best = min(best, rank(h))
    return best

items = []
for line in lines:
    hand, bid = line.strip().split()
    bid = int(bid)
    # r = rank(hand)
    r = best_rank(hand)
    items.append((r, hand_value(hand), bid))

items.sort(reverse=True)
total = 0
for i, x in enumerate(items):
    print(x)
    r, hand, bid = x
    total += (i + 1) * bid
print(total)
