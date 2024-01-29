#!/usr/bin/python3

import sys


def usage():
    """Prints usage message and exits."""
    print("Usage: nqueens N", file=sys.stderr)
    sys.exit(1)


if len(sys.argv) != 2:
    usage()

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number", file=sys.stderr)
    sys.exit(1)

if n < 4:
    print("N must be at least 4", file=sys.stderr)
    sys.exit(1)


def is_valid_placement(board, row, col):
    """Checks if placing a queen at (row, col) is valid."""
    # Check row and column
    for i in range(len(board)):
        if board[i] == col or abs(i - row) == abs(board[i] - col):
            return False
    return True


def solve_n_queens(board, row):
    """Solves the N queens problem using backtracking."""
    if row == len(board):
        # Found a solution, print the board
        print(board)
        return

    for col in range(len(board)):
        if is_valid_placement(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1)
            board[row] = -1  # Backtrack


board = [-1] * n
solve_n_queens(board, 0)
