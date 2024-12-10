
import re


def part_1():
    with open("d3.txt", 'r') as f:
        pattern = r'mul\(\d+,\d+\)'
        ans = 0
        for line in f:
            nums = [i for i in re.findall(pattern, line)]
            for mul in nums:
                n = re.findall(r'\d+', mul)
                ans += int(n[0]) * int(n[1])
    print("part1:", ans)


def part_2():
    with open("d3.txt", 'r') as f:
        pattern = r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)'
        ans = 0
        state = True
        for line in f:
            nums = [i for i in re.findall(pattern, line)]
            for mul in nums:
                if mul == 'do()':
                    state = True
                elif mul == 'don\'t()':
                    state = False
                elif state:
                    n = re.findall(r'\d+', mul)
                    ans += int(n[0]) * int(n[1])
    print("part2:", ans)


if __name__ == "__main__":
    part_1()
    part_2()
