import math

def maximin_with_pruning(state, depth, alpha, beta):
    if depth == 0 or state.is_game_over():
        return state.evaluate(), None

    best_move = None

    if state.current_player == "MAX":
        value = -math.inf
        for move in state.get_possible_moves():
            state.make_move(move)
            result, _ = maximin_with_pruning(state, depth - 1, alpha, beta)
            state.undo_move(move)
            if result > value:
                value = result
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, best_move

    else:
        value = math.inf
        for move in state.get_possible_moves():
            state.make_move(move)
            result, _ = maximin_with_pruning(state, depth - 1, alpha, beta)
            state.undo_move(move)
            if result < value:
                value = result
                best_move = move
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value, best_move

class TrivialGame:
    def __init__(self):
        self.board = [0, 0, 0]
        self.current_player = "MAX"

    def is_game_over(self):
        return sum(self.board) == 3 or all(x == 1 for x in self.board)

    def evaluate(self):
        if sum(self.board) == 3:
            return 1
        elif all(x == 1 for x in self.board):
            return -1
        else:
            return 0

    def get_possible_moves(self):
        return [i for i, v in enumerate(self.board) if v == 0]

    def make_move(self, move):
        self.board[move] = 1
        self.current_player = "MIN" if self.current_player == "MAX" else "MAX"

    def undo_move(self, move):
        self.board[move] = 0
        self.current_player = "MIN" if self.current_player == "MAX" else "MAX"

def main():
    game = TrivialGame()
    while not game.is_game_over():
        if game.current_player == "MAX":
            value, move = maximin_with_pruning(game, depth=3, alpha=-math.inf, beta=math.inf)
            game.make_move(move)
            print(f"MAX moves: {move}")
        else:
            move = int(input("Enter your move (0-2): "))
            game.make_move(move)
        print(f"Current board: {game.board}")
        print()

    print("Game over!")
    if game.evaluate() == 1:
        print("MAX wins!")
    elif game.evaluate() == -1:
        print("MIN wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
