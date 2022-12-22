#!/usr/bin/env python3
import sys

#  AB
#  C
# DE
# F
def transform(p, d):
    # A up
    if p[0] == -1 and 50 <= p[1] < 100:
        # F right
        return (100 + p[1], 0), (0, 1)
    # A left
    if 0 <= p[0] < 50 and p[1] == 49:
        # D right
        return (149 - p[0], 0), (0, 1)
    # B up
    if p[0] == -1 and 100 <= p[1] < 150:
        # F up
        return (199, p[1] - 100), (-1, 0)
    # B right
    if 0 <= p[0] < 50 and p[1] == 150:
        # E lef
        return (149 - p[0], 99), (0, -1)
    # B down
    if p[0] == 50 and 100 <= p[1] < 150:
        # C left
        return (p[1] - 50, 99), (0, -1)
    # C left
    if 50 <= p[0] < 100 and p[1] == 49:
        # D down
        return (100, p[0] - 50), (1, 0)
    # C right
    if 50 <= p[0] < 100 and p[1] == 100:
        # B up
        return (49, p[0] + 50), (-1, 0)
    # D up
    if p[0] == 99 and 0 <= p[1] < 50:
        # C right
        return (p[1] + 50, 50), (0, 1)
    # D left
    if 100 <= p[0] < 150 and p[1] == -1:
        # A right
        return (149 - p[0], 50), (0, 1)
    # E right
    if 100 <= p[0] < 150 and p[1] == 100:
        # B left
        return (149 - p[0], 149), (0, -1)
    # E down
    if p[0] == 150 and 50 <= p[1] < 100:
        # F left
        return (p[1] + 100, 49), (0, -1)
    # F left
    if 150 <= p[0] < 200 and p[1] == -1:
        # A down
        return (0, p[0] - 100), (1, 0)
    # F right
    if 150 <= p[0] < 200 and p[1] == 50:
        # E up
        return (149, p[0] - 100), (-1, 0)
    # F down
    if p[0] == 200 and 0 <= p[1] < 50:
        # B down
        return (0, p[1] + 100), (1, 0)
    return p, d


input = sys.stdin.read()
first, second = input.split("\n\n")

grid = {
    (i, j): v
    for i, line in enumerate(first.split("\n"))
    for j, v in enumerate(line)
    if v != " "
}

p = min(grid)
d = (0, 1)
for ins in second.strip().replace("R", " R ").replace("L", " L ").strip().split(" "):
    if ins == "R":
        d = (d[1], -d[0])
    elif ins == "L":
        d = (-d[1], d[0])
    else:
        for _ in range(int(ins)):
            new_p, new_d = p, d
            while True:
                new_p, new_d = transform(
                    (new_p[0] + new_d[0], new_p[1] + new_d[1]), new_d
                )
                if new_p in grid:
                    break
            if grid[new_p] == "#":
                break
            p, d = new_p, new_d

face = [(0, 1), (1, 0), (0, -1), (-1, 0)]

print(1000 * (p[0] + 1) + 4 * (p[1] + 1) + face.index(d))
