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

def bfs(graph: list[list[tuple[int, int]]], start: int) -> list[int]:
    """
    iterative breadth first search
    :param graph: adjacency list
    :param start: node that bfs begin
    :return: vertices with bfs ordering
    """
    n = len(graph)
    visited = [False] * n
    list_node_bfs = [start]
    queue = [start]
    visited[start] = True

    while queue:
        u = queue.pop(0)

        for v in graph[u]:
            if not visited[v[0]]:
                queue.append(v[0])
                visited[v[0]] = True
                list_node_bfs.append(v[0])

    return list_node_bfs

def count_components(graph: list[list[tuple[int, int]]]) -> int:
    n = len(graph)
    result = 0
    visited = [False] * n
    def local_dfs(u):
        visited[u] = True
        for v, w in graph[u]:
            if not visited[v]:
                local_dfs(v)
    for u in range(n):
        if not visited[u]:
            local_dfs(u)
            result += 1

    return result

def shortest_path_bfs(graph: list[list[tuple[int, int]]], start: int, end: int) -> list[int]:
    """
    :param graph: adjacency list
    :param start: source
    :param end: destination
    :return: the path with the fewest edges
    """
    n = len(graph)
    dist = [float("inf")] * n
    parent = [-1] * n
    queue = [start]

    dist[start] = 0

    while queue:
        u = queue.pop(0)

        for v, w in graph[u]:
            if dist[v] == float("inf"):
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)

    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])

    return path[::-1]




if __name__ == "__main__":
    adjacency_list = load_file()
    for node in adjacency_list:
        print(node)
    print("---------")
    dfs_ordering = dfs(adjacency_list, 0)
    bfs_ordering = bfs(adjacency_list, 0)
    print(dfs_ordering, bfs_ordering)
    print(count_components(adjacency_list))
    print(shortest_path_bfs(adjacency_list, 0, 9))