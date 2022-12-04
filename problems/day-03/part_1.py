#!/usr/bin/env python3
import sys

score = 0
for line in sys.stdin:
    line = line.strip()
    (item,) = set(line[: len(line) // 2]) & set(line[len(line) // 2 :])
    score += ord(item) + (1 - ord("a") if item.islower() else 27 - ord("A"))
print(score)
