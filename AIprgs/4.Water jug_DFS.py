CAP_A = 4 
CAP_B = 3 
GOAL = 2 

def print_state(state): 
    print("Jug A :", state[0], "Liters") # Fixed typo "Jua"
    print("Jug B :", state[1], "Liters") 
    print() 

def get_neighbors(state): 
    neighbors = [] 
    a, b = state 
    if a < CAP_A: 
        neighbors.append(((CAP_A, b), "Fill Jug A")) 
    if b < CAP_B: 
        neighbors.append(((a, CAP_B), "Fill Jug B")) 
    if a > 0: 
        neighbors.append(((0, b), "Empty jug A")) 
    if b > 0: 
        neighbors.append(((a, 0), "Empty jug B")) 
        
    # Pour A -> B
    amount = min(a, CAP_B - b) 
    if amount > 0: 
        neighbors.append( ((a - amount, b + amount), "Pour Jug A -> B") ) 
        
    # Pour B -> A (FIXED)
    amount = min(b, CAP_A - a) 
    if amount > 0: 
        neighbors.append( ((a + amount, b - amount), "Pour Jug B -> A") ) 
    return neighbors

#DFS Algorithm

def dfs(start): 
    stack = [(start, [])] 
    visited = set() 
    while stack: 
        state, path = stack.pop() 
        
        if state in visited: 
            continue 
        visited.add(state) 
        
        if state[0] == GOAL or state[1] == GOAL: 
            return path + [(state, "Goal Reached")] 
            
        for neighbor, action in reversed(get_neighbors(state)): 
            if neighbor not in visited: 
                # Track path as list of tuples (FIXED)
                stack.append((neighbor, path + [(neighbor, action)])) 
    return None 

start = (0, 0) 
solution = dfs(start) 
if solution: 
    print("Solution found in", len(solution) - 1, "moves:\n") 
    print("Initial State:") 
    print_state(start) 
    for state, action in solution: 
        print(action) 
        print_state(state) 
else: 
    print("No Solution found.")
