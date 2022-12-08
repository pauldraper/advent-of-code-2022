#!/usr/bin/env python3
import sys

grid = {
    (i, j): int(v)
    for i, line in enumerate(sys.stdin)
    for j, v in enumerate(line.strip())
}


def visible(p):
    start = grid[p]
    for i in range(len(p)):
        for k in (-1, 1):
            p2 = list(p)
            p2[i] += k
            while tuple(p2) in grid:
                if start <= grid[tuple(p2)]:
                    break
                p2[i] += k
            else:
                return True
    return False


print(sum(map(visible, grid)))
