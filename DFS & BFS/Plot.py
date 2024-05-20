import matplotlib.pyplot as plt
import networkx as nx
from Graph import Graph
from Tree import BinaryTree, TreeNode

def visualize_graph(graph):
    G = nx.Graph()
    G.add_nodes_from(graph.adjacency_list.keys())

    for vertex, neighbors in graph.adjacency_list.items():
        for neighbor in neighbors:
            G.add_edge(vertex, neighbor)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  # Use spring layout for visualization
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_color='black', edge_color='gray', linewidths=1, arrows=False)
    plt.title("Graph Visualization")
    plt.show()

def visualize_binary_tree(root):
    G = nx.DiGraph()

    def add_nodes_edges(node):
        if node:
            G.add_node(node.value)
            if node.left:
                G.add_edge(node.value, node.left.value)
                add_nodes_edges(node.left)
            if node.right:
                G.add_edge(node.value, node.right.value)
                add_nodes_edges(node.right)

    add_nodes_edges(root)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  # Use spring layout for visualization
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightgreen', font_size=12, font_color='black', edge_color='gray', linewidths=1, arrows=True)
    plt.title("Binary Tree Visualization")
    plt.show()

# Example usage:
if __name__ == "__main__":
    # Create a graph instance and add vertices/edges
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')

    # Visualize the graph
    visualize_graph(graph)

    # Create a binary tree instance and insert nodes
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)

    # Visualize the binary tree
    visualize_binary_tree(tree.root)
