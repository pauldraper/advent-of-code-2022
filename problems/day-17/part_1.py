#!/usr/bin/env python3
import itertools
import sys

rocks = (
    (
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
    ),
    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
    (
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 2),
    ),
    (
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
    ),
    ((0, 0), (0, 1), (1, 0), (1, 1)),
)

pushes = iter(itertools.cycle(sys.stdin.read().strip()))
chamber = {(0, i) for i in range(7)}
for rock in itertools.islice(itertools.cycle(rocks), 2022):
    height = max(i for i, _ in chamber)
    position = [4 + height, 2]
    while True:
        direction = {"<": -1, ">": 1}[next(pushes)]
        for r in rock:
            p = (position[0] + r[0], position[1] + r[1] + direction)
            if p in chamber or not (0 <= p[1] < 7):
                break
        else:
            position[1] += direction

        if any((position[0] + r[0] - 1, position[1] + r[1]) in chamber for r in rock):
            chamber.update((position[0] + r[0], position[1] + r[1]) for r in rock)
            break
        position[0] -= 1

print(max(i for i, _ in chamber))
