リポジトリ: 
git@github.com:RyutaroMasuda/Python_Intermediate.git

### Result of Random VS Q_agent

① Fixed First:random Second:q_agent
num of attempts : 1000000
| First | Second | Draw |
| :----: | :---: | :----: |
| 534324  | 413317  | 52359 |

② Fixed First:q_agent Second:random
num of attempts : 100000
| First | Second | Draw |
| :----: | :---: | :----: |
| 75116  | 19405  | 5479 |

③ First becomes Second if First wins (Q_Learning:First)
num of attempts : 100000
| Q_learning | Random | Draw |
| :----: | :---: | :----: |
| 53609  | 41185  | 5206 |
### Result of Random VS Random

num of attempts: 1000

① Fixed First/Second Player
| First | Second | Draw |
| :----: | :---: | :----: |
| 621  | 237  | 142 |

② First becomes Second if First wins

| First win | Second win | draw |
| :---: | :---: | :---: |
|    200    |    192     | 608  |

### implementation
random agent vs human
```
python human_vs_random.py
```
random agent vs random agent
```
python random_vs_random.py
```

- enum_class.py
    - settle enum
    - Player, Cell, GameState
- TicTacToe.py
    - implementation of the game
- agent.py
    - implementation of agent
    - random agent
    - human agent
    - q_learning agent
