
import re


def part_1():
    with open("d4.txt", 'r') as f:
        pattern = r'\d+'
        ans = 0
        for line in f:
            nums = [i for i in re.findall(pattern, line)]
    print("part1:", ans)

def part_2():
    with open("d4.txt", 'r') as f:
        pattern = r'\d+'
        ans = 0
        for line in f:
            nums = [i for i in re.findall(pattern, line)]

    print("part2:", ans)


if __name__ == "__main__":
    part_1()
    part_2()
