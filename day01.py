
import re
from collections import Counter


def solve():
    nums = [[int(i) for i in re.findall(r'\d+', line)] for line in open("d1.txt").read().splitlines()]
    n1 = sorted(n[0] for n in nums)
    n2 = sorted(n[1] for n in nums)
    count = Counter(n2)
    print("part1:", sum(abs(i * count[i] - j) for i, j in zip(n1, n2)))
    print("part2:", sum(i * count[i] for i in n1))

solve()
