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
            if v == source and len(circuit) > 2:
                return circuit + [v]
            if not visited_v[v]:
                be_popped = False
                break

        if be_popped:
            stack.pop()
            circuit.pop()
        else:
            stack.append(v)
            circuit.append(v)
            visited_v[v] = True

    return None


def hierholzer_by_gemini(adj):
    stack = [0]
    circuit = []

    while stack:
        u = stack[-1]

        if adj[u]:
            v = adj[u].pop()
            stack.append(v)
        else:
            circuit.append(stack.pop())

    return circuit[::-1]

def find_euler_circuit_hierholzer(graph: list[list[int]]) -> list[int]:
    """
    :param graph: adjacency list
    :return: array of vertices present euler circuit
    """
    n_vertices = len(graph)
    n_edges = 0
    for i in range(n_vertices):
        n_edges += len(graph[i])
    n_edges //= 2

    result = find_circuit_dfs(graph, 0)
    for i in range(len(result) - 1):
        graph[result[i]].remove(result[i + 1])
        graph[result[i + 1]].remove(result[i])

    for i, v in enumerate(result):
        if len(graph[v]) > 0:
            index = i
            break
    else:
        return result

    while len(result) < n_edges + 1:
        circuit = find_circuit_dfs(graph, result[index])
        for i in range(len(circuit) - 1):
            graph[circuit[i]].remove(circuit[i + 1])
            graph[circuit[i + 1]].remove(circuit[i])

        result = result[0: index] + circuit + result[index + 1:]
        for i, v in enumerate(result):
            if len(graph[v]) > 0:
                index = i
                break
        else:
            return result

    return result

def is_a_bridge(graph: list[list[int]], u: int, v: int) -> bool:
    """
    :param graph: adjacency matrix
    :param u: vertex incident on that edge
    :param v: vertex incident on that edge
    :return: is that edge a bridge?
    """
    graph[v].remove(u)
    graph[u].remove(v)
    n = len(graph)
    visited = [False] * n
    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
    dfs(u)
    graph[u].append(v)
    graph[v].append(u)
    return not visited[v]

def find_euler_circuit_fleury(graph: list[list[int]]) -> list[int]:
    """
    :param graph: adjacency matrix presents graph
    :return: array of vertices presents circuit
    """
    n_vertices = len(graph)
    n_edges = 0
    for i in range(n_vertices):
        n_edges += len(graph[i])
    n_edges //= 2

    lead_vertex = 0
    circuit = [0]
    while n_edges > 0:
        next_vertices = None

        for v in graph[lead_vertex]:
            if not is_a_bridge(graph, lead_vertex, v) or len(graph[lead_vertex]) == 1:
                next_vertices = v
                break

        circuit.append(next_vertices)

        graph[next_vertices].remove(lead_vertex)
        graph[lead_vertex].remove(next_vertices)
        n_edges -= 1

        lead_vertex = next_vertices

    return circuit


def bfs(graph: list[list[int]], start: int):
    n = len(graph)
    visited = [False] * n
    queue = [start]
    visited[start] = True

    while queue:
        u = queue.pop(0)
        print(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)


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
        visited_e[circuit[i]][circuit[i + 1]] = visited_e[circuit[i + 1]][circuit[i]] = True
    return True


if __name__ == "__main__":
    adjacency_matrix = load_graph()
    adjacency_list = to_adjacency_list(adjacency_matrix)
    adjacency_list_2 = to_adjacency_list(adjacency_matrix)
    adjacency_list_3 = to_adjacency_list(adjacency_matrix)
    adjacency_list_4 = to_adjacency_list(adjacency_matrix)
    for i in range(len(adjacency_list)):
        print(i, adjacency_list[i])
    print("--------------------------")
    euler_circuit_hierholzer = find_euler_circuit_hierholzer(adjacency_list_2)
    euler_circuit_fleury = find_euler_circuit_fleury(adjacency_list_3)
    euler_circuit_gemini = hierholzer_by_gemini(adjacency_list_4)
    for i in range(len(adjacency_list)):
        print(i, adjacency_list[i])
    print("--------------------------")
    print(euler_circuit_hierholzer, is_valid_circuit(adjacency_list, euler_circuit_hierholzer))
    print(euler_circuit_fleury, is_valid_circuit(adjacency_list, euler_circuit_fleury))
    print(euler_circuit_gemini, is_valid_circuit(adjacency_list, euler_circuit_gemini))