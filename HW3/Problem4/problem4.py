import sys
from fractions import Fraction


def lines_intersect(line1, line2):

    # Get the endpoints of the first line.
    x1, y1, x2, y2 = line1

    # Get the endpoints of the second line.
    x3, y3, x4, y4 = line2

    # Check whether either line is vertical.
    first_vertical = (x1 == x2)
    second_vertical = (x3 == x4)

    # Case 1: Both lines are vertical.
    if first_vertical and second_vertical:
        # Same x-coordinate means the lines overlap.
        return x1 == x3

    # Case 2: Exactly one line is vertical.
    if first_vertical or second_vertical:
        # A vertical line and a nonvertical line intersect.
        return True

    # Case 3: Neither line is vertical.
    # Calculate the slope and y-intercept of the first line.
    m1 = Fraction(y2 - y1, x2 - x1)
    b1 = Fraction(y1) - m1 * x1

    # Calculate the slope and y-intercept of the second line.
    m2 = Fraction(y4 - y3, x4 - x3)
    b2 = Fraction(y3) - m2 * x3

    # Different slopes mean the lines intersect.
    if m1 != m2:
        return True

    # Same slope and same intercept mean the lines overlap.
    if b1 == b2:
        return True

    # Same slope but different intercepts means
    # the lines are distinct and parallel.
    return False


def main():
    # Read the input.
    # The first value is the number of Ghostbusters.
    # Each following record has the form: B x y G x y.
    tokens = sys.stdin.read().split()

    if not tokens:
        return

    n = int(tokens[0])
    lines = []
    index = 1

    # Create and store one line for each fixed pair.
    for _ in range(n):
        bx = int(tokens[index + 1])
        by = int(tokens[index + 2])
        gx = int(tokens[index + 4])
        gy = int(tokens[index + 5])

        # Preserve the given Ghostbuster-Ghost pairing.
        lines.append((bx, by, gx, gy))

        # Move to the next input record.
        index += 6

    # Compare every distinct pair of lines.
    i = 0

    while i < n - 1:
        j = i + 1

        while j < n:
            # Check whether these two lines intersect or overlap.
            if lines_intersect(lines[i], lines[j]):
                print("All Ghosts: were not eliminated")
                return

            # Check the next line against the current line.
            j += 1

        # Move to the next first line.
        i += 1

    # No two lines intersect or overlap.
    print("All Ghosts: were eliminated")


if __name__ == "__main__":
    main()
