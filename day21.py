import re
from collections import defaultdict
from itertools import combinations, pairwise

from private_input import QUERY
from utils import RIGHT, LEFT, DOWN, UP, P2d

MOVES = {
    RIGHT: '>',
    LEFT: '<',
    UP: '^',
    DOWN: 'v',
}


def find_path_recursive(start, end, grid, path, visited, paths, max_dist):
    if start == end:
        return {path}
    elif len(path) >= max_dist:
        return set()

    for vec in (UP, DOWN, LEFT, RIGHT):
        p = start + vec
        if p in grid and p not in visited:
            paths |= find_path_recursive(p, end, grid, path + MOVES[vec], visited | {p}, paths, max_dist)
    return paths


def get_paths(robot):
    paths = defaultdict(set)
    for i, j in combinations(robot.keys(), 2):
        v1, v2 = robot[i], robot[j]
        max_dist = abs(i.x - j.x) + abs(i.y - j.y)
        v1_v2_paths = find_path_recursive(i, j, robot, '', {i}, set(), max_dist)
        paths[v1 + v2] = v1_v2_paths
        v2_v1_paths = find_path_recursive(j, i, robot, '', {j}, set(), max_dist)
        paths[v2 + v1] = v2_v1_paths

    for k in robot.keys():
        v = robot[k]
        paths[v + v] = {""}
    return paths


def get_robot_instructions(sequence, shortest_paths):
    all_paths = ['']
    for i, j in pairwise('A' + sequence):
        new_paths = []
        for temp_path in all_paths:
            for path_ij in shortest_paths[i + j]:
                new_path = temp_path + path_ij + 'A'
                new_paths.append(new_path)
        all_paths = new_paths
    return all_paths


def get_shortest_paths():
    robot1 = {
        P2d(0, 0): '7',
        P2d(0, 1): '8',
        P2d(0, 2): '9',
        P2d(1, 0): '4',
        P2d(1, 1): '5',
        P2d(1, 2): '6',
        P2d(2, 0): '1',
        P2d(2, 1): '2',
        P2d(2, 2): '3',
        P2d(3, 1): '0',
        P2d(3, 2): 'A',
    }
    robot2 = {
        P2d(0, 1): '^',
        P2d(0, 2): 'A',
        P2d(1, 0): '<',
        P2d(1, 1): 'v',
        P2d(1, 2): '>',
    }
    r1_paths = get_paths(robot1)
    r2_paths = get_paths(robot2)
    return r1_paths, r2_paths


CACHE = dict()

def get_instruction_score(sequence, level, paths):
    if (sequence, level) in CACHE:  # cache
        return CACHE[(sequence, level)]
    if level == 0 or len(sequence) <= 1:  # recursion base case
        return len(sequence)
    score = 0
    for i, j in pairwise('A' + sequence):
        seq_score = float('inf')
        for path_ij in paths[i + j]:
            seq_score = min(get_instruction_score(path_ij + 'A', level - 1, paths), seq_score)
        score += seq_score
    CACHE[(sequence, level)] = score
    return score


def solve(seq, r1_paths, r2_paths, levels):
    print(seq)
    r1_instructions = get_robot_instructions(seq, r1_paths)
    min_len = 1e12
    for r1_path in r1_instructions:
        min_len = min(min_len, get_instruction_score(r1_path, levels, r2_paths))
    mult = int(re.findall(r'\d+', seq)[0])
    return mult * min_len


r1, r2 = get_shortest_paths()
print(sum(solve(s, r1, r2, 2) for s in QUERY))
print(sum(solve(s, r1, r2, 25) for s in QUERY))
