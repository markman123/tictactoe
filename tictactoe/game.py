from os import system
from .enums import GameState, GameMode, BoardState
from .tictactoe import TicTacToe
class Game:
    def __init__(self):
        self.board = TicTacToe()
        self.turns = []
        self.whos_turn = BoardState.X
        self.game_mode = None

    def select_game_mode(self):
    
        print("[1]    vs. AI")
        print("[2]    2 Player")
        print("[Else] Quit")
        game_mode = input("Select game mode: ")

        if game_mode.lower() not in ["1", "2"]:
            self.exit_game()

        if game_mode == "1":
            self.game_mode = GameMode.ONE_PLAYER
            print("Playing against me! ... you're gonna lose. Loser.")
        elif game_mode == "2":
            self.game_mode = GameMode.TWO_PLAYER
            print("Playing with a friend... (BS! Against yourself)")



    def start_game(self):
        system("cls")
        self.select_game_mode()
        self.game_loop()

    def exit_game(self):
        print("Please, play again! I'm lonely...")
        exit(0)

    def game_loop(self):
        system("cls")
        while True:
            print("Here is the board:")
            self.board.print()
            turn = input(
                f"[Turn of {str(self.whos_turn)}] Enter coords (q to quit): "
            )
            turn = self.parse_turn(turn)
            if turn == GameState.EXIT:
                self.exit_game()
            elif not isinstance(turn, GameState):
                self.process_turn(turn[0], turn[1])

    @staticmethod
    def _check_all(check):
        x = lambda x: x == BoardState.X
        o = lambda x: x == BoardState.O
        x_winner = all([x(i) for i in check])
        o_winner = all([o(i) for i in check])

        if x_winner:
            return BoardState.X

        elif o_winner:
            return BoardState.O

    @staticmethod
    def check_winner(board):
        # Check horizontals
        for y in range(3):
            check = board.get(y)
            winner = Game._check_all(check)
            if winner:
                return winner
        # Check Verticals
        for x in range(3):
            check = [board.get(0, x), board.get(1, x), board.get(2, x)]
            winner = Game._check_all(check)
            if winner:
                return winner
        # Check diagonals [00 11 22][02 11 20]
        check = [board.get(0, 0), board.get(1, 1), board.get(2, 2)]
        winner = Game._check_all(check)
        if winner:
            return winner

        check = [board.get(0, 2), board.get(1, 1), board.get(2, 0)]
        winner = Game._check_all(check)
        if winner:
            return winner

        # Check stale mate
        if Game._is_stale_mate(board):
            return GameState.GAME_OVER
        
        return GameState.PLAYING
    @staticmethod
    def _is_stale_mate(board):
        not_blank = lambda x: x != BoardState.BLANK
        return all([not_blank(i) for i in board])

    def reset_game(self):
        self.__init__()
        self.start_game()

    def play_again(self):
        play_again = input("Play again? Y/N: ")
        if play_again.lower() == "y":
            self.reset_game()
        else:
            self.exit_game()

    def process_turn(self, x, y):
        self.turns.append((x, y))
        self.board.set(x, y, self.whos_turn)
        winner = Game.check_winner(self.board)
        if isinstance(winner, BoardState):
            system("cls")
            self.board.print()
            print(f"Congratulations player {str(winner)}! You've won!!")
            self.play_again()
        elif winner == GameState.GAME_OVER:
            print("Yawn... stale mate")
            self.play_again()
        else:
            system("cls")
            self.switch_player()

    def switch_player(self):
        if self.whos_turn == BoardState.X:
            self.whos_turn = BoardState.O
        else:
            self.whos_turn = BoardState.X

    @staticmethod
    def error_text(input):
        system("cls")
        print(f"Bad input: {input}\n\nError, please enter as colrow")

    def parse_turn(self, turn):
        if turn == "q":
            return GameState.EXIT
        if len(turn) != 2:
            Game.error_text(turn)
            return GameState.PLAYING

        if not turn[0].isdigit() or not turn[1].isdigit():
            Game.error_text(turn)
            return GameState.PLAYING

        x, y = int(turn[0]), int(turn[1])

        if x > 2 or y > 2 or x < 0 or y < 0:
            Game.error_text(turn)
            return GameState.PLAYING

        if self.board.get(x, y) != BoardState.BLANK:
            Game.error_text(f"\nNot a blank space! {turn}")
            return GameState.PLAYING

        return x, y