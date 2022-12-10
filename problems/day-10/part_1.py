#!/usr/bin/env python3
import sys

result = 0
register = 1
cycle = 1


def add_cycle():
    global cycle, result
    if cycle in (20, 60, 100, 140, 180, 220):
        result += cycle * register
    cycle += 1


for line in sys.stdin:
    parts = line.strip().split(" ")
    if parts[0] == "noop":
        add_cycle()
    else:
        add_cycle()
        add_cycle()
        register += int(parts[1])

print(result)
