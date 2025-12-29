import numpy as np


def load_graph(filename: str = "graph.txt") -> "adjacency matrix":
    graph = []
    file_in = open(filename)
    for line in file_in:
        graph.append(list(map(int, line.strip().split(","))))
    return graph

def to_adjacency_list(graph: list[list[int]]) -> "adjacency list":
    n = len(graph)
    result = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                result[i].append(j)
    return result

def find_circuit_dfs(graph: list[list[int]], source: int = 0) -> list[int] | None:
    n = len(graph)
    circuit = [source]
    visited_v = [False] * n
    visited_e = [[False] * n for _ in range(n)]

    stack = [source]
    visited_v[source] = True

    while stack:
        u = stack[-1]
        be_popped = True

        for v in graph[u]:
            if v == source and not visited_e[u][v]:
                return circuit + [v]
            if not visited_v[v]:
                be_popped = False
                break

        if be_popped:
            stack.pop()
        else:
            print(v)
            stack.append(v)
            circuit.append(v)
            visited_v[v] = True
            visited_e[u][v] = visited_e[v][u] = True

    return None



if __name__ == "__main__":
    adjacency_matrix = load_graph()
    adjacency_list = to_adjacency_list(adjacency_matrix)
    print(adjacency_list)
    print(find_circuit_dfs(adjacency_list, 0))