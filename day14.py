import re
import sys
import pathlib
from collections import Counter
from utils import progressbar

MAX_X = 101
MAX_Y = 103


def solve(lines, steps, debug=False):
    quadrant = Counter()
    final_pos = Counter()
    for line in lines:
        nums = list(map(int, re.findall(r'-?\d+', line)))
        x_start, y_start, x_vel, y_vel = nums
        x = (x_start + x_vel * steps) % MAX_X
        y = (y_start + y_vel * steps) % MAX_Y
        final_pos[(x, y)] += 1
        if x < MAX_X // 2:
            x_quad = 0
        elif x > MAX_X // 2:
            x_quad = 1
        else:
            continue

        if y < MAX_Y // 2:
            y_quad = 0
        elif y > MAX_Y // 2:
            y_quad = 1
        else:
            continue
        quadrant[(x_quad, y_quad)] += 1

    if debug:
        print_robots(final_pos)
    ans = 1
    for v in quadrant.values():
        ans *= v
    return ans, final_pos


def print_robots(robots):
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if (x, y) in robots:
                robots[(x, y)] = "█"
            to_print = f"\033[91m{robots[(x, y)]}\033[0m" if (x, y) in robots else '.'
            print(to_print, end='')
        print()


ll = pathlib.Path(sys.argv[1]).read_text().splitlines()
print(solve(ll, 100)[0])
all_steps = [i for i in range(10000)]
for i in progressbar(all_steps):
    _, fp = solve(ll, i, debug=False)
    if len(fp) == len(ll):
        _, fp = solve(ll, i, debug=True)
        break
