================================================================================
README.md - Problem 3: Longest Alternating Increasing Squence
================================================================================


--------------------------------------------------------------------------------
 Introduction
--------------------------------------------------------------------------------

This problem is solved using dynamic programming. By creating two DP arrays, 'DP_A' and 'DP_B', which record the lengths of the longest valid alternating increasing sequences ending with elements from 'A' and 'B', and by gradually updating the states using recursive relationships, we can ultimately find the longest sequence that satisfies all conditions.

--------------------------------------------------------------------------------
 Algorithm
--------------------------------------------------------------------------------


step 1 Define the subproblems
--------------------------------------------------------------------------------

1. create 2 DP arrays, DP_A and DP_B, because the elements in the resulting squence must alternate between A and B:


    DP_A[i]: the length of the longest valid alternating increasing sequence ending at A[i]
    DP_B[j]: the length of the longest valid alternating increasing sequence ending at B[j]

step 2 Recurrence Relations
--------------------------------------------------------------------------------

1. the current element comes from A

When A[i] is the last element, then its previous element must comes from B,

and must meet the following conditions simultaneously:

       1. 'j < i' : Ensure that the original positions are in ascending order
       2. 'B[j] < A[i]' : Ensure that the values are in ascending order

      then  DP_A[i] = 1 + max DP_B[j]

             otherwise, DP_A[i] = 1

2. the current element comes from B

When B[j] is the last element, then its previous element must comes from A,

and must meet the following conditions simultaneously:

       1. i < j' : Ensure that the original positions are in ascending order
       2. 'A[i] < B[j]' : Ensure that the values are in ascending order

      then  DP_B[j] = 1 + max DP_A[i]

            otherwise, DP_B[j] = 1

step 3 set base case
--------------------------------------------------------------------------------

Since each individual element can form a sequence of length 1 on its own:

 DP_A[i] = 1
 DP_B[j] = 1


step 4 Pick an Order
--------------------------------------------------------------------------------

Since each status depends on elments with smaller original positions , we need to

process elements from left to right, according to their original positions:

At each position [i]:
 1. Calculate DP_A[i] by checking the DP_B arrays at the previous positions
 2. Calculate DP_B[j] by checking the DP_A arrays at the previous positions
 3. Check that both conditions(the original order of the positions and strictly increasing values)are met
 4. Add the current element to the longest valid prefix sequence and increment the sequence length by 1
 5. Continue processing the next location until all elements have be evaluated

step 5 Read the final answer
--------------------------------------------------------------------------------

The final answer is the maximum value in both DP arrays as the longest valid alternating increasing sequence can end at any element in either array

Therefore,

Answer = max(max(DP_A),max(DP_B))

--------------------------------------------------------------------------------
Interesting aspect
--------------------------------------------------------------------------------
1. Two DP Arrays: Create DP_A and DP_B to record the lengths of the longest valid sequences that can be formed when an element from either A or B is used as the last element. By distinguishing the source of the last element, we ensure that subsequent elements are selected alternately from A and B.

2. Recurrence Relations: When the current element comes from A, the previous element must come from B; when the current element comes from B, the previous element must come from A. Each time an element is connected.

3. Base Case: Initialize all elements in both DP arrays to 1, since each individual element can form a valid sequence of length 1.

--------------------------------------------------------------------------------
How to run
--------------------------------------------------------------------------------

python3 problem3.py 1 < Problem3Resource/longest_seq1.txt
python3 problem3.py 2 < Problem3Resource/longest_seq2.txt
python3 problem3.py 3 < Problem3Resource/longest_seq3.txt
python3 problem3.py 4 < Problem3Resource/longest_seq4.txt
python3 problem3.py 5 < Problem3Resource/longest_seq5.txt
python3 problem3.py 6 < Problem3Resource/longest_seq6.txt

The outputs from all three test runs are recorded in problem2Executions.txt and screenshots folder.
