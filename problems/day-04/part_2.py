#!/usr/bin/env python3
import sys

count = 0
for line in sys.stdin:
    (a1, a2), (b1, b2) = (map(int, section.split("-")) for section in line.split(","))
    count += a1 <= b1 <= a2 or a1 <= b2 <= a2 or b1 <= a1 <= b2 or b1 <= a2 <= b2
print(count)
