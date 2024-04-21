from Graph import Graph
from Tree import BinaryTree, TreeNode
from DFS import dfs



# Example usage in main script (DFS.py)
if __name__ == "__main__":
    # Example usage with Graph
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'E')
    graph.add_edge('D', 'E')

    print("DFS traversal of Graph:")
    dfs('A', graph, lambda vertex: print(vertex, end=' '))
    print()  # New line

    # Example usage with Tree
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)

    print("DFS traversal of Tree:")
    dfs(tree.root, tree, lambda node: print(node.value, end=' '))
