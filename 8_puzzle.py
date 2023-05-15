# def general_search(problem, QUEUEING_FUNCTION):
#     nodes = make_queue(make_node(problem['INITIAL_STATE']))
    
#     while True:
#         if empty(nodes):
#             return "failure"
        
#         node = remove_front(nodes)
        
#         if problem['GOAL_TEST'](node['STATE']):
#             return node
        
#         nodes = QUEUEING_FUNCTION(nodes, expand(node, problem['OPERATORS']))