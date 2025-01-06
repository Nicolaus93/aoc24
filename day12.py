
from utils import P2d, UP, RIGHT, LEFT, DOWN


def explore(p, grid):
    perimeter = 0
    queue = [p]
    visited = set()
    while queue:
        current = queue.pop()
        letter = grid[current]
        visited.add(current)
        for vec in (UP, RIGHT, LEFT, DOWN):
            new_p = current + vec
            if grid.get(new_p, False) == letter and new_p not in visited:
                if new_p not in queue:
                    queue.append(new_p)
            elif new_p not in visited:
                perimeter += 1

    return len(visited) * perimeter, visited


def solve(grid, n, m):
    part_1 = part_2 = 0
    visited = set()
    for i in range(n):
        for j in range(m):
            if P2d(i, j) not in visited:
                score, cluster = explore(P2d(i, j), grid)
                res = 0
                for _ in range(4):
                    res += count_left(cluster)
                    cluster = {P2d(p.y, -p.x) for p in cluster}  # rotate grid
                part_2 += res * len(cluster)
                visited |= cluster
                part_1 += score
    return part_1, part_2


def count_left(cluster):
    if len(cluster) <= 2:
        return 1
    min_x, *_, max_x = sorted(p.x for p in cluster)
    min_y, *_, max_y = sorted(p.y for p in cluster)

    sides = 0
    for j in range(min_y - 1, max_y):  # start from one off on the left
        is_right_occ = False
        for i in range(min_x, max_x + 2):  # exit one more down
            if P2d(i, j) in cluster:
                if is_right_occ:
                    sides += 1
                is_right_occ = False  # reset
                continue

            # outside
            if P2d(i, j + 1) in cluster:
                is_right_occ = True
            else:
                if is_right_occ:
                    sides += 1
                    is_right_occ = False

    return sides


with open('d12.txt') as f:
    ll = [i.strip() for i in f.readlines()]
    g = dict()
    for i in range(len(ll)):
        for j in range(len(ll[0])):
            g[P2d(i, j)] = ll[i][j]

print(solve(g, len(ll), len(ll[0])))
