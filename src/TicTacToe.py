import ipdb
import random

class TicTacToe:
    """ This class is for " n in row " game.
        First player is represented as  "〇", and Second player is represented as "×".
    """
    def __init__(self,n=3):
        self.n = n
        self.next = 1
        self.state = 0
        self.size = n
        self.winner = None
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def play(self, player,x,y):
        if player != self.next:
            print("今はプレイヤー", self.next, "の手番です")
            return
        
        if self.board[x][y] == 0:
            if player == 1:
                self.board[x][y] = "〇"
                self.next = 2
            elif player == 2:
                self.board[x][y] = "×"
                self.next = 1
        else:
            print("Caution: You can't put the piece here!")
        
    def judgement(self):
        for idx in range(self.n):
            # 横方向
            if(idx % self.n == 0):
                x, y = self.idx2coordinate(idx)
                while(x + 1 < self.n and self.board[x][y]!=0 and self.board[x][y] == self.board[x+1][y]):
                    if x  == self.n - 2:
                        self.winner = self.board[x][y]
                        self.state = 2
                        self.next = None
                        break
                    x+=1
            # 縦方向
            if(idx//self.n == 0):
                x, y = self.idx2coordinate(idx)
                while(y + 1 < self.n and self.board[x][y]!=0 and self.board[x][y] == self.board[x][y+1]):
                    if y == self.n - 2:
                        self.winner = self.board[x][y]
                        self.state = 2
                        self.next = None
                        break
                    y+=1
            # 斜め方向
            if(idx==0 or idx == self.n-1):
                x, y = self.idx2coordinate(idx)
                while(x+1 <self.n and y+1< self.n and self.board[x][y]!=0 and self.board[x][y] == self.board[x+1][y+1]):
                    if x == self.n - 2:
                        self.winner = self.board[x][y]
                        self.state = 2
                        self.next = None
                        break
                    y+=1
                    x+=1
            if all(self.board[i][j] != 0 for i in range(self.n) for j in range(self.n)):
                self.state = 1   
                self.next = None
                self.winner = None
    
    def idx2coordinate(self, idx):
        x = idx % self.n
        y = idx // self.n
        return x,y

    def coordinate2idx(self, x,y):
        idx = y * self.n + x
        return idx

    def print_board(self):
        if self.next == 1:
            print("先行プレイヤの番です\n")
        elif self.next == 2:
            print("後攻プレイヤの番です\n")
        for i in range(self.n):
            for j in range(self.n):
                print(f"{self.board[i][j]} ", end ="")
            print("\n")

    
if __name__ == "__main__":
    print("これはn目並べゲームです。\n")
    tictactoe = TicTacToe(5)
    while(tictactoe.winner == None):
        tictactoe.print_board()
        if tictactoe.next ==1 :
            print("x座標は")
            x = int(input())
            while(x<0 or x>tictactoe.n):
                print("もう一度入れなおして\n")
                print("x座標は")
                x=int(input())
            print("y座標は")
            y = int(input())
            while(y<0 or y>tictactoe.n):
                print("もう一度入れなおして\n")
                print("y座標は")
                y=int(input())
        elif tictactoe.next == 2:
            x = random.randrange(tictactoe.n)
            y = random.randrange(tictactoe.n)
        tictactoe.play(tictactoe.next,x-1,y-1)
        tictactoe.judgement()
        if(tictactoe.winner == "〇"):
            print("先行の勝利")
        elif(tictactoe.winner == "×"):
            print("後攻の勝利")
