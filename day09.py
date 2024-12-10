import sys
import uuid
from dataclasses import dataclass
from itertools import pairwise

from utils import progressbar
from line_profiler_pycharm import profile
from collections import defaultdict


def sol(lines):
    ans = 0
    for line in lines:
        expand = []
        for pos, value in enumerate(line):
            if pos % 2 == 0:
                expand += [pos // 2] * int(value)
            else:
                expand += ['.'] * int(value)

        left = 0
        right = len(expand) - 1
        while left < right:
            if expand[left] != '.':
                left += 1
                continue
            if expand[right] == '.':
                right -= 1
                continue
            expand[left], expand[right] = expand[right], expand[left]
            left += 1
            right -= 1
        ans += sum(pos * int(value) for pos, value in enumerate(expand) if value != '.')

    return ans


def part_3(lines):
    ans = 0
    mem = list(map(int, lines[0]))

    return ans

@profile
def part_2(lines):

    ans = 0
    for line in lines:
        expand = []
        for pos, value in enumerate(line):
            if pos % 2 == 0:
                expand += [pos // 2] * int(value)
            else:
                expand += ['.'] * int(value)

        it = [i for i in reversed(range(expand[-1] + 1))]
        for i in progressbar(it):
            count = expand.count(i)
            r = expand.index(i)
            l = count_point = 0
            while l < r:
                if expand[l] == '.':
                    for count_point, value in enumerate(pairwise(expand[l:])):
                        if value[0] != value[1]:
                            break
                    count_point += 1
                    if count_point >= count:
                        break
                    l += count_point
                else:
                    l += 1

            if count_point >= count:
                expand[l:l + count], expand[r:r + count] = expand[r:r + count], expand[l:l + count]
            # print(''.join((str(i) for i in expand)), i)

        ans += sum(pos * int(value) for pos, value in enumerate(expand) if value != ".")

    return ans


@dataclass(frozen=True)
class File:
    size: int
    id: int


def solv(lines):
    ans = 0
    files = []
    points = defaultdict(list)
    for pos, value in enumerate(map(int, lines[0])):
        if pos % 2 == 0:
            files.append(File(value, pos // 2))
        else:
            points[value].append(pos // 2)

    for f in files[::-1]:
        print(f)

    print(points)
    return ans


def solve(lines):
    ans = 0
    count = dict()
    for line in lines:
        expand = ''
        for pos, value in enumerate(line):
            if pos % 2 == 0:
                expand += str(pos // 2) * int(value)
                count[pos // 2] = int(value)
            else:
                expand += '.' * int(value)

        max_key = max(map(int, count.keys()))
        right = len(expand) - 1
        for i in reversed(range(max_key + 1)):
            last = str(i)
            count = count[i]
            right -= count - 1
            if expand[:right].find('.' * count) >= 0:
                first = expand[:right].replace('.' * count, last * count, 1)
                second = expand[right:].replace(last * count, '.' * count, 1)
                expand = first + second
                # print(expand)
            while expand[right] != str(i - 1) and right > 0:
                right -= 1

        ans += sum(pos * int(value) for pos, value in enumerate(expand.replace('.', '0')))
    return ans


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        ll = [i.strip() for i in f.readlines()]

    # print(sol(ll))
    # print(part_2(ll))
    print(solv(ll))