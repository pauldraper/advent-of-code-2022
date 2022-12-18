#!/usr/bin/env python3
import sys

lava = {tuple(map(int, line.split(","))) for line in sys.stdin}

count = sum(
    tuple(v + magnitude * (i == direction) for i, v in enumerate(p)) not in lava
    for p in lava
    for direction in range(3)
    for magnitude in (-1, 1)
)
print(count)
