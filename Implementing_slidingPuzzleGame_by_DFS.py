from collections import deque


class Puzzle:
    def __init__(self, board):
        self.board = board
        self.n = len(board)
        self.goal = self.generate_goal()

    def generate_goal(self):
        goal = [[0] * self.n for _ in range(self.n)]
        num = 1
        for i in range(self.n):
            for j in range(self.n):
                goal[i][j] = num % (self.n * self.n)
                num += 1
        return goal

    def find_empty(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 0:
                    return i, j

    def is_goal(self):
        return self.board == self.goal

    def get_neighbors(self):
        neighbors = []
        x, y = self.find_empty()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbors.append(Puzzle(new_board))
        return neighbors

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])


def dfs(puzzle):
    stack = deque([puzzle])
    visited = set()

    while stack:
        current = stack.pop()
        if current.is_goal():
            return current
        visited.add(current)

        for neighbor in current.get_neighbors():
            if neighbor not in visited:
                stack.append(neighbor)

    return None


# Example usage
initial_board = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

puzzle = Puzzle(initial_board)
solution = dfs(puzzle)

if solution:
    print("Solution found:")
    print(solution)
else:
    print("No solution found.")
