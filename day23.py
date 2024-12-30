
from collections import defaultdict

def build_graph():
    ll = open("d23.txt", 'r').read().splitlines()
    graph = defaultdict(set)
    for l in ll:
        source, dest = l.split('-')
        graph[source].add(dest)
        graph[dest].add(source)
    return graph


def find_3_cliques(graph):
    all_cliques = set()
    for v1 in graph:
        edges = graph[v1]
        for v2 in edges:
            for v3 in edges - {v2}:
                if v1 in graph[v3] and v2 in graph[v3]:
                    sorted_clique = sorted((v1, v2, v3))
                    all_cliques.add(tuple(sorted_clique))
    return all_cliques


def find_k_cliques(k_set: tuple[str, ...], graph):

    k_cliques = set()
    for clique in k_set:
        intersection = graph[clique[0]]
        for node in clique[1:]:
            intersection &= graph[node]
        new_nodes = intersection - set(clique)
        for node in new_nodes:
            new_clique = sorted(clique + (node,))
            k_cliques.add(tuple(new_clique))
    return k_cliques


def solve():
    graph = build_graph()
    cliques_3 = find_3_cliques(graph)
    res = 0
    for cl in cliques_3:
        if any(s[0] == 't' for s in cl):
            res += 1
    print(res)

    c_k = cliques_3
    while c_k:
        c_k_plus_one = find_k_cliques(c_k, graph)
        for c in c_k_plus_one:
            print(','.join(c))
        c_k = c_k_plus_one


if __name__ == '__main__':
    solve()
