#!/usr/bin/env python3
import sys

stacks = []

while True:
    line = sys.stdin.readline()
    if line[1] == "1":
        break
    for i, c in enumerate(line[1::4]):
        if c == " ":
            continue
        while len(stacks) <= i:
            stacks.append([])
        stacks[i].insert(0, c)

sys.stdin.readline()

for line in sys.stdin:
    line = line.strip()
    _, count, _, start, _, end = line.split(" ")
    count = int(count)
    start = int(start) - 1
    end = int(end) - 1

    stacks[end] += stacks[start][-count:]
    del stacks[start][-count:]

print("".join(stack[-1] for stack in stacks))
