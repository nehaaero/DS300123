def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # Check if no queens threaten the current position
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            j = row - i
            if col - j >= 0 and board[i][col - j] == 'Q':
                return False
            if col + j < n and board[i][col + j] == 'Q':
                return False
        return True

    def backtrack(row):
        # Base case: All rows have been filled, add the solution
        if row == n:
            solutions.append([''.join(row) for row in board])
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return solutions

# Test the implementation
n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens problem: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()
    