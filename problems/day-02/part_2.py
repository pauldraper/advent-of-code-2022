#!/usr/bin/env python3
import sys

score = 0
for line in sys.stdin:
    opponent, outcome = line.strip().split(" ")

    opponent = ord(opponent) - ord("A")
    outcome = ord(outcome) - ord("X")

    me = (opponent + outcome - 1) % 3

    score += me + 1 + outcome * 3
print(score)
