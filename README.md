リポジトリ: 
git@github.com:RyutaroMasuda/Python_Intermediate.git

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
