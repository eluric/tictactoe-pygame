class TicTacToe():
    def __init__(self, size: int, x_turn: bool):
        self.state = [
            " " for i in range(size * size)
        ]
        self.moves_made = []
        self.last_move = -9
        self.size = size
        self.available_moves = [i for i in range(size * size)]
        self.x_turn = x_turn
        self.game_finished = False

    def get_state(self) -> list[str]:
        return self.state

    def get_available_moves(self) -> list[int]:
        return self.available_moves

    def get_size(self) -> int:
        return self.size

    def is_x_turn(self) -> bool:
        return self.x_turn

    def is_game_finished(self) -> bool:
        return self.game_finished

    def is_empty(self, space: int) -> bool:
        if self.state[space] == " ":
            return True
        else:
            return False

    def make_move(self, space: int) -> None:
        if -9 == space:
            return
        if not self.is_empty(space):
            return

        if self.x_turn:
            self.state[space] = "X"
            self.available_moves.remove(space)
            self.x_turn = False
        else:
            self.state[space] = "O"
            self.available_moves.remove(space)
            self.x_turn = True

        self.moves_made.append(space)
        self.last_move = space

        return

    def undo(self) -> None:
        space = self.last_move
        self.state[space] = " "

        self.moves_made.pop()
        self.available_moves.insert(0, self.last_move)
        # self.available_moves = sorted(self.available_moves)
        self.last_move = self.moves_made[-1] if self.moves_made else -9

        self.x_turn = not self.x_turn

    # checks if either player has won
    # returns a tuple of two booleans
    # (x_wins, o_wins)
    # if return value is (True, False), then x has won
    def check_win(self) -> tuple[bool, bool]:
        if -9 == self.last_move:
            return False, False

        win_conditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],

            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],

            [0, 4, 8],
            [2, 4, 6]
        ]

        space = self.last_move

        won_game = False
        for win in win_conditions:
            if space in win:
                if self.state[win[0]] == self.state[win[1]] and self.state[win[0]] == self.state[win[2]]:
                    won_game = True

        if won_game:
            if self.state[space] == "O":
                return False, True
            else:
                return True, False
        
        if len(self.available_moves) == 0:
            return True, True
        
        return False, False
        

    # def check_win(self) -> tuple[bool, bool]:
    #     # only need to check the horizontal, vertical and diagonal of the last move
    #     # if no player has won until that point, then none of the previous moves were winning moves
    #     # therefore, if a player has won this round, then only the last move placed will result in a win
    #     if self.last_move == (-1, -1):
    #         return False, False

    #     space= self.last_move

    #     horizontal_win = True
    #     # first, check the row
    #     for i in range(self.size - 1):
    #         if self.state[row][i] != self.state[row][i+1]:
    #             horizontal_win = False
    #             break
        
    #     if horizontal_win:
    #         self.game_finished = True
    #         if self.state[row][0] == "O":
    #             return False, True
    #         else:
    #             return True, False
        
        
    #     vertical_win = True
    #     # check column
    #     for i in range(self.size - 1):
    #         if self.state[i][column] != self.state[i+1][column]:
    #             vertical_win = False
    #             break

    #     if vertical_win:
    #         self.game_finished = True
    #         if self.state[0][column] == "O":
    #             return False, True
    #         else:
    #             return True, False

    #     """
    #     If the row and column are the same, then we know that the last move placed was
    #     in range of the down diagonal and we need to check the down diagonal.
    #     e.g (0, 0), (1, 1), (2, 2)
    #     O| | 
    #     ------
    #      |O| 
    #     ------
    #      | |O

    #     If the row and column add up to to equal the total number of rows or total number of columns,
    #     then we know that the last move was in range of the up diagonal.
    #     e.g (3, 0), (2, 1), (0, 3). The total number of rows is 3.
    #      | |O
    #     ------
    #      |O| 
    #     ------
    #     O| |
    #     """
    #     down_diagonal_win = True
    #     if row == column:
    #         for i in range(self.size - 1):
    #             if self.state[i][i] != self.state[i+1][i+1]:
    #                 down_diagonal_win = False
    #                 break

    #         if down_diagonal_win:
    #             self.game_finished = True
    #             if self.state[0][0] == "O":
    #                 return False, True
    #             else:
    #                 return True, False

        
    #     up_diagonal_win = True
    #     if row + column == self.size - 1:
    #         for i in range(self.size - 1):
    #             if self.state[i][self.size-1 - i] != self.state[i+1][self.size-1 - i-1]:
    #                 up_diagonal_win = False
    #                 break
        
    #         if up_diagonal_win:
    #             self.game_finished = True
    #             if self.state[self.size-1][0] == "O":
    #                 return False, True
    #             else:
    #                 return True, False

    #     # if there are no more moves to play, it is a draw
    #     if not self.available_moves:
    #         return True, True

    #     return False, False
