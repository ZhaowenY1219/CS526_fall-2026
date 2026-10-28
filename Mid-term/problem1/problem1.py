import sys


def main():
    # Step 1: Read the number of days and cumulative snowfall totals.
    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])
    cumulative_values = list(map(int, data[1:1 + n]))

    # A[0] = 0 represents the cumulative snowfall before Day 1.
    A = [0] + cumulative_values

    # Step 2: Check whether there are enough days.
    answer = "NO"

    if n >= 3:

        # Step 3: Calculate the total snowfall and half of the total.
        total = A[n]
        half = total / 2

        # Step 4: Check every group of three consecutive days.
        for i in range(1, n - 1):
            three_day_snowfall = A[i + 2] - A[i - 1]

            if three_day_snowfall > half:
                answer = "YES"
                break

    # Step 5: Print the input values and the final answer.
    print(
        " ".join(map(str, cumulative_values))
        + f" solution: {answer}"
    )


if __name__ == "__main__":
    main()
