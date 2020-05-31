from .enums import BoardState
from .tictactoe import TicTacToe

from .enums import GameState, BoardState
from itertools import permutations
import random
class GameAI():
    
    def __init__(self, game_cls, ai_player=BoardState.O):
        self.game_cls = game_cls
        self.ai = ai_player

    def evaluate(self, board, player):
        result = self.game_cls.check_winner(board)
        if isinstance(result, BoardState):
            return 10 if player == self.ai else -10
        return 0

    def minimax(self, board, depth, player, previous_moves):
        score = self.evaluate(board, player)
        if abs(score) == 10:
            return score, previous_moves
        
        if self.game_cls.no_moves_left(board):
            return 0, previous_moves

        possible_moves = list(filter(lambda x: board.board[x] == BoardState.BLANK, list(range(len(board.board)))))
        if self.ai == player:
            best = -1000
            f = max
        elif self.ai == self.game_cls.other_player(player):
            best = 1000
            f = min
        
        branch = {}
        for move in possible_moves:
            board.board[move] = player
            this, result = self.minimax(board, depth+1, self.game_cls.other_player(player), branch)
            branch[move] = {"moves": result, "value": this}
            best = f(best, this)
            board.board[move] = BoardState.BLANK
        
        return best, branch

    def get_best_move(self, board):
        possible_moves = [i for i in range(len(board.board)) \
             if board.board[i] == BoardState.BLANK]

        best_val = -1000
        best_idx = -1
        output = {}
        for move in possible_moves:
            board.board[move] = self.ai
            move_val, moves = self.minimax(board, 0, self.game_cls.other_player(self.ai), [move])
            output[move] = {"moves": moves, "value": move_val}
            board.board[move] = BoardState.BLANK
            if move_val > best_val:
                best_idx = move
                best_val = move_val
        return best_idx

    def build_(self, board_state: TicTacToe, depth=3):
        possible_moves = list(filter(lambda x: board_state.board[x] == BoardState.BLANK, list(range(len(board_state.board)))))
        new_board = board_state
        moveset = permutations(possible_moves)
        output = {i:[] for i in range(9)}
        whos_turn = self.ai
        for perm in moveset:
            for idx, move in enumerate(perm):
                if idx > depth:
                    break
                new_board.board[move] = whos_turn
                status = self.game_cls.check_winner(new_board)
                if status == GameState.GAME_OVER:
                    break    
                elif isinstance(status, BoardState):
                    output[perm[0]].append({"moveset": list(perm)[0:idx+1],
                                    "value": 1 if whos_turn == self.ai else -1 ,
                                    })
                whos_turn = self.game_cls.other_player(whos_turn)
        scores = []
        for move in possible_moves:
            score = sum([i["value"] for i in output[move].values()])
            scores.append(score)
        
        best = max(scores)
        return possible_moves[scores.index(best)]

                
        
            


