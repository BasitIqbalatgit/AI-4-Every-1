from queue import PriorityQueue
import itertools

class Node:
    def __init__(self, city, path, cost):
        self.city = city
        self.path = path
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def calculate_cost(path, graph):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i+1]]
    cost += graph[path[-1]][path[0]]  # Return to the starting city
    return cost

def branch_and_bound_tsp(graph):
    start_city = next(iter(graph))
    pq = PriorityQueue()
    pq.put(Node(start_city, [start_city], 0))

    num_cities = len(graph)

    while not pq.empty():
        current_node = pq.get()

        if len(current_node.path) == num_cities:  # Visited all cities
            return current_node.path, current_node.cost

        for city in graph:
            if city not in current_node.path:
                new_path = current_node.path + [city]
                new_cost = calculate_cost(new_path, graph)
                pq.put(Node(city, new_path, new_cost))

    return None, float('inf')

# Example graph with distances between cities
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

shortest_path, shortest_cost = branch_and_bound_tsp(graph)

if shortest_path:
    print("Shortest Path:", shortest_path)
    print("Shortest Cost:", shortest_cost)
else:
    print("No feasible solution found.")
