import heapq
from path_problem import load_file, to_edges_list


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

    def nlr(self):
        print(self.val, end=" ")
        if self.left:
            self.left.nlr()
        if self.right:
            self.right.nlr()

    def lnr(self):
        if self.left:
            self.left.lnr()
        print(self.val, end=" ")
        if self.right:
            self.right.lnr()

    def lrn(self):
        if self.left:
            self.left.lrn()
        if self.right:
            self.right.lrn()
        print(self.val, end=" ")

def construct_bst_from_array(arr: list[int]) -> TreeNode | None:
    arr.sort()
    nodes = [TreeNode(val) for val in arr]
    for i in range(len(nodes) - 1):
        nodes[i].right = nodes[i + 1]

    return nodes[0]

def preorder_inorder(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    if len(preorder) == 0:
        return None
    if len(preorder) == 1:
        return TreeNode(preorder[0])
    if len(preorder) == 2:
        if preorder[0] == inorder[0]:
            root = TreeNode(preorder[0])
            leaf = TreeNode(preorder[1])
            root.right = leaf
            return root
        else:
            root = TreeNode(inorder[1])
            leaf = TreeNode(inorder[0])
            root.left = leaf
            return root

    root_val = preorder[0]
    root_index_in_inorder = inorder.index(root_val)
    left_child_inorder_length = root_index_in_inorder

    root = TreeNode(root_val)
    left_child = preorder_inorder(preorder[1: 1 + left_child_inorder_length], inorder[0: left_child_inorder_length])
    right_child = preorder_inorder(preorder[1 + left_child_inorder_length:], inorder[root_index_in_inorder + 1:])

    root.left = left_child
    root.right = right_child

    return root


def prims_algorithm(graph: list[list[int]]) -> (list[tuple[int]], int):
    """
    :param graph: adjacency list
    :return: edges in mst and total cost
    """
    n = len(graph)
    key = [float("inf")] * n
    in_mst = [False] * n
    pq = []
    parent = [-1] * n
    total_cost = 0

    src = 0
    key[src] = 0
    parent[src] = 0
    heapq.heappush(pq, (0, src))

    while pq:
        w, u = heapq.heappop(pq)

        if in_mst[u]:
            continue

        in_mst[u] = True
        total_cost += w

        for v, w in graph[u]:
            if not in_mst[v] and w < key[v]:
                key[v] = w
                parent[v] = u
                heapq.heappush(pq, (w, v))

    mst_edges = []
    for i in range(1, n):
        mst_edges.append((parent[i], i, key[i]))
    mst_edges.sort(key= lambda x: x[2])

    return mst_edges, total_cost

def has_a_path(graph: list[list[int]], src: int, des: int) -> bool:
    n = len(graph)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)

    dfs(src)

    return visited[des]

def kruskal_algorithm(edges: list[tuple[int, int, int]], n: int) -> (list[tuple[int]], int):
    """
    find minimum spanning tree by kruskal algorithm
    :param edges: edges present the graph (u, v, weight)
    :param n: number of graph's vertices
    :return: edges in mst and total cost
    """
    graph = [[] for _ in range(n)]
    mst_edges = []
    total_cost = 0

    heapq.heapify(edges)
    while len(mst_edges) < n - 1:
        w, u, v  = heapq.heappop(edges)
        if has_a_path(graph, u, v):
            continue
        else:
            mst_edges.append((u, v, w))
            total_cost += w
            graph[u].append(v)
            graph[v].append(u)

    return mst_edges, total_cost

if __name__ == "__main__":
    adjacency_list = load_file()
    edges_list = to_edges_list(adjacency_list)
    n_vertices = len(adjacency_list)

    mst_prim, cost_prim = prims_algorithm(adjacency_list)
    mst_kruskal, cost_kruskal = kruskal_algorithm(edges_list, n_vertices)

    print(mst_prim, cost_prim)
    print(mst_kruskal, cost_kruskal)


