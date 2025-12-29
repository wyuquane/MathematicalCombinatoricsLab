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

    stack = [source]
    visited_v[source] = True

    while stack:
        u = stack[-1]
        be_popped = True

        for v in graph[u]:
            print(v, u, graph[u])
            if v == source and len(circuit) > 2:
                return circuit + [v]
            if not visited_v[v]:
                be_popped = False
                break

        if be_popped:
            stack.pop()
        else:
            stack.append(v)
            circuit.append(v)
            visited_v[v] = True

    return None

def is_valid_circuit(graph: list[list[int]], circuit):
    if circuit[0] != circuit[-1]:
        return False
    n = len(graph)
    visited_e = [[False] * n for _ in range(n)]
    for i in range(len(circuit) - 1):
        if circuit[i + 1] not in graph[circuit[i]]:
            print("khong co canh")
            return False
        if visited_e[circuit[i]][circuit[i + 1]]:
            print("lap canh")
            return False
        visited_e[circuit[i]][circuit[i + 1]] = visited_e[circuit[i]][circuit[i + 1]] = True
    return True


if __name__ == "__main__":
    adjacency_matrix = load_graph()
    adjacency_list = to_adjacency_list(adjacency_matrix)
    for i in range(len(adjacency_list)):
        print(i, adjacency_list[i])
    print("-------------")
    circuit = find_circuit_dfs(adjacency_list, 6)
    print(circuit)