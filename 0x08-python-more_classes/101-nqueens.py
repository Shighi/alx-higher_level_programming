#!/usr/bin/python3
"""N queens solution finder"""
import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed on board[row][col]

    Args:
        board: The current state of the board
        row: Row to check
        col: Column to check
        n: Size of the board

    Returns:
        Boolean indicating if the position is safe
    """
    # Check this row on left side
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                   range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1),
                   range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n, solutions):
    """Recursively solve N Queens problem using backtracking

    Args:
        board: The current state of the board
        col: Current column being processed
        n: Size of the board
        solutions: List to store all solutions

    Returns:
        True if solution is found, False otherwise
    """
    # Base case: If all queens are placed, store the solution
    if col >= n:
        pos = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    pos.append([i, j])
        solutions.append(pos)
        return True

    # Consider this column and try placing this queen in all rows
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            res = solve_nqueens(board, col + 1, n, solutions) or res

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0

    return res


def create_board(n):
    """Create an empty n x n board

    Args:
        n: Size of the board

    Returns:
        Empty board of size n x n
    """
    return [[0 for x in range(n)] for y in range(n)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = create_board(n)
    solutions = []

    solve_nqueens(board, 0, n, solutions)

    # Print all solutions
    for sol in solutions:
        print(sol)
