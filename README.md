# Tic-Tac-Toe (Console Edition)

A simple, classic **Tic-Tac-Toe** game built entirely in Python — no external libraries required.

Play against a friend in turns using numbers 1–9 on a clean text-based board.


Enter numbers 1 to 9 to place your mark (X or O).

## Features

- Two-player hot-seat mode (X vs O)
- Input validation (can't place on occupied cell)
- Automatic win detection (rows, columns, diagonals)
- Draw detection (board full, no winner)
- Clean text-based board display
- Very beginner-friendly code structure

## How to Play

1. Run the script:

```bash
python tictactoe.py

Players take turns entering a number 1–9 corresponding to these positions:

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

First player is X, second is O
Game ends when someone wins or the board is full (draw)

What's your turn? 5
_ | _ | _
_ | X | _
_ | _ | _

What's your turn? 1
O | _ | _
_ | X | _
_ | _ | _
