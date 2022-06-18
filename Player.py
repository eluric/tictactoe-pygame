from TicTacToe import TicTacToe

class AI():

    def minimax(
        self, ttt: TicTacToe,
        is_maximising: bool, depth: int
    ) -> int:

        if depth == 0:
            return 0

        available_moves = ttt.get_available_moves()

        # the AI player is always trying to maximise
        # for now, the AI is always x
        # check winner
        x_wins, o_wins = ttt.check_win()

        if x_wins and o_wins:
            return 0
        elif x_wins:
            if is_maximising:
                return 1
            else:
                return -1
        elif o_wins:
            if is_maximising:
                return -1
            else:
                return 1

        best_score = -float("inf") if is_maximising else float("inf")

        # if no winner, then call minimax again
        for move in available_moves:
            row, column = move
            ttt.make_move(row, column)
            
            score = self.minimax(ttt, not is_maximising, depth-1)

            ttt.undo()

            if is_maximising:
                if score > best_score:
                    best_score = score
            else:
                if score < best_score:
                    best_score = score

        return best_score

    def make_best_move(self, ttt: TicTacToe) -> tuple[int, int]:
        available_moves = ttt.get_available_moves()
        
        best_score = -float("inf")
        best_move = (-1, -1)

        for move in available_moves:
            row, column = move
            ttt.make_move(row, column)

            # check how good the move was
            score = self.minimax(ttt, True, 9)

            ttt.undo()

            # compare against current score
            if score > best_score:
                best_score = score
                best_move = (row, column)
        
        return best_move
