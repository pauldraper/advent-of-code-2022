#!/usr/bin/env python3
import sys

most = 0
current = 0
for line in sys.stdin:
    if line.strip():
        current += int(line)
    else:
        most = max(most, current)
        current = 0
print(most)
