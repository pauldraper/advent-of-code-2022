#!/usr/bin/env python3
import sys


def compare(a, b):
    if type(a) == int and type(b) == int:
        return a - b
    if type(a) == int:
        a = [a]
    if type(b) == int:
        b = [b]
    return next(
        (c for c in (compare(x, y) for x, y in zip(a, b)) if c), len(a) - len(b)
    )


pairs = sys.stdin.read().strip().split("\n\n")
result = sum(
    i for i, pair in enumerate(pairs, 1) if compare(*map(eval, pair.split("\n"))) <= 0
)
print(result)
