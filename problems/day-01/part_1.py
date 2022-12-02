#!/usr/bin/env python3
import sys

most = 0
current = 0
while True:
    line = sys.stdin.readline()
    if line.strip():
        current += int(line)
    else:
        most = max(most, current)
        current = 0
    if not line:
        break
print(most)
