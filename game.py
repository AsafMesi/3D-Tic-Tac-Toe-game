class Game:
    def __init__(self, board_size=4):
        self.board_size = board_size
        self.blank = "*"
        self.board = [[[self.blank for i in range(board_size)] for j in range(board_size)] for k in range(board_size)]
        self.moves_count = 0
        self.current_player = "X"
        self.winner = None
        self.invalid = None
        self.moves_set = set(range(4))
        self.winning_sequence = ""

    def check_horizontal_winner(self, x, z):
        # Check for a top to bottom win
        if all(self.board[x][i][z] == self.current_player for i in range(4)):
            self.winning_sequence = [(x, i, z) for i in range(4)]
            return True

    def check_vertical_winner(self, x, y):
        # Check for a left to right win
        if all(self.board[x][y][i] == self.current_player for i in range(4)):
            self.winning_sequence = [(x, y, i) for i in range(4)]
            return True

    def check_depth_winner(self, y, z):
        # Check for a win along the x-axis
        if all(self.board[i][y][z] == self.current_player for i in range(4)):
            self.winning_sequence = [(i, y, z) for i in range(4)]
            return True

    def check_slant_winner(self, x):
        # Check for a top left slant win.
        if all(self.board[x][i][i] == self.current_player for i in range(4)):
            self.winning_sequence = [(x, i, i) for i in range(4)]
            return True

        # Check for a top right slant win.
        if all(self.board[x][i][3-i] == self.current_player for i in range(4)):
            self.winning_sequence = [(x, i, (3-i)) for i in range(4)]
            return True

        return False

    def check_diagonal_winner(self):
        # Check for a diagonal win along the 0 0 0 -> 3 3 3 diagonal
        if all(self.board[i][i][i] == self.current_player for i in range(4)):
            self.winning_sequence = [(i, i, i) for i in range(4)]
            return True

        # Check for a diagonal win along the 0 0 3 -> 3 3 0 diagonal
        if all(self.board[i][i][3-i] == self.current_player for i in range(4)):
            self.winning_sequence = [(i, i, (3-i)) for i in range(4)]
            return True

        # Check for a diagonal win along the 0 3 0 -> 3 0 3 diagonal
        if all(self.board[i][3-i][i] == self.current_player for i in range(4)):
            self.winning_sequence = [(i, (3-i), i) for i in range(4)]
            return True

        # Check for a diagonal win along the 0 3 3 -> 3 0 0 diagonal
        if all(self.board[i][3-i][3-i] == self.current_player for i in range(4)):
            self.winning_sequence = [(i, (3-i), (3-i)) for i in range(4)]
            return True

        return False

    def check_winner(self, x, y, z):
        if self.check_horizontal_winner(x, z):
            return True
        if self.check_vertical_winner(x, y):
            return True
        if self.check_depth_winner(y, z):
            return True
        if self.check_slant_winner(x):
            return True
        if self.check_diagonal_winner():
            return True
        # If none of the wins are found, return False
        return False

    def is_valid_move(self, x, y, z):
        move = {x, y, z}
        return move.issubset(self.moves_set) and self.board[x][y][z] == self.blank

    def switch_current_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_move(self, x, y, z):
        if not self.is_valid_move(x, y, z):
            self.invalid = "Y"
            return

        self.board[x][y][z] = self.current_player
        self.moves_count += 1

        if self.check_winner(x, y, z):
            self.winner = self.current_player
            return

        self.switch_current_player()

    def is_game_over(self):
        if self.winner or self.invalid or self.moves_count == self.board_size**3:
            return True
        return False

    def print_board(self):
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    print(f"({x} {y} {z}) ", end='')
                for z in range(4):
                    print(f"{self.board[x][y][z]} ", end='')
                print()
            print()

    def state(self):
        if self.winner:
            return f"The winner is {self.winner}!"
        if self.invalid:
            return "Invalid move was entered!"
        if self.moves_count == self.board_size**3:
            return "It's a tie!"
        return "Game is not over yet."
