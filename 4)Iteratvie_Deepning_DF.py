from collections import deque


def depth_limited_dfs(graph, start_node, limit):
    stack = deque([(start_node, 0)])
    visited = set()
    dfs_order = []

    while stack:
        node, depth = stack.popleft()

        if node not in visited:
            visited.add(node)
            dfs_order.append(node)


            if depth < limit:
                for neighbor in reversed(graph[node]):
                    if neighbor not in visited:
                        stack.appendleft((neighbor, depth + 1))

    return dfs_order, visited


def iddfs(graph, start_node, goal, max_depth):
    for depth in range(max_depth + 1):
        dfs_order, visited = depth_limited_dfs(graph, start_node, depth)
        print(f"Depth: {depth}, DFS Order: {dfs_order}")
        if goal in visited:
            return dfs_order

    return None



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': []
}

goal = 'A'


result = iddfs(graph, 'A', goal, 3)
if result:
    print("Goal found. DFS Order:", result)
else:
    print("Goal not found within the depth limit.")
