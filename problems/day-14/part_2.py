#!/usr/bin/env python3
import itertools
import sys

exists = set()
for line in sys.stdin:
    parts = [tuple(map(int, part.split(","))) for part in line.split(" -> ")]
    for a, b in zip(parts, parts[1:]):
        for i in (0, 1):
            if a[i] == b[i]:
                continue
            p = list(a)
            for k in range(min(a[i], b[i]), max(a[i], b[i]) + 1):
                p[i] = k
                exists.add(tuple(p))
lowest = max(y for _, y in exists)

for sand in itertools.count(1):
    p = (500, 0)
    while p[1] <= lowest:
        try:
            positions = ((p[0] + dx, p[1] + 1) for dx in (0, -1, 1))
            p = next(p for p in positions if p not in exists)
        except StopIteration:
            break
    if not p[1]:
        break
    exists.add(p)
print(sand)
