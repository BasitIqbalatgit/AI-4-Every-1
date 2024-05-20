from collections import deque


def depth_limited_dfs(graph, start_node, limit):
    stack = deque([(start_node, 0)])
    visited = set()
    dfs_order = []

    while stack:
        # Pop a node and its depth from the stack
        node, depth = stack.popleft()

        if node not in visited:
            # Mark the node as visited
            visited.add(node)
            dfs_order.append(node)

            # Only add neighbors if the current depth is less than the limit
            if depth < limit:
                # Add all unvisited neighbors to the stack with incremented depth
                for neighbor in reversed(graph[node]):
                    if neighbor not in visited:
                        stack.appendleft((neighbor, depth + 1))

    return dfs_order



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['N'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs_order = depth_limited_dfs(graph, 'A', 2)
print("Depth-Limited DFS order:", dfs_order)
