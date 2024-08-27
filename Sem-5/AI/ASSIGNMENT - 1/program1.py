from collections import deque

def bfs(graph, start):
    # Initialize a queue for BFS
    queue = deque([start])
    # Set to keep track of visited nodes
    visited = set([start])
    
    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        print(node, end=' ')
        
        # Get all adjacent nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
    
print("BFS traversal starting from node 'A':")
bfs(graph, 'A')
