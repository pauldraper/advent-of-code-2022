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

pushes, push_i = sys.stdin.read().strip(), 0
counts, heights = {}, {}
chamber = {(0, i) for i in range(7)}
for count, rock in enumerate(itertools.cycle(rocks)):
    height = max(i for i, _ in chamber)
    heights[count] = height

    top = tuple(sorted((i - height, j) for i, j in chamber if height <= i + 50))
    key = (rock, top, push_i)
    if key in counts:
        start = counts[key]
        break
    counts[key] = count

    position = [4 + height, 2]
    while True:
        direction = {"<": -1, ">": 1}[pushes[push_i]]
        push_i = (push_i + 1) % len(pushes)
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

q, m = divmod(1000000000000 - start, count - start)
print(heights[start + m] + q * (heights[count] - heights[start]))
