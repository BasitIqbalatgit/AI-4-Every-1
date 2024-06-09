from collections import deque


def depth_limited_dfs(tree, start_node, limit):
    closed_list = list()
    open_List = deque([(start_node,0)])

    while open_List:
        current_node, depth = open_List.popleft()
        closed_list.append(current_node)

        if depth<limit:
            for neighbour in reversed(tree[current_node]):
                if neighbour not in closed_list:
                    open_List.append((neighbour,depth+1))
    return closed_list



def iddfs(tree, start_node, goal, max_depth):
    for limit in range(max_depth + 1):
        closed_lists = depth_limited_dfs(tree,start_node,limit)
        print(f"Depth: {limit}, DFS Order : {closed_lists}")
        if goal in closed_lists:
            return closed_lists
    return None



tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': []
}
starting_node = 'A'
goal = 'F'


result = iddfs(tree, starting_node, goal, 3)
if result:
    print("Goal found. DFS Order:", result)
else:
    print("Goal not found within the depth limit.")
