
import sys
from utils import P2d

DOWN = P2d(1, 0)
UP = P2d(-1, 0)
RIGHT = P2d(0, 1)
LEFT = P2d(0, -1)


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


def part_1(grid, n, m):
    ans = 0
    visited = set()
    for i in range(n):
        for j in range(m):
            if P2d(i, j) not in visited:
                score, new_visited = explore(P2d(i, j), grid)
                visited |= new_visited
                ans += score
    return ans


def count_sides(grid, n, m):
    ans = 0
    visited = set()
    for i in range(n):
        for j in range(m):
            if P2d(i, j) not in visited:
                _, cluster = explore(P2d(i, j), grid)
                res = 0
                for _ in range(4):
                    res += count_left(cluster)
                    cluster = {P2d(p.y, -p.x) for p in cluster}  # rotate grid
                ans += res * len(cluster)
                visited |= cluster
    return ans


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


def print_grid(grid):
    min_x, *_, max_x = sorted(p.x for p in grid)
    min_y, *_, max_y = sorted(p.y for p in grid)

    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            print(grid.get(P2d(i, j)), end="")
        print()


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        ll = [i.strip() for i in f.readlines()]
        g = dict()
        for i in range(len(ll)):
            for j in range(len(ll[0])):
                g[P2d(i, j)] = ll[i][j]

    print(part_1(g, len(ll), len(ll[0])))
    print(count_sides(g, len(ll), len(ll[0])))
