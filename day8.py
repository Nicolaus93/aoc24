
import sys
from collections import defaultdict
from itertools import combinations


def solve(lines, part_2=False, debug=False):
    n, m = len(lines), len(lines[0])
    antennas = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if lines[i][j] != ".":
                antennas[lines[i][j]].append((i, j))

    antinodes = set()
    for a, loc in antennas.items():
        for p1, p2 in combinations(loc, 2):
            p1, p2 = sorted((p1, p2), key=lambda p: p[1])  # sort by x
            dir_y = p2[0] - p1[0]
            dir_x = p2[1] - p1[1]

            y = p1[0] - dir_y
            x = p1[1] - dir_x
            while 0 <= x < m and 0 <= y < n:
                antinodes.add((y, x))
                if not part_2:
                    break
                y -= dir_y
                x -= dir_x

            y = p2[0] + dir_y
            x = p2[1] + dir_x
            while 0 <= x < m and 0 <= y < n:
                antinodes.add((y, x))
                if not part_2:
                    break
                y += dir_y
                x += dir_x

        if part_2:
            antinodes |= set(loc)

    if debug:
        for i in range(n):
            for j in range(m):
                if (i, j) in antinodes:
                    print("#", end="")
                else:
                    print(lines[i][j], end="")
            print()
    return len(antinodes)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        ll = [i.strip() for i in f.readlines()]
    
    print(solve(ll))
    print(solve(ll, part_2=True))
