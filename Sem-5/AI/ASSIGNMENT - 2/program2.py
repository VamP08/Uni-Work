from collections import deque

def is_solvable(puzzle):
    flat_puzzle = [num for row in puzzle for num in row if num != 0]
    inversions = sum(
        1 for i in range(len(flat_puzzle)) for j in range(i + 1, len(flat_puzzle))
        if flat_puzzle[i] > flat_puzzle[j]
    )
    return inversions % 2 == 0

def get_neighbors(state):
    neighbors = []
    zero_pos = next((r, c) for r, row in enumerate(state) for c, val in enumerate(row) if val == 0)
    row, col = zero_pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
            new_state = [list(row) for row in state]
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            neighbors.append(new_state)
    return neighbors

def bfs(initial_state, goal_state):
    if not is_solvable(initial_state):
        return "The puzzle is not solvable."

    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        visited.add(tuple(tuple(row) for row in current_state))

        if current_state == goal_state:
            return path

        for neighbor in get_neighbors(current_state):
            neighbor_tuple = tuple(tuple(row) for row in neighbor)
            if neighbor_tuple not in visited:
                queue.append((neighbor, path + [neighbor_tuple]))
                visited.add(neighbor_tuple)
    
    return "No solution found."

def print_path(path):
    for state in path:
        for row in state:
            print(row)
        print()

initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution_path = bfs(initial_state, goal_state)

if isinstance(solution_path, str):
    print(solution_path)
else:
    print("Solution found!")
    print_path(solution_path)
