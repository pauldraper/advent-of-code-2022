#!/usr/bin/env python3
import sys

screen = [["."] * 40 for _ in range(6)]
register = 1
cycle = 0


def add_cycle():
    global cycle
    if abs(cycle % 40 - register) <= 1:
        screen[cycle // 40][cycle % 40] = "#"
    cycle += 1


for line in sys.stdin:
    parts = line.strip().split(" ")
    if parts[0] == "noop":
        add_cycle()
    else:
        add_cycle()
        add_cycle()
        register += int(parts[1])

for row in screen:
    print("".join(row))
