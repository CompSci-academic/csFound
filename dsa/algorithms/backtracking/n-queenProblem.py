def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n):
    if row == n:
        return [board[:]]  # Found a solution

    solutions = []
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solutions += solve_n_queens_util(board, row + 1, n)
            board[row][col] = 0  # Backtrack

    return solutions

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = solve_n_queens_util(board, 0, n)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(' '.join(['Q' if cell == 1 else '.' for cell in row]))
        print()

n = 4  # Adjust the value of N as needed
solutions = solve_n_queens(n)
print(f"Solutions for {n}-Queens Problem:")
print_solutions(solutions)
