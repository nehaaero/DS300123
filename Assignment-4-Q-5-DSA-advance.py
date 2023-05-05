from collections import deque

def count_nodes_at_level(root, target_level):
    if root is None:
        return 0

    queue = deque([(root, 0)])  # (node, level)
    count = 0

    while queue:
        node, level = queue.popleft()

        if level == target_level:
            count += 1

        for child in node.children:  # Assuming the tree is represented using nodes with 'children' attribute
            queue.append((child, level + 1))

    return count
