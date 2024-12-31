
import re
from itertools import pairwise

def solve():
    lines = [[int(i) for i in re.findall(r'\d+', line)] for line in open("d2.txt").read().splitlines()]
    is_safe = lambda x: all(i > 0 and abs(i) <= 3 for i in x) or all(i < 0 and abs(i) <= 3 for i in x)
    print("part 1:", sum(is_safe([i - j for i, j in pairwise(nums)]) for nums in lines))
    print("part 2:", sum((any((is_safe([j - k for j, k in pairwise([n for pos, n in enumerate(nums) if i != pos])]) for i in range(len(nums)))) for nums in lines)))

solve()
