from .enums import BoardState

class TicTacToe:
    def __init__(self):
        self.board = [[BoardState.BLANK for _ in range(3)] for _ in range(3)]

    def __repr__(self):
        output = "   +-0--+-1--+-2--+\n"
        for idx, row in enumerate(self.board):
            
            cell0 = f" {idx}0 " if row[0] == BoardState.BLANK else f" {row[0]}  "
            cell1 = f" {idx}1 " if row[1] == BoardState.BLANK else f" {row[1]}  "
            cell2 = f" {idx}2 " if row[2] == BoardState.BLANK else f" {row[2]}  "
            row = f"{idx}: |{cell0}|{cell1}|{cell2}|"
            output += row + "\n"
        output += "   +----+----+----+"
        return output

    def get(self, x, y=None):
        if y == None:
            return self.board[x]

        return self.board[x][y]

    def set(self, x, y, to: BoardState):
        self.board[x][y] = to

    def print(self):
        print(str(self))

    def print_guide(self):
        print("""
   +--0-+--1-+--2-+
0: | 00 | 01 | 02 |
1: | 10 | 11 | 12 |
2: | 20 | 21 | 22 |
   +----+----+----+
""")
