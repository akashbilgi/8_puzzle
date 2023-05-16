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
    max_queue_size = 1
    nodes_expanded = 0

    while not nodes.empty():
        _, _, node = nodes.get()

        if goal_test(node['STATE']):
            return node, max_queue_size, nodes_expanded

        visited.add(node['STATE'])
        nodes_expanded += 1

        for child_node in expand(node, problem['OPERATORS']):
            if child_node['STATE'] not in visited:
                cost = child_node['COST']
                nodes.put((cost, id(child_node), child_node))
                if nodes.qsize() > max_queue_size:
                    max_queue_size = nodes.qsize()

    return "failure", max_queue_size, nodes_expanded

# Define the problem
problem = {
    'INITIAL_STATE': None,
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


# Test cases
test_cases = [
    [1, 2, 3, 4, 5, 6, 7, 8, 0],
    [1, 2, 3, 4, 5, 6, 0, 7, 8],
    [1, 2, 3, 5, 0, 6, 4, 7, 8],
    [1, 3, 6, 5, 0, 2, 4, 7, 8],
    [1, 3, 6, 5, 0, 7, 4, 8, 2],
    [1, 6, 7, 5, 0, 3, 4, 8, 2],
    [7, 1, 2, 4, 8, 5, 6, 3, 0],
    [0, 7, 2, 4, 6, 1, 3, 5, 8]
]

for i, test_case in enumerate(test_cases):
    print(f"Test Case #{i+1}")
    problem['INITIAL_STATE'] = tuple(test_case)
    solution, max_queue_size, nodes_expanded = general_search(problem, queueing_function=PriorityQueue)

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

        # Print additional information
        print("Nodes Expanded:", nodes_expanded)
        print("Max Queue/Heap Size:", max_queue_size)
        print("Depth:", len(path))
        print()
