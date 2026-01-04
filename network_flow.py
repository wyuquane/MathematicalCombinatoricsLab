import numpy as np


def load_graph(filename: str = "directed_weighted_graph.txt") -> list[list[int]]:
    """
    :param filename:
    :return: adjacency matrix
    """
    graph = []
    file_in = open(filename)
    for line in file_in:
        graph.append(list(map(int, line.strip().split())))
    return graph

def compute_s_t_cut(graph: list[list[int]], s: list[int], t: list[int]) -> int:
    """
    :param graph: adjacency matrix
    :param s:
    :param t:
    :return: capacity of the cut
    """
    result = 0
    for u in s:
        for v in t:
            result += graph[u][v]

    return result

def print_all_cuts(graph: list[list[int]]) -> None:
    n = len(graph)
    in_s = [False] * n
    in_s[0]  = True

    def backtracking(index: int):
        if index == n - 1:
            s = []
            t = []
            for i in range(n):
                if in_s[i]:
                    s.append(i)
                else:
                    t.append(i)
            capacity = compute_s_t_cut(graph, s, t)
            print(s, t, capacity)
            return

        in_s[index] = 0
        backtracking(index + 1)
        in_s[index] = 1
        backtracking(index + 1)

    backtracking(1)


def construct_residual_graph(capacity: list[list[int]], flow: list[list[int]]) -> residual_graph:
    n = len(graph)
    residual_graph = [[0] * n for _ in range(n)]

    for u in range(n):
        for v in range(n):
            residual_graph[u][v] += capacity[u][v] - flow[u][v]
            residual_graph[v][u] += flow[u][v]

    return residual_graph



if __name__ == "__main__":
    adjacency_matrix = load_graph()
    print(np.array(adjacency_matrix))
    print_all_cuts(adjacency_matrix)
