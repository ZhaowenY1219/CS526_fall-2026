================================================================================
README.txt - Problem 2: Node and Singly Linked List classes
================================================================================


--------------------------------------------------------------------------------
Introduction (what the homework asks and what your code does)
--------------------------------------------------------------------------------
This homework asks me to create a Node class and a SinglyLinkedList class. 
The linked list stores nodes connected in one direction using a next pointer. 
My code supports adding, deleting, finding, getting, and updating nodes. 
It also keeps track of the head, tail, and number of nodes in the list.

--------------------------------------------------------------------------------
Algorithm
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
1. Define Node Class (Node Definition)
--------------------------------------------------------------------------------

class Node:

1.store a given value in the node 
2.set the next of node to None
3.Initialize the node, so the newly created isolated node has no connections before.
    

--------------------------------------------------------------------------------
2. Define SinglyLinkedList Class (Initialization and Length)
--------------------------------------------------------------------------------

class SinglyLinkedList:

Purpose: Initialize an empty linked list.
1. Set head to None because the list is initially empty
2. Set tail to None because there is no node in the list
3.set the node count to 0     

 __len__(self):
Return the count of the number of nodes stored in the list


--------------------------------------------------------------------------------
3. Create (Add Operations)
--------------------------------------------------------------------------------


3.1 prepend(value)


Before:head -> [A] -> [B] -> tail
 After: head -> [N] -> [A] -> [B] -> tail 

1. Let the next of node [N] point to the old head node [A].
2. Change head from [A] to [N].
3. Increase the list length by 1.

3.2 append(value)

before:head -> [A] -> [B] -> tail
 after:head -> [A] -> [B] -> [N] -> tail

1. Let the next of the old tail node [B] point to the new node [N].
2. Change tail from [B] to [N].
3. Increase the list length by 1.

If the list is empty:
head -> None
tail -> None

After append(N):
head -> [N] -> tail

Which means，both of head and tail point to node [N]


3.3 insert(index, value)

Before:head -> [A] -> [B] -> tail
After: head -> [A] -> [N] -> [B] -> tail

1.If the index is out of range, raise an IndexError.
2.Starting from head, locate the node before the insertion position.
3. Let the next of the new node [N] point to node [B].
4. Let the next of node [A] point to the new node [N].
5. Increase the list length by 1.

--------------------------------------------------------------------------------
4. Delete (Removal Operations)
--------------------------------------------------------------------------------

4.1 delete(value)


Find the value, and starting from head：

1. Check the current node’s value.
2. If it is not the target value, move to the next node.
3. Continue until the value is found or the end of the list is reached.
4. If the value is not found, the list remains unchanged.

#Case 1: Delete the head node 

Before:head -> [A] -> [B]->tail
 After:head -> [B] ->tail

1. Change head from [A] to [B].
2. The node [A] is removed from the list.
3. Decrease the list length by 1

If the list contains only one node

1. Set head = None.
2. Set tail = None.
3. Set the list length to 0.

#Case 2: Delete the tail node

Before: head -> [A] -> [B]->tail
After: head -> [A] ->tail

1. Let the next of node [A] point to None, which disconnects [A] from [B].
2. Change tail from [B] to [A].
3. Decrease the list length by 1.


#case 3: Delete a middle node

Before:head -> [A] -> [B]->[C]-> tail
 After: head -> [A] -> [C]-> tail

1. Let the next of node [A] point to node [C].
2. The node [B] is removed from the list.
3. Decrease the list length by 1.


--------------------------------------------------------------------------------
4.2 delete _at(index)
--------------------------------------------------------------------------------

If the index is out of range, raise an IndexError.

#case 1: index==0

Before:head -> [A] -> [B]->tail
After: head -> [B] -> tail

1. Change head from [A] to [B].
2. The node [A] is removed from the list.
3. Decrease the list length by 1.

If the list contains only one node

1. Set head = None.
2. Set tail = None.
3. Set the list length to 0.

#case 2: Delete the tail node

before: head -> [A] -> [B]->tail
After: head -> [A] -> tail

1. Starting from head, move index - 1 steps and stop at the node before the tail node, [A].
2. Let the next of node [A] point to None.
3. Change tail from [B] to [A].
4. Decrease the list length by 1.

#case 3: Delete a middle node

1. Starting from head, move index - 1 steps and stop at the node before the target node, [A].
2. Let the next of node [A] point to node [C].
3. Decrease the list length by 1.


--------------------------------------------------------------------------------
5. Read
--------------------------------------------------------------------------------

5.1 get(index)

1. Start from the head node.
2. Move to the next node until reaching the given index.
3. Return the value stored in that node.
4. If the index is out of range, raise an IndexError.


5.2 find(value)


1. Start from the head node.
2. Check the value of the current node.
3. If the value matches the target value, return its index.
4. Otherwise, move to the next node and continue searching.
5. If the value is not found, return -1.

5.3 __len__() returns the number of nodes currently stored in the linked list.

--------------------------------------------------------------------------------
6.update(index, value)
--------------------------------------------------------------------------------

1. Start from the head node.
2. Move to the node at the given index.
3. Replace the value stored in that node with the new value.
4. If the index is out of range, raise an IndexError.

--------------------------------------------------------------------------------
7.print_list()
--------------------------------------------------------------------------------

1. Start from the head node.
2. Print the value of the current node.
3. Move to the next node and continue until reaching None.
4. If the list is empty, print (empty).


--------------------------------------------------------------------------------
Interesting aspects
--------------------------------------------------------------------------------
I handle different edge cases, such as an empty list, a list with only one node, deleting the head or tail, 
and deleting a node from the middle.
For invalid indexes, the code raises an IndexError.
For find, the code returns -1 when the value is not found.


--------------------------------------------------------------------------------
How to run
--------------------------------------------------------------------------------

From the Problem2 directory, run the driver program with the provided basic input:

python3 problem2_driver.py < problem2Resources/problem2_basic.txt

