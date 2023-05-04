class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_subtrees_with_sum(root, target_sum):
    def dfs(node):
        nonlocal count

        if not node:
            return 0

        # Calculate the sum of the current subtree
        subtree_sum = node.val + dfs(node.left) + dfs(node.right)

        if subtree_sum == target_sum:
            count += 1

        return subtree_sum

    count = 0
    dfs(root)
    return count
