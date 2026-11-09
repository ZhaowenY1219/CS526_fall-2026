================================================================================
README.md - Problem 1
================================================================================


--------------------------------------------------------------------------------
 Introduction 
--------------------------------------------------------------------------------

The program implements four main operations: AddNode(), DeleteNode(), FindNode(), and PrintTree(), which are used to insert nodes, delete nodes, find nodes, and print the nodes in the tree, respectively.

According to the assignment requirements, the program will randomly generate an input set containing 5 to 50 integers, each in the range of 1 to 1000. It will then create an initial BST, test node insertion, deletion, and search operations in sequence, and print the tree after each operation.


--------------------------------------------------------------------------------
 Algorithm
--------------------------------------------------------------------------------

step 1 define the node ADT
--------------------------------------------------------------------------------

create a Node ADT, each node contains:
1. value: the value stored in the node
2. left: a reference to the left child
3. right: a reference to the right child

step 2 define the BST ADT
--------------------------------------------------------------------------------

create a BST ADT with root reference and need to follow the operations:
1. AddNode(Value)
2. DeleteNode(Value)
3. FindNode(Value)
4. PrintTree()

Meanwhile, the BST need to follow ordering properties:

All values in the left subtree must be less than or equal to the parent node, and all values in the right subtree must be greater than the parent node.


step 3 AddNode(Value)
--------------------------------------------------------------------------------

compare the new value with the current node,starting from the root:
1. if the tree is empty, create a new node and set it as the root
2. if the new value is equal to the current node's value, do not insert a duplicate node
3. if the new value is smaller than the current node, move to the left subtree
4. if the new value is greater than the current node, move to the right subtree
5. if an empty position is reached, create a new node and insert it there


step 4 FindNode(Value)
--------------------------------------------------------------------------------
Start searching from the root node

compare the target value with the current node:
1. if the target = the current node, return True
2. if the target < the current node, continue searching in the left subtree
3. if the target > the current node, continue searching in the right subtree
4. if an empty position is reached without finding the target, return False
5. if the tree is empty, return False

step 5 DeleteNode(Value)
--------------------------------------------------------------------------------

Search for the node containing the target value:

1. start from the root node and initialize the parent reference to None
2. compare the target value with the current node and move to the left or right subtree, while keeping track of the parent node
3. if the current node becomes None, return False


Case 1: the node has no children

1. if the node to be deleted is the parent's left child, set 'parent.left' to 'None'
2. if the node to be deleted is the parent's right child, set 'parent.right' to 'None'
3. if the node is the root, set the root to None

Case 2: the node has one child

1. identify the existing child, either the left child or the right child
2. if the node is the root, update the root to point to the existing child
3. if the node is the parent's left child, update the parent's left reference to point to the existing child
4. if the node is the parent's right child, update the parent's rifht reference to point to the existing child


Case 3: the node has two children

1. move to the target node's left subtree
2. find the largest node in the left subtree by following the right child until no right child exists
3. copy the value of the in-order predecessor into the node to be deleted, replacing the original value
4. if the predecessor node is the target node’s direct left child, use the target node’s left reference; otherwise, use the right reference of the predecessor node’s parent
5. update this reference to point to the predecessor node’s left child (if one exists); otherwise, set it to None and remove the predecessor node from its original position

after deleting the node, return True

step 6 PrintTree( )
--------------------------------------------------------------------------------

The printing process: using inorder traversal to print all nodes in the BST in ascending order

1. check whether the tree is empty. If the root is None, print a message indicating that the tree is empty and stop
2. start from the root node and call the recursive helper method with the current node 
3. check whether the current node is None. If the node is None, stop the recursion and return to the previous call
4. visit the left child recursively by calling the helper method with the left child 
5. after the entire left subtree has been visited, print the value of the current node
6. visit the right child recursively by calling the helper method with the right child 
7. If the right child node does not exist, the recursive call stops and returns to the previous call.
8. Continues the process until all node have been visited and printed
9. The process follows the order: left -> root -> right. 
10. Call 'PrintTree()' after creating the initial tree and every 'AddNode()' and 'DeleteNode()'

--------------------------------------------------------------------------------
 Interesting aspects
--------------------------------------------------------------------------------

1.This program recursively traverses the nodes in the order "left -> root -> right". Due to the sorting property of a binary search tree (BST), this traversal method prints the values of all nodes in ascending order.

2.The deletion process depends on whether the target node has no children, one child, or two children. For nodes with two children, the program uses the "inorder predecessor" to perform the deletion operation.

--------------------------------------------------------------------------------
 How to run
--------------------------------------------------------------------------------

python3 HW5/problem1/problem1.py

