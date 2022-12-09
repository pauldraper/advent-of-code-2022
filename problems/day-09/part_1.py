#!/usr/bin/env python3
import sys

visited = set()
head = [0, 0]
tail = [0, 0]
visited.add(tuple(tail))
for line in sys.stdin:
    direction, distance = line.split(" ")
    for _ in range(int(distance)):
        if direction == "D":
            head[1] -= 1
        elif direction == "L":
            head[0] -= 1
        elif direction == "R":
            head[0] += 1
        elif direction == "U":
            head[1] += 1
        while any(1 < abs(tail[j] - head[j]) for j in (0, 1)):
            for j in (0, 1):
                tail[j] += (tail[j] < head[j]) - (head[j] < tail[j])
        visited.add(tuple(tail))
print(len(visited))
