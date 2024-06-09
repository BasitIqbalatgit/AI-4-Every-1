from collections import deque

def dfs(tree, start_node, goal_node):
    closed_List = list()
    open_List = deque([start_node])

    while open_List:
        current_node = open_List.popleft()
        closed_List.append(current_node)

        if goal_node in closed_List:
            return closed_List

        for neighbour in reversed(tree[current_node]):
            if neighbour not in closed_List:
                open_List.appendleft(neighbour)
    return -1



# Example tree represented as an adjacency list
tree = {
    1: [2, 3],
    2: [4, 6, 5],
    3: [7],
    4: [],
    5: [],
    6: [],
    7: []
}

starting_node = 1
goal_node = 7

dfs_result = dfs(tree, starting_node, goal_node)

if dfs_result != -1:
    print("Path Detected By DFSff is :", dfs_result)
else:
    print("Goal Node not in The Treef")
