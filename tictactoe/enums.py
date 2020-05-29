from enum import Enum

class GameMode(Enum):
    ONE_PLAYER = 0
    TWO_PLAYER = 1

class GameState(Enum):
    PLAYING = 0
    EXIT = 1
    GAME_OVER = 2

class BoardState(Enum):
    BLANK = 0
    X = 1
    O = 2

    def __str__(self):
        if self.name == "BLANK":
            return "-"
        elif self.name == "X":
            return "X"
        elif self.name == "O":
            return "O"
