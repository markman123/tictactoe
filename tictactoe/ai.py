from .enums import BoardState
from .tictactoe import TicTacToe

class GameAI():
    scoring = {BoardState.O: 1, BoardState.X = -1}
    def __init__(self, ai_player=BoardState.O):
        self.ai = ai_player

    def get_move(self, board_state: TicTacToe):
        pass