import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappush, heappop

# Graph with 10 nodes
graph = {
    'A': {'B': 2, 'C': 4, 'D': 7},
    'B': {'E': 5, 'F': 6},
    'C': {'F': 1, 'G': 3},
    'D': {'G': 2, 'H': 5},
    'E': {'I': 2},
    'F': {'I': 4, 'J': 8},
    'G': {'J': 4},
    'H': {'J': 3},
    'I': {},
    'J': {}
}

# Heuristic values for each node
heuristics = {
    'A': 10,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 4,
    'F': 6,
    'G': 4,
    'H': 3,
    'I': 2,
    'J': 0
}


def visualize_graph(graph, heuristics):
    G = nx.DiGraph()

    for node, edges in graph.items():
        for adjacent, cost in edges.items():
            G.add_edge(node, adjacent, weight=cost)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    node_labels = {node: f"{node}\n(h={h})" for node, h in heuristics.items()}

    nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=2000, node_color='skyblue')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Graph Visualization with Heuristic Values and Edge Costs")
    plt.show()


visualize_graph(graph, heuristics)


class Node:
    def __init__(self, value, parent=None, g_score=0, h_score=0):
        self.value = value
        self.parent = parent
        self.g_score = g_score
        self.h_score = h_score
        self.f_score = g_score + h_score

    def __lt__(self, other):
        return self.f_score < other.f_score


def a_star(graph, heuristics, start, goal):
    open_list = []
    closed_list = set()

    start_node = Node(value=start, g_score=0, h_score=heuristics[start])
    heappush(open_list, start_node)

    while open_list:
        current_node = heappop(open_list)
        closed_list.add(current_node.value)

        if current_node.value == goal:
            path = []
            while current_node:
                path.append(current_node.value)
                current_node = current_node.parent
            return path[::-1]

        for neighbor, cost in graph[current_node.value].items():
            if neighbor in closed_list:
                continue

            g_score = current_node.g_score + cost
            h_score = heuristics[neighbor]
            neighbor_node = Node(value=neighbor, parent=current_node, g_score=g_score, h_score=h_score)

            if neighbor_node not in open_list:
                heappush(open_list, neighbor_node)

    return None


# Define start and goal nodes
start_node = 'A'
goal_node = 'J'

# Perform A* search
path = a_star(graph, heuristics, start_node, goal_node)

if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
