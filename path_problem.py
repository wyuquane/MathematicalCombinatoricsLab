def load_file(filename: str = "weighted_graph.txt") -> list[list[tuple[int, int]]]:
    """
    :param filename: text file contains a weighted graph
    :return: adjacency list presents graph
    """
    file_in = open(filename, "rt")
    graph = []
    for i, line in enumerate(file_in):
        line = line.strip()
        line = line[1: -1]
        pairs = list(line.split("), ("))
        neighbors = []
        for p in pairs:
            v, w = map(int, p.split(", "))
            neighbors.append((v, w))
        graph.append(neighbors)

    return graph

def to_adjacency_matrix(graph: list[list[tuple[int, int]]]) -> list[list[int]]:
    """
    :param graph: adjacency list
    :return: adjacency matrix
    """
    n = len(graph)
    result = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, w in graph[u]:
            result[u][v] = w

    return result

def to_edges_list(graph: list[list[tuple[int, int]]]) -> list[tuple[int, int, int]]:
    """
    :param graph: adjacency list
    :return: edges list
    """
    result = []
    n = len(graph)
    for u in range(n):
        for v, w in graph[u]:
            if u < v:
                result.append((u, v, w))
    return result

def dfs(graph: list[list[tuple[int, int]]], start: int) -> list[int]:
    """
    iterative depth first search
    :param graph: adjacency list
    :param start: node that dfs begin
    :return: vertices with dfs ordering
    """
    n = len(graph)
    visited = [False] * n
    stack = [start]
    list_node_dfs = [start]
    visited[start] = True

    while stack:
        u = stack[-1]
        for v in graph[u]:
            if not visited[v[0]]:
                visited[v[0]] = True
                stack.append(v[0])
                list_node_dfs.append(v[0])
                break
        else:
            stack.pop()

    return list_node_dfs


if __name__ == "__main__":
    adjacency_list = load_file()
    for node in adjacency_list:
        print(node)
    nodes = dfs(adjacency_list, 2)
    print(nodes)