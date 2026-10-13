import sys


def is_palindrome(s):
    
    left = 0
    right = len(s) - 1

    # Compare characters from both ends toward the middle.
    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    # All corresponding characters match.
    return True


def main():
    palindrome_count = 0

    # Read each line from the input file.
    for line in sys.stdin:
        # Remove surrounding whitespace and spaces between characters.
        s = line.strip().replace(" ", "")

        # Check whether the current string is a palindrome.
        result = is_palindrome(s)

        # Print True or False for the current string.
        print(result)

        # Count the palindromes.
        if result:
            palindrome_count += 1

    # Print the total number of palindromes.
    print(palindrome_count)


if __name__ == "__main__":
    main()
