import re
import sys
from itertools import product
from operator import add, mul
from utils import progressbar


def solve(lines, is_part_2=False):
    ans = 0
    all_ops = [add, mul]
    for line in progressbar(lines):
        n, *nums = [int(i) for i in re.findall(r'\d+', line)]
        if is_part_2:
            all_ops.append(lambda x, y: int(str(x) + str(y)))
        for ops in product(all_ops, repeat=len(nums) - 1):
            result = nums[0]
            for i, op in enumerate(ops):
                result = op(result, nums[i + 1])
                if result > n:
                    break

            if result == n:
                ans += n
                break
    return ans



if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        ll = [line.strip() for line in f]

    
    print(solve(ll))
    print(solve(ll, is_part_2=True))
