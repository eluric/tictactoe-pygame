from TicTacToe import TicTacToe

class AI():

    def minimax(self, ttt: TicTacToe, is_maximising: bool) -> int:
        available_moves = ttt.get_available_moves()

        # the AI player is always trying to maximise
        # for now, the AI is always o
        # check winner
        x_wins, o_wins = ttt.check_win()

        if x_wins and o_wins:
            return 0
        elif x_wins:
            return -1
        elif o_wins:
            return 1

        best_scores = []

        # if no winner, then call minimax again
        # for move in available_moves:
        #     ttt.make_move(move)
            
        #     score = self.minimax(ttt, not is_maximising)

        #     ttt.undo()

        #     best_scores.append(score)

        num_squares = ttt.get_size() ** 2
        for i in range(num_squares):
            if " " == ttt.get_state()[i]:
                ttt.make_move(i)

                score = self.minimax(ttt, not is_maximising)

                ttt.undo()

                best_scores.append(score)

        return max(best_scores) if is_maximising else min(best_scores)

    def make_best_move(self, ttt: TicTacToe) -> tuple[int, int]:
        available_moves = ttt.get_available_moves()
        print(available_moves)
        
        best_score = -float("inf")
        best_move = -9

        # for move in available_moves:
        #     ttt.make_move(move)

        #     # check how good the move was
        #     score = self.minimax(ttt, False)
        #     print(score, move)

        #     ttt.undo()

        #     # compare against current score
        #     if score > best_score:
        #         best_score = score
        #         best_move = move

        num_squares = ttt.get_size() ** 2
        for i in range(num_squares):
            if " " == ttt.get_state()[i]:
                ttt.make_move(i)

                score = self.minimax(ttt, False)
                
                ttt.undo()

                if score > best_score:
                    best_score = score
                    best_move = i
        
        return best_move

# ttt = TicTacToe(3, False)
# ttt.state = [
#     ["X", "O", " "],
#     ["X", " ", " "],
#     [" ", " ", " "]
# ]
# ttt.available_moves.remove((0, 0))
# ttt.available_moves.remove((0, 1))
# ttt.available_moves.remove((1, 0))
# ttt.moves_made.append((0, 0))
# ttt.moves_made.append((0, 1))
# ttt.moves_made.append((1, 0))
# ttt.last_move = (1, 0)

# ai = AI()
# ai_move = ai.make_best_move(ttt)
# print(ai_move)