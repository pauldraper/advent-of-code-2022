#!/usr/bin/env python3
import sys

visited = set()
rope = [[0, 0] for _ in range(10)]
visited.add(tuple(rope[-1]))
for line in sys.stdin:
    direction, distance = line.split(" ")
    for _ in range(int(distance)):
        if direction == "D":
            rope[0][1] -= 1
        elif direction == "L":
            rope[0][0] -= 1
        elif direction == "R":
            rope[0][0] += 1
        elif direction == "U":
            rope[0][1] += 1
        for prev, cur in zip(rope, rope[1:]):
            while any(1 < abs(cur[j] - prev[j]) for j in (0, 1)):
                for j in (0, 1):
                    cur[j] += (cur[j] < prev[j]) - (prev[j] < cur[j])
        visited.add(tuple(rope[-1]))
print(len(visited))
