
class TicTacToe:
    def __init__(self,n=3,next=1,board,state=0,winner):
        self.n = n
        self.next = next
        self.state = state
        for i in range(n):
            for j in range(n):
                self.board[i][j] = 0
        self.winner = None

    def play(player,x,y):
        if self.board[x][y] == 0:
            if player == 1:
                self.board[x][y] = "〇"
                self.next = 2
            else if player == 2:
                self.board[x][y] = "×"
                self.next = 1
        else:
            print("Caution: You can't put the piece here!")

    def print_board():
        for i in range(self.n):
            for j in range(self.n):
                print(f"|{self.board[i][j]}|")
            print("\n")

    
if '__name__' == "__main__":
