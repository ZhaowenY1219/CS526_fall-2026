================================================================================
README.md - Problem 1
================================================================================


--------------------------------------------------------------------------------
 Introduction 
--------------------------------------------------------------------------------



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
1. if the new value is smaller than or equal to the current node, move to the left subtree
2. if the new value is greater than the current node, move to the right subtree
3. if an empty position is reached, create a new node and insert it there
4. if the value already exists, do not create a duplicate node

step 4 FindNode(Value)
--------------------------------------------------------------------------------

compare the target value with the current node:
1. if the target = the current node, return True
2. if the target < the current node, continue searching in the left subtree
3. if the target > the current node, continue searching in the right subtree
4. if an empty position is reached without finding the target, return False
5. if the tree is empty, return False

After the entire left subtree has been visited, print the value of the current node
step 6 PrintTree( )
--------------------------------------------------------------------------------

The printing process: using inorder traversal to print all nodes in the BST in ascending order

1. check whether the tree is empty. If the root is None, print a message indicating that the tree is empty and stop
2. start from the root node and call the recursive helper method with the current node and set the initial depth = 0
3. check whether the current node is None. If the node is None, stop the recursion and return to the previous call
4. visit the left child recursively by calling the helper method with the left child and and increment the depth by 1.
5. after the entire left subtree has been visited, print the value of the current node
6. visit the right child recursively by calling the helper method with the right child and and increment the depth by 1.
7. If the right child node does not exist, the recursive call stops and returns to the previous call.
8. Continues the process until all node have been visited and printed
9. The process follows the order: left -> root -> right. 
10. Call 'PrintTree()' after creating the initial tree and every 'AddNode()' and 'DeleteNode()'




