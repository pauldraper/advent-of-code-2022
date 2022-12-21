#!/usr/bin/env python3
import operator
import sys

monkeys = {}


def calculator(args):
    if len(args) == 1:
        return lambda: int(args[0])
    a, sym, b = args
    op = {
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.floordiv,
        "+": operator.add,
    }[sym]
    return lambda: op(monkeys[a](), monkeys[b]())


for line in sys.stdin:
    name, b = line.strip().split(": ")
    args = b.split(" ")
    monkeys[name] = calculator(args)

print(monkeys["root"]())
