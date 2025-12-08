from TicTacToe import TicTacToe
from agent import RandomAgent, HumanAgent
from enum_class import Player, GameState

if __name__ == "__main__":
    print("これはn目並べゲームです。\n")
    ttt = TicTacToe(5)

    while ttt.state == GameState.CONTINUE:
        ttt.print_board()

        if ttt.next == Player.FIRST:
            # 人間（先手）
            x,y = HumanAgent.select_action(Player.FIRST, ttt)
            ttt.play(Player.FIRST, x, y)

        else:
            # ランダムCPU（後手）
            x,y = RandomAgent.select_action(Player.SECOND, ttt)
            ttt.play(Player.SECOND, x, y)
    # 最終盤面と結果
    ttt.print_board()

    if ttt.state == GameState.DRAW:
        print("引き分けです")
    elif ttt.winner == Player.FIRST:
        print("先行の勝利")
    elif ttt.winner == Player.SECOND:
        print("後攻の勝利")