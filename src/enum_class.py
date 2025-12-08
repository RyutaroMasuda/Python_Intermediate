from enum import Enum

class Player(Enum):
    FIRST = 1   # 先手
    SECOND = 2  # 後手


class Cell(Enum):
    EMPTY = 0
    FIRST = 1   # 〇
    SECOND = 2  # ×


class GameState(Enum):
    CONTINUE = 0
    DRAW = 1
    FINISHED = 2