from collections import deque


def bfs(tree, start_node, goal_node):
    if tree is None:
        return -1

    close_List = list()
    open_List = deque([start_node])


    while open_List:
        current_node = open_List.popleft()
        close_List.append(current_node)

        if goal_node in close_List:
            return close_List

        for neighbour in tree[current_node]:
            if neighbour not in close_List:
                open_List.append(neighbour)

    return -1


tree={
    1:[2,3],
    2:[4,6,5],
    3:[7],
    4:[],
    5:[],
    6:[],
    7:[]
}


starting_node = 1
goal_node = 7

bfs_result = bfs(tree, starting_node, goal_node)

if bfs_result != -1:
    print("Path Detected By BFS is : ", bfs_result)
else:
    print("Goal Node not in The Tree")