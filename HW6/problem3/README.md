================================================================================
README.md - Problem 3
================================================================================


--------------------------------------------------------------------------------
  Introduction 
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
  Algorithm
--------------------------------------------------------------------------------

step 1: Initialize two heaps
--------------------------------------------------------------------------------
Create two heaps:
1. lower_heap: a Max-Heap that stores the smaller half of the sales amounts. its root contains the largest value in the lower half.
2. upper_heap: a Min- Heap that stores the larger half of the sales amounts. its root contains the smallest value in the upper half.

The two heaps must maintain the following conditions:
1. every value in lower_heap must be less than or equal to every value in upper_heap
2. the number of  values in the two heaps must be euqal , or lower-heap may contain exactly one more value than upper_heap

step 2: read the input and initialize the result list
--------------------------------------------------------------------------------
1. read the sales amounts from standard input as a single list, preserving their original order
2. initialize an empty lower_heap and an empty upper - heap
3. initialize an empty list called running_medians to store the median after each new sale
4. if the input list is empty, print an empty list and stop the  program

step 3: insert each sale into the appropriate Heap
--------------------------------------------------------------------------------
process each sale in its original input order
1. if lower_heap is empty, or the new sale is less than or euqal to the root value of the lower_heap, insert it into lower_heap
2. otherwise, insert the new sale into the upper_heap

the root of the Max - Heap represents the largest value in the lower half, while the root of the Min - Heap represents the smallest value in the upper half. therefore, when comparing the new sale with the root of the lower_heap could determines which half should receive it.

step 4: rebalance the two heaps
--------------------------------------------------------------------------------
after inserting a new sale, check the number of values in both heaps
1. if lower_heap contains more than one additional value compared with upper_heap, remove the maxinmum value from lower_heao and insert it into upper_heap
2. if upper_heap contains more values than lower_heap, remove the minimum value from upper_heap and insert it into lower_heap
3. continue until the two heaps contain the same number of values, or lower_heap contains exactly one more value

step 5: calculate the current median
--------------------------------------------------------------------------------
1. if both heaps contain the same number of values, the total number of sale is even, than calculate the average of the two root values
2. if lower_heap contains one more value than upper_heap, the total number of sale is odd, the median is the root of the lower_heap
Since the roots contain the two middle values when the total number of sale is even, and the middle value when it ids odd, the median can be obtained without sorting the data

step 6: store and print the medians
--------------------------------------------------------------------------------
1. append the current median to 'running_medians'
2. continue processing the remaining sales, repeating Step3-5 after each new sale
3. after all sale have been processed, print the complete 'running_median' list


--------------------------------------------------------------------------------
 Interesting aspects
--------------------------------------------------------------------------------



--------------------------------------------------------------------------------
 How to run
--------------------------------------------------------------------------------




