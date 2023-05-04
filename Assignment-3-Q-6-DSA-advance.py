class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def sum_of_left_leaves(root):
    def helper(node, is_left):
        if not node:
            return 0

        if not node.left and not node.right and is_left:
            return node.val

        return helper(node.left, True) + helper(node.right, False)

    return helper(root, False)

# Create the binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Compute the sum of left leaves
sum_left_leaves = sum_of_left_leaves(root)
print(sum_left_leaves)  # Output: 24