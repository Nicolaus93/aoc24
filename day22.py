
from itertools import pairwise
from utils import progressbar


def next_secret_num(n):
    res = n * 64
    n = n ^ res
    n = n % 16777216
    res = n // 32
    n = n ^ res
    n = n % 16777216
    res = n * 2048
    n = n ^ res
    n = n % 16777216
    return n


def get_best_price(diffs):
    seqs = set()
    for d in diffs:
        seqs |= d.keys()
    ans = 0
    for seq in progressbar(seqs):
        res = sum(diff.get(seq, 0) for diff in diffs)
        ans = max(ans, res)
    return ans


def get_diff(last_digit):
    d = dict()
    diff = [j - i for i, j in pairwise(last_digit)]
    for pos in range(4, len(last_digit)):
        i, j, k, l = diff[pos - 4], diff[pos - 3], diff[pos - 2], diff[pos - 1]
        if (i, j, k, l) not in d:
            d[(i, j, k, l)] = last_digit[pos]
    return d


def solve():
    nums = [int(i) for i in open("d22.txt").read().splitlines()]
    ans = 0
    diffs = []
    for m in nums:
        last_digit = [m % 10]
        for _ in range(2000):
            m = next_secret_num(m)
            last_digit.append(m % 10)
        diffs.append(get_diff(last_digit))

        ans += m
    print(ans)
    print(get_best_price(diffs))


solve()
