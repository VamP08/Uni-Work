
def dfs(graph, start):
    # Initialize a stack for DFS
    stack = [start]
    # Set to keep track of visited nodes
    visited = set([start])
    
    while stack:
        # Pop a node from the stack
        node = stack.pop()
        print(node, end=' ')
        
        # Get all adjacent nodes
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
    
print("DFS traversal starting from node 'A':")
dfs(graph, 'A')
