from collections import deque


def bfs(graph, start_node):
    """
  Performs Breadth-First Search on a graph.

  Args:
      graph: Adjacency list representation of the graph.
      start_node: The starting node for the BFS traversal.

  Returns:
      A list containing the nodes visited in BFS order.
  """
    visited = set()  # Keeps track of visited nodes
    queue = deque([start_node])  # Queue for BFS traversal

    while queue:
        current_node = queue.popleft()
        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return visited


# Example usage
graph = {
    0: [1, 2],
    1: [3, 4, 6],
    2: [5],
    3: [],
    4: [],
    5: [],
    6: [],

}

starting_node = 1

bfs_order = bfs(graph, starting_node)

print(f"BFS traversal starting from node {starting_node}: {bfs_order}")
