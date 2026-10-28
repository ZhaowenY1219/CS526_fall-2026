
================================================================================
README.txt - Problem 1:Snow fall
================================================================================


--------------------------------------------------------------------------------
 Introduction 
--------------------------------------------------------------------------------

This question need us to determine whether any three consecutive days have a combined snowfall strictly greater than half of the total snowfall, given the cumulative snowfall totals for n days. 

My program reads the input, checks every possible group of three consecutive days using cumulative totals, and prints the input values followed by solution: YES or solution: NO. It outputs NO when fewer than three days are provided.

--------------------------------------------------------------------------------
 Algorithm
--------------------------------------------------------------------------------

Step 1: Read Input
--------------------------------------------------------------------------------

1. Read an n, representing the number of consecutive days of snowfall.

2. Read n cumulative snowfall amounts and store them in array A. 'A[i]' represents the cumulative snowfall from Day 1 through Day i. Therefore, 'A[1]' means the actual snowfall on the first day, while 'A[n]' represents the total snowfall over all n days.

3. For convenience in calculations, we define 'A[0] = 0', indicating that the cumulative snowfall before the start of Day 1 is 0.

Step 2: Check whether there are enough days
--------------------------------------------------------------------------------

1.Check whether the number of days meets the requirement: 'n < 3'

1.1 If the condition( n < 3 ) is true, it means the number of days recorded is less than 3, so it is not possible to form a consecutive three-day period. Set the final answer to 'NO'.

1.2 If n >= 3, this means there is at least one set of three consecutive days, so we need to proceed to next step.

Step 3: Calculate the total snowfall and half of that amount
--------------------------------------------------------------------------------

1. The total snowfall for all days is: 'total = A[n]'

2. Half of the total snowfall: 'half = total / 2'


Step 4: Iterate through all combinations of three consecutive days
--------------------------------------------------------------------------------

1. Use a loop to select the starting day of a three-day consecutive period

1.1 Let i represent the first day of the current three-day consecutive period: days i, i+1, and i+2.

1.2. After each check, if no qualifying combination is found, the loop continues; increment i by 1 and check the next three-day consecutive period.

2. Calculate the total snowfall for the current three consecutive days
   
                 three_day_snowfall = A[i+2]-A[i-1]


3. Compare the actual total snowfall over the past three days with half:

                   if three_day_snowfall > half:

3.1 If the condition is true, set the final answer to ‘YES’ and stop iterating through the remaining combinations.

3.2 If the condition is false, continue checking the next group.

3.3 If all groups have been checked and no combination meets the condition, the final answer is ‘NO’.


Step 5: Determine the final answer and output the result
--------------------------------------------------------------------------------

-------------------------------------------------------------------------------
Interesting aspects
--------------------------------------------------------------------------------

1. The program calculates snowfall over three consecutive days by subtracting cumulative totals: A[i+2] - A[i-1], with A[0] = 0.

2. A group qualifies only if its snowfall is greater than half of the total snowfall.

3. Once a qualifying group is found, the program stops checking. If no group qualifies, it outputs 'NO'.

--------------------------------------------------------------------------------
 How to run
--------------------------------------------------------------------------------

Run the program using input redirection:

python3 problem1.py < problem1Resources/snowfall_input1.txt
python3 problem1.py < problem1Resources/snowfall_input2.txt
python3 problem1.py < problem1Resources/snowfall_input3.txt
python3 problem1.py < problem1Resources/snowfall_input4.txt
python3 problem1.py < problem1Resources/snowfall_input5.txt

The results for all five test files are recorded in problem1Executions.txt and screenshots folder.
