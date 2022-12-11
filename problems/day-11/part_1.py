#!/usr/bin/env python3
import sys

items = []
operations = []
divs = []
falses = []
trues = []

while sys.stdin.readline():
    items.append(
        [
            int(item)
            for item in sys.stdin.readline()
            .replace("  Starting items: ", "")
            .split(", ")
        ]
    )
    operations.append(
        eval(f'lambda old: {sys.stdin.readline().replace("  Operation: new = ", "")}')
    )
    divs.append(int(sys.stdin.readline().split(" ")[-1]))
    trues.append(int(sys.stdin.readline().split(" ")[-1]))
    falses.append(int(sys.stdin.readline().split(" ")[-1]))
    sys.stdin.readline()

counts = [0] * len(items)
for _ in range(20):
    for i, (items_, operation, div, true, false) in enumerate(
        zip(items, operations, divs, trues, falses)
    ):
        for item in items_:
            item = operation(item) // 3
            items[false if item % div else true].append(item)
        counts[i] += len(items_)
        items_.clear()

counts.sort()
print(counts[-1] * counts[-2])
