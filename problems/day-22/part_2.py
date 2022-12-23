#!/usr/bin/env python3
import collections
import itertools
import sys

grid = {
    (i, j)
    for i, line in enumerate(sys.stdin)
    for j, v in enumerate(line.strip())
    if v == "#"
}

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for round in itertools.count(1):
    moved = False
    proposals = collections.defaultdict(list)
    for p in grid:
        if (
            sum((p[0] + i, p[1] + j) in grid for i in (-1, 0, 1) for j in (-1, 0, 1))
            == 1
        ):
            continue
        for d in dirs:
            if all(
                (p[0] + (d[0] or k), p[1] + (d[1] or k)) not in grid for k in (-1, 0, 1)
            ):
                proposals[(p[0] + d[0], p[1] + d[1])].append(p)
                break
    for end, starts in proposals.items():
        if 1 < len(starts):
            continue
        grid.remove(starts[0])
        grid.add(end)
        moved = True
    if not moved:
        break
    dirs.append(dirs.pop(0))

print(round)
