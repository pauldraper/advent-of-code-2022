#!/usr/bin/env python3
import collections
import sys

sizes = collections.defaultdict(int)
line = next(sys.stdin, None)
while line:
    parts = line.strip().split(" ")
    if parts[1] == "cd":
        if parts[2] == "/":
            path = ()
        elif parts[2] == "..":
            path = path[:-1]
        else:
            path += (parts[2],)
        line = next(sys.stdin, None)
    elif parts[1] == "ls":
        while True:
            line = next(sys.stdin, None)
            if not line or line.startswith("$"):
                break
            detail, name = line.split(" ")
            if detail == "dir":
                continue
            for i in range(len(path) + 1):
                sizes[path[: len(path) - i]] += int(detail)

total = sizes[()]
print(min(s for s in sizes.values() if total - s <= 70000000 - 30000000))
