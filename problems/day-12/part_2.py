#!/usr/bin/env python3
import heapq
import sys

grid = {
    (i, j): ord(value.replace("S", "a"))
    for i, line in enumerate(sys.stdin)
    for j, value in enumerate(line.strip())
}
end = next(position for position, value in grid.items() if value == ord("E"))
grid[end] = ord("z")

directions = ((-1, 0), (0, -1), (0, 1), (1, 0))

queue = [(0, end)]
dists = {}
while queue:
    dist, position = heapq.heappop(queue)
    if position in dists and dists[position] <= dist:
        continue
    dists[position] = dist
    for direction in directions:
        new_position = tuple(sum(x) for x in zip(position, direction))
        if new_position in grid and grid[position] - 1 <= grid[new_position]:
            heapq.heappush(queue, (dist + 1, new_position))
print(
    min(
        dists[position]
        for position, value in grid.items()
        if position in dists and value == ord("a")
    )
)
