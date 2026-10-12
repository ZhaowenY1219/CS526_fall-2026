
================================================================================
README.txt - Problem 3: Reverses a stack 
================================================================================

## Introduction

My program pushes the numbers 1 through 10 onto each stack, prints the stack before reversing, reverses the existing stack using recursion, and prints the stack again after reversing.

## Algorithm

--------------------------------------------------------------------------------
Create three types of stacks
--------------------------------------------------------------------------------

Step 1: Create three types of stacks

Create an array-based stack, a singly linked list stack, and a doubly linked list stack, respectively

1.1 define the SinglyNode class

    Each node stores a data value (value) and a next pointer to the next node.

1.2 Define the DoublyNode class

     Each node stores a data value, a prev pointer to the previous node, and a next pointer to the   next node. Both pointers are initialized to None.



Step 2: Implement a Stack Using an Array

1.Initialize an empty list `items` to hold the elements of the stack, with the end of the list as the top of the stack.

2.`push(value)`: Adds an element to the end of the list.

3.`pop()`: Removes and returns the last element of the list; reports an error if the stack is empty.

4.`peek()`: Returns the last element of the list without removing it.

5.`is_empty()`: Checks if the list is empty and returns the corresponding boolean value.


Step 3: Implement a Stack Using a Singly Linked List


1.Initialize `top = None` to indicate an empty stack. `top` always points to the top node of the stack.

2.`push(value)`: Creates a new node, makes it point to the original top node, and then updates `top`.

3.`pop()`: Saves the value of the top node, moves `top` to the next node, and returns the saved value; if the stack is empty, it reports an error.

4.`peek()`: Returns the value of the top node, but does not remove the node.

5.`is_empty()`: Checks if `top` is None.



Step 4: Implement a Stack Using a Doubly Linked List

1.Initialize `top = None` and `bottom = None`, representing the top and bottom of the stack, respectively. An empty stack contains no nodes.

2.`push(value)`: Creates a new node, connects it to the original top node, updates the relevant pointers, and updates `top` to the new node. If the original stack is empty, the new node becomes both the top and bottom node.

3.`pop()`: Saves the value of the top node, moves `top` to the next node, and updates the relevant pointers. If the stack becomes empty, `bottom` is set to `None`; finally, the saved value is returned.

4.`peek()`: Returns the value of the top node, but does not remove the node.

5.`is_empty()`: Checks if `top` is `None`.


Step 5: For each stack, call push() sequentially from 1 to 10 to push the stack in order


Step 6: Print the contents before reversal

--------------------------------------------------------------------------------
Recursive reversal function (reverse_stack(stack))
--------------------------------------------------------------------------------

Step 7: Check if the Stack is empty

If stack.is_empty() returns True, it means there are no elements in the stack that need to be reversed, so return directly and end the recursion

Step 8: Remove the top element from the stack

If Stack is not empty, use stack.pop() to remove the top element from the stack and store it in the variable value.


Step 9: Call reverse_stack(stack) to reverse the remaining stack

Step 10: After the recursive call is completed, call ‘insert_at_bottom(stack, value)’ to insert the saved element at the bottom of the reversed Stack.


--------------------------------------------------------------------------------
Helper function (insert_at_bottom(stack, value))
--------------------------------------------------------------------------------

Step 11: If the stack is empty（stack.is_empty() returns True）, it means that there are no other elements that need to be temporarily removed. Then call ‘stack.push(value)’ to push the target element into the empty stack, and then return to end the current recursion.


Step 12: If the Stack is not empty, use stack.pop() to remove the top element and store it in another variable, for example, top_value.

Step 13: Call ‘insert_at_bottom(stack, value)’ to continue inserting the target element towards the bottom of the stack.

Step 14: After the recursive call returns, use `stack.push(top_value)` to push the previously saved element back onto the stack. This ensures that the target element remains at the bottom, while the original order of other elements is not disrupted.


--------------------------------------------------------------------------------
Print the reversed result
--------------------------------------------------------------------------------

Step 15. Call `reverse_stack()` on the array `Stack`, then print the reversed contents.

Step 16. Call `reverse_stack()` on the singly linked list `Stack`, then print the reversed contents.

Step 17. Call `reverse_stack()` on the doubly linked list `Stack`, then print the reversed contents.



##interesting things

1.Recursive design: The program uses two recursive functions. reverse_stack() reverses the remaining stack, while insert_at_bottom() inserts a saved element at the bottom.

2.Base cases: Both recursive functions have stopping conditions. reverse_stack() returns when the stack is empty, and insert_at_bottom() pushes the target value when the stack is empty.

##how to run

Save the Python program as problem3.py.

Run the program with the following command:

python3 problem3.py


