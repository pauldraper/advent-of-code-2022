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
    rate = int(rate)
    if rate:
        rates[start] = rate
    tunnels[start] = valves.split(", ")

rates = {k: v for k, v in rates.items() if v}


@functools.cache
def dist(a, b, visited=set()):
    if a == b:
        return 0
    if b in visited:
        return float("inf")
    visited.add(b)
    best = min(dist(a, c) for c in tunnels[b])
    visited.remove(b)
    return best + 1


def total(current, time, nodes):
    result = 0
    for node in nodes:
        new_time = time - dist(current, node) - 1
        if new_time <= 0:
            continue
        new_nodes = tuple(n for n in nodes if n != node)
        result = max(result, new_time * rates[node] + total(node, new_time, new_nodes))
    return result


for partition in range(1 << (len(rates) - 1)):
    if partition % 1000 == 0:
        print(partition, best)
    a = tuple(node for i, node in enumerate(rates) if partition & (1 << i))
    b = tuple(node for i, node in enumerate(rates) if not partition & (1 << i))
    best = max(best, total("AA", 26, a) + total("AA", 26, b))
print(best)
