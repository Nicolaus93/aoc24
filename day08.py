
import sys
from collections import defaultdict
from itertools import combinations
from utils import P2d


def sol(lines, part_2=False, debug=False):
    rows, cols = len(lines), len(lines[0])
    antennas = defaultdict(list)
    for y in range(rows):
        for x in range(cols):
            if lines[y][x] != ".":
                antennas[lines[y][x]].append(P2d(x, y))

    antinodes = set()
    for a, loc in antennas.items():
        for p1, p2 in combinations(loc, 2):
            vec = p2 - p1
            for mul, start in zip((-1, 1), (p1, p2)):
                p = start + (mul * vec)  # first in p1 direction, then in p2 direction
                while 0 <= p.y < rows and 0 <= p.x < cols:
                    antinodes.add(P2d(p.x, p.y))
                    if not part_2:
                        break
                    p = p + (mul * vec)

        if part_2:
            antinodes |= set(loc)

    if debug:
        for y in range(rows):
            for x in range(cols):
                if P2d(x, y) in antinodes:
                    print("#", end="")
                else:
                    print(lines[y][x], end="")
            print()
    return len(antinodes)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        ll = [i.strip() for i in f.readlines()]
    
    print(sol(ll))
    print(sol(ll, part_2=True))
