================================================================================
README.txt - Problem 2: Unique substring
================================================================================

##introduction

My program reads one string from the input file and uses two recursive functions to generate all consecutive substrings. 

The first recursive function keeps the starting position fixed and extends the ending position to generate longer substrings.

The second recursive function moves the starting position forward to process the rest of the string.

The program stores the substrings in a set to remove duplicates, then sorts them alphabetically and prints each unique substring on a separate line. Finally, it prints the total number of unique substrings.


##Algorithm 

I. Initialization Result Set

Create an empty set 'result = set()' to store all the distinct substrings


II. Recursive function A: Expands the current substring

1. Determine when to stop the recursion

If end >= len(s), it means there are no more characters to add to the substring (because the index of the last character of the string is len(s) - 1), so stop the recursion and return.

2. If the stopping condition is not met, generate the slice 's[start:end + 1]' (because the right boundary of the slice is not included in the result, the index of the right boundary is 'end + 1'), and add the substring to the result collection.

3. Increment end by 1, recursively call function A, and continue to expand the substring corresponding to the current starting position.



III. Recursive function B: Moves to the starting position

1. Determine when to stop recursion

If 'start >= len(s)', it means that all valid starting positions have been processed, and function B stops recursing.

2. call function A if the start index < len(s), and use the current start as both the initial start index and end index, so that function A can find all substrings starting from the current position and save the substrings

3. increment the start index by 1 after function A completes, and then call the recursive function B to continue processing the next starting position.

4. Repeat the above process until all valid starting positions have been processed.


IV. Sort and output the results

1. Use 'sorted(result)' to sort the elements in the collection alphabetically.

2. Use a for loop to iterate through the sorted list, printing one substring at a time, with each substring on a separate line.

3. Use 'len(result)' to count the number of distinct substrings in the collection and print this total.


##Interesting aspects

1.This program uses two recursive functions. 'extend_substrings()' generates substrings by keeping the starting index fixed and increasing the ending index. 'generate_substrings()' moves the starting index forward to process every possible starting position

2.This program uses a set to store substrings, so repeated substrings are stored only once

3.This program uses 'sorted()' to arrange the unique substrings alphabetically before printing them


##How to run

Save the Python source code as problem2.py

python3 problem2.py < problem2Resources/unique_substrings_input_0.txt

python3 problem2.py < problem2Resources/unique_substrings_input_1.txt

python3 problem2.py < problem2Resources/unique_substrings_input_2.txt

The test execution results are saved in both problem2Executions.txt and screenshot folder in the main Problem1 folder.

