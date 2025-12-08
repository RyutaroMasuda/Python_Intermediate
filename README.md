リポジトリ: 
git@github.com:RyutaroMasuda/Python_Intermediate.git

### Random VS Randomの対戦結果

試行回数1000回

①先攻後攻固定
| 先行 | 後攻 | 引き分け |
| :----: | :---: | :----: |
| 621  | 237  | 142 |

②先攻が勝ったら高校になるルール

| First win | Second win | draw |
| :---: | :---: | :---: |
|    200    |    192     | 608  |

### 実装
ランダムエージェントVS人間
```
python human_vs_random.py
```
ランダムエージェントVSランダムエージェント
```
python random_vs_random.py
```

- enum_class.py
    - enumをまとめている
- TicTacToe.py
    - 試合の実装
- agent.py
    - agentの実装
