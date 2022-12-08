#!/usr/bin/env python3
import sys

grid = {
    (i, j): int(v)
    for i, line in enumerate(sys.stdin)
    for j, v in enumerate(line.strip())
}

best = 0
for p, base in grid.items():
    score = 1
    for i in range(len(p)):
        for k in (-1, 1):
            s = 0
            p2 = list(p)
            p2[i] += k
            while tuple(p2) in grid:
                s += 1
                if base <= grid[tuple(p2)]:
                    break
                p2[i] += k
            score *= s
    best = max(best, score)

print(best)
