from abc import ABCMeta, abstractmethod
import random
from enum_class import Player, Cell, GameState

class TicTacToeAgent(metaclass=ABCMeta):
    def __init__(self,player:Player):
        self.player = player

    @abstractmethod
    def select_action(self,game):
        pass
    
class RandomAgent(TicTacToeAgent):
    def __init__(self,player:Player):
        super().__init__()
    def select_action(self,game):
        if_not_empty = True 
        while(if_not_empty):
            x = random.randrange(game.size)
            y = random.randrange(game.size)
            if(game.board[y][x] == Cell.EMPTY):
                if_not_empty = False
        return x,y

class HumanAgent(TicTacToeAgent):
    def __init__(self,player:Player):
        super().__init__()
    def select_action(self,game):
        print("x座標は(1〜{})".format(game.size))
        x = int(input())
        while x < 1 or x > game.size :
            print("もう一度入れなおして\nx座標は(1〜{})".format(game.size ))
            x = int(input())

        print("y座標は(1〜{})".format(game.size))
        y = int(input())
        while y < 1 or y > game.size:
            print("もう一度入れなおして\ny座標は(1〜{})".format(game.size))
            y = int(input())

        x-=1
        y-=1
        return x,y
    
    
if __name__ == '__main__':
    pass
