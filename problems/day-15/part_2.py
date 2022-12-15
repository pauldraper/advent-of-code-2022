#!/usr/bin/env python3
import sys

sensors = []
beacons = []

for line in sys.stdin:
    s, b = (
        line.replace("x=", "")
        .replace("y=", "")
        .replace("Sensor at ", "")
        .replace(" closest beacon is at", "")
        .split(":")
    )
    s_x, s_y = map(int, s.split(","))
    b_x, b_y = map(int, b.split(","))
    sensors.append((s_x, s_y))
    beacons.append((b_x, b_y))

y_min = 0
y_max = 4000000

for y in range(y_min, y_max + 1):
    segments = []
    for (s_x, s_y), (b_x, b_y) in zip(sensors, beacons):
        dist = abs(s_x - b_x) + abs(s_y - b_y) - abs(s_y - y)
        if 0 <= dist:
            segments.append((s_x - dist, s_x + dist))

    segments.sort()

    end = y_min
    for s in segments:
        x = end + 1
        if x < s[0] and x <= y_max and (x, y) not in beacons:
            print(x * 4000000 + y)
        end = max(end, s[1])
