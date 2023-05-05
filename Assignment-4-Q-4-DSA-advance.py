def has_cycle(graph):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    recursion_stack = [False] * num_nodes

    def dfs(node):
        visited[node] = True
        recursion_stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif recursion_stack[neighbor]:
                return True

        recursion_stack[node] = False
        return False

    for node in range(num_nodes):
        if not visited[node]:
            if dfs(node):
                return True

    return False

