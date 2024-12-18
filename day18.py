import heapq
from utils import P2d, UP, DOWN, LEFT, RIGHT, progressbar


def dijkstra(grid, end):
    visited = {P2d(0, 0)}
    queue = [(0, 0, 0)]
    while queue:
        dist, x, y = heapq.heappop(queue)
        if x == y == end:
            return dist

        for vec in (UP, DOWN, LEFT, RIGHT):
            p = P2d(x, y) + vec
            neigh = (dist + 1, p.x, p.y)
            if grid.get(p) == '.' and p not in visited:
                visited.add(p)
                heapq.heappush(queue, neigh)

    raise ValueError('No path found')


def build_grid(lines, steps, max_coord):
    grid = dict()
    for i in range(steps):
        p = P2d(*[int(j) for j in lines[i].split(",")])
        grid[p] = '#'

    for i in range(max_coord):
        for j in range(max_coord):
            if (p := P2d(i, j)) not in grid:
                grid[p] = '.'

    return grid


def part_2(grid, lines, steps, end):
    it = [i for i in range(steps, len(lines))]
    for i in progressbar(it):
        x, y = lines[i].split(",")
        new_byte = P2d(int(x), int(y))
        grid[new_byte] = '#'
        try:
            dijkstra(grid, end)
        except ValueError:
            return x, y

    raise ValueError('No blocking byte found')


ll = open("d18.txt", 'r').read().splitlines()
e = 70
steps_ = 1024
g = build_grid(ll, steps_, e + 1)
print(dijkstra(g, e))
print(part_2(g, ll, steps_, e))
