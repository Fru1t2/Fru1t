import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

inorder_index = {val: idx for idx, val in enumerate(inorder)}
post_idx = [n - 1]

class Tree:
    def __init__(self, node):
        self.left = None
        self.right = None
        self.node = node

def build(in_left, in_right):
    if in_left > in_right:
        return None

    node_val = postorder[post_idx[0]]
    post_idx[0] -= 1
    root = Tree(node_val)

    idx = inorder_index[node_val]

    root.right = build(idx + 1, in_right)
    root.left = build(in_left, idx - 1)

    return root

def preorder(node):
    if node:
        print(node.node, end=' ')
        preorder(node.left)
        preorder(node.right)

tree_root = build(0, n - 1)
preorder(tree_root)
