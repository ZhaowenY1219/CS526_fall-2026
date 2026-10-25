================================================================================
README.md - Problem 3
================================================================================


--------------------------------------------------------------------------------
Introduction 
--------------------------------------------------------------------------------

This problem asks me to count the unique right triangles that can be formed by choosing three points from a given set of 2D coordinates. 
The algorithm uses slope calculations and counting tables to improve efficiency.


--------------------------------------------------------------------------------
 Algorithm
--------------------------------------------------------------------------------


step 1 Read the number of points and their coordinates
--------------------------------------------------------------------------------
 1.Read the number of points n, then save all coordinates into a list.

step 2 Let A be a fixed right-angle vertex
--------------------------------------------------------------------------------
 1.Use a loop to treat each coordinate point in turn as a possible right-angle vertex A = (x_A, y_A), and all other points as B = (x_B, y_B).
   Once we've found a potential fixed right-angle vertex A, we simply need to find the other two points, B and C, such that the sides AB and AC are perpendicular to each other. 
   This avoids having to check every possible combination of the three points.

step 3 Initialize the vertex count table
--------------------------------------------------------------------------------
Whenever a vertex A is updated, the following three variables must be initialized:

1.horizontal_count: Counts the number of other points on the horizontal line
2.vertical_count: Counts the number of other points on the vertical line
3.slope_count: Stores the general slope and the corresponding number of points

step 4 Calculate and count the number of slopes formed by vertex A and other points
--------------------------------------------------------------------------------

Let the other points be B = (x_B, y_B) and vertex A = (x_A, y_A). Then,

 m = dy/dx = (yB - y_A)/(x_B - x_A)


Case 1: Vertical Line

If the slope is undefined(dx = 0),it means that vertices A and B lie on the same vertical line. 

Therefore, count the number of coordinate points on the vertical line separately, incrementing the count by 1 each time such a point is encountered:

'vertical_count += 1'


Case 2: Horizontal Line

If m = 0, that is, when dy = 0 and dx != 0, this means that both points lie on a horizontal line, therefore,'horizontal_count += 1'


Case 3: Non-vertical & non-horizontal line

Calculate m = dy/dx = (y_b - y_a) / (x_b - x_a)

Then count the number of coordinate points for each slope
(Note: Save the results for all slopes above as fractions to avoid errors caused by floating-point numbers affecting the determination of right angles)

step 5 Calculating the Number of Right Triangles
--------------------------------------------------------------------------------

Case 1: Calculating the Number of Combinations of Horizontal and Vertical Lines

In mathematics, a vertical line and a horizontal line are always perpendicular to each other. 

Therefore, when point A is the vertex of the right angle, the number of right triangles that can be formed is:

Number of right triangles = (Number of points on horizontal lines) * (Number of points on vertical lines)


Case 2: Calculating Right-Angle Triangle Combinations for Ordinary Lines

1. Calculating the Negative Reciprocal of the Slope

It is known that for two lines to be perpendicular, the following condition must be satisfied: m_1 * m_2 = -1

Therefore,

m_2 = -1/m_1

2. Count the number of coordinate points for each negative reciprocal , and cache them in the slope_count table

3. Multiply the counts of the two slope groups (slope m and the negative reciprocal of slope m) to obtain the number of right triangles formed by selecting one point from each group.

   3.1 Since each pair of vertical slope values is calculated twice (once for each order), dividing the sum of the ordinary slopes by 2 yields the correct number of right triangles formed by the ordinary slopes.

       Number of right triangles = ( (the counts of slope m ) * (the counts of the negative reciprocal of slope m) ) / 2
                                 = (count_slope_m  *  count_slope_(-1/m)) / 2


step 6 Sum the total number of right triangles
--------------------------------------------------------------------------------

Total number of right triangles = (Number of points on horizontal lines) * (Number of points on vertical lines) + ( (the counts of slope m ) * (the counts of the negative reciprocal of slope m) ) / 2

Finally, return the total count


--------------------------------------------------------------------------------
Interesting aspects
--------------------------------------------------------------------------------

1.Fixed Vertex: Treat each point as a potential right-angle vertex and examine the slopes to the other points.

2.Slope Grouping: Store the number of points for each slope and use the negative reciprocal rule to identify perpendicular lines.

3. Special Cases: Handle horizontal and vertical lines separately because as the standard slope formula cannot be used for this calculation.

4. Efficiency: Reuse stored slope counts to avoid checking every combination of three points.

--------------------------------------------------------------------------------
how to run
--------------------------------------------------------------------------------
