import sys


def main():
    # Step 1: Read the input and initialize the board.
    values = sys.stdin.read().split()

    if not values:
        return

    N = int(values[0])

    # Create an N x N board. "." means healthy and "X" means infected.
    board = [["." for column in range(N)] for row in range(N)]

    # Mark the initially infected counties.
    for index in range(1, len(values), 2):
        row = int(values[index])
        column = int(values[index + 1])
        board[row][column] = "X"

    # Step 2-4: Simulate the spread until no new infections occur.
    while True:
        # Record the coordinates of today's new infections.
        new_infections = []

        # Step 2: Scan every row and every column.
        for row in range(N):
            for column in range(N):

                # Skip counties that are already infected.
                if board[row][column] == "X":
                    continue

                infected_neighbors = 0

                # Check the neighbor above.
                if row > 0 and board[row - 1][column] == "X":
                    infected_neighbors += 1

                # Check the neighbor below.
                if row < N - 1 and board[row + 1][column] == "X":
                    infected_neighbors += 1

                # Check the neighbor on the left.
                if column > 0 and board[row][column - 1] == "X":
                    infected_neighbors += 1

                # Check the neighbor on the right.
                if column < N - 1 and board[row][column + 1] == "X":
                    infected_neighbors += 1

                # Step 3: Record counties with at least two
                # infected neighbors. Do not update the board yet.
                if infected_neighbors >= 2:
                    new_infections.append((row, column))

        # Step 4: Stop if no new infections were found.
        if not new_infections:
            break

        # Otherwise, update all new infections together.
        for row, column in new_infections:
            board[row][column] = "X"

    # Step 5: Check the final board for any healthy county.
    healthy_found = False

    for row in range(N):
        for column in range(N):
            if board[row][column] == ".":
                healthy_found = True
                break

        if healthy_found:
            break

    if healthy_found:
        print("There are healthy counties left")
    else:
        print("There are no healthy counties left")


if __name__ == "__main__":
    main()
