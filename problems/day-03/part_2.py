#!/usr/bin/env python3
import sys

score = 0
while True:
    try:
        (item,) = (
            set(sys.stdin.readline().strip())
            & set(sys.stdin.readline().strip())
            & set(sys.stdin.readline().strip())
        )
    except ValueError:
        break
    score += ord(item) + (1 - ord("a") if item.islower() else 27 - ord("A"))
print(score)
