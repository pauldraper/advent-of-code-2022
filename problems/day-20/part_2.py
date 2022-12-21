#!/usr/bin/env python3
import sys

monkeys = {}


def calculator(args):
    if len(args) == 1:
        return lambda: int(args[0])
    a, sym, b = args
    return lambda: f"({monkeys[a]()} {sym} {monkeys[b]()})"


for line in sys.stdin:
    name, b = line.strip().split(": ")
    args = b.split(" ")
    if name == "root":
        args[1] = "="
    monkeys[name] = (lambda: "x") if name == "humn" else calculator(args)

print(monkeys["root"]())
