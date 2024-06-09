class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def add_child(self, child_node):
        self.children.append(child_node)


# 1) Build Leaf Tree
leaf_values = [
    [5, 6],
    [7, 4, 5],
    [3],
    [6],
    [6, 9],
    [7],
    [5],
    [9, 8],
    [6]
]


# 2) Build a Tree Structure:
def build_tree(leaf_nodes):
    # Build the tree structure
    node3 = Node([5, 6])
    node3.add_child(leaf_nodes[0])
    node3.add_child(leaf_nodes[1])

    node4 = Node([7, 4, 5])
    node4.add_child(leaf_nodes[2])
    node4.add_child(leaf_nodes[3])

    node5 = Node([3])
    node5.add_child(leaf_nodes[4])
    node5.add_child(leaf_nodes[5])

    node6 = Node([6])
    node6.add_child(leaf_nodes[6])
    node6.add_child(leaf_nodes[7])

    node2 = Node([6, 9])
    node2.add_child(node3)
    node2.add_child(node4)

    node1 = Node([5])
    node1.add_child(node2)
    node1.add_child(node5)
    node1.add_child(node6)

    return node1


# 3) Draw the tree:
def draw_tree(root, level=0):
    if root:
        print(" " * (level * 4) + '+-' + str(root.value))
        for child in root.children:
            draw_tree(child, level + 1)

# 4) minmax code;
def min_max(node, depth, mxPlayer):
    if depth == 0 or not node.children:
        return max(node.value) if mxPlayer else min(node.value)
    if mxPlayer:
        value = float('-inf')
        for child in node.children:
            value = max(value, min_max(child, depth - 1, False))
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, min_max(child, depth - 1, True))
        return value

# Convert leaf_values to Node objects
leaf_nodes = [Node(value) for value in leaf_values]

# Build the tree
tr = build_tree(leaf_nodes)

# Draw the tree
draw_tree(tr)

# Find the optimal value using min-max algorithm
optimal_val = min_max(tr, 2, True)
print("Optimal Value : ", optimal_val)
