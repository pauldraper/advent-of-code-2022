#!/usr/bin/env python3
import sys

totals = []
current = 0
while True:
    line = sys.stdin.readline()
    if line.strip():
        current += int(line)
    else:
        totals.append(current)
        current = 0
    if not line:
        break
totals.sort()
print(sum(totals[-3:]))
