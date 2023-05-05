def DFS(graph, start_vertex, visited):
    # Mark the current vertex as visited
    visited[start_vertex] = True
    print(start_vertex, end=" ")

    # Recur for all the neighbors of the current vertex
    for neighbor in graph[start_vertex]:
        if not visited[neighbor]:
            DFS(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [6],
    5: [],
    6: []
}

# Initialize visited array
visited = [False] * len(graph)

# Call the DFS function with a starting vertex
DFS(graph, 0, visited)