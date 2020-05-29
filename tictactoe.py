from enum import Enum
from os import system


class States(Enum):
    BLANK = 0
    X = 1
    O = 2

    def __str__(self):
        if self.name == "BLANK":
            return " - "
        elif self.name == "X":
            return " X "
        elif self.name == "O":
            return " O "


"""
+---+----+---+
| - | - | - |
| - | - | - |
| - | - | - |
"""
"""
+---+----+---+
| 00 | 01 | 02 |
| 10 | 11 | 12 |
| 20 | 21 | 22 |
[00 11 22][02 11 20]
"""


class TicTacToe:
    def __init__(self):
        self.board = [[States.BLANK for _ in range(3)] for _ in range(3)]

    def __repr__(self):
        output = "   +-0-+-1-+-2-+\n"
        for idx, row in enumerate(self.board):
            row = [str(i) for i in row]
            row = f"{idx}: |{row[0]}|{row[1]}|{row[2]}|"
            output += row + "\n"
        output += "   +---+---+---+"
        return output

    def get(self, x, y=None):
        if y == None:
            return self.board[x]

        return self.board[x][y]

    def set(self, x, y, to: States):
        self.board[x][y] = to

    def print(self):
        print(str(self))


class Game:
    def __init__(self):
        self.board = TicTacToe()
        self.turns = []
        self.whos_turn = States.X

    def start_game(self):
        self.game_loop()

    def game_loop(self):
        system("cls")
        while True:
            print("Here is the board:")
            print(self.board)
            turn = input(
                f"[Turn of {str(self.whos_turn)}] Enter turn as colrow e.g. 01, 22 (q to quit): "
            )
            turn = self.parse_turn(turn)
            if turn == -1:
                print("Please, play again! I'm lonely...")
                exit(0)
            elif turn:
                self.process_turn(turn[0], turn[1])

    @staticmethod
    def _check_all(check):
        x = lambda x: x == States.X
        o = lambda x: x == States.O
        x_winner = all([x(i) for i in check])
        o_winner = all([o(i) for i in check])

        if x_winner:
            return States.X

        elif o_winner:
            return States.O

    def check_winner(self):
        # Check horizontals
        for y in range(3):
            check = self.board.get(y)
            winner = Game._check_all(check)
            if winner:
                return winner
        # Check Verticals
        for x in range(3):
            check = [self.board.get(0, x), self.board.get(1, x), self.board.get(2, x)]
            winner = Game._check_all(check)
            if winner:
                return winner
        # Check diagonals [00 11 22][02 11 20]
        check = [self.board.get(0, 0), self.board.get(1, 1), self.board.get(2, 2)]
        winner = Game._check_all(check)
        if winner:
            return winner

        check = [self.board.get(0, 2), self.board.get(1, 1), self.board.get(2, 0)]
        winner = Game._check_all(check)
        if winner:
            return winner

        # Check stale mate
        if self._is_stale_mate():
            return -1

    def _is_stale_mate(self):
        flat = []
        for x in range(3):
            for y in range(3):
                flat.append(self.board.get(x, y))

        not_blank = lambda x: x != States.BLANK

        return all([not_blank(i) for i in flat])

    def reset_game(self):
        self.__init__()

    def play_again(self):
        play_again = input("Play again? Y/N: ")
        if play_again.lower() == "Y":
            self.reset_game()
        else:
            exit(0)

    def process_turn(self, x, y):
        self.turns.append((x, y))
        self.board.set(x, y, self.whos_turn)
        winner = self.check_winner()
        if winner and winner.value >= 0:
            system("cls")
            print(self.board)
            print(f"Congratulations player {str(winner)}! You've won!!")
            self.play_again()
        else:
            system("cls")
            self.switch_player()

    def switch_player(self):
        if self.whos_turn == States.X:
            self.whos_turn = States.O
        else:
            self.whos_turn = States.X

    @staticmethod
    def error_text(input):
        system("cls")
        print(f"Bad input: {input}\n\nError, please enter as colrow")

    def parse_turn(self, turn):
        if turn == "q":
            return -1
        if len(turn) != 2:
            Game.error_text(turn)
            return

        if not turn[0].isdigit() or not turn[1].isdigit():
            Game.error_text(turn)
            return

        x, y = int(turn[0]), int(turn[1])

        if x > 2 or y > 2 or x < 0 or y < 0:
            Game.error_text(turn)
            return

        if self.board.get(x, y) != States.BLANK:
            Game.error_text(f"\nNot a blank space! {turn}")
            return

        return x, y


game = Game().start_game()
