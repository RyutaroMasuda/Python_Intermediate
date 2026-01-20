import os
import sys
"""
ply:手数
symmetry:同一パターン数

ply=0 symmetry=1 raw=1
ply=1 symmetry=3 raw=9
ply=2 symmetry=12 raw=72
ply=3 symmetry=38 raw=252
ply=4 symmetry=108 raw=756
ply=5 symmetry=174 raw=1260
ply=6 symmetry=204 raw=1520
ply=7 symmetry=153 raw=1140
ply=8 symmetry=57 raw=390
ply=9 symmetry=15 raw=78

"""
# Make sure we can import the provided modules when running from anywhere.
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from TicTacToe import TicTacToe
from enum_class import Player, Cell, GameState


def clone_game(g):
    """Manual deep clone without importing copy/deepcopy."""
    ng = TicTacToe(g.size)
    ng.next = g.next
    ng.state = g.state
    ng.winner = g.winner
    ng.board = [[g.board[y][x] for x in range(g.size)] for y in range(g.size)]
    return ng


def board_to_int_tuple(board):
    """Hashable + orderable representation (row-major) using Cell.value."""
    n = len(board)
    out = []
    for y in range(n):
        for x in range(n):
            out.append(board[y][x].value)
    return tuple(out)


def transform_int_tuple(t, n, map_rc):
    """Apply a coordinate transform to a row-major int-tuple board."""
    out = [0] * (n * n)
    for r in range(n):
        for c in range(n):
            nr, nc = map_rc(r, c, n)
            out[nr * n + nc] = t[r * n + c]
    return tuple(out)


# --- D4 transforms ---

def id_map(r, c, n):
    return r, c


def rot90(r, c, n):
    return c, n - 1 - r


def rot180(r, c, n):
    return n - 1 - r, n - 1 - c


def rot270(r, c, n):
    return n - 1 - c, r


def refl_h(r, c, n):
    return n - 1 - r, c


def refl_v(r, c, n):
    return r, n - 1 - c


def refl_d(r, c, n):
    return c, r


def refl_ad(r, c, n):
    return n - 1 - c, n - 1 - r


D4_MAPS = (id_map, rot90, rot180, rot270, refl_h, refl_v, refl_d, refl_ad)


def canonical_int_tuple(t, n):
    """Return the lexicographically smallest representative under D4."""
    best = None
    for f in D4_MAPS:
        cand = transform_int_tuple(t, n, f)
        if best is None or cand < best:
            best = cand
    return best


def valid_actions(g):
    acts = []
    n = g.size
    for y in range(n):
        for x in range(n):
            if g.board[y][x] == Cell.EMPTY:
                acts.append((x, y))
    return acts


def enumerate_reachable(n=3):
    """BFS over reachable game states; stop expansion at terminal."""
    start = TicTacToe(n)

    raw_by_ply = {}  # ply -> set[int_tuple]
    can_by_ply = {}  # ply -> set[int_tuple canonical]

    # frontier holds (game, ply)
    frontier = [(start, 0)]

    while frontier:
        g, ply = frontier.pop()

        raw = board_to_int_tuple(g.board)
        can = canonical_int_tuple(raw, n)

        if ply not in raw_by_ply:
            raw_by_ply[ply] = set()
            can_by_ply[ply] = set()
        raw_by_ply[ply].add(raw)
        can_by_ply[ply].add(can)

        # terminal? (win/draw) -> do not expand
        if g.state != GameState.CONTINUE:
            continue

        p = g.next
        for (x, y) in valid_actions(g):
            ng = clone_game(g)
            ng.play(p, x, y)
            frontier.append((ng, ply + 1))

    return raw_by_ply, can_by_ply


def main():
    raw_by_ply, can_by_ply = enumerate_reachable(3)

    for ply in range(10):
        print("ply=%d symmetry=%d raw=%d" % (
            ply,
            len(can_by_ply.get(ply, set())),
            len(raw_by_ply.get(ply, set())),
        ))


if __name__ == "__main__":
    main()