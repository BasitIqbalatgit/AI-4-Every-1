from collections import deque


def depth_limited_dfs(tree, start_node, limit, goal):
    if tree is None:
        return -1
    closed_List= list()
    open_List  = deque([(start_node, 0) ])

    while open_List:
        current_node, depth = open_List.popleft()
        closed_List.append(current_node)

        if goal in closed_List:
            return closed_List

        if depth< limit:
            for neighbour in reversed(tree[current_node]):
                if neighbour not in closed_List:
                    open_List.appendleft((neighbour,depth+1))

    return  -1




graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['N'],
    'D': [],
    'E': ['F'],
    'F': []
}
starting_node = 'A'
limit =2
goal = 'F'

dfs_order = depth_limited_dfs(graph, starting_node, limit, goal)
if dfs_order != -1:
    print("Depth-Limited DFS order:", dfs_order)
else:
    print("Goal Not Found ....!")
