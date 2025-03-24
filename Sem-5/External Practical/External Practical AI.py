from collections import deque

def bfs(jug1_capacity, jug2_capacity, target):
    queue = deque()
    visited = set()
    
    queue.append((0, 0))
    visited.add((0, 0))
    
    while queue:
        (jug1, jug2) = queue.popleft()
        print(jug1,jug2)
        
        if jug1 == target or jug2 == target:
            return True
        
        next_states = [
            (jug1_capacity, jug2),            # Fill Jug1
            (jug1, jug2_capacity),            # Fill Jug2
            (0, jug2),                        # Empty Jug1
            (jug1, 0),                        # Empty Jug2
            (min(jug1 + jug2, jug1_capacity), jug2 - (min(jug1 + jug2, jug1_capacity) - jug1)),  # Pour Jug2 into Jug1
            (jug1 - (min(jug1 + jug2, jug2_capacity) - jug2), min(jug1 + jug2, jug2_capacity))   # Pour Jug1 into Jug2
        ]
        
        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
    
    return False

jug1_capacity = int(input("Capacity of Jug1: ")) 
jug2_capacity = int(input("Capacity of Jug2: "))
target = int(input("Target Amount: "))
    
if bfs(jug1_capacity, jug2_capacity, target):
    print(f"It is possible to measure {target} liters using the jugs.")
else:
    print(f"It is not possible to measure {target} liters using the jugs.")