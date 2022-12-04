#!/usr/bin/env python3
import sys

count = 0
for line in sys.stdin:
    a, b = line.split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    count += a1 <= b1 <= b2 <= a2 or b1 <= a1 <= a2 <= b2
print(count)
