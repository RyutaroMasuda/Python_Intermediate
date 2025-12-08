import random
from enum_class import Player,Cell,GameState

class TicTacToe:
    """ This class is for " n in row " game.
        First player is represented as  "〇", and Second player is represented as "×".
    """

    def __init__(self, n=3):
        self.size = n            # 課題仕様の size
        self.next = Player.FIRST # 次のプレイヤー（先手から）
        self.state = GameState.CONTINUE
        self.winner = None       # Player or None
        self.board = [[Cell.EMPTY for _ in range(n)] for _ in range(n)]

    # x: 列(0〜n-1), y: 行(0〜n-1)
    def play(self, player, x, y):
        # ゲーム終了後は打てない
        if self.state != GameState.CONTINUE:
            print("ゲームはすでに終了しています。")
            return

        # 手番チェック
        if player != self.next:
            print("今はプレイヤー", self.next, "の手番です")
            return

        # 範囲チェック
        if not (0 <= x < self.size  and 0 <= y < self.size ):
            print("盤外です")
            return

        # 空きマスチェック
        if self.board[y][x] != Cell.EMPTY:
            print("Caution: You can't put the piece here!")
            return

        # 石を置く
        if player == Player.FIRST:
            self.board[y][x] = Cell.FIRST
            self.next = Player.SECOND
        else:
            self.board[y][x] = Cell.SECOND
            self.next = Player.FIRST

        # 勝敗・引き分け判定
        self.judgement()

    def judgement(self):
        n = self.size 
        b = self.board

        # 横
        for y in range(n):
            if b[y][0] != Cell.EMPTY and all(b[y][x] == b[y][0] for x in range(1, n)):
                self.winner = Player.FIRST if b[y][0] == Cell.FIRST else Player.SECOND
                self.state = GameState.FINISHED
                self.next = None
                return

        # 縦
        for x in range(n):
            if b[0][x] != Cell.EMPTY and all(b[y][x] == b[0][x] for y in range(1, n)):
                self.winner = Player.FIRST if b[0][x] == Cell.FIRST else Player.SECOND
                self.state = GameState.FINISHED
                self.next = None
                return

        # 斜め（左上→右下）
        if b[0][0] != Cell.EMPTY and all(b[i][i] == b[0][0] for i in range(1, n)):
            self.winner = Player.FIRST if b[0][0] == Cell.FIRST else Player.SECOND
            self.state = GameState.FINISHED
            self.next = None
            return

        # 斜め（右上→左下）
        if b[0][n - 1] != Cell.EMPTY and all(b[i][n - 1 - i] == b[0][n - 1] for i in range(1, n)):
            self.winner = Player.FIRST if b[0][n - 1] == Cell.FIRST else Player.SECOND
            self.state = GameState.FINISHED
            self.next = None
            return

        # 引き分け判定（空きマスなし）
        if all(b[y][x] != Cell.EMPTY for y in range(n) for x in range(n)):
            self.state = GameState.DRAW
            self.next = None
            self.winner = None
        else:
            self.state = GameState.CONTINUE

    def print_board(self):
        # 手番表示
        if self.next == Player.FIRST:
            print("先行プレイヤの番です\n")
        elif self.next == Player.SECOND:
            print("後攻プレイヤの番です\n")

        # マスの表示文字を決める
        def cell_to_char(cell: Cell) -> str:
            if cell == Cell.EMPTY:
                return "・"
            elif cell == Cell.FIRST:
                return "〇"
            elif cell == Cell.SECOND:
                return "×"

        for y in range(self.size ):
            for x in range(self.size ):
                print(cell_to_char(self.board[y][x]), end=" ")
            print()
        print()


if __name__ == "__main__":
    print("これはn目並べゲームです。\n")
    ttt = TicTacToe(5)

    while ttt.state == GameState.CONTINUE:
        ttt.print_board()

        if ttt.next == Player.FIRST:
            # 人間（先手）
            print("x座標は(1〜{})".format(ttt.size ))
            x = int(input())
            while x < 1 or x > ttt.size :
                print("もう一度入れなおして\nx座標は(1〜{})".format(ttt.size ))
                x = int(input())

            print("y座標は(1〜{})".format(ttt.size))
            y = int(input())
            while y < 1 or y > ttt.size:
                print("もう一度入れなおして\ny座標は(1〜{})".format(ttt.size))
                y = int(input())

            # 入力は1始まりなので -1 して内部座標に
            ttt.play(Player.FIRST, x - 1, y - 1)

        else:
            # ランダムCPU（後手）
            while True:
                rx = random.randrange(ttt.size)
                ry = random.randrange(ttt.size)
                if ttt.board[ry][rx] == Cell.EMPTY:
                    ttt.play(Player.SECOND, rx, ry)
                    break

    # 最終盤面と結果
    ttt.print_board()

    if ttt.state == GameState.DRAW:
        print("引き分けです")
    elif ttt.winner == Player.FIRST:
        print("先行の勝利")
    elif ttt.winner == Player.SECOND:
        print("後攻の勝利")
