from collections import deque, defaultdict
from itertools import combinations

from utils import P2d, UP, DOWN, LEFT, RIGHT
import heapq


def get_grid(lines):

    grid = dict()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            grid[P2d(i, j)] = lines[i][j]
            if lines[i][j] == 'S':
                start = P2d(i, j)
            if lines[i][j] == 'E':
                end = P2d(i, j)

    return grid, start, end


def dijkstra(grid, start, end):
    visited = {start}
    queue = [(0, start)]
    prev = dict()
    all_dist = {start: 0}
    while queue:
        dist, curr = heapq.heappop(queue)
        if curr == end:
            path = deque()
            while curr is not None:
                path.append(curr)
                curr = prev.get(curr)
            return dist, path, all_dist

        for vec in (UP, DOWN, LEFT, RIGHT):
            p = curr + vec
            neigh = (dist + 1, p)
            if grid.get(p) in '.E' and p not in visited:  # if it's already visited then its cost will be bigger for sure
                visited.add(p)
                heapq.heappush(queue, neigh)
                prev[p] = curr
                all_dist[p] = dist + 1

    raise RuntimeError('No path found')


def find_shortcut(wall, all_dist):
    for vec in (UP, LEFT):
        p1 = wall + vec
        p2 = wall - vec
        if p1 in all_dist and p2 in all_dist:
            origin = min((p1, p2), key=all_dist.get)
            dest = max((p1, p2), key=all_dist.get)
            saving = all_dist[dest] - all_dist[origin] - 2  # 2 to account for the steps through #
            yield saving, origin, dest


def find_all_cheats(path, all_dist, steps=20):
    all_savings = defaultdict(set)
    for p1, p2 in combinations(path, 2):
        cheat_dist = abs(p1.x - p2.x) + abs(p1.y - p2.y)
        if cheat_dist <= steps:
            origin = min((p1, p2), key=all_dist.get)
            dest = max((p1, p2), key=all_dist.get)
            saving = all_dist[dest] - all_dist[origin] - cheat_dist
            if saving >= 100:
                all_savings[saving].add((origin, dest))
    return all_savings


def get_min_shortcut(path, all_dist, grid):
    all_savings = defaultdict(set)
    for p in path:
        for vec in (UP, DOWN, LEFT, RIGHT):
            if grid.get(p + vec) == "#":
                for saving, origin, dest in find_shortcut(p + vec, all_dist):
                    all_savings[saving].add((origin, dest))
    return all_savings


def print_path(grid, path):
    max_x = max(grid, key=lambda p: p.x)
    max_y = max(grid, key=lambda p: p.y)
    for i in range(max_x.x + 1):
        for j in range(max_y.y + 1):
            to_print = "x" if P2d(i, j) in path else grid.get(P2d(i, j))
            print(to_print, end='')
        print()


def main():
    ll = open("d20.txt", 'r').read().splitlines()
    grid, start, end = get_grid(ll)
    dist, path, all_dist = dijkstra(grid, start, end)

    print("Finding cheats..")
    # all_savings = get_min_shortcut(path, all_dist, grid)
    all_savings = find_all_cheats(path, all_dist)
    count = 0
    for saving, cheats_set in all_savings.items():
        if saving >= 100:
            print(f"Saving {saving}: {len(cheats_set)} times")
            count += len(cheats_set)
    print(count)

main()
