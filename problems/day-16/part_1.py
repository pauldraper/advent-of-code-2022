#!/usr/bin/env python3
import functools
import sys

tunnels = {}
rates = {}

for line in sys.stdin:
    start, rate, valves = (
        line.strip()
        .replace("Valve ", "")
        .replace(" has flow rate=", ";")
        .replace(" tunnel leads to valve ", "")
        .replace(" tunnels lead to valves ", "")
        .split(";")
    )
    rates[start] = int(rate)
    tunnels[start] = valves.split(", ")


@functools.cache
def max_flow(current, time, opened=()):
    if time <= 1:
        return 0
    if rates[current] and current not in opened:
        new_opened = tuple(sorted(opened + (current,)))
        result = (time - 1) * rates[current] + max_flow(current, time - 1, new_opened)
    else:
        result = 0
    return max(result, *(max_flow(node, time - 1, opened) for node in tunnels[current]))


print(max_flow("AA", 30))
