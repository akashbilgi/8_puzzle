# def general_search(problem, QUEUEING_FUNCTION):
#     nodes = make_queue(make_node(problem['INITIAL_STATE']))
    
#     while True:
#         if empty(nodes):
#             return "failure"
        
#         node = remove_front(nodes)
        
#         if problem['GOAL_TEST'](node['STATE']):
#             return node
        
#         nodes = QUEUEING_FUNCTION(nodes, expand(node, problem['OPERATORS']))


import heapq

goal_state = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]

# Define the heuristic function
def uniform_cost_search(initial_state):
    # Initialize the open and closed sets
    open_set = []
    closed_set = set()
    heapq.heappush(open_set, (0, initial_state, []))
    max_heap_size = 1
    nodes_expanded = 0

    # Search for the goal state
    while open_set:
        cost, state, path = heapq.heappop(open_set)
        if state == goal_state:
            return path, len(path), max_heap_size, nodes_expanded
        closed_set.add(tuple(state))
        nodes_expanded += 1

        # Generate the successors of the current state
        successors = []
        blank_index = state.index(0)
        if blank_index > 2:
            new_state = state[:]
            new_state[blank_index], new_state[blank_index - 3] = new_state[blank_index - 3], new_state[blank_index]
            if tuple(new_state) not in closed_set:
                successors.append((cost + 1, new_state, path + ['Down']))
        if blank_index < 6:
            new_state = state[:]
            new_state[blank_index], new_state[blank_index + 3] = new_state[blank_index + 3], new_state[blank_index]
            if tuple(new_state) not in closed_set:
                successors.append((cost + 1, new_state, path + ['Up']))
        if blank_index % 3 > 0:
            new_state = state[:]
            new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
            if tuple(new_state) not in closed_set:
                successors.append((cost + 1, new_state, path + ['Right']))
        if blank_index % 3 < 2:
            new_state = state[:]
            new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
            if tuple(new_state) not in closed_set:
                successors.append((cost + 1, new_state, path + ['Left']))

        # Add the successors to the open set
        for successor in successors:
            heapq.heappush(open_set, successor)
        max_heap_size = max(max_heap_size, len(open_set))

    # If the goal state is not found, return None
    return None


test_cases = [
    #[1, 2, 3, 4, 5, 6, 7, 8, 0],
    #[1, 2, 3, 4, 5, 6, 0, 7, 8],
    [1, 2, 3, 5, 0, 6, 4, 7, 8],
    #[1, 3, 6, 5, 0, 2, 4, 7, 8],
    # [1, 3, 6, 5, 0, 7, 4, 8, 2],
    # [1, 6, 7, 5, 0, 3, 4, 8, 2],
    # [7, 1, 2, 4, 8, 5, 6, 3, 0],
    # [0, 7, 2, 4, 6, 1, 3, 5, 8]
]

for i, test_case in enumerate(test_cases):
    solution, depth, max_heap_size, nodes_expanded = uniform_cost_search(test_case)
    print(f"Test Case {i+1}:")
    print("Solution:", solution)
    print("Depth of solution:", depth)
    print("Maximum heap size:", max_heap_size)
    print("Nodes expanded:", nodes_expanded)
    print()

    # Print h(n), g(n), and next state of the puzzle for each step in the solution
    if solution is not None:
        current_state = test_case
        print("Step\t h(n)\t g(n)\t Next State")
        print("--------------------------------")
        for step, action in enumerate(solution):
            blank_index = current_state.index(0)
            if action == "Up":
                next_state = current_state[:]
                next_state[blank_index], next_state[blank_index - 3] = next_state[blank_index - 3], next_state[blank_index]
            elif action == "Down":
                next_state = current_state[:]
                next_state[blank_index], next_state[blank_index + 3] = next_state[blank_index + 3], next_state[blank_index]
            elif action == "Left":
                next_state = current_state[:]
                next_state[blank_index], next_state[blank_index - 1] = next_state[blank_index - 1], next_state[blank_index]
            elif action == "Right":
                next_state = current_state[:]
                next_state[blank_index], next_state[blank_index + 1] = next_state[blank_index + 1], next_state[blank_index]
            
            h_n = 0  # Update the heuristic function here
            g_n = step + 1

            # Print the formatted next state
            formatted_next_state = [next_state[j:j+3] for j in range(0, 9, 3)]
            for row in formatted_next_state:
                print('\t'.join(map(str, row)))
            
            print(f"\nStep: {step+1}\t h(n): {h_n}\t g(n): {g_n}\n")
            current_state = next_state

        print()
