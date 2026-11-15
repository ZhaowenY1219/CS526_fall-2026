================================================================================
README.md - Problem 2
================================================================================


--------------------------------------------------------------------------------
 Introduction 
--------------------------------------------------------------------------------



--------------------------------------------------------------------------------
 Algorithm
--------------------------------------------------------------------------------

step 1 Define the Node ADT
--------------------------------------------------------------------------------
Create a Node ADT to represent each individual node in the binary heap, and each node must following below conditions:

1. 'value': stores the value held by the current node
2. 'left':stroes a reference to the left child node. if no left child exists, set it to 'None':left = None
3. 'right':stroes a reference to the right child node. if no right child exists, set it to 'None':right = None
4. 'parent':stroes a reference to the parent node. if no parent exists, set it to 'None':parent = None

When creating a new node, initialize its values ​​with the given input, and set its left, right, and parent references to 'None'

when connecting nodes to form the binary tree, update the references between the parent node and its children. FOr example,

           root_node.left = left_node   # set the parent's left reference to point to the left child
           root_node.right = right_node # set the parent's right reference to point to the right child

           left_node.parent = root_node  # set the left child's parent reference to point back to the parent node
           right_mode.parent = root_node # set the right child's parent reference to point back to the parent node
