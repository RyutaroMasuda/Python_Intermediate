from TicTacToe import TicTacToe
from agent import RandomAgent, HumanAgent
from enum_class import Player, GameState

if __name__ == "__main__":
    num_First_win = 0
    num_Second_win = 0
    num_draw = 0 
    num_PlayerA_win = 0
    PlayerA_state = "First"
    for i in range(1000):
        print(f"これは{i}試合目のn目並べゲームです。\n")
        ttt = TicTacToe(5)

        while ttt.state == GameState.CONTINUE:
            ttt.print_board()

            if ttt.next == Player.FIRST:
                # Player_FIRST
                x,y = RandomAgent.select_action(Player.FIRST, ttt)
                ttt.play(Player.FIRST, x, y)

            else:
                # Player_SECOND
                x,y = RandomAgent.select_action(Player.SECOND, ttt)
                ttt.play(Player.SECOND, x, y)
        # 最終盤面と結果
        ttt.print_board()

        if ttt.state == GameState.DRAW:
            num_draw+=1
            print(f"引き分けです")
        elif ttt.winner == Player.FIRST:
            num_First_win+=1
            print(f"先行の勝利")
            if PlayerA_state == "First":
                num_PlayerA_win+=1
            PlayerA_state = "Second"
        elif ttt.winner == Player.SECOND:
            num_Second_win+=1
            print(f"後攻の勝利")
            if PlayerA_state == "Second":
                num_PlayerA_win+=1
            PlayerA_state = "First"
        print(f"引き分け{num_draw}回")
        print(f"先行の勝利{num_First_win}回")
        print(f"後攻の勝利{num_Second_win}回")
        print(f"Aの勝利数{num_PlayerA_win}")
            