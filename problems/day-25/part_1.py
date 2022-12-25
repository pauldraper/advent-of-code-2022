#!/usr/bin/env python3
import functools
import sys

digit_value = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
digit_name = dict(map(reversed, digit_value.items()))

total = sum(
    functools.reduce(
        lambda t, c: t * 5 + digit_value[c],
        line.strip(),
        0,
    )
    for line in sys.stdin
)
result = ""
while total:
    m = total % 5
    if m not in digit_name:
        m -= 5
        total += 5
    result += digit_name[m]
    total //= 5
print("".join(reversed(result)))
