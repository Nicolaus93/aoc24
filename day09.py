from collections import defaultdict
from itertools import pairwise
from bisect import insort


def expand_nums(block):
    expand = []
    for pos, value in enumerate(block):
        if pos % 2 == 0:
            expand += [pos // 2] * int(value)
        else:
            expand += ['.'] * int(value)
    return expand


def get_free_sizes(mem):
    free_sizes = defaultdict(list)
    for pos, couple in enumerate(pairwise(mem)):
        i, j = couple
        if i != j and j == '.':
            free_size = 1
        elif i == j == '.':
            free_size += 1
        elif i != j and i == '.':
            free_sizes[free_size].append(pos - free_size + 1)
    return free_sizes


def part_1(lines):
    expand = expand_nums(lines[0])
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
    return sum(pos * int(value) for pos, value in enumerate(expand) if value != '.')


def get_block_size(n, mem, r_idx):
    l_idx = r_idx
    while mem[l_idx] == n and l_idx >= 0:
        l_idx -= 1
    return l_idx + 1


def part_2(disk_map):
    mem = expand_nums(disk_map)
    free_sizes = get_free_sizes(mem)
    n = 9999
    r = len(mem) - 1
    while n > 0:
        l = get_block_size(n, mem, r)
        block_size = r + 1 - l
        keys = [k for k in free_sizes.keys() if k >= block_size]
        key = min(keys, key=lambda k: free_sizes[k][0], default=-1)
        if key != -1:
            pos = free_sizes[key].pop(0)
            if not free_sizes[key]: del free_sizes[key]
            if pos < r:
                mem[pos:pos + block_size], mem[l:l + block_size] = mem[l:l + block_size], mem[pos:pos + block_size]
                # update free sizes
                if (left_space := key - block_size) > 0:
                    insort(free_sizes[left_space], pos + block_size)
        n -= 1
        while 0 < n != mem[r]:
            r -= 1
    return sum(pos * int(value) for pos, value in enumerate(mem) if value != ".")


ll = open("d9.txt", 'r').read().splitlines()
print("part 1:", part_1(ll))
print("part 2:", part_2(ll[0]))
