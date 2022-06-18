class TicTacToe():
    def __init__(self, size: int, x_turn: bool):
        self.state = [
            [" " for i in range(size)] for j in range(size)
        ]
        self.last_move = (-1, -1)
        self.size = size
        self.available_moves = [(i, j) for i in range(size) for j in range(size)]
        self.x_turn = x_turn
        self.game_finished = False

    def get_state(self) -> list[list[str]]:
        return self.state

    def is_game_finished(self) -> bool:
        return self.game_finished

    def is_empty(self, row: int, column: int) -> bool:
        if self.state[row][column] == " ":
            return True
        else:
            return False

    def make_move(self, row: int, column: int) -> None:
        if not self.is_empty(row, column):
            return

        if self.x_turn:
            self.state[row][column] = "X"
            self.available_moves.remove((row, column))
            self.x_turn = False
        else:
            self.state[row][column] = "O"
            self.available_moves.remove((row, column))
            self.x_turn = True

        self.last_move = (row, column)

        return

    def check_win(self) -> tuple[bool, bool]:
        # only need to check the horizontal, vertical and diagonal of the last move
        # if no player has won until that point, then none of the previous moves were winning moves
        # therefore, if a player has won this round, then only the last move placed will result in a win
        if self.last_move == (-1, -1):
            return False, False

        row, column = self.last_move

        horizontal_win = True
        # first, check the row
        for i in range(self.size - 1):
            if self.state[row][i] != self.state[row][i+1]:
                horizontal_win = False
                break
        
        if horizontal_win:
            self.game_finished = True
            if self.state[row][0] == "O":
                return False, True
            else:
                return True, False
        
        
        vertical_win = True
        # check column
        for i in range(self.size - 1):
            if self.state[i][column] != self.state[i+1][column]:
                vertical_win = False
                break

        if vertical_win:
            self.game_finished = True
            if self.state[0][column] == "O":
                return False, True
            else:
                return True, False

        """
        If the row and column are the same, then we know that the last move placed was
        in range of the down diagonal and we need to check the down diagonal.
        e.g (0, 0), (1, 1), (2, 2)
        O| | 
        ------
         |O| 
        ------
         | |O

        If the row and column add up to to equal the total number of rows or total number of columns,
        then we know that the last move was in range of the up diagonal.
        e.g (3, 0), (2, 1), (0, 3). The total number of rows is 3.
         | |O
        ------
         |O| 
        ------
        O| |
        """
        down_diagonal_win = True
        if row == column:
            for i in range(self.size - 1):
                if self.state[i][i] != self.state[i+1][i+1]:
                    down_diagonal_win = False
                    break

            if down_diagonal_win:
                self.game_finished = True
                if self.state[0][0] == "O":
                    return False, True
                else:
                    return True, False

        
        up_diagonal_win = True
        if row + column == self.size:
            for i in range(self.size - 1):
                if self.state[i][self.size-i] != self.state[i+1][self.size-i-1]:
                    up_diagonal_win = False
                    break
        
            if up_diagonal_win:
                self.game_finished = True
                if self.state[self.size-1][0] == "O":
                    return False, True
                else:
                    return True, False

        return False, False
