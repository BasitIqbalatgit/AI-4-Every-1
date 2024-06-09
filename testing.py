class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"Node({self.value})"

def build_tree(leaf_values):
    # Create leaf nodes from the given values
    leaf_nodes = [Node(value) for value in leaf_values]

    # Create level 3 nodes
    node3 = Node('Node3')
    node3.add_child(leaf_nodes[0])
    node3.add_child(leaf_nodes[1])

    node4 = Node('Node4')
    node4.add_child(leaf_nodes[2])
    node4.add_child(leaf_nodes[3])

    node5 = Node('Node5')
    node5.add_child(leaf_nodes[4])
    node5.add_child(leaf_nodes[5])

    node6 = Node('Node6')
    node6.add_child(leaf_nodes[6])
    node6.add_child(leaf_nodes[7])

    # Create level 2 node
    node2 = Node('Node2')
    node2.add_child(node3)
    node2.add_child(node4)

    # Create root node
    node1 = Node('Node1')
    node1.add_child(node2)
    node1.add_child(node5)
    node1.add_child(node6)

    return node1

def print_tree(node, level=0):
    print("  " * level + str(node))
    for child in node.children:
        print_tree(child, level + 1)

# Example usage
leaf_values = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8']
root = build_tree(leaf_values)
print_tree(root)
