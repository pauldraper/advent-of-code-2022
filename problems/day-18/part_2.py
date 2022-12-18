#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10000)

lava = {tuple(map(int, line.split(","))) for line in sys.stdin}
mins = tuple(min(i[d] - 1 for i in lava) for d in range(3))
maxs = tuple(max(i[d] + 1 for i in lava) for d in range(3))


def adjacent(p):
    for direction in range(3):
        for magnitude in (-1, 1):
            yield tuple(v + magnitude * (i == direction) for i, v in enumerate(p))


outside = set()


def visit(p):
    if (
        p in outside
        or p in lava
        or not all(mins[d] <= p[d] <= maxs[d] for d in range(3))
    ):
        return
    outside.add(p)
    for p2 in adjacent(p):
        visit(p2)


visit(mins)

print(sum(p2 in outside for p in lava for p2 in adjacent(p)))
