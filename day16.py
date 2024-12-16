import contextlib
import heapq
from collections import defaultdict
from dataclasses import dataclass
from typing import Self
from utils import P2d, RIGHT, UP, DOWN, LEFT


@dataclass(frozen=True)
class Deer:
    pos: P2d
    dir: P2d = RIGHT
    dist: int = 0
    prev: Self = None

    def __lt__(self, other):
        return self.dist < other.dist


def dijkstra(grid, start):
    visited = set()
    queue = [Deer(pos=start, dir=RIGHT, dist=0)]
    while queue:
        current = heapq.heappop(queue)
        if grid[current.pos] == 'E':
            return current.dist, current.pos

        new_dir_1 = P2d(current.dir.y, -current.dir.x)
        new_dir_2 = P2d(-current.dir.y, current.dir.x)
        for vec in (current.dir, new_dir_1, new_dir_2):
            neigh_score = current.dist + 1 if vec == current.dir else current.dist + 1001
            neigh = Deer(current.pos + vec, vec, neigh_score)
            if grid.get(neigh.pos) in '.E' and (neigh.pos, neigh.dir) not in visited:
                visited.add((neigh.pos, neigh.dir))
                heapq.heappush(queue, neigh)

    raise ValueError('No path found')


def part_2(grid: dict[P2d, str], start: P2d, end: P2d, score: int) -> int:
    """
    From wikipedia:
    A more general problem is to find all the shortest paths between source and target. Then instead of storing only a
    single node in each entry of prev[] all nodes satisfying the relaxation condition can be stored. For example, if
    both r and source connect to target and they lie on different shortest paths through target (because the edge cost
    is the same in both cases), then both r and source are added to prev[target]. When the algorithm completes, prev[]
    data structure describes a graph that is a subset of the original graph with some edges removed. Its key property is
    that if the algorithm was run with some starting node, then every path from that node to any other node in the new
    graph is the shortest path between those nodes graph, and all paths of that length from the original graph are
    present in the new graph. Then to actually find all these shortest paths between two given nodes, a path finding
    algorithm on the new graph, such as depth-first search would work.
    """
    all_dists = dict()
    new_graph = defaultdict(set)
    queue = [Deer(pos=start, dir=RIGHT, dist=0)]
    while queue:
        current = heapq.heappop(queue)
        if current.dist > score:
            break

        if (current.pos, current.dir) in all_dists:
            if current.dist <= all_dists[(current.pos, current.dir)]:
                # only add those that keep the current path valid (if > then it's not the min dist to the node anymore)
                new_graph[(current.pos, current.dir)].add((current.prev.pos, current.prev.dir))
            continue

        all_dists[(current.pos, current.dir)] = current.dist
        with contextlib.suppress(AttributeError):  # trying to add start
            new_graph[(current.pos, current.dir)].add((current.prev.pos, current.prev.dir))

        new_dir_1 = P2d(current.dir.y, -current.dir.x)
        new_dir_2 = P2d(-current.dir.y, current.dir.x)
        for vec in (current.dir, new_dir_1, new_dir_2):
            neigh_dist = current.dist + 1 if vec == current.dir else current.dist + 1001
            neigh = Deer(pos=current.pos + vec, dir=vec, dist=neigh_dist, prev=current)
            if grid.get(neigh.pos) in '.E':
                heapq.heappush(queue, neigh)

    return get_all_paths(end, new_graph)  # dfs on new graph


def get_all_paths(start_pos: P2d, graph: dict[tuple[P2d, P2d], set]):
    visited_verts = set()
    visited_pos = set()
    queue = [(start_pos, vec) for vec in (UP, DOWN, LEFT, RIGHT)]
    while queue:
        current = queue.pop()
        visited_verts.add(current)
        visited_pos.add(current[0])
        for neighbor in graph[current]:
            if neighbor not in visited_verts:
                queue.append(neighbor)
    return len(visited_pos)


def read_input(lines):
    grid = dict()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            p = P2d(i, j)
            grid[p] = lines[i][j]
            if lines[i][j] == 'S':
                start = p
    return grid, start


ll = open("d16.txt", 'r').read().splitlines()
g, s = read_input(ll)
best_score, e = dijkstra(g, s)
print(best_score)
print(part_2(g, s, e,best_score))
