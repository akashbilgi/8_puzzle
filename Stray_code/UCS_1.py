from queue import PriorityQueue

def make_node(state, parent=None, action=None, depth=0, cost=0):
    return {
        'STATE': state,
        'PARENT': parent,
        'ACTION': action,
        'DEPTH': depth,
        'COST': cost
    }

def expand(node, operators):
    expanded_nodes = []
    for operator in operators:
        new_state = apply_operator(node['STATE'], operator)
        if new_state:
            child_node = make_node(new_state, parent=node, action=operator, depth=node['DEPTH'] + 1, cost=node['COST'] + 1)
            expanded_nodes.append(child_node)
    return expanded_nodes

def apply_operator(state, operator):
    # Implement the logic to apply an operator on the state
    # and return the new state if valid, otherwise return None
    if state is None:
        return None
    
    new_state = list(state)
    empty_tile_index = new_state.index(0)
    
    if operator == 'UP':
        if empty_tile_index >= 3:
            new_state[empty_tile_index], new_state[empty_tile_index - 3] = new_state[empty_tile_index - 3], new_state[empty_tile_index]
            return tuple(new_state)
    elif operator == 'DOWN':
        if empty_tile_index < 6:
            new_state[empty_tile_index], new_state[empty_tile_index + 3] = new_state[empty_tile_index + 3], new_state[empty_tile_index]
            return tuple(new_state)
    elif operator == 'LEFT':
        if empty_tile_index % 3 != 0:
            new_state[empty_tile_index], new_state[empty_tile_index - 1] = new_state[empty_tile_index - 1], new_state[empty_tile_index]
            return tuple(new_state)
    elif operator == 'RIGHT':
        if empty_tile_index % 3 != 2:
            new_state[empty_tile_index], new_state[empty_tile_index + 1] = new_state[empty_tile_index + 1], new_state[empty_tile_index]
            return tuple(new_state)
    
    return None


def goal_test(state):
    return state == (1, 2, 3, 4, 5, 6, 7, 8, 0)

def general_search(problem, queueing_function):
    nodes = PriorityQueue()
    initial_node = make_node(problem['INITIAL_STATE'])
    nodes.put((initial_node['COST'], id(initial_node), initial_node))
    visited = set()

    while not nodes.empty():
        _, _, node = nodes.get()

        if goal_test(node['STATE']):
            return node

        visited.add(node['STATE'])

        for child_node in expand(node, problem['OPERATORS']):
            if child_node['STATE'] not in visited:
                cost = child_node['COST']
                nodes.put((cost, id(child_node), child_node))

    return "failure"

# Define the problem
problem = {
    'INITIAL_STATE': (1, 2, 3, 4, 5, 6, 0, 7, 8),
    'OPERATORS': ['UP', 'DOWN', 'LEFT', 'RIGHT'],  # Define the available operators for moving the tiles
}

# Function to print the state
def print_state(state):
    if state is None:
        print("Invalid state")
        return

    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# Solve the problem using Uniform Cost Search (UCS)
# Solve the problem using Uniform Cost Search (UCS)
solution = general_search(problem, queueing_function=PriorityQueue)

# Print the solution
if solution == "failure":
    print("Failed to find a solution.")
else:
    path = []
    while solution:
        if solution['ACTION'] is not None:
            path.insert(0, solution['ACTION'])
        solution = solution['PARENT']

    print("Solution path:", path)

    # Display the final state
    print("Final state:")
    print_state(problem['INITIAL_STATE'])

    # Apply actions to the initial state to reach the goal state
    current_state = problem['INITIAL_STATE']
    for action in path:
        current_state = apply_operator(current_state, action)
        if current_state is None:
            print(f"Action: {action}")
            print("Invalid state")
        else:
            print(f"Action: {action}")
            print_state(current_state)


