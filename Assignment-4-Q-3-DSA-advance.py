from collections import deque

def count_nodes_at_level(root, target_level):
    if root is None:
        return 0
    
    queue = deque()
    queue.append((root, 0))  # (node, level)
    node_count = 0
    
    while queue:
        node, level = queue.popleft()
        
        if level == target_level:
            node_count += 1
        
        for child in node.children:  # Assuming the tree has a list of children for each node
            queue.append((child, level + 1))
    
    return node_count