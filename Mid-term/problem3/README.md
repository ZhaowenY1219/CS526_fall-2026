================================================================================
README.txt - Problem 3
================================================================================

--------------------------------------------------------------------------------
 Introduction 
--------------------------------------------------------------------------------

This question ask us to determine whether an N × N puzzle board is valid. Every non-empty cell must contain an allowed symbol, and no symbol may appear more than once in any row, column, or sub-board.

My program reads the board size, allowed symbols, and board contents. The program checks for duplicate symbols in each row, each column, and each sub-board. For example, for a given row, it fixes the row index and, by iterating through the column index, compares each cell with the cell to its right; during the duplicate check, empty cells (.) are skipped. If an invalid symbol or a duplicate symbol is found, the program stops the relevant check and returns `False`. Only when both the input check and all three duplicate checks are passed is the board considered valid. 

--------------------------------------------------------------------------------
 Algorithm
--------------------------------------------------------------------------------

Step 1: Check the symbols on the board 
--------------------------------------------------------------------------------

1.The size of the board: n , and calculate the side length of each sub-board: 'size = √n'

2.Iterate through every position on the board, board[i][j], where [i] is the row index and [j] is the column index, both ranging from 0 to n-1.

3.If board[i][j] == ".", skip that position.

4. If the position is not empty and its symbol is not part of the set of allowed symbols, return 'False'.

5. If all non-blank cells contain valid characters, continues to Step 2 to check each line 


Step 2: Check each line for duplicate symbols
--------------------------------------------------------------------------------

1. Use the first loop to iterate through each row, setting the range of the row index ‘I’ to be from 0 to 'n-1'.

2. For the current row, keep the row index [i] fixed, and use a second loop to iterate through each position in the current row. Regard [j] as the position of the current symbol, (board[I][j]), and let the column index [j] range from 0 to n-1.

3.If board[i][j] == ".", skip the current position.

4. Use a third loop, starting at 'k = j + 1', to check each position board[i][k] following the current symbol, which means compare board[i][j] with board[i][j + 1], board[i][j + 2], and so on, up to board[i][n - 1].

5. If board[i][k] == ".", skip that position.

6. If board[i][j] == board[i][k] and neither of the two characters is '.', this indicates a duplicate character, and the function should immediately return 'False'.

7. If all rows have been checked and no duplicate non-empty symbols were found, the row check is considered successful. Proceed to Step 3 to check each column.


Step 3: Check each column for duplicate symbols
--------------------------------------------------------------------------------

1. Use the first loop to iterate through each column, where [j] represents the index of the current column, and let the range of column index [j] be from 0 to n-1.

2. For the current column, keep [j] constant, and use the second loop to iterate through each position in the current column, starting from the first row and moving downward. Use [i] to denote the index of the current row. The current symbol is board[i][j], where the row index i ranges from 0 to n-1.

3. If board[i][j] == ".", skip the current position.

4. In the third loop, starting at 'k = i + 1', check each position below the current symbol in sequence until the last row. In other words, compare board[i][j] with board[i + 1][j], board[i + 2][j], and so on, up to board[n - 1][j].

5. If board[k][j] == ".", skip that position.

6. If board[i][j] == board[k][j] and neither of the two characters is '.', this indicates that duplicate characters have appeared in the same column, return 'False'

7.If all columns have been checked and no duplicate non-empty symbols were found, the column check is successful. Proceed to Step 4 to check each sub-board.


Step 4: Check each sub-board for duplicate symbols
--------------------------------------------------------------------------------

1. Iterate through all the sub-boards

Use two nested loops:

1.1 The first loop selects the starting row (startRow) for each sub-board, with values from the range (0, n, size);

1.2 The second loop selects the starting column (startCol) for each sub-board, with values from the range (0, n, size).


2. Determine the range of the current sub-board

The row index range of the current sub-board is: range(startRow, startRow + size)

The column index range is: range(startCol, startCol + size)


3. Select the current cell and use two nested loops to iterate through every cell board[i][j] in the current sub-board

Within the current sub-board, use two nested loops:

3.1 The third loop iterates through all rows in the current sub-board.

3.2 The fourth loop iterates over all columns in the current sub-board.

The ranges are:

range(startRow, startRow + size)

range(startCol, startCol + size)


4. If board[i][j] == ".", skip the current position


5. Find the candidate 'board[k][l]' for comparison

Use two additional nested loops:

5.1 The fifth loop iterates over all rows in the current sub-board.

5.2 The sixth loop iterates over all columns in the current sub-board.

The ranges are:

range(startRow, startRow + size)

range(startCol, startCol + size)


6. To avoid duplicate comparisons:

 k > i, or
 k == i and l > j

If the candidate cell comes before the current position, or is the current position itself, skip it.


7. If board[k][l] == ".", skip the candidate cell.


8. If board[i][j] == board[k][l], return 'False'.


9. If no duplicate symbols are found in any of the sub-boards, return 'True'.


--------------------------------------------------------------------------------
Interesting aspects
--------------------------------------------------------------------------------


1. For each row, the row index stays fixed while the column indices change. For each column, the column index stays fixed while the row indices change.

2. Within each row, column, or sub-board, each non-empty cell is compared with the cells that follow it. This detects duplicate symbols without checking the same pair twice.

3. The program uses the starting row and column indices to identify each sub-board and compares cells only within that sub-board.

4. Empty Cells and Early Termination: Empty cells (.) are skipped. When an invalid symbol or duplicate is found, the relevant function immediately returns 'False'.


--------------------------------------------------------------------------------
How to run
--------------------------------------------------------------------------------
Run the program using input redirection:

python3 problem3.py < problem3Resources/puzzle_game_input1.txt
python3 problem3.py < problem3Resources/puzzle_game_input2.txt
python3 problem3.py < problem3Resources/puzzle_game_input3.txt
python3 problem3.py < problem3Resources/puzzle_game_input4.txt

The execution results for all four test input files are recorded in problem3Executions.txt and screenshots folder.
