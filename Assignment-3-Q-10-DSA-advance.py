class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_odd_level_nodes(root):
    if not root:
        return

    stack = [(root, 1)]

    while stack:
        node, level = stack.pop()

        if level % 2 != 0:
            print(node.val)

        if node.right:
            stack.append((node.right, level + 1))

        if node.left:
            stack.append((node.left, level + 1))


# Example usage
# Create a tree
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#             \
#              7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

print("Nodes at odd levels:")
print_odd_level_nodes(root)
