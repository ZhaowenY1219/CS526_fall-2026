
import math
import sys


def symbols_are_valid(board, symbols):
    """Check whether every non-empty cell contains an allowed symbol."""
    n = len(board)

    for i in range(n):
        for j in range(n):
            if board[i][j] == ".":
                continue

            if board[i][j] not in symbols:
                return False

    return True


def rows_are_valid(board):
    """Check each row for duplicate non-empty symbols."""
    n = len(board)

    for i in range(n):
        for j in range(n):
            if board[i][j] == ".":
                continue

            # Compare with every cell to the right.
            for k in range(j + 1, n):
                if board[i][k] == ".":
                    continue

                if board[i][j] == board[i][k]:
                    return False

    return True


def columns_are_valid(board):
    """Check each column for duplicate non-empty symbols."""
    n = len(board)

    for j in range(n):
        for i in range(n):
            if board[i][j] == ".":
                continue

            # Compare with every cell below.
            for k in range(i + 1, n):
                if board[k][j] == ".":
                    continue

                if board[i][j] == board[k][j]:
                    return False

    return True


def subboards_are_valid(board):
    """Check every sub-board using pairwise comparison."""
    n = len(board)
    size = math.isqrt(n)

    # Select each sub-board.
    for startRow in range(0, n, size):
        for startCol in range(0, n, size):

            # Select the current cell.
            for i in range(startRow, startRow + size):
                for j in range(startCol, startCol + size):
                    if board[i][j] == ".":
                        continue

                    # Select candidate cells in the same sub-board.
                    for k in range(startRow, startRow + size):
                        for l in range(startCol, startCol + size):

                            # Skip the current cell and earlier cells.
                            if not (
                                k > i or
                                (k == i and l > j)
                            ):
                                continue

                            if board[k][l] == ".":
                                continue

                            if board[i][j] == board[k][l]:
                                return False

    return True


def is_valid_board(n, symbols, board):
    """Check all the rules for a valid puzzle board."""

    if n <= 0 or math.isqrt(n) ** 2 != n:
        return False

    if len(symbols) != n or len(board) != n:
        return False

    for row in board:
        if len(row) != n:
            return False

    # Step 1: Check that all symbols are allowed.
    if not symbols_are_valid(board, symbols):
        return False

    # Step 2: Check rows.
    if not rows_are_valid(board):
        return False

    # Step 3: Check columns.
    if not columns_are_valid(board):
        return False

    # Step 4: Check sub-boards.
    if not subboards_are_valid(board):
        return False

    return True


def parse_input(text):
    """Read n, the symbols, and the puzzle board from the input."""
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if len(lines) < 2:
        raise ValueError("Input must contain n and the symbols.")

    n = int(lines[0])
    symbols = [
        value.strip()
        for value in lines[1].split(",")
    ]

    if len(lines) < n + 2:
        raise ValueError("Input does not contain all board rows.")

    board = []

    for line in lines[2:n + 2]:
        row = [
            value.strip()
            for value in line.split(",")
        ]
        board.append(row)

    return n, symbols, board


def main():
    """Read input and print the required result."""

    try:
        # Accept a filename or standard input.
        if len(sys.argv) > 1:
            with open(
                sys.argv[1], "r", encoding="utf-8"
            ) as input_file:
                input_text = input_file.read()
        else:
            input_text = sys.stdin.read()

        n, symbols, board = parse_input(input_text)

        if is_valid_board(n, symbols, board):
            print("The board is valid")
        else:
            print("The board is invalid")

    except (OSError, ValueError) as error:
        print(f"Input error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
