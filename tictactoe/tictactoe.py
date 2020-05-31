from .enums import BoardState

class TicTacToe:
    def __init__(self):
        self.board = [BoardState.BLANK for _ in range(9)]

    def __repr__(self):
        output = "   +--0--+--1--+--2--+\n"
        for idx in range(3):
            idx *= 3
            row = self.board[idx:idx+3]
            cell0 = f" {idx//3}0  " if row[0] == BoardState.BLANK else f"  {row[0]}  "
            cell1 = f" {idx//3}1  " if row[1] == BoardState.BLANK else f"  {row[1]}  "
            cell2 = f" {idx//3}2  " if row[2] == BoardState.BLANK else f"  {row[2]}  "
            row = f"{idx//3}: |{cell0}|{cell1}|{cell2}|"
            output += row + "\n"
        output += "   +-----+-----+-----+"
        return output

    def get(self, x, y=None):
        x *= 3
        if y == None:
            #0, 3, 6
            return self.board[x:x+3]

        return self.board[x + y]
    @staticmethod
    def get_x_y(i):
        x = i//3
        y = i - x * 3
        return x, y

    def set(self, x, y, to: BoardState):
        x *= 3
        self.board[x + y] = to

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
