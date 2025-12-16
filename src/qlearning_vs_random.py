from TicTacToe import TicTacToe
from agent import RandomAgent, HumanAgent, QLearningAgent
from enum_class import Player, GameState

if __name__ == "__main__":
    num_First_win = 0
    num_Second_win = 0
    num_draw = 0 
    num_PlayerA_win = 0
    PlayerA_state = "First"
    num_q_win = 0

    dummy_game = TicTacToe(4)
    q_agent = QLearningAgent(Player.FIRST,dummy_game)

    for i in range(100000):
        print(f"これは{i}試合目のn目並べゲームです。\n")
        ttt = TicTacToe(5)

        # if PlayerA_state == "First":
        #     q_player = Player.FIRST
        #     r_player = Player.SECOND
        # else:
        #     q_player = Player.SECOND
        #     r_player = Player.FIRST
        q_player = Player.FIRST
        r_player = Player.SECOND

        r_agent = RandomAgent(r_player)

        s = None
        a = None
        while ttt.state == GameState.CONTINUE:
            ttt.print_board()
            # ------- Qのターン -------
            if ttt.next == q_player:
                s = q_agent.encode_state(ttt.board)
                a = q_agent.select_action(ttt)

                x,y = a
                ttt.play(q_player, x, y)

                if ttt.state != GameState.CONTINUE:
                    ns = q_agent.encode_state(ttt.board)
                    done = True

                    if ttt.state == GameState.FINISHED and ttt.winner == q_player:
                        reward = +1
                    elif ttt.state == GameState.FINISHED:
                        reward = -1
                    else:
                        reward = 0

                    q_agent.bellman_update(s, a, reward, ns, done)
                    s = None
                    a = None

            else:
                # ------- Randomのターン -------
                x,y = r_agent.select_action(ttt)
                ttt.play(r_player, x, y)

                if s is not None:
                    ns = q_agent.encode_state(ttt.board)
                    done = (ttt.state != GameState.CONTINUE)

                    if ttt.state == GameState.FINISHED and ttt.winner == q_player:
                        reward = +1
                    elif ttt.state == GameState.FINISHED:
                        reward = -1
                    elif ttt.state == GameState.DRAW:
                        reward = 0
                    else:
                        reward = 0

                    q_agent.bellman_update(s, a, reward, ns, done)
                    s = None
                    a = None

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
        if ttt.winner == q_player:
            num_q_win += 1
        print(f"引き分け{num_draw}回")
        print(f"先行の勝利{num_First_win}回")
        print(f"後攻の勝利{num_Second_win}回")
        print(f"qの勝利数{num_q_win}")
            