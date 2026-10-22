================================================================================
README.txt - Problem 1: Whether each of a list of strings is a palindrome 
================================================================================

--------------------------------------------------------------------------------
##Introduction
--------------------------------------------------------------------------------

My program reads strings from an input file, one string per line. 
It removes spaces between characters before checking whether each string is a palindrome. 
The program prints True if a string is a palindrome and False otherwise. After processing all input strings, it prints the total number of palindromes.

--------------------------------------------------------------------------------
##Algorithm
--------------------------------------------------------------------------------

Step 1: Initialize the palindrome counter (palindrome_count = 0) to record the total number of palindromic strings in the input file


Step 2: Read all lines from the input file

2.1 Use 'sys.stdin.readlines()' to read all lines from standard input at once and save them to a list named 'lines'. After saving all input lines, use a for loop to process each line one by one until all lines in the list have been processed


Step 3: Remove spaces and prepare the current string

3.1 Use 'line.strip()' to remove leading and trailing whitespace characters from a string;

3.2 then use 'replace(" ", "")' to remove ordinary spaces used as separators between characters and preserve the original case of the characters.


Step 4: Call 'is_palindrome(s)' function to determine if a string is a palindrome

4.1 Initialize the left and right pointers

    * 'left=0', points to the first character of the string;

    * 'right=len(s)-1', points to the last character of the string because a string in Python indices start from 0, not 1, so the index of             the last character is the string length minus 1.

4.2 Use a while loop to compare characters from both ends

    * Use a 'while left < right' loop to determine whether further comparisons are needed:

    * If 'left < right', it means that the two pointers haven't met or crossed yet, so we need to continue the comparison，
         
    * that is, continue comparing the characters at the corresponding positions on the left and right.

     
4.3 Return False if the characters do not match

    * If 's[left] != s[right]', it means that the characters on the left and right ends are different, and the string is not a palindrome.          
    * Therefore, we directly return False, end the helper function, and stop comparing the remaining characters.

4.4 Move both pointers toward the middle if the characters match

    * If 's[left] == ​​s[right]', it means that the current pair of characters matches, and we can continue to move from both ends toward the middle and check the remaining parts

    At this point, the following actions are executed:

    1.'left=left+1', shifting it one position to the right, 

    2.'right=right-1', shifting it one position to the left,

    3. Then, returning to the 'while left < right' condition, the comparison of the new left and right characters continues.


4.5 Return True if all comparisons match & return False if comparisons do not match

    * The 'is_palindrome(s)' function returns True or False, and the main algorithm saves the result to the variable 'result'.


Step 5: Print the result and update the counter

5.1 Use 'print(result)' to output the result of the comparison of the current string

    * If result is True, the current string is a palindrome, so `palindrome_count` is incremented by 1.

    * If result is False, the current string is not a palindrome, and the counter is not incremented.


Step 6: Print the total number of palindromes

After all input lines have been processed, use 'print(palindrome_count)' to output the total number of palindromes

--------------------------------------------------------------------------------
##interesting aspect
--------------------------------------------------------------------------------

1.The is_palindrome() function uses two pointers, left and right, to compare characters from opposite ends of the string. The pointers move toward the middle after each successful comparison.

2.The program does not convert strings to uppercase or lowercase, so uppercase and lowercase letters are compared as they appear in the input.

--------------------------------------------------------------------------------
##how to run
--------------------------------------------------------------------------------

Save the Python source code as problem1.py

To run one test case：
python3 problem1.py < problem1Resources/palendrome_0.txt

The test execution results are saved in both problem1Executions.txt and screenshot folder in the main Problem1 folder.
