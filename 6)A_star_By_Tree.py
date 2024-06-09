from collections import deque

class Node:
    def __init__(self, value, children=None, h_score=None, g_score=0):
        self.value = value
        self.children = children or []  # Default empty list of children
        self.parent = None  # Initially parent not set
        self.g_score = g_score  # Cost from start node to this node
        self.h_score = h_score  # Heuristic estimate of cost from this node to goal
        self.f_score = g_score + h_score  # Total score (g_score + h_score)

def a_star_algo(tree, start_value, goal_value):
    open_list = deque([])
    closed_list = set()

    # Initialize nodes from the dictionary
    node_map = {key: Node(value=key, children=tree[key]['children'], h_score=tree[key]['h_score']) for key in tree}
    start_node = node_map[start_value]
    open_list.append(start_node)

    while open_list:
        # Sort open_list by f_score before popping the node with the lowest f_score
        open_list = deque(sorted(open_list, key=lambda x: x.f_score))
        current_node = open_list.popleft()
        closed_list.add(current_node.value)

        if goal_value == current_node.value:
            path = []
            while current_node:
                path.append(current_node.value)
                current_node = current_node.parent
            return path[::-1]

        for child_value in current_node.children:
            child_node = node_map[child_value]

            if child_node.value in closed_list:
                continue

            tentative_g_score = current_node.g_score + tree[child_value]['g_score']
            if child_node not in open_list or tentative_g_score < child_node.g_score:
                child_node.parent = current_node
                child_node.g_score = tentative_g_score
                child_node.f_score = child_node.g_score + child_node.h_score

                if child_node not in open_list:
                    open_list.append(child_node)

    return None

# Tree with pre-defined heuristic values for each node
tree = {
    'S': {'value': 'S', 'children': ['A', 'B', 'C'], 'h_score': 5, 'g_score': 0},
    'A': {'value': 'A', 'children': [], 'h_score': 1, 'g_score': 7},
    'B': {'value': 'B', 'children': ['D', 'H'], 'h_score': 3, 'g_score': 2},
    'C': {'value': 'C', 'children': [], 'h_score': 7, 'g_score': 3},
    'D': {'value': 'D', 'children': [], 'h_score': 2, 'g_score': 4},
    'H': {'value': 'H', 'children': ['F', 'G'], 'h_score': 4, 'g_score': 1},
    'F': {'value': 'F', 'children': [], 'h_score': 0, 'g_score': 3},
    'G': {'value': 'G', 'children': ['E'], 'h_score': 1, 'g_score': 2},
    'E': {'value': 'E', 'children': [], 'h_score': 0, 'g_score': 2},
}

start_value = 'S'
goal_value = 'E'

path = a_star_algo(tree, start_value, goal_value)

if path:
    print("Path from", start_value, "to", goal_value, ":", path)
else:
    print("Goal not found in the tree")
