import sys


def longest_alternating_sequence(A, B):

    # Step 1: Create two DP arrays
    # Each individual element can form a sequence of length 1
    dp_a = [1] * len(A)
    dp_b = [1] * len(B)

    # Step 4: Process elements from left to right
    for pos in range(max(len(A), len(B))):

        # Case 1: The current element comes from A
        if pos < len(A):

            for j in range(min(pos, len(B))):

                # Check original position and increasing value
                if B[j] < A[pos]:
                    dp_a[pos] = max(dp_a[pos], dp_b[j] + 1)

        # Case 2: The current element comes from B
        if pos < len(B):

            for i in range(min(pos, len(A))):

                # Check original position and increasing value
                if A[i] < B[pos]:
                    dp_b[pos] = max(dp_b[pos], dp_a[i] + 1)

    # Step 5: Calculate the final answer
    answer = max(dp_a + dp_b, default=0)

    return answer


def main():

    # Read input data
    data = sys.stdin.read().split()

    if not data:
        return

    # Read the sizes of arrays A and B
    m = int(data[0])
    n = int(data[1])

    # Read the two arrays
    A = list(map(int, data[2:2 + m]))
    B = list(map(int, data[2 + m:2 + m + n]))

    # Check the input format
    if len(data) != 2 + m + n:
        raise ValueError("Invalid input data.")

    # Get the input file number
    if len(sys.argv) != 2:
        raise SystemExit(
            "Usage: python3 problem3.py <file_number> < input_file"
        )

    file_number = sys.argv[1]

    # Calculate the longest sequence
    answer = longest_alternating_sequence(A, B)

    # Print the required output
    print(f"File Input: longest_seq{file_number}.txt")
    print(f"Longest Sequence: {answer}")


if __name__ == "__main__":
    main()
