
import re
import sys
from functools import cache


@cache
def transform(n, times):
    if times == 0:
        return 1
    if n == 0:
        return transform(1, times - 1)
    elif (l := len(str(n))) % 2 == 0:
        n1 = int(str(n)[: l // 2])
        n2 = int(str(n)[l // 2 :])
        return transform(n1, times - 1) + transform(n2, times - 1)
    else:
        return transform(n * 2024, times - 1)


def solve(nums, times):
    for _ in range(times):
        total = 0
        for pos, n in enumerate(nums):
            total += transform(n, times)
        return total


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        ll = list(map(int, re.findall(r"\d+", f.read())))

    print("part1", solve(ll, 25))
    print("part2", solve(ll, 75))
