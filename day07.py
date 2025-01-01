import re
from itertools import product
from operator import add, mul
from utils import progressbar


def solve(lines, is_part_2=False):
    ans = 0
    all_ops = [add, mul]
    if is_part_2:
        all_ops.append(lambda x, y: int(str(x) + str(y)))

    for line in progressbar(lines):
        n, *nums = [int(i) for i in re.findall(r'\d+', line)]
        for pos, ops in enumerate(product(all_ops, repeat=len(nums) - 1)):
            result = nums[0]
            for op, next_n in zip(ops, nums[1:]):
                result = op(result, next_n)
                if result > n:
                    break
            if result == n:
                ans += n
                break
    return ans


ll = open("d7.txt", 'r').read().splitlines()
print(solve(ll))
print(solve(ll, is_part_2=True))
