from collections import deque
import copy

class BoardState:
    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.goal_state = self.get_goal_state()

    def get_goal_state(self):
        goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return goal_board

    def is_goal_state(self):
        return self.board == self.goal_state

    def move_up(self, row, col):
        if row > 0:
            self.board[row][col], self.board[row - 1][col] = self.board[row - 1][col], self.board[row][col]
            return True
        return False

    def move_down(self, row, col):
        if row < self.size - 1:
            self.board[row][col], self.board[row + 1][col] = self.board[row + 1][col], self.board[row][col]
            return True
        return False

    def move_left(self, row, col):
        if col > 0:
            self.board[row][col], self.board[row][col - 1] = self.board[row][col - 1], self.board[row][col]
            return True
        return False

    def move_right(self, row, col):
        if col < self.size - 1:
            self.board[row][col], self.board[row][col + 1] = self.board[row][col + 1], self.board[row][col]
            return True
        return False

    def generate_next_states(self):
        next_states = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    if self.move_up(i, j):
                        next_states.append(copy.deepcopy(self.board))
                        self.move_down(i - 1, j)
                    if self.move_down(i, j):
                        next_states.append(copy.deepcopy(self.board))
                        self.move_up(i + 1, j)
                    if self.move_left(i, j):
                        next_states.append(copy.deepcopy(self.board))
                        self.move_right(i, j - 1)
                    if self.move_right(i, j):
                        next_states.append(copy.deepcopy(self.board))
                        self.move_left(i, j + 1)
                    return next_states

def solve_puzzle(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        if tuple(map(tuple, state.board)) in visited:
            continue

        visited.add(tuple(map(tuple, state.board)))
        if state.is_goal_state():
            return path

        for next_state in state.generate_next_states():
            queue.append((BoardState(next_state), path + [next_state]))

def print_board(board):
    for row in board:
        print(row)
    print()

initial_board = [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
initial_state = BoardState(initial_board)

solution = solve_puzzle(initial_state)
if solution:
    print("Rozwiązanie znalezione:")
    for step in solution:
        print_board(step)
else:
    print("Nie znaleziono rozwiązania.")
