
import re
from itertools import pairwise


def is_safe(diff):
    if all(i > 0 and abs(i) <= 3 for i in diff):
        return True
    if all(i < 0 and abs(i) <= 3 for i in diff):
        return True
    return False


def part_1():
    with open("d2.txt", 'r') as f:
        pattern = r'\b\d+\b'
        safe = 0
        safe_2 = 0
        for line in f:
            nums = [int(i) for i in re.findall(pattern, line)]
            diff = [i - j for i, j in pairwise(nums)]
            if is_safe(diff):
                safe += 1
            else:
                for i in range(len(nums)):
                    new_nums = [n for pos, n in enumerate(nums) if i != pos]
                    diff = [i - j for i, j in pairwise(new_nums)]
                    if is_safe(diff):
                        safe_2 += 1
                        break

    print("part1:", safe)
    print("part2:", safe_2 + safe)


if __name__ == "__main__":
    part_1()
