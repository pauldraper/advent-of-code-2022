#!/usr/bin/env python3
import itertools
import sys

directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
blizzards = {
    (i, j): set() if v == "." else {directions[v]}
    for i, line in enumerate(sys.stdin.readlines()[1:-1])
    for j, v in enumerate(line.strip()[1:-1])
}
maxes = tuple(max(p[k] for p in blizzards) + 1 for k in range(2))
start = (-1, 0)
end = (maxes[0], maxes[1] - 1)

moves = ((0, 0),) + tuple(directions.values())
queue = {start}
for time in itertools.count():
    if end in queue:
        break
    new_queue = set()
    for pos in queue:
        if pos not in (start, end) and blizzards.get(pos, True):
            continue
        new_queue.update(tuple(pos[k] + move[k] for k in range(2)) for move in moves)
    queue = new_queue
    blizzards = {
        p: {
            d
            for d in directions.values()
            if d in blizzards[(tuple((p[k] - d[k]) % maxes[k] for k in range(2)))]
        }
        for p in blizzards
    }

print(time)
