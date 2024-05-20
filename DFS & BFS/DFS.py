from Tree import TreeNode


def dfs(start, structure, visit_func):
    visited = set()

    def _dfs_recursive(node):
        visited.add(node)
        visit_func(node)

        if hasattr(structure, 'get_neighbors'):
            neighbors = structure.get_neighbors(node)
        elif isinstance(node, TreeNode):
            neighbors = [node.left, node.right]
        else:
            raise ValueError("Unsupported start node type")

        for neighbor in neighbors:
            if neighbor and neighbor not in visited:
                _dfs_recursive(neighbor)

    if isinstance(start, str):
        start_node = start
    elif isinstance(start, TreeNode):
        start_node = start
    else:
        raise ValueError("Unsupported start type")

    _dfs_recursive(start_node)
