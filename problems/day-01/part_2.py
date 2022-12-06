#!/usr/bin/env python3
import sys

totals = []
current = 0
for line in sys.stdin:
    if line.strip():
        current += int(line)
    else:
        totals.append(current)
        current = 0
print(sum(sorted(totals)[-3:]))
