#!/usr/bin/env python3
import sys

input = sys.stdin.read()
first, second = input.split("\n\n")

grid = {
    (i, j): v
    for i, line in enumerate(first.split("\n"))
    for j, v in enumerate(line)
    if v != " "
}

limit = tuple(1 + max(p[i] for p in grid) for i in range(2))

p = min(grid)
d = (0, 1)
for ins in second.strip().replace("R", " R ").replace("L", " L ").strip().split(" "):
    if ins == "R":
        d = (d[1], -d[0])
    elif ins == "L":
        d = (-d[1], d[0])
    else:
        for _ in range(int(ins)):
            new_p = p
            while True:
                new_p = ((new_p[0] + d[0]) % limit[0], (new_p[1] + d[1]) % limit[1])
                if new_p in grid:
                    break
            if grid[new_p] == "#":
                break
            p = new_p

face = [(0, 1), (1, 0), (0, -1), (-1, 0)]

print(1000 * (p[0] + 1) + 4 * (p[1] + 1) + face.index(d))
