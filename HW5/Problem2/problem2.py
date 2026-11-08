import sys


def vowel_combinations(morse_code):
    n = len(morse_code)

    # Step 1: Create a state table with 3 rows and n columns
    # Row 0: 1 symbol (E)
    # Row 1: 2 symbols (A, I)
    # Row 2: 3 symbols (O, U)
    table = [[0] * n for _ in range(3)]

    # Step 2, 3 and 4: Process each offset from left to right
    for offset in range(n):

        # Step 2: Base case
        if offset == 0:
            p = 1

        # Step 3: Calculate P(offset)
        else:
            p = 0

            if offset - 1 >= 0:
                p += table[0][offset - 1]

            if offset - 2 >= 0:
                p += table[1][offset - 2]

            if offset - 3 >= 0:
                p += table[2][offset - 3]

        # Step 4: Check the next 1 symbol
        if morse_code[offset:offset + 1] == ".":
            table[0][offset] = p

        # Check the next 2 symbols
        if morse_code[offset:offset + 2] == ".-" or \
           morse_code[offset:offset + 2] == "..":
            table[1][offset] = p

        # Check the next 3 symbols
        if morse_code[offset:offset + 3] == "---" or \
           morse_code[offset:offset + 3] == "..-":
            table[2][offset] = p

    # Step 5: Calculate the final answer P(n)
    answer = 0

    if n >= 1:
        answer += table[0][n - 1]

    if n >= 2:
        answer += table[1][n - 2]

    if n >= 3:
        answer += table[2][n - 3]

    return answer


def main():

    # Read the input file
    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])
    morse_code = data[1] if len(data) > 1 else ""

    if len(morse_code) != n:
        raise ValueError("The input length does not match n.")

    # Get the input file number from the command line
    if len(sys.argv) != 2:
        raise SystemExit(
            "Usage: python3 morseVowel.py <file_number> < input_file"
        )

    file_number = sys.argv[1]

    # Calculate the number of vowel combinations
    answer = vowel_combinations(morse_code)

    # Print the required output
    print(f"File Input: vowel_input{file_number}.txt")
    print(f"The Number of Vowel combinations is: {answer}")


if __name__ == "__main__":
    main()
