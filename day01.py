

import re
from collections import Counter


def part_1():
    with open("d1.txt", 'r') as f:
        lines = f.readlines()
        pattern = r'\b\d+\b'
        n1 = []
        n2 = []
        for line in lines:
            integer_numbers = re.findall(pattern, line)

            # Convert the matched strings to integers
            integer_numbers = [int(num) for num in integer_numbers]
            n1.append(integer_numbers[0])
            n2.append(integer_numbers[1])

        n1 = sorted(n1)
        n2 = sorted(n2)

    count = Counter(n2)
    dist = 0
    sim_score = 0
    for m1, m2 in zip(n1, n2):
        m1 = m1 * count[m1]
        dist += abs(m1 - m2)
        sim_score += m1

    print("part1:", dist)
    print("part2:", sim_score)


if __name__ == "__main__":
    part_1()
