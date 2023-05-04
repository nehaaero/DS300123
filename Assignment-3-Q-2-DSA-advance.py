class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def tree_height(root):
    if root is None:
        return 0
    else:
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)
        return max(left_height, right_height) + 1