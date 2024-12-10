from collections import defaultdict
from itertools import combinations


def is_valid(nums, greater_than):
    for i, j in combinations(nums, 2):
        if not j in greater_than[i]:
            return False
    return True


def part_1(lines):
    ans = ans_2 = 0
    greater_than = defaultdict(list)
    for line in lines:
        if "|" in line:
            order = line.split("|")
            greater_than[order[0]].append(order[1])
        elif "," in line:
            nums = line.split(",")

            if is_valid(nums, greater_than):
                ans += int(nums[len(nums) // 2])
            else:
                while not is_valid(nums, greater_than):
                    for i in range(len(nums)):
                        for j in range(i + 1, len(nums)):
                            if not nums[j] in greater_than[nums[i]]:
                                nums[j], nums[i] = nums[i], nums[j]
                ans_2 += int(nums[len(nums) // 2])

    print("part1:", ans)
    print("part2:", ans_2)


if __name__ == "__main__":
    with open("d5.txt", "r") as f:
        ll = [line.strip() for line in f]

    part_1(ll)
