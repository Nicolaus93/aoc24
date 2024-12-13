import re
import sys
import pathlib
from utils import P2d


def grab(p1, p2, p3):
    score = 0
    a, a_rem = divmod(p2.x * p3.y - p2.y * p3.x, p1.y * p2.x - p1.x * p2.y)
    if a_rem == 0:  # check "a" is integer
        b, b_rem = divmod(p3.x - a * p1.x, p2.x)
        if b_rem == 0:  # check "b" is integer
            score = a * 3 + b
    return score


def solve(lines, part_2=False):
    ans = 0
    points = []
    for line in lines:
        try:
            p = P2d(*map(int, re.findall(r'\d+', line)))
            points.append(p)
        except TypeError:  # new line
            if part_2:
                points[-1] = points[-1] + P2d(10000000000000, 10000000000000)
            ans += grab(*points)
            points = []

    return ans


ll = pathlib.Path(sys.argv[1]).read_text().splitlines()
print(solve(ll))
print(solve(ll, part_2=True))
