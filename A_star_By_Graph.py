import heapq


def heuristic(a, b):
    # Manhattan distance as the heuristic (for grid-like graphs)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(graph, start, goal):
    # Priority queue to store nodes to explore, initialized with the start node
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Dictionaries to store the cost of reaching each node and the path
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_set:
        # Pop the node with the lowest f_score
        current = heapq.heappop(open_set)[1]

        # If the goal is reached, reconstruct and return the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse the path to start from the beginning

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost

            # If the new path to the neighbor is shorter
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # Return None if there is no path


# Example graph represented as an adjacency list with costs
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1, (0, 2): 1},
    (0, 2): {(0, 1): 1, (1, 2): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 1},
    (1, 1): {(1, 0): 1, (0, 1): 1, (1, 2): 1, (2, 1): 1},
    (1, 2): {(1, 1): 1, (0, 2): 1, (2, 2): 1},
    (2, 0): {(1, 0): 1, (2, 1): 1},
    (2, 1): {(2, 0): 1, (1, 1): 1, (2, 2): 1},
    (2, 2): {(2, 1): 1, (1, 2): 1},
}

start = (0, 0)  # Define start node
goal = (2, 0)  # Define goal node

# Find the shortest path using A* algorithm
path = a_star(graph, start, goal)
print("Shortest path:", path)
