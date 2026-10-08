================================================================================
README.txt - Problem 3: Climbing Stairs
================================================================================



--------------------------------------------------------------------------------
1. Introduction ((what the homework asks and what your code does)
--------------------------------------------------------------------------------

This homework asks me to write a recursive function that calculates the number of ways to climb a staircase when I can take 1, 2, or 3 steps at a time. 
My function ways(n) returns the total number of valid ways to reach the top of a staircase with n steps.

--------------------------------------------------------------------------------
2. Algorithm
--------------------------------------------------------------------------------

Recursive ways(n)

#case 1: have reached the top of the stairs (n==0)
 ways(0)=1, because there is one way to reach the top when there are no steps left.

#case 2: the remaining steps are less than 0 (n<0)

ways(n)=0, because the number of steps has gone past the top, it is  impossible to reach the exact position.

#case 3: there are still steps to climb (n>0)

The first step can be:

* Take one step;
* Take two steps;
* Take three steps

the number of ways for the remaining steps:
* ways(n - 1) if the first move is 1 step;
* ways(n - 2) if the first move is 2 steps;
* ways(n - 3) if the first move is 3 steps.

Therefore, ways(n) = ways(n - 1) + ways(n - 2) + ways(n - 3).

Answer(a): 
My base cases are  n==0 and n<0. 

* n==0：ways(0)=1, Because when there are 0 steps left, we have successfully reached the top of the stairs, which can be considered a success.

* n<0:ways(n)=0，Because we have gone past the top of stairs, so there are no valid ways.


Answer(b): If we could only climb 1 or 2 steps at a time, ways(n) would produce the Fibonacci sequence(1,1,2,3,5,8,...) because ways(n) = ways(n - 1) + ways(n - 2).


--------------------------------------------------------------------------------
3. Interesting aspects
--------------------------------------------------------------------------------
The function has two base cases. 
When n == 0, it returns 1 because reaching the top is one successful way to finish. 
When n < 0, it returns 0 because the steps have gone past the top. 
These base cases stop the recursion and prevent it from continuing indefinitely.

--------------------------------------------------------------------------------
4. How to run
--------------------------------------------------------------------------------

From the Problem3 directory, run:

python3 problem3_driver.py


