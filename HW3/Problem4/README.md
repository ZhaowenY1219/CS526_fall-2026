================================================================================
README.txt - Problem 4: Ghostbuster & Ghost
================================================================================


--------------------------------------------------------------------------------
##Introduction
--------------------------------------------------------------------------------

My program reads the number of Ghostbusters and the coordinates of each Ghostbuster and its assigned ghost. Each pair of coordinates defines an infinite line representing a proton stream. 

The given pairings must remain unchanged.

The program compares every distinct pair of lines and determines whether they intersect or overlap. 

If any pair intersects or overlaps, it prints All Ghosts: were not eliminated. 

If no two lines intersect or overlap, it prints All Ghosts: were eliminated.


--------------------------------------------------------------------------------
##Algorithm 
--------------------------------------------------------------------------------

Step1:
--------------------------------------------------------------------------------
Read the input and save the coordinates of each Ghostbuster and its corresponding Ghost

Step 2:
--------------------------------------------------------------------------------
use the coordinates of Ghostbuster as the first endpoint and the coordinates of the corresponding Ghost as the second endpoint, thereby determining a straight line.

Repeat the above process until all (n) pairs of coordinates have been processed and all lines have been determined and saved


Step 3: use two nested while loops to check each pair of distinct lines to determine if any two lines intersect or overlap:
--------------------------------------------------------------------------------

3.1 Initialize the outer loop. Set the outer loop index i to 0. Whenever i < n - 1, select the i-th line as the first line to compare.


3.2 Initialize the inner loop. Each time the inner loop is entered, set the inner loop index j to i + 1. Whenever j < n, compare the i-th line with the j-th line.


3.3 Call a helper function to determine if the two lines intersect or coincide:

 
  (1) Determine whether two lines are vertical lines:

** For the first line, check if the x-coordinates of its two endpoints are the same. If x_1 = x_2, then the first line is a vertical line

** For the second line, check if the x-coordinates of its two endpoints are the same. If x_3 = x_4, then the second line is a vertical line

**If only one line is vertical, return True, because a vertical line must intersect an infinitely extending non-vertical line

**If both lines are vertical, compare their x-coordinates. If x_1 = x_3, the two lines coincide, return True; if x_1 is not equal to x_3, the two lines are distinct parallel lines, return False

  
  (2) If neither of the two lines is a vertical line, then calculate their slope and y-intercept

      ** Calculate the slopes of the two lines respectively:
   
          m_1=(y2-y1)/(x2-x1)

          m_2=(y4-y3)/(x4-x3)

     ** Calculate the y-intercepts of the two lines respectively:

          b_1=y1-m1*x1

          b_2=y3-m2*x3


  (3) Compare the slope and y-intercept of two lines:

- If the two lines have different slopes (m_1 != m_2), return True, because two infinitely extending lines with different slopes must intersect

- If the two lines have the same slope (m_1 = m_2), then continue comparing their y-intercepts

- If the two lines also have the same y-intercept (b_1 = b_2), then the two lines coincide, and return True

- If the two lines have different y-intercepts (b_1 != b_2), then the two lines are distinct parallel lines, and return False



4. Use an 'if' statement to check the return value of the helper function.

- If the helper function returns 'True', it means that at least one pair of lines intersects or coincides. Immediately output "All Ghosts: were not eliminated" and terminate the main algorithm, no longer checking other line pairs

- If the helper function returns 'False', it means that the current pair of lines does not intersect or coincide. In this case, increment 'j' by 1 and continue checking the current line with the next line that has not yet been compared



5. Continue the outer loop

When the inner loop ends and no intersection or overlap is found between the current line and other lines, increment i by 1 and select the next line as the first line for comparison. Then reset j to i + 1 and continue checking subsequent lines using the inner loop.

When all distinct line pairs have been checked and no pair intersects or overlaps, both loops end

Step 4: Output the final result
--------------------------------------------------------------------------------

If the helper function returns True during the check, the main algorithm will output: "All Ghosts: were not eliminated";

Instead, the output is: “All Ghosts were eliminated”.


--------------------------------------------------------------------------------
##Interesting aspects
--------------------------------------------------------------------------------

For nonvertical lines, this program calculates their slopes and y-intercepts. Different slopes mean the lines intersect, while equal slopes require comparing the y-intercepts to determine whether the lines overlap or are distinct parallel lines.

A vertical line cannot be represented using the usual slope-intercept formula because its slope calculation requires division by zero. The program checks vertical lines separately and determines whether they overlap or are distinct parallel lines.


--------------------------------------------------------------------------------
##How to run 
--------------------------------------------------------------------------------

Save the Python source code as problem4.py

Run one test：

python3 problem4.py < problem4Resources/ghostbusters_input_0.txt

The test execution results are saved in both problem4Executions.txt and screenshot folder in the main Problem1 folder.
