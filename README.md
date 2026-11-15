# tiny-chess-01 entry — packed Sunfish

A deterministic Python chess engine for the make.fun tiny-chess-01 competition,
packed into a single 4077-byte `main.py`.

The chess core is a fork of [Sunfish](https://github.com/thomasahle/sunfish)
by Thomas Ahle (GPL-3.0), lightly pruned for size (history-heuristic table,
transposition-table eviction, time-deadline plumbing removed; node-capped
iterative MTD/bisect search intact). It plays each gauntlet game through the
env API, rebuilding the position history from the move list, and budgets at
most 45,000 search nodes per move (well inside the 10 s move limit).

Sunfish GPL-3.0 credit: SPDX-License-Identifier: GPL-3.0 applies to the
derived engine code; see LICENSE.
