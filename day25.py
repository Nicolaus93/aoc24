from itertools import product


def get_max_heights(pattern):
    max_heights = [None] * len(pattern[0])
    for j in range(len(pattern[0])):
        for i in range(len(pattern)):
            if pattern[i][j] == '#':
                max_heights[j] = i
    return max_heights


def read_keys():
    lines = open("d25.txt", 'r').read().splitlines()
    pattern = []
    patterns = []
    for line in lines:
        line = line.strip()
        if len(line) > 1:
            pattern.append(line)
        else:
            patterns.append(pattern)
            pattern = []

    locks = []
    keys = []
    for p in patterns:
        if p[0].startswith("#"):
            locks.append(p)
        elif p[0].startswith("."):
            keys.append(p)
    return keys, locks

def solve():
    keys, locks = read_keys()
    locks_heights = [get_max_heights(d) for d in locks]
    keys_heights = [get_max_heights(k[::-1]) for k in keys]
    ans = 0
    for couple in product(locks_heights, keys_heights):
        lock, key = couple
        if all(a + b <= 5 for a, b in zip(lock, key)):
            ans += 1
    return ans


print(solve())
