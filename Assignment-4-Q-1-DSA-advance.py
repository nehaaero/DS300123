from collections import deque

def bfs(graph, start_vertex):
    visited = set()  # To keep track of visited vertices
    queue = deque()  # Queue for BFS traversal
    queue.append(start_vertex)
    visited.add(start_vertex)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")  # Process the vertex

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS Traversal:")
bfs(graph, 'A')
