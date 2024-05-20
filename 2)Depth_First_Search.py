
from collections import deque


def dfs_iterative(graph, start_node):

    queue = deque([start_node])
    visited = set()

    dfs_order = []
    while queue:

        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            dfs_order.append(node)

            # Add all unvisited neighbors to the queue in reverse order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    queue.appendleft(neighbor)

    return dfs_order


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting the DFS traversal from node 'A'
dfs_order = dfs_iterative(graph, 'A')
print("DFS order:", dfs_order)
