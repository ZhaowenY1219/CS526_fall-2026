================================================================================
README.txt - Problem 4: Sorted Doubly Linked List Class
================================================================================


--------------------------------------------------------------------------------
1. Introduction ((what the homework asks and what your code does)
--------------------------------------------------------------------------------

This homework asks me to create a Node class and a SortedDoublyLinkedList class. 
The list stores values in ascending order, and each node has both prev and next pointers. 
My code supports adding and deleting nodes, searching for values, counting values,
calculating the total, finding the sum of the middle three values, and finding the median.

--------------------------------------------------------------------------------
2.Algorithm
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2.1 Define Node Class (Node Definition)
--------------------------------------------------------------------------------

class Node:
    # A node of a doubly linked list needs to know its own value, the previous node, and the next node. 
   
1.store a given value in the node 
2.set the next of node to None
3.set the prev of node to None
3.Initialize the node, so the newly created isolated node has no connections before and after
    


--------------------------------------------------------------------------------
2.2 Define SortedDoublyLinkedList Class (Initialization and Length)
--------------------------------------------------------------------------------

class SortedDoublyLinkedList:
Purpose: Initialize an empty linked list.

1. Set head to None because the list is initially empty
2. Set tail to None because there is no node in the list
3.set the node count to 0     


 __len__(self):
Return the count of the number of nodes stored in the list


--------------------------------------------------------------------------------
2.3 Create (Add Operations)
--------------------------------------------------------------------------------

add(value) 


# Case 1: Add to the head of the current list (The new value is smaller than all values)


Before: head <==> [A] <==> [B] <==> tail
 After: head <==> [N] <==> [A] <==> [B] <==> tail

1.The next of new node [N] points to node [A], [N].next ----> [A]

2.The prev of node [A] points to the new node [N], [A].prev ----> [N]

3.Let head change from pointing to [A] to pointing to [N], head <==> [N]

4.Increase the list length by 1


# Case 2: Add to the tail of the current list (The new value is greater than all values)

Before: head <==> [A] <==> [B] <==> tail
 After: head <==> [A] <==> [B] <==> [N] <==> tail

1.The prev of new node [N] points to node [B], [N].prev ---->[B]

2.The next of node [B] points to the new node [N], [B].next ----> [N]

3.Because the new node has become the last node of the linked list, let tail change from pointing to [B] to pointing to [N], [N] <==> tail

4.Increase the list length by 1


# Case 3: Insert in the middle

Before: head <==> [A] <==> [B] <==> tail
 After: head <==> [A] <==> [N] <==> [B] <==> tail


1.Start from the head and traverse the list to find the correct position for the new node [N]

2.Stop when the current node’s value is greater than or equal to the value of [N]

3.Let the prev of new node [N] point to the original first node [A], [N].prev ----> [A]

4.Let the next of new node [N] point to the original second node [B], [N].next ----> [B]

5.Let the next of the original first node [A] point to the new node [N], [A].next ----> [N]

6.Let the prev of the original second node [B] point to the new node [N], [B].prev ----> [N]

7.Increase the list length by 1


# Case 4:Add to an empty list

The original list is empty: head -> None, tail -> None ,length is 0

add node [N] into it.

Becomes:  head <==> [N] <==> tail 


1.Create node [N]

2.Let both head and tail point to node [N].head ---> [N] and tail ----> [N]

3.Increase the list length by 1

--------------------------------------------------------------------------------
2.4 Delete a Node (Removal Operations)
--------------------------------------------------------------------------------

List: head <==> [A] <==> [B]<==>[C]<==> tail

Start from the head:

1. Compare the current node's value with the target value

2. If the current value is smaller than the target, move to the next node

3. If the current value equals the target, delete this node

4. If the current value is greater than the target, stop because the target cannot appear later

5. If the value is not found, leave the list unchanged


#Case 1: Delete a head node 

Before:head <==> [A] <==> [B]<==>[C]<==> tail

 After:head <==> [B]<==> [C]<==>tail

1. Set head to the next node, [B]

2. Set [B].prev = None to disconnect [B] from the old head node

3. Decrease the list length by 1



#Case 2: Delete the tail node

Before:head <==> [A] <==> [B]<==>[C]<==> tail

After: head <==> [A]<==> [B]<==> tail


1. Set tail to the previous node, [B]

2. Set [B].next = None to disconnect [B] from the old tail node

3. Decrease the list length by 1



#Case 3: Delete a middle node

Before:head <==> [A] <==> [B]<==>[C]<==> tail

After:head <==> [A]<==> [C]<==> tail

1.let the next of node A point to node C

2.let the prev of node C point to the node A

3.Decrease the list length by 1



#Case 4: The list contains only one node

Before:head <==> [A] <==> tail

After:
head -> None
tail -> None

1. Set head = None

2. Set tail = None

3. Set the list length to 0


#Case 5: The list contains two nodes and one node is deleted

For example, deleting [A]:
Before:
head <==> [A] <==> [B] <==> tail

After:
head <==> [B] <==> tail

1. Set head to [B]

2. Set [B].prev = None to disconnect [B] from [A]

3. Decrease the list length by 1


#Case 6: The value to be deleted is not found

1. The nodes in the linked list remain unchanged

2. The head and tail remain unchanged

3. The length of the linked list remains unchanged



--------------------------------------------------------------------------------
2.5 exists(value)
--------------------------------------------------------------------------------

Assume sorted doubly linked list is: head <==> [A] <==> [B] <==> [C] <==> tail

The data in the linked list is arranged in ascending order: 
                                      head <==> 2 <==> 4 <==> 8 <==> 10 <==> tail

#Case 1: Successfully Found

If we call exists(8):

Check [2]: 2 is less than 8, continue recursively checking the next node [4].

Check [4]: 4 is less than 8, continue recursively checking the next node [8].

Check [8]: 8 equals 8, return True.

#Case 2: stop early

We call exists(5):

Check [2]: 2 is less than 5, not there yet, continue recursively checking the next node ([4]).

Check [4]: 4 is less than 5, not there yet, continue recursively checking the next node ([8]).

Check [8]: 8 is greater than 5. Directly return False, no longer check the later [10].

#Case 3: Not Found

The target value is greater than all numbers in the linked list, we call exists(12):

Check [2]: 2 is less than 12, not found yet, recursively call node.next to check the next node [4]

Check [4]: 4 is less than 12, continue recursively checking the next node [8]

Check [8]: 8 is less than 12, continue recursively checking the next node [10]

Check [10]: 10 is less than 12, continue recursively checking the next of node [10], which is None at this time, directly return False


--------------------------------------------------------------------------------
2.6 total()
--------------------------------------------------------------------------------

Doubly linked list: head <==> [2] <==> [4] <==> [8] <==> [10] <==> tail

Ask layer by layer backward:

[2] asks [4], returning 2 + total([4])

[4] asks [8], returning 4 + total([8])

[8] asks [10], returning 8 + total([10])

[10] asks None, returning 10 + total(None)

None returns 0 (Base Case)

Add back (Return layer by layer):

[10] got 0, calculated its own sum: 10 + 0 = 10, then handed 10 to the person in front.

[8] got 10, calculated the sum: 8 + 10 = 18, handed 18 to the person in front.

[4] got 18, calculated the sum: 4 + 18 = 22, handed 22 to the person in front.

[2] got 22, calculated the sum: 2 + 22 = 24, handed 24 to the original caller.

Final Result: Sum of the entire linked list = 24
   

--------------------------------------------------------------------------------
2.7 count(value)
--------------------------------------------------------------------------------


# Case 1: Target Found

Assume we want to count count(4)

Check [2]: 2 is less than 4 (not at target yet), trigger recursive case. Pass down: count([2]) returns count([4]).

Check [4]: 4 equals 4 (Hit the target!). Because we don't know if there are duplicate 4s afterward, we need to continue searching downward. 

Return 1 + count([8]).

Check [8]: 8 is greater than 4. Because the linked list is in ascending order, 8 is greater than 4, so the subsequent ones will definitely be larger, there cannot be another 4, so return 0.

Report layer by layer:

[8] returns 0.

[4] got 0, calculated 1 + 0 = 1, handed 1 to [2].

[2] got 1, returns 1.

Final Result: count(4) = 1



# Case 2: Target Does Not Exist

Assume we want to count count(5)

Check [2]: 2 is less than 5, continue downward: count([4]).

Check [4]: 4 is less than 5, continue downward: count([8]).

Check [8]: 8 is greater than 5! Trigger early pruning. Because after 8 it will only be 10 or further numbers, it is absolutely impossible to have 5. Directly return 0, terminate recursion.

Report layer by layer: 4 got 0, 2 got 0. 

Final Result: count(5) = 0.



#Case 3: Duplicate Target

Given the list: 2 <==> 4 <==> 4 <==> 8
Let's trace count(4):

At [2]: 2 < 4. Recurse on [4].

At first [4]: 4 == 4. Returns 1 + count([4]).

At second [4]: 4 == 4. Returns 1 + count([8]).

At [8]: 8 > 4. Early pruning triggers, returns 0.

Backtracking: [8] returns 0 → second [4] returns 1 + 0 = 1 → first [4] returns 1 + 1 = 2 → [2] returns 2.

Final Result: count(4) = 2.



--------------------------------------------------------------------------------
2.8 sum_middle_three()
--------------------------------------------------------------------------------


1.if the length n is less than 3, raise a ValueError. Calculate mid = n // 2.

2.If n is odd: Sum the values at indices mid-1, mid, and mid+1.

3.If n is even: Sum the values at indices mid-2, mid-1, and mid.

To implement this without recursion, we use a for loop starting from the head:

For an odd-length list, traverse to index mid - 1. 

For an even-length list, traverse to index mid - 2.

sum the required nodes.


--------------------------------------------------------------------------------
2.9 median()
--------------------------------------------------------------------------------

1.If the list is empty, raise a ValueError. Calculate mid = n // 2 and traverse mid steps from the head.

2.If n is odd: The middle node is exactly at mid. Return its value.

3.If n is even: The two middle nodes are at mid and mid-1. Return the average of current.value and current.prev.value. 



--------------------------------------------------------------------------------
print_list()
--------------------------------------------------------------------------------


1. Start from the head node.
2. Print the value of the current node.
3. Move to the next node and continue until reaching None.
4. If the list is empty, print (empty).


--------------------------------------------------------------------------------
3. Interesting aspects
--------------------------------------------------------------------------------
Because the list is sorted, some search operations can stop early. 
For example, if the current value is greater than the target value, the target cannot appear later in the list. 
The code also handles edge cases such as an empty list, a one-node list, duplicate values, 
and lists with fewer than three nodes when calculating the middle three values.

--------------------------------------------------------------------------------
4. How to run
--------------------------------------------------------------------------------


From the Problem4 directory, run the driver program with the provided basic input:

python3 problem4_driver.py < problem4Resources/problem4_basic.txt





