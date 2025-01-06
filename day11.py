
from functools import cache
from private_input import DAY_11 as nums


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


print("part1", solve(nums, 25))
print("part2", solve(nums, 75))
