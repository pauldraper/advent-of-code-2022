#!/usr/bin/env python3
import heapq
import sys

grid = {
    (i, j): ord(value)
    for i, line in enumerate(sys.stdin)
    for j, value in enumerate(line.strip())
}
start = next(position for position, value in grid.items() if value == ord("S"))
end = next(position for position, value in grid.items() if value == ord("E"))
grid[start] = ord("a")
grid[end] = ord("z")

directions = ((-1, 0), (0, -1), (0, 1), (1, 0))

queue = [(0, start)]
dists = {}
while queue:
    dist, position = heapq.heappop(queue)
    if position in dists and dists[position] <= dist:
        continue
    dists[position] = dist
    for direction in directions:
        new_position = tuple(sum(x) for x in zip(position, direction))
        if new_position in grid and grid[new_position] <= grid[position] + 1:
            heapq.heappush(queue, (dist + 1, new_position))
print(dists[end])
