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
    right_child_inorder_length = len(inorder) - left_child_inorder_length - 1

    root = TreeNode(root_val)
    left_child = preorder_inorder(preorder[1: 1 + left_child_inorder_length], inorder[0: left_child_inorder_length])
    right_child = preorder_inorder(preorder[1 + left_child_inorder_length:], inorder[root_index_in_inorder + 1:])

    root.left = left_child
    root.right = right_child

    return root