#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TicTacToe (3x3) の各ply(手数)ごとの局面パターン数を
バーンサイドの補題（Burnside's lemma）で求めるスクリプト。

同一視する対称変換（D4, 8通り）:
- 回転: 0°, 90°, 180°, 270°
- 反転: 水平、垂直、主対角(45°)、副対角(-45°)

手順:
1) 初期局面から合法手で到達可能な局面を ply ごとに列挙（勝敗確定で打ち切り）
2) 各 ply の到達集合 S_ply について
   orbit_count(ply) = (1/8) * sum_{g in D4} Fix_g(ply)
   Fix_g(ply) = |{ b in S_ply : g(b) == b }|

使ってよい import は os, sys のみ。TicTacToe/enum_class を最大限活用。

RESULTS（到達可能局面 S_ply を対象、勝敗確定後は展開しない）:

Raw reachable positions per ply (|S_ply|):
ply=0:    1
ply=1:    9
ply=2:   72
ply=3:  252
ply=4:  756
ply=5: 1260
ply=6: 1520
ply=7: 1140
ply=8:  390
ply=9:   78

Symmetry-reduced unique patterns per ply (Burnside orbits |S_ply/D4|):
ply=0:   1
ply=1:   3
ply=2:  12
ply=3:  38
ply=4: 108
ply=5: 174
ply=6: 204
ply=7: 153
ply=8:  57
ply=9:  15
"""

import os
import sys

# Ensure local imports work
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from TicTacToe import TicTacToe
from enum_class import Player, Cell, GameState


# -------------------------
# Utilities: clone & encoding
# -------------------------
def clone_game(g):
    """Manual deep clone without importing copy/deepcopy."""
    ng = TicTacToe(g.size)
    ng.next = g.next
    ng.state = g.state
    ng.winner = g.winner
    ng.board = [[g.board[y][x] for x in range(g.size)] for y in range(g.size)]
    return ng


def board_to_int_tuple(board):
    """Hashable representation (row-major) using Cell.value."""
    n = len(board)
    out = []
    for y in range(n):
        for x in range(n):
            out.append(board[y][x].value)
    return tuple(out)


def valid_actions(g):
    """Return list of (x,y) empty cells."""
    acts = []
    n = g.size
    for y in range(n):
        for x in range(n):
            if g.board[y][x] == Cell.EMPTY:
                acts.append((x, y))
    return acts


# -------------------------
# D4 group action (8 symmetries)
# We operate on row-major int-tuples.
# -------------------------
def transform_int_tuple(t, n, map_rc):
    out = [0] * (n * n)
    for r in range(n):
        for c in range(n):
            nr, nc = map_rc(r, c, n)
            out[nr * n + nc] = t[r * n + c]
    return tuple(out)


def id_map(r, c, n):      return (r, c)
def rot90(r, c, n):       return (c, n - 1 - r)
def rot180(r, c, n):      return (n - 1 - r, n - 1 - c)
def rot270(r, c, n):      return (n - 1 - c, r)
def refl_h(r, c, n):      return (n - 1 - r, c)          # horizontal axis
def refl_v(r, c, n):      return (r, n - 1 - c)          # vertical axis
def refl_d(r, c, n):      return (c, r)                  # main diagonal
def refl_ad(r, c, n):     return (n - 1 - c, n - 1 - r)  # anti-diagonal

D4 = (
    ("id",      id_map),
    ("rot90",   rot90),
    ("rot180",  rot180),
    ("rot270",  rot270),
    ("refl_h",  refl_h),
    ("refl_v",  refl_v),
    ("refl_d",  refl_d),
    ("refl_ad", refl_ad),
)


# -------------------------
# Enumerate reachable positions per ply
# (stop expanding at terminal states)
# -------------------------
def enumerate_reachable_by_ply(n=3):
    start = TicTacToe(n)
    by_ply = {}  # ply -> set[int_tuple]

    stack = [(start, 0)]
    while stack:
        g, ply = stack.pop()

        bt = board_to_int_tuple(g.board)
        if ply not in by_ply:
            by_ply[ply] = set()
        by_ply[ply].add(bt)

        # terminal? -> do not expand
        if g.state != GameState.CONTINUE:
            continue

        p = g.next
        for (x, y) in valid_actions(g):
            ng = clone_game(g)
            ng.play(p, x, y)
            stack.append((ng, ply + 1))

    return by_ply


# -------------------------
# Burnside's lemma on S_ply under D4
# -------------------------
def burnside_orbit_count(S, n):
    """
    S: set of int-tuple boards (reachable at some ply)
    return: (orbits, fix_counts_dict)
    """
    fix_counts = {}
    total_fix = 0

    for name, f in D4:
        cnt = 0
        for b in S:
            if transform_int_tuple(b, n, f) == b:
                cnt += 1
        fix_counts[name] = cnt
        total_fix += cnt

    # |G| = 8
    orbits = total_fix // 8  # should be integer
    return orbits, fix_counts, total_fix


def main():
    n = 4
    by_ply = enumerate_reachable_by_ply(n)

    # Print summary using Burnside
    for ply in range(0, n * n + 1):
        S = by_ply.get(ply, set())
        orbits, fix_counts, total_fix = burnside_orbit_count(S, n)
        print("ply=%d raw=%d orbits=%d (sumFix=%d)" % (ply, len(S), orbits, total_fix))


if __name__ == "__main__":
    main()
