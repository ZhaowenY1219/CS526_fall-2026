import sys


def find_minimum_count(array, target):
    # Sort the array in descending order.
    sorted_array = sorted(array, reverse=True)

    total = 0
    count = 0

    # Add elements from largest to smallest.
    for number in sorted_array:
        total += number
        count += 1

        # Stop when the sum is strictly greater than the target.
        if total > target:
            return count

    # The problem guarantees that the total sum is greater than target.
    return count


def main():
    # Read all input values from the input file.
    data = sys.stdin.read().split()

    if not data:
        return

    # The first line contains the number of elements.
    n = int(data[0])

    # The second line contains the target value.
    target = int(data[1])

    # The remaining values form the original array.
    if len(data) != n + 2:
        raise ValueError("The number of input values does not match n.")

    array = list(map(int, data[2:]))

    # Find the minimum number of elements needed.
    answer = find_minimum_count(array, target)

    # Print the original array, target, and answer.
    array_string = ",".join(map(str, array))
    print(f"Input: {array_string} Target: {target} Answer: {answer}")


if __name__ == "__main__":
    main()
