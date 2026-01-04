import numpy as np


def load_graph(filename: str = "directed_weighted_graph.txt") -> list[list[int]]:
    graph = []
    file_in = open(filename)
    for line in file_in:
        graph.append(list(map(int, line.strip().split())))
    return graph

def print_all_cut(graph: list[list[int]]) -> None:
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
            print(s, t)
            return

        in_s[index] = 0
        backtracking(index + 1)
        in_s[index] = 1
        backtracking(index + 1)

    backtracking(1)



if __name__ == "__main__":
    adjacency_matrix = load_graph()
    print(np.array(adjacency_matrix))
    print_all_cut(adjacency_matrix)
