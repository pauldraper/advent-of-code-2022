#!/usr/bin/env python3
import sys

y = 2000000

segments = []
beacon_xs = set()
for line in sys.stdin:
    a, b = (
        line.replace("x=", "")
        .replace("y=", "")
        .replace("Sensor at ", "")
        .replace(" closest beacon is at", "")
        .split(":")
    )
    ax, ay = map(int, a.split(","))
    bx, by = map(int, b.split(","))
    if by == y:
        beacon_xs.add(bx)
    dist = abs(ax - bx) + abs(ay - by) - abs(ay - y)
    if 0 <= dist:
        segments.append((ax - dist, ax + dist + 1))

segments.sort()

c = 0
end = segments[0][0]
for s in segments:
    start = max(s[0], end)
    end = max(end, s[1])
    c += end - start - sum(start <= x < end for x in beacon_xs)
print(c)
