

----------------------------------------------------------------------------------------------------------------------------------------
Introduction
----------------------------------------------------------------------------------------------------------------------------------------

This problem asks me to find the minimum number of elements from an array whose sum is strictly greater than a given target value T. 
My algorithm sorts the array in descending order and accumulates the largest elements first until their sum exceeds the target.

----------------------------------------------------------------------------------------------------------------------------------------
Algorithm
----------------------------------------------------------------------------------------------------------------------------------------

Step 1: Read the Input Data
----------------------------------------------------------------------------------------------------------------------------------------
Read the number of elements n, the target value T, and the entire array from the input file.

Step 2: Sort the array in descending order
----------------------------------------------------------------------------------------------------------------------------------------
Sort the array in descending order.
In this way, we can start adding from the largest element without having to find the current largest element each time.

Step 3: Initialize Variables
---------------------------------------------------------------------------------------------------------------------------------------
Set two variables:

1.'total = 0': Record the cumulative sum of the currently selected elements.

2.'count = 0': Record the number of elements currently used.

Step 4: Start summing from the largest element
---------------------------------------------------------------------------------------------------------------------------------------
Starting with the first element in the sorted array, perform the following steps in order:

1. Add the current element to 'total'
2. Increment 'count' by 1.
3. Check whether 'total' is greater than the target value T

If total is less than or equal to T, we need to continue adding the next element

If 'total' > T, we can immediately stop the loop and print the final answer



Step 5: Output the Results
----------------------------------------------------------------------------------------------------------------------------------------

After the loop stops, output the original input array, the target value T, and the minimum number of elements ('count')

----------------------------------------------------------------------------------------------------------------------------------------
intersting aspects
----------------------------------------------------------------------------------------------------------------------------------------

1.Use a greedy algorithm: Select the largest available element first to minimize the number of elements required.

2.These k largest elements have the maximum sum among any k elements, thereby ensuring that the algorithm finds the minimum number of elements.

3. Efficiency: Stop as soon as the sum exceeds the target.



----------------------------------------------------------------------------------------------------------------------------------------
how to run
----------------------------------------------------------------------------------------------------------------------------------------


python3 problem2.py < problem2Resources/fewest_1.txt

python3 problem2.py < problem2Resources/fewest_2.txt

python3 problem2.py < problem2Resources/fewest_3.txt

The outputs from all three test runs are recorded in problem2Executions.txt and screenshots folder.
