from collections import deque


class Node:
    def __init__(self, value, children=None, h_score=None):
        self.value = value
        self.parent = None
        self.children = children or []
        self.h_score = h_score


def beam_first_search(tree, start_value, goal_value, beam_width):
    if tree is None:
        return None

    # Initialize the open list with the start node
    open_list = deque(
        [Node(value=start_value, children=tree[start_value]['children'], h_score=tree[start_value]['h_score'])])
    closed_list = set()

    while open_list:
        # Sort the open list by heuristic score before processing
        open_list = deque(sorted(open_list, key=lambda x: x.h_score))

        # Keep only the top beam_width nodes
        current_level_nodes = [open_list.popleft() for _ in range(min(beam_width, len(open_list)))]

        for current_node in current_level_nodes:
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

                child_node = Node(value=child_value, children=tree[child_value]['children'],
                                  h_score=tree[child_value]['h_score'])
                child_node.parent = current_node

                if not any(node.value == child_node.value for node in open_list):
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
beam_width = 2  # Define the beam width

path = beam_first_search(tree, start_value, goal_value, beam_width)

if path:
    print("Path from", start_value, "to", goal_value, ":", path)
else:
    print("Goal not found in the tree")
