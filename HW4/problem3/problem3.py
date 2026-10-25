import sys
from fractions import Fraction


def count_right_triangles(points: list[tuple[int, int]]) -> int:

    n = len(points)
    total_count = 0

    # Fix each point as a possible right-angle vertex A.
    for i, (xa, ya) in enumerate(points):
        horizontal_count = 0
        vertical_count = 0
        slope_count: dict[Fraction, int] = {}

        # Count the directions from A to every other point.
        for j, (xb, yb) in enumerate(points):
            if i == j:
                continue

            dx = xb - xa
            dy = yb - ya

            # Case 1: Vertical line. Its slope is undefined.
            if dx == 0:
                vertical_count += 1

            # Case 2: Horizontal line. Its slope is zero.
            elif dy == 0:
                horizontal_count += 1

            # Case 3: Ordinary nonzero, finite slope.
            else:
                slope = Fraction(dy, dx)
                slope_count[slope] = slope_count.get(slope, 0) + 1

        # Count horizontal-vertical combinations.
        count_at_a = horizontal_count * vertical_count

        # Count ordinary perpendicular slope groups.
        ordinary_sum = 0

        for slope, count in slope_count.items():
            perpendicular_slope = -Fraction(1, 1) / slope

            perpendicular_count = slope_count.get(
                perpendicular_slope, 0
            )

            ordinary_sum += count * perpendicular_count

        # Each ordinary perpendicular pair was counted twice.
        count_at_a += ordinary_sum // 2

        # Add triangles whose right-angle vertex is A.
        total_count += count_at_a

    return total_count


def main() -> None:
    """Read input and print the number of right triangles."""

    tokens = sys.stdin.read().split()

    if not tokens:
        return

    n = int(tokens[0])

    if n < 0:
        raise ValueError("The number of points cannot be negative.")

    if len(tokens) != 1 + 2 * n:
        raise ValueError(
            f"Expected {n} coordinate pairs, "
            f"but received an incorrect number of integers."
        )

    values = list(map(int, tokens[1:]))

    points = [
        (values[k], values[k + 1])
        for k in range(0, len(values), 2)
    ]

    print(count_right_triangles(points))


if __name__ == "__main__":
    main()
