# Step 1: Define Function A.
# Generate all substrings starting at a fixed start position.
def extend_substrings(s, start, end, result):

    # Step 1.1: Base case.
    # Stop when end reaches the length of the string.
    if end >= len(s):
        return

    # Step 1.2: Generate and store the current substring.
    # Python slicing excludes the right boundary, so use end + 1.
    substring = s[start:end + 1]
    result.add(substring)

    # Step 1.3: Extend the substring by moving end one position right.
    # Keep start unchanged and recursively generate the next substring.
    extend_substrings(s, start, end + 1, result)


# Step 2: Define Function B.
# Move through all possible starting positions.
def generate_substrings(s, start, result):

    # Step 2.1: Base case.
    # Stop when all starting positions have been processed.
    if start >= len(s):
        return

    # Step 2.2: Call Function A.
    # Start with a substring containing only the current character.
    extend_substrings(s, start, start, result)

    # Step 2.3: Move to the next starting position.
    # Recursively process the remaining starting positions.
    generate_substrings(s, start + 1, result)


# Step 3: Read and prepare the input string.
def main():
    s = input().replace(" ", "")

    # Step 4: Initialize an empty set to store distinct substrings.
    result = set()

    # Step 5: Start the recursive process from index 0.
    generate_substrings(s, 0, result)

    # Step 6: Sort the distinct substrings alphabetically
    # and print each substring on a separate line.
    for substring in sorted(result):
        print(substring)

    # Step 7: Print the total number of distinct substrings.
    print(len(result))


if __name__ == "__main__":
    main()
