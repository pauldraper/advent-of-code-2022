#!/usr/bin/env python3
import functools
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


packets = [eval(line) for line in sys.stdin if line.strip()] + [[[2]], [[6]]]
packets.sort(key=functools.cmp_to_key(compare))

a = packets.index([[2]]) + 1
b = packets.index([[6]]) + 1
print(a * b)
