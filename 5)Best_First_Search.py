from collections import deque

class Node:
    def __init__(self, value, children=None, h_score=None):
        self.value = value
        self.children = children or []  # Default empty list of children
        self.parent = None  # Initially parent not set
        self.h_score = h_score  # Heuristic value provided during initialization

def best_first_search(tree, start_value, goal_value):
    if tree is None:
        return None

    # Initialize the open list as a deque
    open_list = deque([Node(value=start_value, children=tree[start_value]['children'], h_score=tree[start_value]['h_score'])])
    closed_list = set()

    while open_list:
        # Sort the open list by heuristic score before processing
        open_list = deque(sorted(open_list, key=lambda x: x.h_score))

        current_node = open_list.popleft()
        closed_list.add(current_node.value)

        if current_node.value == goal_value:
            path = []
            while current_node:
                path.append(current_node.value)
                current_node = current_node.parent
            return path[::-1]

        for child_value in current_node.children:
            if child_value in closed_list:
                continue

            child_node = Node(value=child_value, children=tree[child_value]['children'], h_score=tree[child_value]['h_score'])
            child_node.parent = current_node

            if child_node not in open_list:
                open_list.append(child_node)

    return None

# Tree with pre-defined heuristic values for each node
tree = {
    'S': {'value': 'S', 'children': ['A', 'B', 'C'], 'h_score': 5},
    'A': {'value': 'A', 'children': [], 'h_score': 1},
    'B': {'value': 'B', 'children': ['D', 'H'], 'h_score': 3},
    'C': {'value': 'C', 'children': [], 'h_score': 7},
    'D': {'value': 'D', 'children': [], 'h_score': 2},
    'H': {'value': 'H', 'children': ['F', 'G'], 'h_score': 4},
    'F': {'value': 'F', 'children': [], 'h_score': 0},
    'G': {'value': 'G', 'children': ['E'], 'h_score': 1},
    'E': {'value': 'E', 'children': [], 'h_score': 0},
}

start_value = 'S'
goal_value = 'E'

path = best_first_search(tree, start_value, goal_value)

if path:
    print("Path from", start_value, "to", goal_value, ":", path)
else:
    print("Goal not found in the tree")
