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
        super().__init__(player)
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
class QLearningAgent(TicTacToeAgent):
    """
    this is qlearning agent.
    args.
    alpha : learning rate
    gamma : discount rate
    epsilon : argument for epsilon-greedy method
    state : size(3*(game.size**2)). state on the board.
    """
    def __init__(self,player:Player,game,alpha=0.1,gamma=0.9,epsilon=0.1):
        super().__init__(player)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.size = game.size
    
        self.q_table = {}

    def encode_state(self,board):
        """
        This method is make "board" tuple from list. 
        It is imposiible to preserve q_table with "list", so use "tuple" ,which is immutable and can adopt to "dictionary".
        """
        return tuple(tuple(cell for cell in row) for row in board)
    
    # -------return q value from state-------
    def ensure_state(self,state):
        
        if state not in self.q_table:
            self.q_table[state] = [0.0] * (self.size * self.size)
        return self.q_table[state]

    # ------- return list of coodinates on which players can action -------
    def valid_actions(self,game):
        acts = []
        for y in range(game.size):
            for x in range(game.size):
                if game.board[y][x] == Cell.EMPTY:
                    acts.append((x,y))
        return acts

    def action_to_index(self, x, y):
        return y * self.size + x

    # ------- use epsilon-greedy -------
    def select_action(self,game):
        state = self.encode_state(game.board)
        q_value = self.ensure_state(state)

        acts = self.valid_actions(game)

        # random
        if random.random() < self.epsilon:
            return random.choice(acts)
        # use policy
        best = max(acts,key=lambda xy: q_value[self.action_to_index(xy[0],xy[1])])
        return best
        
    def bellman_update(self,state,action,reward,next_state,done):
        """
        args.
            state, next_state:encoded state(tuple of tuples)
            action : (x,y)
            done : terminal flag
        """
        q_s = self.ensure_state(state)
        q_ns = self.ensure_state(next_state)

        a = self.action_to_index(action[0],action[1])

        current = q_s[a]
        max_next = 0.0 if done else max(q_ns)
        target = reward + self.gamma * max_next

        q_s[a] = current + self.alpha * (target - current)

    
if __name__ == '__main__':
    pass
