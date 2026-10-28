================================================================================
README.txt - Problem 2:Pandemic
================================================================================


--------------------------------------------------------------------------------
  Introduction 
--------------------------------------------------------------------------------

The program reads the board size and the coordinates of initially infected counties from standard input. Each day, a healthy county becomes infected if it has at least two infected neighbors directly above, below, to the left, or to the right. Diagonal counties are not considered neighbors.

The simulation continues until no new counties become infected. The program then checks the final board and prints whether any healthy counties remain.

--------------------------------------------------------------------------------
  Algorithm
--------------------------------------------------------------------------------

Step 1: Initialize the board
--------------------------------------------------------------------------------

1. Read the value of N from the input, which represents the size of the board. The board has N rows and N columns, for a total of N * N cells.

2. Create an N × N two-dimensional grid called 'board' and initialize all cells as '.'which represents a healthy county, and 'X' represents an infected county.

3. Each coordinate consists of a row and a column(row, column), representing the row index and column index respectively. 

4.For each set of initial infection coordinates, set the corresponding cell to X: board[row][column] = “X”


Step 2: Check for and count infected neighbors
--------------------------------------------------------------------------------

1. Use two nested for loops:

1.1 First loop: Iterate through the rows, letting 'row' range from 0 to N-1 and move to the right

1.2 Second loop: Iterate through the columns, for the currently selected row, let 'column' range from 0 to N-1 and move down


2. Check the status of the current cell

2.1 If board[row][column] == “X”, it means the current county is already infected, skip this cell and move on to the next one.

2.2 If board[row][column] == “.”, it means the current county is still healthy, continue checking its neighbors.


3. Create a counter variable: ‘infected_neighbors = 0’

This variable is used to track the number of infected neighboring counties surrounding the current county. 

Each time a healthy county begins its inspection, this variable is reset to 0.

4. Check the cell above the current cell: board[row - 1][column]

4.1 The valid range for the row index is 0 to N-1, so only when row > 0 can the existence of an upper neighbor be verified, and only then can we proceed to determine whether that neighbor is infected.

4.2 If board[row - 1][column] == “X”, then ‘infected_neighbors += 1’.

5. Check the neighbor below the current cell: board[row + 1][column]

5.1 Because valid range for the row index is 0 to N-1, so only when row < N - 1 can the existence of a lower neighbor be verified, and only then can we proceed to determine whether that neighbor is infected.

5.2 If board[row + 1][column] == “X”, then ‘infected_neighbors += 1’.


6. Check the neighbor on the left: board[row][column - 1]

6.1 Because valid range for the row index is 0 to N-1, so only when column > 0 can the existence of a left neighbor be verified, and only then can we proceed to determine whether that neighbor is infected.

6.2 If board[row][column - 1] == “X”, then ‘infected_neighbors += 1’.

7. Check the neighbor on the right: board[row][column + 1]

7.1 Because valid range for the row index is 0 to N-1, so only when column < N - 1 can the existence of a right neighbor be verified, and only then can we proceed to determine whether that neighbor is infected.

7.2 If board[row][column + 1] == “X”, then ‘infected_neighbors += 1’.


Step 3: Record all counties with new infections on that day
--------------------------------------------------------------------------------

1. First,create an empty list to track the number of infected neighbors later: ‘new_infections = []’


2. Check the value of `infected_neighbors`

2.1 If `infected_neighbors` >= 2, the infection condition is met, and the coordinates of the current cell are added to the list;

2.2 If infected_neighbors < 2, do not add that coordinate


Step 4: Update the game board uniformly
--------------------------------------------------------------------------------

After checking all counties for the day, make the following determination:

Case A: There are no new infected counties for the day (new_infections is an empty list), execute a break and exit the loop.

Case B: There is one or more new infected counties for the day (new_infections is not empty), update the entire board by changing all cells corresponding to the coordinates of the new infections recorded that day to X.

Step 5: Check the final board and output the result
--------------------------------------------------------------------------------

1. After Step 4 exits the loop using a `break`, use two nested loops to traverse each cell on the final board again.

2. If 'board[row][column] == “.”' is found, it means there are still healthy counties, then output “There are healthy counties left” and end the traversal.

3. If no “.” is found after traversing the entire board, it means all counties are infected, then output: “There are no healthy counties left”

--------------------------------------------------------------------------------
  Interesting aspects
--------------------------------------------------------------------------------

1. Nested Loops and Boundary Checks: Nested for loops scan the board and check the four possible neighbors. Boundary checks prevent accessing positions outside the board.

2. Simultaneous Updates: New infections are recorded in ‘new_infections’ and applied to the board only after the entire board has been checked, ensuring that new infections do not spread again on the same day.

3. Termination and Final Check: A while loop continues the simulation until ‘new_infections’ is empty. The program then checks the final board and prints whether healthy counties remain.

--------------------------------------------------------------------------------
  How to run
--------------------------------------------------------------------------------

Run the program using input redirection:

python3 problem2.py < problem2Resources/pandemic_input1.txt

python3 problem2.py < problem2Resources/pandemic_input2.txt

The execution results for both test input files are recorded in problem2Executions.txt and screenshots folder.

