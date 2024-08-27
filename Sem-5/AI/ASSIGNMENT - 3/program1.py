import heapq
def a_star(graph, start, goal, H):
    open_set = []
    heapq.heappush(open_set, (H[start], start))
    came_from = {}
    G = {start: 0}
    F = {start: H[start]} 
    while open_set:
        _, current = heapq.heappop(open_set)        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]       
        for neighbor, cost in graph[current]:
            tentative_g_score = G[current] + cost
            if neighbor not in G or tentative_g_score < G[neighbor]:
                came_from[neighbor] = current
                G[neighbor] = tentative_g_score
                F[neighbor] = tentative_g_score + H[neighbor]
                heapq.heappush(open_set, (F[neighbor], neighbor))
    return None
# Example usage
# Define the graph as an adjacency list
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 1), ('E', 5)],
    'C': [('A', 3), ('F', 2)],
    'D': [('B', 1)],
    'E': [('B', 5), ('G', 2)],
    'F': [('C', 2), ('G', 3)],
    'G': [('E', 2), ('F', 3)]
}
# Define the heuristic values (H) for each node
H = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 3,
    'G': 0
}
start = 'A'
goal = 'G'
path = a_star(graph, start, goal, H)
print("Path from start to goal:")
print(path)
