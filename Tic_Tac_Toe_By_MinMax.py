import math

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_draw()

    def get_empty_cells(self):
        return [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == ' ']

    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def undo_move(self, row, col):
        self.board[row][col] = ' '

class MinimaxAI:
    def __init__(self):
        self.computer = 'O'
        self.player = 'X'

    def get_opponent(self, player):
        return 'O' if player == 'X' else 'X'

    def minimax(self, state, depth, alpha, beta, maximizing_player):
        if state.is_winner(self.computer):
            return 10 - depth
        elif state.is_winner(self.player):
            return depth - 10
        elif state.is_draw():
            return 0

        if maximizing_player:
            max_eval = -math.inf
            for row, col in state.get_empty_cells():
                state.make_move(row, col, self.computer)
                eval = self.minimax(state, depth + 1, alpha, beta, False)
                state.undo_move(row, col)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for row, col in state.get_empty_cells():
                state.make_move(row, col, self.player)
                eval = self.minimax(state, depth + 1, alpha, beta, True)
                state.undo_move(row, col)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_best_move(self, state):
        best_eval = -math.inf
        best_move = None
        alpha = -math.inf
        beta = math.inf
        for row, col in state.get_empty_cells():
            state.make_move(row, col, self.computer)
            eval = self.minimax(state, 0, alpha, beta, False)
            state.undo_move(row, col)
            if eval > best_eval:
                best_eval = eval
                best_move = (row, col)
        return best_move

def main():
    game = TicTacToe()
    ai = MinimaxAI()

    while not game.is_game_over():
        game.print_board()
        print("Player's turn (X):")
        row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
        while not game.make_move(row, col, 'X'):
            print("Invalid move! Try again.")
            row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
        if game.is_game_over():
            break

        best_row, best_col = ai.get_best_move(game)
        game.make_move(best_row, best_col, 'O')

    game.print_board()
    if game.is_winner('X'):
        print("Player wins!")
    elif game.is_winner('O'):
        print("Computer wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
