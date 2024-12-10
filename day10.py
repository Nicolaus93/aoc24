
import sys


def search(grid, i, j, part1=True):
    n, m = len(grid), len(grid[0])
    nines = set() if part1 else list()
    queue = [(i, j)]
    while queue:
        i, j = queue.pop()
        for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ii = i + x
            jj = j + y
            if 0 <= ii < n and 0 <= jj < m and grid[ii][jj] - grid[i][j] == 1:
                queue.append((ii, jj))
                if grid[ii][jj] == 9:
                    if part1:
                        nines.add((ii, jj))
                    else:
                        nines.append((ii, jj))

    return len(nines)


def solve(lines):
    ans1 = ans2 = 0
    grid = []
    for line in lines:
        grid.append([int(i) if i.isdigit() else -1 for i in line])

    n, m = len(lines), len(lines[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                ans1 += search(grid, i, j, part1=True)
                ans2 += search(grid, i, j, part1=False)
    print("part1", ans1)
    print("part2", ans2)


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        ll = [i.strip() for i in f.readlines()]

    solve(ll)
